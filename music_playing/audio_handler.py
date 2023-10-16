import eventlet
import logging
import pyaudio
from queue import Queue
from backend.client.main_page_emitter import MainPageEmitter
from music_playing.song_class import SongInfo, SongBuffer, SongChunk
import threading
import time
from custom_logging import log_calls
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.client.client_socket import ClientSocketHandler

CHUNK = 4096

class AudioHandler:
    def __init__(self, main_page_emitter :MainPageEmitter):
        self.p = pyaudio.PyAudio()
        self.stream = None
        self.main_page_emitter = main_page_emitter
        self.lock = threading.Lock()
        
        self.songs_to_play :list[SongBuffer] = []
        
        self.play_event = threading.Event()
        self.play_event.set()
        
        self.current_song_buffer : SongBuffer = None
        
        self.skip_song_flag : bool = False
        self.socket_handler : 'ClientSocketHandler' = None
        
        self.next_expected_order = 0

    @log_calls
    def add_to_song_queue(self, song_info :SongInfo, song_order : int):
        new_song_buffer = SongBuffer(song_info, song_order)
        
        if new_song_buffer.order != self.next_expected_order:
            logging.error(f"Song orders don't match! {new_song_buffer.order=}, {self.next_expected_order=}")
            raise Exception(f"Song orders don't match! {new_song_buffer.order=}, {self.next_expected_order=}")
        
        self.songs_to_play.append(new_song_buffer)
        
        logging.debug(f"Appended. {self.songs_to_play=}")
        self.next_expected_order += 1
        
    def song_list_received(self, song_list : list[dict[str, str]]):
        song_info_list = [SongInfo(**song_dict) for song_dict in song_list]
        self.song_name_to_info = {info.name : info for info in song_info_list}
    
    def play_next_song(self):
        if not self.songs_to_play:
            logging.error("No more songs to play")
            return
                
        if self.current_song_buffer:
            logging.info("Can't start playing next song, current song is playing")
            return
        
        self.current_song_buffer = self.songs_to_play[0]
        logging.checkpoint(f"Starting to play next song: {self.current_song_buffer}")
        
        self.setup_stream()
        self.play_song()
        logging.info("Done playing song...")
        self.songs_to_play.pop(0)
        
        self.current_song_buffer = None
        
        self.play_next_song()

    def play_song(self):
        logging.checkpoint("Playing new song...")
        self.next_sequence_number = 0
        max_seq = self.current_song_buffer.info.max_seq
        
        
        while self.next_sequence_number < max_seq:
            logging.debug(f"{self.next_sequence_number=}, {max_seq=}")
            
            if self.skip_song_flag:
                self.skip_song_flag = False
                logging.info("Skipping song...")
                break
            
            self.play_event.wait()
            self.await_next_seq_num() 
            logging.debug("Done waiting for seq num!")   
            self.write_song_data()
            self.emit_progress_to_bar()
        logging.checkpoint("Done playing song...")

    def write_song_data(self):
        data = self.current_song_buffer.pop(self.next_sequence_number)
        self.stream.write(data)
        self.next_sequence_number += 1
        
    def await_next_seq_num(self):
        logging.debug(f"Waiting for {self.next_sequence_number}, {self.current_song_buffer=}")
        while self.next_sequence_number not in self.current_song_buffer:
            eventlet.sleep(0.01)
            
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

    def add_to_buffer(self, song_chunk : SongChunk):
        logging.debug(f"{song_chunk=}, {self.songs_to_play=}")
        
        for song_buffer in self.songs_to_play:
            if song_buffer.order != song_chunk.order:
                continue
            
            song_buffer[song_chunk.seq] = song_chunk.chunk
            logging.debug("Added to buffer!")
            return
                

    def emit_progress_to_bar(self):
        progress = int(self.next_sequence_number* 100 /self.current_song_buffer.info.max_seq)
        self.main_page_emitter.update_song_progress.emit(progress)
        
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


