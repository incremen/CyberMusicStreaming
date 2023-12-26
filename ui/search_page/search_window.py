from ui.search_page.search_page_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QListWidget, QListWidgetItem
from ui import gui_funcs

from typing import TYPE_CHECKING
from ui.album_page import album_window
if TYPE_CHECKING:
    from client.client_socket import ClientSocketHandler
    from music_playing.audio_handler import AudioHandler
    from client.shared_state import SharedState
    from client.window_manager import WindowManager
    from ui.album_page.album_window import AlbumWindow

class SearchWindow(Ui_MainWindow, QMainWindow): 
    def __init__(self, shared_state :'SharedState', window_manager :'WindowManager'):
       super(SearchWindow, self).__init__()
       self.socket_handler = shared_state.socket_handler
       self.audio_handler = shared_state.audio_handler
       self.window_manager = window_manager
       self.setupUi(self)
       self.setup_btns()
       
    def start(self):
       self.show()
       
    def setup_btns(self):
       grid_btns = gui_funcs.get_objects_from_boxlayout(self.album_grid)
       for btn in grid_btns:
           btn.clicked.connect(self.album_btn_click)
           
    def album_btn_click(self, btn_clicked):
      self.window_manager.hide_window(SearchWindow)
      self.window_manager.start_window(album_window.AlbumWindow)
    
       
        
