from ui.miniplayer.miniplayer_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QListWidget, QListWidgetItem
from ui import gui_funcs
from ui.window_interface import WindowInterface
from typing import TYPE_CHECKING
from ui.album_page import album_window


if TYPE_CHECKING:
    from client.client_socket import ClientSocketHandler
    from music_playing.audio_handler import AudioHandler
    from client.shared_state import SharedState
    from client.window_manager import WindowManager
    from ui.album_page.album_window import AlbumWindow
from ui.user_profile.user_profile_window import UserProfileWindow


class SearchWindow(Ui_MainWindow, WindowInterface, QMainWindow): 
   def __init__(self, shared_state :'SharedState', window_manager :'WindowManager'):
      super(SearchWindow, self).__init__()
      self.socket_handler = shared_state.socket_handler
      self.audio_handler = shared_state.audio_handler
      self.window_manager = window_manager
      self.setupUi(self)
      self.setup_btns()