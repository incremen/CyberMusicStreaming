from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt, QThread, pyqtSlot
import logging
from music_playing.song_class import SongInfo
from typing import TYPE_CHECKING
import threading
from custom_logging import log_calls
from ui.album_page.album_window_ui import Ui_MainWindow
from ui.album_page.album_window_config import PROGRESS_BAR_MAXIMUM
from ui.search_page.search_window import SearchWindow


from ui.window_interface import WindowInterface


if TYPE_CHECKING:
    from client.client_socket import ClientSocketHandler
    from music_playing.audio_handler import AudioHandler
    from client.shared_state import SharedState
    from client.window_manager import WindowManager


class PlaylistWindow(Ui_MainWindow, WindowInterface, QMainWindow): 
    def __init__(self, shared_state :'SharedState', window_manager :'WindowManager'):
        super(PlaylistWindow, self).__init__()

        self.setupUi(self)
        self.socket_handler = shared_state.socket_handler
        self.audio_handler = shared_state.audio_handler
        self.window_manager = window_manager
        self.setup_widgets()
        
    def setup_widgets():
        
        