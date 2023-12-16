from PyQt5.QtCore import QThread
from threading import Event
from typing import TYPE_CHECKING
import logging
if TYPE_CHECKING:
  from music_playing.audio_handler import AudioHandler

class PlayNextSongThread(QThread):
    def __init__(self, audio_handler : 'AudioHandler'):
      QThread.__init__(self)
      self.audio_handler = audio_handler
      self.continue_playing = Event()
      self.continue_playing.set()
      self.killed = False

    def run(self):
        while True:
            if self.killed:
                return
            self.continue_playing.wait()
            self.play_next_song()
            
    def play_next_song(self):
        if self.audio_handler.playing_song:
            logging.error("Already playing a song.")
            return
        if not self.audio_handler.song_queue:
            logging.error("No songs in queue to play...")
            return
        song_to_play = self.audio_handler.song_queue[0]
        
        self.audio_handler.play_song(song_to_play)
        self.audio_handler.song_queue.pop(0)
        
        self.audio_handler.songs_played.append(song_to_play)
            
    def skip_current_song(self):
        self.audio_handler.player.stop()

    def pause_playing(self):
        self.continue_playing.clear() 

    def resume_playing(self):
        self.continue_playing.set() 
        
    def kill_thread(self):
        self.killed = True
