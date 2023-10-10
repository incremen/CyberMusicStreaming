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
        
        self.current_song_buffer : SongBuffer = None
        
        self.skip_song_flag : bool = False
        
        self.buffer_empty_condition = threading.Condition()

    @log_calls
    def add_to_song_queue(self, song_info :SongInfo):
        
        new_song_buffer = SongBuffer(song_info)
        self.songs_to_play.append(new_song_buffer)
        logging.debug(f"Appended. {self.songs_to_play=}")
        
        if len(self.songs_to_play) == 1:
            self.start_playing_next_song()
            
    def current_song_buffer_not_empty(self):
        return not self.current_song_buffer.empty()
    
    @log_calls
    def start_playing_next_song(self):
        if not self.songs_to_play:
            logging.info("No more songs to play")
            return

        self.current_song_buffer = self.songs_to_play[0]
        
        logging.debug(f"{self.current_song_buffer=}")
        self.setup_stream()
        
        self.play_song()
        logging.info("Done playing song...")
        self.songs_to_play.pop(0)
        
        self.current_song_buffer = None
        
        self.start_playing_next_song()

    def play_song(self):
        logging.debug("Playing new song...")
        self.frames_played = 0
        progress = 0
        
        while progress < 100:
            if self.skip_song_flag:
                self.skip_song_flag = False
                logging.info("Skipping song...")
                break
            
            logging.info("waiting for buffer to not be empty...")
            
            self.await_song_playing_conditions()
            
            self.write_song_data()
            progress = self.calculate_progress()
            self.main_page_emitter.update_song_progress.emit(progress)
            

    def write_song_data(self):
        data = self.current_song_buffer.get()
        self.stream.write(data)
        self.frames_played += CHUNK


    def await_song_playing_conditions(self):
        with self.buffer_empty_condition:
            self.buffer_empty_condition.wait_for(self.current_song_buffer_not_empty)
            
        self.play_event.wait()

    def setup_stream(self):
        logging.debug("Beginning of setup stream...")
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        
        song_info = self.current_song_buffer.info
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
            if song_buffer.info.name != song_name:
                continue
            
            with self.lock:
                song_buffer.put(data)
            logging.debug("Added to buffer!")
            return
                
        logging.debug("Didn't find song in list")

    def calculate_progress(self):
        current_song_info = self.current_song_buffer.info
        progress = int(self.frames_played * 100 *current_song_info.nchannels*2 / current_song_info.nframes)
        logging.debug(f"{self.frames_played=} / {current_song_info.nframes * current_song_info.nchannels=} = {progress}")
        return progress
        
    def pause_or_resume(self):
        if self.play_event.is_set():
            self.play_event.clear()
        else:
            self.play_event.set()
    
    @log_calls
    def skip_song(self):
        logging.info("Skipping song...")
        if not self.current_song_buffer:
            logging.info("Can't skip song, no song playing")
            return
        
        self.skip_song_flag = True


