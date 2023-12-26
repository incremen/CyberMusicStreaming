from ui.search_page.search_page_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QListWidget, QListWidgetItem
import ui.main_page.main_page
from ui import gui_funcs

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from client.client_socket import ClientSocketHandler
    from music_playing.audio_handler import AudioHandler
    from client.shared_state import SharedState

class SearchWindow(Ui_MainWindow, QMainWindow): 
   def __init__(self, shared_state :'SharedState'):
       super(SearchWindow, self).__init__()
       self.socket_handler = shared_state.socket_handler
       self.audio_handler = shared_state.audio_handler
       self.setupUi(self)
       self.setup_btns()
       self.show()
       
   def setup_btns(self):
       grid_btns = gui_funcs.get_objects_from_boxlayout(self.album_grid)
       for btn in grid_btns:
           btn.clicked.connect(self.album_btn_click)
           
   def album_btn_click(self, btn_clicked):
      self.main_window = ui.main_page.main_page.MainPage(self.socket_handler, self.audio_handler)
           
    
       
        
