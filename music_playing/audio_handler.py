import logging
import pyaudio
from queue import Queue
from backend.client.main_page_emitter import MainPageEmitter
from music_playing.song_class import SongInfo, return_as_songinfo
import threading
import time
from music_playing.song_info_and_buffer import SongInfoAndBuffer

CHUNK = 1024


class AudioHandler:
    def __init__(self, main_page_emitter :MainPageEmitter):
        self.p = pyaudio.PyAudio()
        self.stream = None
        self.current_song_buffer = Queue()
        self.main_page_emitter = main_page_emitter
        self.frames_played = 0
        self.current_song_info : SongInfo= None
        self.lock = threading.Lock()
        
        self.song_info_buffer_queue = Queue()

    def add_to_song_queue(self, song_info :SongInfo):
        song_buffer = Queue()
        
        song_queue_was_empty = self.song_info_buffer_queue.empty()
        self.song_info_buffer_queue.put( SongInfoAndBuffer(song_info, song_buffer ) )
        
        if song_queue_was_empty:
            self.start_playing_next_song()
    
    def start_playing_next_song(self):
        if self.song_info_buffer_queue.empty():
            logging.info("Queue is done")
            return
        
        self.current_song_info, self.current_song_buffer = self.song_info_buffer_queue.get()
        
        self.setup_stream()
        
        self.play_song()
        
        self.start_playing_next_song()

    def play_song(self):
        logging.debug("Playing new song...")
        
        self.frames_played = 0
        progress = 0
        
        while progress < 100:
            if self.current_song_buffer.empty():
                time.sleep(0.01)
            else:
                data = self.current_song_buffer.get()
                self.stream.write(data)
                self.frames_played += CHUNK * self.current_song_info.nchannels *2
                progress = self.calculate_progress()
                self.main_page_emitter.update_song_progress.emit(progress)

    def setup_stream(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        
        self.stream = self.p.open(format=self.p.get_format_from_width(2),
                             channels=self.current_song_info.nchannels,
                             rate=self.current_song_info.framerate, 
                             output=True,
                             frames_per_buffer=CHUNK)

        self.stream.start_stream()

    def add_to_buffer(self, data, song_name):
        with self.lock:
            song_buffer_list = list(self.song_info_buffer_queue)
            
            for song_info, song_buffer in song_buffer_list:
                if song_info.name == song_name:
                    song_buffer.put(data)
                    return
            
        logging.debug("Added data to buffer")

    def calculate_progress(self):
        progress = int(self.frames_played * 100 / self.current_song_info.nframes)
        logging.debug(f"{self.frames_played=} / {self.current_song_info.nframes * self.current_song_info.nchannels=} = {progress}")
        return progress


    def terminate(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.frames_played = 0  


