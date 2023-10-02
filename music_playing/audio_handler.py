import logging
import pyaudio
from queue import Queue
from backend.client.main_page_emitter import MainPageEmitter
from music_playing.song_class import SongInfo, return_as_songinfo, SongBuffer
import threading
import time
from custom_logging import log_calls
CHUNK = 1024


class AudioHandler:
    def __init__(self, main_page_emitter :MainPageEmitter):
        self.p = pyaudio.PyAudio()
        self.stream = None
        self.main_page_emitter = main_page_emitter
        self.frames_played = 0
        self.lock = threading.Lock()
        
        self.songs_to_play :list[SongBuffer] = []
        
        self.play_event = threading.Event()
        self.play_event.set()

    @log_calls
    def add_to_song_queue(self, song_info :SongInfo):
        
        new_song_buffer = SongBuffer(song_info)
        self.songs_to_play.append(new_song_buffer)
        logging.debug(f"Appended. {self.songs_to_play=}")
        
        if len(self.songs_to_play) == 1:
            self.start_playing_next_song()
    
    @log_calls
    def start_playing_next_song(self):
        if not self.songs_to_play:
            logging.info("No more songs to play")
            return

        new_song_buffer = self.songs_to_play[0]
        new_song_info = new_song_buffer.info
        logging.debug(f"{new_song_info=}, {new_song_buffer=}")
        self.setup_stream(new_song_info)
        
        self.play_song(new_song_buffer)
        
        self.start_playing_next_song()

    def play_song(self, current_song_buffer : SongBuffer):
        logging.debug("Playing new song...")
        
        self.frames_played = 0
        progress = 0
        
        while progress < 100:
            self.play_event.wait()
            
            if current_song_buffer.empty():
                time.sleep(0.01)
                continue
            
            data = current_song_buffer.get()
            self.stream.write(data)
            self.frames_played += CHUNK
            progress = self.calculate_progress(current_song_buffer.info)
            self.main_page_emitter.update_song_progress.emit(progress)
            
        self.songs_to_play.pop(0)

    def setup_stream(self, song_info :SongInfo):
        logging.debug("Beginning of setup stream...")
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        
        self.stream = self.p.open(format=self.p.get_format_from_width(2),
                             channels=song_info.nchannels,
                             rate=song_info.framerate, 
                             output=True,
                             frames_per_buffer=CHUNK)

        self.stream.start_stream()
        logging.debug("Finished setting up stream...")

    def add_to_buffer(self, data, song_name):
        logging.debug(f"{song_name=}, {len(self.songs_to_play)=}")
        for song_buffer in self.songs_to_play:
            logging.debug(f"{song_buffer.info.name=}")
            if song_buffer.info.name != song_name:
                continue
            
            with self.lock:
                song_buffer.put(data)
            logging.debug("Added to buffer!")
            return
                
        logging.debug("Didn't find song in list")

    def calculate_progress(self, current_song_info):
        progress = int(self.frames_played * 100 *current_song_info.nchannels*2 / current_song_info.nframes)
        logging.debug(f"{self.frames_played=} / {current_song_info.nframes * current_song_info.nchannels=} = {progress}")
        return progress

    def terminate(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.frames_played = 0  
        
    def pause_or_resume(self):
        if self.play_event.is_set():
            self.play_event.clear()
        else:
            self.play_event.set()


