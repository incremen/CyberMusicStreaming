from PyQt5.QtCore import QThread
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from music_playing.audio_handler import AudioHandler

class PlayNextSongThread(QThread):
    def __init__(self, audio_handler : 'AudioHandler'):
        QThread.__init__(self)
        self.audio_handler = audio_handler

    def run(self):
        self.audio_handler.play_next_song()