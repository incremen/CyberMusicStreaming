from PyQt5.QtCore import QObject, pyqtSignal
from typing import TYPE_CHECKING

class PlaylistWidgetEmitter(QObject):
    update_playlist = pyqtSignal(list, int)
        
    def setup_connections(self, user_playlist_window ):
        self.update_playlist.connect(user_playlist_window.update_playlist_widget)