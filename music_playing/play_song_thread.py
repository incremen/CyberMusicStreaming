from PyQt5.QtCore import QThread
from threading import Event
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from music_playing.audio_handler import AudioHandler

class PlayNextSongThread(QThread):
    def __init__(self, audio_handler : 'AudioHandler'):
      QThread.__init__(self)
      self.audio_handler = audio_handler
      self.continue_playing = Event()
      self.kill_thread = False

    def run(self):
        while True:
            if self.kill_thread:
                return
            self.continue_playing.wait()
            self.audio_handler.play_next_song()
            
    def skip_current_song(self):
        self.audio_handler.player.stop()

    def pause_playing(self):
        self.continue_playing.clear() 

    def resume_playing(self):
        self.continue_playing.set() 
        
    def kill_thread(self):
        self.kill_thread = True
