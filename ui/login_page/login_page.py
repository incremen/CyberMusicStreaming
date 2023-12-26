from ui.login_page.login_page_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QListWidget, QListWidgetItem
import ui.album_page.album_window
from ui import gui_funcs
from typing import TYPE_CHECKING


from ui.search_page.search_window import SearchWindow


if TYPE_CHECKING:
    from client.client_socket import ClientSocketHandler
    from music_playing.audio_handler import AudioHandler
    from client.shared_state import SharedState
    from client.window_manager import WindowManager



class LoginWindow(Ui_MainWindow, QMainWindow): 
    def __init__(self, shared_state :'SharedState', window_manager :'WindowManager'):
       super(LoginWindow, self).__init__()
       self.socket_handler = shared_state.socket_handler
       self.audio_handler = shared_state.audio_handler
       self.window_manager = window_manager
       self.setupUi(self)
       self.setup_btns()
       
    def start(self):
        self.show()
       
    def setup_btns(self):
       self.ready_btn.clicked.connect(self.ready_btn_click)
       
    def ready_btn_click(self):
        self.window_manager.start_window(SearchWindow)
        self.window_manager.hide_window(LoginWindow)
           

           
    
       
        
