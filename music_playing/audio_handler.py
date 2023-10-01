import logging
import pyaudio
import queue
from backend.client.main_page_emitter import MainPageEmitter
from music_playing.song_class import SongInfo, return_as_songinfo
import threading
import time

CHUNK = 8000

class AudioHandler:
    def __init__(self, main_page_emitter :MainPageEmitter):
        self.p = pyaudio.PyAudio()
        
        self.stream = None
        self.buffer = queue.Queue()
        self.main_page_emitter = main_page_emitter
        self.frames_played = 0
        
        self.song_info : SongInfo= None
        self.lock = threading.Lock()
        self.stream.start_stream()
        
class AudioHandler:
    def __init__(self, main_page_emitter :MainPageEmitter):
        self.p = pyaudio.PyAudio()
        self.stream = None
        self.buffer = queue.Queue()
        self.main_page_emitter = main_page_emitter
        self.frames_played = 0
        self.song_info : SongInfo= None
        self.lock = threading.Lock()

    def start_playing(self, song_info : SongInfo):
        self.frames_played = 0
        self.song_info = song_info

        self.setup_stream()

        progress = 0
        
        while progress < 100:
            data = self.buffer.get()
            self.stream.write(data)
            self.frames_played += CHUNK
            progress = self.calculate_progress()
            self.main_page_emitter.update_song_progress.emit(progress)

    def setup_stream(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        
        self.stream = self.p.open(format=self.p.get_format_from_width(2),
                             channels=1,
                             rate=self.song_info.framerate, 
                             output=True,
                             frames_per_buffer=CHUNK)

        self.stream.start_stream()

    def add_to_buffer(self, data):
        with self.lock:
            self.buffer.put(data)
        logging.debug("Added data to buffer")

    def calculate_progress(self):
        progress = (self.frames_played / self.song_info.nframes) * 100
        logging.debug(f"{self.frames_played=} / {self.song_info.nframes=} = {progress}")
        return progress

    def terminate(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.frames_played = 0  


