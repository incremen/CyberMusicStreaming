from ui.user_playlists.user_playlists_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QListWidget, QListWidgetItem
from ui import gui_funcs
from ui.window_interface import WindowInterface
from typing import TYPE_CHECKING
from ui.album_page import album_window
from ui.login_page import login_window

if TYPE_CHECKING:
    from client.client_socket import ClientSocketHandler
    from music_playing.audio_handler import AudioHandler
    from client.shared_state import SharedState
    from client.window_manager import WindowManager
    from ui.album_page.album_window import AlbumWindow


class UserPlaylistsWindow(Ui_MainWindow, WindowInterface, QMainWindow): 
   def __init__(self, shared_state :'SharedState', window_manager :'WindowManager'):
       super(UserPlaylistsWindow, self).__init__()
       self.socket_handler = shared_state.socket_handler
       self.audio_handler = shared_state.audio_handler
       self.window_manager = window_manager
       self.login_manager = shared_state.login_manager
       self.setupUi(self)
       self.setup_btns()
       
   def start(self):
      self.show()
      self.show_user_info()

   def show_user_info(self):
       current_user = self.login_manager.current_user
       user_info_text = f"username: {current_user.username} \npassword: {current_user.password}"
       self.user_info_label.setText(user_info_text)
       
   def setup_btns(self):
      self.sign_out_btn.clicked.connect(self.signout_btn_click)
      
      self.playlist_btns = [
         self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6, self.btn_7, self.btn_8
      ]
      for btn in self.playlist_btns:
         btn.clicked.connect(self.playlist_btn)
           
   def playlist_btn(self, btn_clicked):
      self.window_manager.hide_window(UserPlaylistsWindow)
      
      album_window_obj = self.window_manager.windows[album_window.AlbumWindow]
      album_window_obj.album_mode = "query_local"
      self.window_manager.start_window(album_window.AlbumWindow)
      
   def signout_btn_click(self, btn_clicked):
      self.login_manager.logout()
      self.window_manager.hide_window(UserPlaylistsWindow)
      self.window_manager.start_window(login_window.LoginWindow)
    
       
        
