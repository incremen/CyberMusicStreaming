from PyQt5.QtWidgets import (QMainWindow, QPushButton, QLabel, QWidget, 
QListWidget, QListWidgetItem, QInputDialog, QMessageBox)
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, QThread, Qt
import logging
from backend.protocol.common_json_types import MsgType
import backend.protocol.protocols as proto
from backend.protocol.protocols import JsonKeys
from ui.tictactoe import TictactoeWindow
from custom_logging import log_calls
from typing import TYPE_CHECKING
from ui.gui_funcs import create_message_box, create_yes_no_question

if TYPE_CHECKING:
    from backend.client_side.client_msg_handler import ClientMsgHandler

class Lobby(QMainWindow):
    def __init__(self, client_logger, msg_handler, lobby_emitter):
        super(Lobby, self).__init__()
        self.lobby_emitter = lobby_emitter
        self.msg_handler : ClientMsgHandler= msg_handler
        self.client_logger = client_logger
        
        self.setup_properties()
        
        self.setup_window()
        
        self.main_widget = self.findChild(QWidget, "main_widget")
        
        self.setup_widgets()

    def setup_properties(self):
        self.client_name = None
        self.in_lobby = False
        self.in_game = False
        self.client_socket = None
        self.server_is_connected = False
        self.awaiting_response = False
        self.handling_play_request = False
        self.tictactoe_window = None
        self.player_color = None

    def setup_widgets(self):
        self.list_widget = self.main_widget.findChild(QListWidget, "list_widget")
        self.list_widget.itemClicked.connect(self.user_in_lobby_click)
        
        self.game_end_msg = self.main_widget.findChild(QLabel, "game_end_msg")
        
        self.username_label = self.main_widget.findChild(QLabel, "username_label")
        logging.info(f"{self.username_label=}")
        
        self.join_btn = self.main_widget.findChild(QPushButton, "join_btn")
        self.join_btn.clicked.connect(self.join_btn_click)
        
        self.leave_btn = self.main_widget.findChild(QPushButton, "leave_btn")
        self.leave_btn.clicked.connect(self.leave_btn_click)
    
    def game_window_closed(self):
        self.in_game = False
        self.game_end_msg.setText("Alright, GG!")
        
    def server_disconnected(self):
        self.in_lobby = False
        self.server_is_connected = False
        self.username_label.setText("Not in lobby")
        self.game_end_msg.setText("Server disconnected")
        self.list_widget.clear()
        self.main_widget.setStyleSheet("")
        self.close_game_if_game_open()
        
    def server_connected(self, client_socket):
        self.client_socket = client_socket
        self.game_end_msg.setText("Server connected")
        self.server_is_connected = True
        
    def closeEvent(self, event):
        if not event.spontaneous():
            self.close_game_if_game_open()
            return
        
        wants_to_close = create_yes_no_question("Are you sure you want to exit?","Exit Confirmation")

        if not wants_to_close:
            event.ignore()
            return
        
        self.close_game_if_game_open()
        
        self.msg_handler.close_socket()
        event.accept() 

    def close_game_if_game_open(self):
        if self.tictactoe_window:
            self.tictactoe_window.close()
            self.tictactoe_window = None 

    @log_calls
    def change_name(self, name):
        logging.debug("Changing name...")
        self.setWindowTitle(f"Lobby- {self.client_name}")
        self.username_label.setText(name)
        self.client_name = name
        self.client_logger.add_name_to_log_format(self.client_name)
        self.in_lobby = True
        
    def remove_from_lobby(self):
        logging.debug("Removing name...")
        self.client_name = None
        self.username_label.setText("Not in lobby")
        self.in_lobby = False
        
    def send_request_to_other_cli(self, other_cli_name):
        logging.client(f"Sending request to {other_cli_name}")
        proto.send_message(self.client_socket, MsgType.PLAY_REQUEST,
                        {JsonKeys.SEND_TO : other_cli_name})
        
    def accept_request_from_other_cli(self, other_cli_name):
        json_data = {JsonKeys.REQUEST_RESPONSE: True, JsonKeys.SEND_TO : other_cli_name}
        logging.client(f"sending {json_data}")
        proto.send_message(self.client_socket, MsgType.REQUEST_RESPONSE, json_data)
        
        self.start_game(other_cli_name)
    
    def user_in_lobby_click(self, user_clicked):
        logging.debug(f"{self.in_lobby=}, {self.awaiting_response=}")
        if not self.in_lobby or self.awaiting_response:
            return
        name_clicked = user_clicked.text()
        if name_clicked == self.client_name:
            return
        
        self.awaiting_response = True
        
        wants_to_play = create_yes_no_question(f"send request to {name_clicked}?", f"{self.client_name}- send request?")
        if not wants_to_play:
            return
        
        logging.client(f"Sending request to {name_clicked}")
        proto.send_message(self.client_socket, MsgType.PLAY_REQUEST,
                        {JsonKeys.SEND_TO : name_clicked})
        
    def play_request_received(self, json_data):
        request_from = json_data.get(JsonKeys.SENT_FROM)
        
        if self.handling_play_request or self.awaiting_response:
            wants_to_play = False
        else:
            self.handling_play_request = True
            wants_to_play = create_yes_no_question(f"Accept request from {request_from}?", f"{self.client_name}- accept request?")
            self.handling_play_request = False
        
        json_data = {JsonKeys.REQUEST_RESPONSE: wants_to_play, JsonKeys.SEND_TO : request_from}
        proto.send_message(self.client_socket, MsgType.REQUEST_RESPONSE, json_data)
        
        if wants_to_play:
            self.start_game(request_from)
        
    def request_response_received(self, json_data):
        self.awaiting_response = False
        
        response_from = json_data.get(JsonKeys.SENT_FROM)
        response = json_data.get(JsonKeys.REQUEST_RESPONSE)
        logging.client(f"Received response from {response_from} with response {response}")
        if not response:
            self.handle_rejected_request(response_from)
            return
        
        self.start_game(response_from)
        
    @log_calls
    def start_game(self, opponent_name):
        self.in_game = True
        self.game_thread = QThread()
        self.opponent_name = opponent_name
        self.game_thread.started.connect(self.start_the_game_threaded)
        self.game_thread.start()

    @log_calls
    def start_the_game_threaded(self):
        self.tictactoe_window = TictactoeWindow(self.client_name, self.client_socket, 
                                    self.player_color, self.opponent_name, self.lobby_emitter)
        self.tictactoe_window.show()
        self.msg_handler.game_emitter.setup_connections(self.tictactoe_window)
        self.remove_from_lobby()
        self.game_thread.quit()

    def handle_rejected_request(self, response_from):
        response_msg = QMessageBox()
        response_msg.setText(f"Aw, too bad {self.client_name}! {response_from} has rejected your request.")
        response_msg.exec_()
        
    def change_bgr_color(self, json_data):
        color = json_data.get(JsonKeys.BGR_COLOR)
        self.player_color = color
        self.main_widget.setStyleSheet(f"background-color: {color};")
    
    def setup_window(self):
        uic.loadUi("ui/lobby_gui.ui", self)
        self.setWindowTitle("Lobby")
        self.show()
        
    def update_lobby_list(self, json_data):
        lobby_list = json_data.get(JsonKeys.LOBBY_LIST)
        logging.info(f"Updating lobby list to {lobby_list}")
            
        self.list_widget.clear()
        for player in lobby_list:
            self.add_player(player)
    
    def leave_btn_click(self):
        if not self.in_lobby or not self.server_is_connected:
            return
        self.remove_from_lobby()
        proto.leave_lobby(self.client_name, self.client_socket)        
    
    def join_btn_click(self):
        logging.debug(f"{self.server_is_connected=}")
        if self.in_lobby or self.in_game or not self.server_is_connected:
            return
        
        client_name, ok = QInputDialog.getText(self, "Enter Username", "Username:")
        
        if not (ok and client_name):
            return
        
        if self.list_widget.findItems(client_name, Qt.MatchExactly):
            create_message_box(f"The name {client_name} is already taken.", "Name already taken")
            return
        
        logging.debug("Changing name...")
        self.change_name(client_name)
        
        logging.client("About to run join lobby func")
        proto.join_lobby(client_name, self.client_socket)

    def add_player(self, player_name):
        item = QListWidgetItem(player_name)
        item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.list_widget.addItem(item)
        


    