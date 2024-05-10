from ui.user_profile.user_profile_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QListWidget, QListWidgetItem
from ui import gui_funcs
from ui.window_interface import WindowInterface
from typing import TYPE_CHECKING
from ui.album_page import album_window
from ui.login_page import login_window
from itertools import zip_longest
import logging
from ui.user_playlist_page.user_playlist_window import UserPlaylistWindow
from database.models import User
from ui.discover_page import discover_window
from result import Ok, Err, Result, is_ok, is_err

from ui.miniplayer.miniplayer_window import MiniplayerWindow
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
      self.show_user_info()
      self.show()
      self.socket_handler.emit_to_server("get_user_info")

   def show_user_info(self):
       user_info_text = f"username: {self.login_manager.username}"
       self.user_info_label.setText(user_info_text)
       
   def setup_btns(self):
      self.sign_out_btn.clicked.connect(self.signout_btn_click)
      self.home_btn.clicked.connect(self.home_btn_click)
      
      self.playlist_btns = [
         self.playlist_btn_1, self.playlist_btn_2, self.playlist_btn_3, self.playlist_btn_4, self.playlist_btn_5, self.playlist_btn_6, self.playlist_btn_7, self.playlist_btn_8
      ]
      for playlist_btn in self.playlist_btns:
         playlist_btn.clicked.connect(self.playlist_btn_click)
         
      self.play_btns = [
         self.play_btn_1, self.play_btn_2, self.play_btn_3, self.play_btn_4, self.play_btn_5, self.play_btn_6, self.play_btn_7, self.play_btn_8
      ]
      
      for play_btn in self.play_btns:
         play_btn.clicked.connect(self.play_btn_click)
      
      self.play_btn_to_playlist_btn = {play_btn : playlist_btn for play_btn, playlist_btn in zip(self.play_btns, self.playlist_btns)}
      
   def play_btn_click(self):
      play_btn_clicked = self.sender()
      playlist_name = self.play_btn_to_playlist_btn.get(play_btn_clicked).text()
      if playlist_name == "+":
         return
         
      logging.info(f"{playlist_name=}")
      self.window_manager.start_window(MiniplayerWindow)
      
      for user_playlist in self.login_manager.playlists:
         if user_playlist["name"] == playlist_name:
            to_load = user_playlist
      
      self.audio_handler.clear_queue_and_played()
      self.audio_handler.setup_song_name_to_info(to_load["songs"])
      for song in to_load["songs"]:
         self.audio_handler.add_to_song_queue(song["name"])
      
         
   def home_btn_click(self):
      self.hide()
      self.window_manager.start_window(discover_window.DiscoverWindow)
         
   def load_user_playlists(self, user_data : dict):
      self.show_user_info()
      logging.info(f"{user_data=}")
      logging.info(f"{user_data['playlists']=}")
      for playlist, playlist_btn in zip_longest(user_data["playlists"], self.playlist_btns):
         if not playlist:
            playlist_btn.setText("+")
            continue
         
         playlist_btn.setText(playlist["name"])
         self.playlist_btn_to_playlist[playlist_btn] = playlist
           
   def playlist_btn_click(self):
      self.playlist_btn_clicked = self.sender()
         
      self.window_manager.hide_window(UserProfileWindow)
      self.window_manager.start_window(UserPlaylistWindow)
      
   def signout_btn_click(self, btn_clicked):
      self.login_manager.logout()
      self.window_manager.hide_window(UserProfileWindow)
      self.window_manager.start_window(login_window.LoginWindow)
    
   def get_last_clicked_playlist_name(self):
      logging.checkpoint(f"{self.playlist_btn_clicked.text()=}")
      last_clicked_playlist_name = self.playlist_btn_to_playlist.get(self.playlist_btn_clicked)
      if not last_clicked_playlist_name:
         return Err("No playlist name")
      return Ok(last_clicked_playlist_name)
      
        
