from ui.signup_page.signup_page_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QListWidget, QListWidgetItem
import ui.album_page.album_window
from ui import gui_funcs
from typing import TYPE_CHECKING
from ui.window_interface import WindowInterface
from ui.search_page import search_window
from ui.login_page import login_window

if TYPE_CHECKING:
    from client.client_socket import ClientSocketHandler
    from music_playing.audio_handler import AudioHandler
    from client.shared_state import SharedState
    from client.window_manager import WindowManager
import logging



class SignupWindow(Ui_MainWindow, WindowInterface, QMainWindow): 
    def __init__(self, shared_state :'SharedState', window_manager :'WindowManager'):
       super(SignupWindow, self).__init__()
       self.socket_handler = shared_state.socket_handler
       self.audio_handler = shared_state.audio_handler
       self.window_manager = window_manager
       self.login_manager = shared_state.login_manager
       self.setupUi(self)
       self.setup_btns()
       
    def start(self):
        self.show()
       
    def setup_btns(self):
       self.ready_btn.clicked.connect(self.ready_btn_click)
       self.already_have_account_btn.clicked.connect(self.already_have_account_btn_click)
       
    def already_have_account_btn_click(self):
        self.window_manager.start_window(login_window.LoginWindow)
        self.window_manager.hide_window(SignupWindow)
       
    def ready_btn_click(self):
        username = self.username_input.text()
        password = self.password_input.text()
        self.login_manager.create_new_account(username, password)
            
    def handle_new_acc_response(self, result : bool):
        if result:
            self.handle_new_account_success()
        else:
            self.handle_new_account_failure()

    def handle_new_account_failure(self):
        logging.error(f"Failed to create account")

    def handle_new_account_success(self):
        logging.info("New account created successfully.")
        self.window_manager.start_window(search_window.SearchWindow)
        self.window_manager.hide_window(SignupWindow)

           

           
    
       
        
