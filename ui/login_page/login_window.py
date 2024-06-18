from ui.login_page.login_page_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QListWidget, QListWidgetItem
import ui.album_page.album_window
from ui import gui_funcs
from typing import TYPE_CHECKING
from ui.window_interface import WindowInterface
from ui.discover_page import discover_window
from ui.signup_page import signup_window
import logging
from ui.user_profile import user_profile_window
from ui.gui_funcs import create_message_box
if TYPE_CHECKING:
    from client.client_socket import ClientSocketHandler
    from music_playing.audio_handler import AudioHandler
    from client.shared_state import SharedState
    from client.window_manager import WindowManager

class LoginWindow(Ui_MainWindow, WindowInterface, QMainWindow):
    def __init__(self, shared_state: 'SharedState', window_manager: 'WindowManager'):
        super(LoginWindow, self).__init__()
        self.socket_handler = shared_state.socket_handler
        self.audio_handler = shared_state.audio_handler
        self.window_manager = window_manager
        self.login_manager = shared_state.login_manager
        self.setupUi(self)
        self.setup_btns()

    def start(self):
        self.username_input.setText("")
        self.password_input.setText("")
        self.show()
        
    def client_disconnected(self):
        gui_funcs.create_message_box("Connection from server lost.", "Error")

    def setup_btns(self):
        self.ready_btn.clicked.connect(self.ready_btn_click)
        self.dont_have_account_btn.clicked.connect(self.already_have_account_btn_click)
        
    def already_have_account_btn_click(self):
        self.window_manager.start_window(signup_window.SignupWindow)
        self.window_manager.hide_window(LoginWindow)

    def ready_btn_click(self):
        username = self.username_input.text()
        password = self.password_input.text()
        result = self.login_manager.login(username, password)

    def handle_login_fail(self, message : str):
        logging.error(f"Failed to login")
        create_message_box(message, "Error")

    def handle_login_success(self):
        logging.info("Login successful.")
        self.window_manager.start_window(user_profile_window.UserProfileWindow)
        self.window_manager.hide_window(LoginWindow)
            
    def handle_login_response(self, result : bool, message : str):
        if result:
            self.handle_login_success()
        else:
            self.handle_login_fail(message)