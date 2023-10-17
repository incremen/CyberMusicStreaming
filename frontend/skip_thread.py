from PyQt5.QtCore import Qt, QThread, pyqtSlot
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.client.client_socket import ClientSocketHandler
    from music_playing.audio_handler import AudioHandler
    
    
class SkipThread(QThread):
    def __init__(self, audio_handler : 'AudioHandler', socket_handler : 'ClientSocketHandler'):
        super().__init__()
        self.audio_handler = audio_handler
        self.socket_handler = socket_handler

    def run(self):
        self.socket_handler.send_skip_song_event()
        self.audio_handler.skip_song()