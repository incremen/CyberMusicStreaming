from ui.user_profile.user_playlists_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QListWidget, QListWidgetItem
from ui import gui_funcs
from ui.window_interface import WindowInterface
from typing import TYPE_CHECKING
from ui.album_page import album_window
from ui.login_page import login_window
from itertools import zip_longest
import logging
from ui.user_playlist_page.user_playlist_window import UserPlaylistWindow


if TYPE_CHECKING:
    from client.client_socket import ClientSocketHandler
    from music_playing.audio_handler import AudioHandler
    from client.shared_state import SharedState
    from client.window_manager import WindowManager
    from ui.album_page.album_window import AlbumWindow


class UserProfileWindow(Ui_MainWindow, WindowInterface, QMainWindow): 
   def __init__(self, shared_state :'SharedState', window_manager :'WindowManager'):
       super(UserProfileWindow, self).__init__()
       self.socket_handler = shared_state.socket_handler
       self.audio_handler = shared_state.audio_handler
       self.window_manager = window_manager
       self.login_manager = shared_state.login_manager
       self.setupUi(self)
       self.playlist_btn_to_playlist : dict[QPushButton] = {}
       self.setup_btns()
       
   def start(self):
      self.show()
      self.show_user_info()
      self.setup_btns_text()

   def show_user_info(self):
       current_user = self.login_manager.get_current_user()
       user_info_text = f"username: {current_user.username} \npassword: {current_user.password}"
       self.user_info_label.setText(user_info_text)
       
   def setup_btns(self):
      self.sign_out_btn.clicked.connect(self.signout_btn_click)
      
      self.playlist_btns = [
         self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6, self.btn_7, self.btn_8
      ]
      for btn in self.playlist_btns:
         btn.clicked.connect(self.playlist_btn_click)
         
   def setup_btns_text(self):
      user_playlists = self.login_manager.get_current_user().playlists
      for playlist, playlist_btn in zip_longest(user_playlists, self.playlist_btns):
         if not playlist:
            playlist_btn.setText("+")
            continue
         
         playlist_btn.setText(playlist.name)
         self.playlist_btn_to_playlist[playlist_btn] = playlist
           
   def playlist_btn_click(self):
      user_playlists_window = self.window_manager.windows[UserPlaylistWindow]
      
      self.playlist_btn_clicked = self.sender()
      logging.info(f"{self.playlist_btn_clicked=}")
      logging.info(f"{self.playlist_btn_to_playlist=}")
      logging.info(f"{self.playlist_btn_to_playlist.get(self.playlist_btn_clicked)=}")
      
      playlist = self.playlist_btn_to_playlist.get(self.playlist_btn_clicked)
      logging.debug(f"{playlist=}")
      
      if playlist:
         user_playlists_window.query_mode = "query_playlist"
      else:
         user_playlists_window.query_mode = "search_db"
         
      self.window_manager.hide_window(UserProfileWindow)
      self.window_manager.start_window(UserPlaylistWindow)
      
   def signout_btn_click(self, btn_clicked):
      self.login_manager.logout()
      self.window_manager.hide_window(UserProfileWindow)
      self.window_manager.start_window(login_window.LoginWindow)
    
   def get_last_clicked_playlist(self):
      return self.playlist_btn_to_playlist[self.playlist_btn_clicked] 
        
