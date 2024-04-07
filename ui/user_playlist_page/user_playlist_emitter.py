from PyQt5.QtCore import QObject, pyqtSignal
from ui.user_playlist_page.user_playlist_window import UserPlaylistWindow

class PlaylistWindowEmitter(QObject):
    search_result_received = pyqtSignal(list)
        
    def setup_connections(self, playlist_window : UserPlaylistWindow):
        self.search_result_received.connect(playlist_window.search_result_received)
