from ui.login_page.login_page_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QListWidget, QListWidgetItem
import ui.main_page.main_page
from ui import gui_funcs
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from client.client_socket import ClientSocketHandler
    from music_playing.audio_handler import AudioHandler
    from client.shared_state import SharedState



class LoginWindow(Ui_MainWindow, QMainWindow): 
   def __init__(self, shared_state :'SharedState'):
       super(LoginWindow, self).__init__()
       self.socket_handler = shared_state.socket_handler
       self.audio_handler = shared_state.audio_handler
       self.setupUi(self)
       self.setup_btns()
       self.show()
       
   def setup_btns(self):
    #    self.ready_btn.clicked.connect(self.ready_btn_click)
    ...
           

           
    
       
        
