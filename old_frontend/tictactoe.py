from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget
from ui.gui_funcs import create_message_box, create_yes_no_question
from PyQt5 import uic, QtGui
import logging
from backend.protocol.common_json_types import MsgType
import backend.protocol.protocols as proto
from backend.protocol.protocols import JsonKeys
import random
from PyQt5.QtGui import QTransform
from PyQt5.QtCore import QTimer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.client_side.lobby_emitter import LobbySignalEmitter
from PyQt5.QtGui import QFont


class TictactoeWindow(QMainWindow):
    def __init__(self, client_name, client_socket, player_color, opponent_name, lobby_emitter):
        super(TictactoeWindow, self).__init__()
        
        self.opponent_name = opponent_name
        self.lobby_emitter : LobbySignalEmitter = lobby_emitter
        self.client_socket = client_socket
        self.client_name = client_name
        self.player_btn_color = player_color
        
        uic.loadUi(r"ui\tictactoe_gui.ui", self)
        self.setWindowTitle(f"Tictactoe- {client_name}")
        
        self.opponent_btn_color = None
        self.player_symbol = None
        self.opponent_symbol = None
        self.awaiting_response = False
        
        self.main_widget = self.findChild(QWidget, "main_widget")
        self.setup_main_widget_properties()
        
        self.show()
        
        self.setup_color_map()
        
    def setup_color_map(self):
        self.lighter_to_darker_map = {
                'LightCoral': 'Tomato',
                'LightSkyBlue': 'DeepSkyBlue',
                'PaleGreen': 'LimeGreen',
                'LightYellow': 'Yellow',
                'Plum': 'MediumOrchid',
                'PeachPuff': 'SandyBrown',
                'LightPink': 'HotPink',
                'Aqua': 'DeepSkyBlue',
                'Thistle': 'MediumOrchid',
                'PaleGreen': 'LimeGreen'
            }
        
    def closeEvent(self, event):
        if not event.spontaneous():
            return

        wants_to_close = create_yes_no_question("Are you sure you want to exit?","Exit Confirmation")

        if not wants_to_close:
            event.ignore()
            return
        
        proto.send_message(self.client_socket, MsgType.SURRENDER)
        self.lobby_emitter.game_window_closed.emit()
        event.accept()  
    
    def rotate_board_btns(self, angle):
       transform = QTransform().rotate(angle)
       for btn in self.board_btn_list:
           btn.setGraphicsEffect(transform)
           
    def handle_game_end(self, json_data):
        if json_data.get(JsonKeys.IS_TIE):
            self.handle_tie()
            return
        
        you_win = json_data.get(JsonKeys.YOU_WIN)
        if you_win:
            self.handle_player_win(json_data)
        else:
            self.handle_player_loss()
            
    def handle_tie(self):
        self.player_msg.setText("Tie!")
        self.fill_bg_animation("#F0F0F0")
        self.disable_all_btns()

    def setup_main_widget_properties(self):
        main_widget = self.main_widget
        self.player_msg = main_widget.findChild(QLabel, "player_msg")
        self.player_msg.setFont(QFont("Voltage", 70))

        self.rematch_btn = main_widget.findChild(QPushButton, "btn_reset")
        self.rematch_btn.clicked.connect(self.rematch_btn_click)

        self.player_symbol_edit = main_widget.findChild(QLabel, "player_symbol_label")
        self.opponent_symbol_edit = main_widget.findChild(QLabel, "opponent_symbol_label")
        
        self.setup_board_btns()

    def setup_board_btns(self):
        main_widget = self
        self.btn_1 = main_widget.findChild(QPushButton, "btn_1")
        self.btn_2 = main_widget.findChild(QPushButton, "btn_2")
        self.btn_3 = main_widget.findChild(QPushButton, "btn_3")
        self.btn_4 = main_widget.findChild(QPushButton, "btn_4")
        self.btn_5 = main_widget.findChild(QPushButton, "btn_5")
        self.btn_6 = main_widget.findChild(QPushButton, "btn_6")
        self.btn_7 = main_widget.findChild(QPushButton, "btn_7")
        self.btn_8 = main_widget.findChild(QPushButton, "btn_8")
        self.btn_9 = main_widget.findChild(QPushButton, "btn_9")
        
        self.board_btn_list = [self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, 
        self.btn_6, self.btn_7, self.btn_8, self.btn_9]
        
        for btn in self.board_btn_list:
        #You have to make btn a default paramater because the non default paramater becomes a boolean
            btn.clicked.connect(lambda clicked, btn=btn: self.board_btn_click(btn))	
            
        self.disable_all_btns()

    def game_info_received(self, json_data):
        if opponent_color := json_data.get(JsonKeys.OPPONENT_COLOR):
            self.opponent_btn_color = opponent_color
                
        if player_symbol := json_data.get(JsonKeys.YOUR_SYMBOL):
            self.player_symbol = player_symbol
            self.player_symbol_edit.setText(self.player_symbol)
                
        if opponent_symbol := json_data.get(JsonKeys.OPPONENT_SYMBOL):
            self.opponent_symbol = opponent_symbol
            self.opponent_symbol_edit.setText(self.opponent_symbol)
            
        if game_board := json_data.get(JsonKeys.GAME_BOARD):
            self.update_board(game_board)
        
    def disable_all_btns(self):
        for btn in self.board_btn_list:
            btn.setEnabled(False)
    
    def enable_all_btns(self):
        for btn in self.board_btn_list:
            btn.setEnabled(True)
    
    def board_btn_click(self, btn_clicked):
        btn_clicked.setText(self.player_symbol)
        self.disable_all_btns()
        self.set_btn_color(btn_clicked, self.player_btn_color)
        btn_index = self.board_btn_list.index(btn_clicked)
        logging.client(f"{btn_index=}")
        
        proto.send_message(
            self.client_socket,
            MsgType.GAME_MOVE, 
            {JsonKeys.BTN_INDEX: btn_index}
        )
    
    def move_request_received(self, json_data):
        game_board = json_data[JsonKeys.GAME_BOARD]
        self.update_board(game_board, enable_btns=True)

    def update_board(self, updated_board, enable_btns = False):
        for btn, symbol in zip(self.board_btn_list, updated_board):
            self.update_btn(btn, symbol, enable_btns)

    def update_btn(self, btn, symbol, enable_btns = False):
        if symbol is None and enable_btns:
            btn.setEnabled(True)
            btn.setStyleSheet("")
            return
        
        btn.setText(symbol)
        btn.setEnabled(False)
        if symbol == self.player_symbol:
            self.set_btn_color(btn, self.player_btn_color)
        elif symbol == self.opponent_symbol:
            self.set_btn_color(btn, self.opponent_btn_color)
            
    def set_btn_color(self, btn, color):
        logging.debug(f"background-color: {color}; color: black;")
        btn.setStyleSheet(f"background-color: {color}; color: black;")

    def handle_player_win(self, json_data):
        if json_data.get(JsonKeys.OPPONENT_DISCONNECT):
            win_msg = "They're gone!"
            enable_rematch = False
        else:
            enable_rematch = True
            win_msg = "You win!"
            
        self.player_msg.setText(win_msg)
        self.fill_bg_animation(self.lighter_to_darker_map[self.player_btn_color], enable_rematch)
        self.disable_all_btns()
    
    def handle_player_loss(self):
        self.player_msg.setText("You lose!")
        self.fill_bg_animation(self.lighter_to_darker_map[self.opponent_btn_color])
        self.disable_all_btns()
            
    def rematch_btn_click(self):
        proto.send_message(self.client_socket, MsgType.REMATCH_REQUEST,
                           {JsonKeys.SEND_TO: self.opponent_name})
        self.rematch_btn.setEnabled(False)
        
        self.awaiting_response = True
    
    def rematch_response_received(self, json_data):
        self.awaiting_response = False
        self.rematch_btn.setEnabled(True)
        if not json_data.get(JsonKeys.REQUEST_RESPONSE):
            create_message_box("Unfortunately they don't wanna play with you", "Request response")
            return
        
        self.setup_rematch()
        logging.info(json_data)

    def setup_rematch(self):
        self.reset_all_btns()
        self.player_msg.setText("Rematch!")

    def reset_all_btns(self):
        for btn in self.board_btn_list:
            btn.setText("")
            btn.setEnabled(True)
            btn.setStyleSheet("")
    
    def rematch_request_received(self, json_data):
        wants_to_play = create_yes_no_question(f"Play again with {self.opponent_name}?", f"{self.client_name}- accept request")
        
        if wants_to_play:
            self.setup_rematch()
        
        new_json_data = {JsonKeys.REQUEST_RESPONSE: wants_to_play, JsonKeys.SEND_TO: self.opponent_name}
        proto.send_message(
            self.client_socket, MsgType.REMATCH_RESPONSE, new_json_data)
    
    def fill_bg_animation(self, bg_color, enable_rematch=True):
        self.rematch_btn.setEnabled(False)
        
        rand_btns = random.sample(self.board_btn_list, len(self.board_btn_list))
        delay = 50  # 50ms delay between button updates
        for i, btn in enumerate(rand_btns):
            QTimer.singleShot(int((i * delay)**1.2),
                lambda btn=btn: self.animate_button(btn, bg_color))
        
        if not enable_rematch or self.awaiting_response:
            return
        
        self.animation_done_timer = QTimer()
        self.animation_done_timer.timeout.connect(
            lambda: self.rematch_btn.setEnabled(True)
            )
        
        self.animation_done_timer.start( int( (8* delay)**1.2) ) #total time annimation takes

    def animate_button(self, btn, bg_color, text=""):
        btn.setStyleSheet(f"background-color: {bg_color};")
        btn.setText(text)



    
