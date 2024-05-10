from ui.search_page.search_page_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QListWidget, QListWidgetItem
from ui import gui_funcs
from ui.window_interface import WindowInterface
from typing import TYPE_CHECKING
from ui.album_page import album_window
from ui.user_profile import user_profile_window


if TYPE_CHECKING:
   from client.client_socket import ClientSocketHandler
   from music_playing.audio_handler import AudioHandler
   from client.shared_state import SharedState
   from client.window_manager import WindowManager
   from ui.album_page.album_window import AlbumWindow


class DiscoverWindow(Ui_MainWindow, WindowInterface, QMainWindow): 
   def __init__(self, shared_state :'SharedState', window_manager :'WindowManager'):
      super(DiscoverWindow, self).__init__()
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
         
      self.see_own_playlists_btn.clicked.connect(self.user_playlists_btn_click)
            
   def user_playlists_btn_click(self, btn_clicked):
      self.window_manager.hide_window(DiscoverWindow)
      self.window_manager.start_window(user_profile_window.UserProfileWindow)
           
   def album_btn_click(self, btn_clicked):
      self.album_window = self.window_manager.get_window(album_window.AlbumWindow)
      self.album_window.album_mode = "query_server"
      self.window_manager.hide_window(DiscoverWindow)
      self.window_manager.start_window(album_window.AlbumWindow)
       
        
