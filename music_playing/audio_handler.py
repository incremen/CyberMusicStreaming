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
from music_playing.song_queue import SongQueue


if TYPE_CHECKING:
    from backend.client.client_socket import ClientSocketHandler

CHUNK = 4096

class AudioHandler:
    def __init__(self, main_page_emitter :MainPageEmitter):
        self.p = pyaudio.PyAudio()
        self.stream = None
        self.main_page_emitter = main_page_emitter
        self.lock = threading.Lock()
        
        self.song_queue = SongQueue(main_page_emitter.update_song_queue)
        
        self.play_event = threading.Event()
        self.play_event.set()
        
        self.current_song_buffer : SongBuffer = None
        
        self.skip_song_flag : bool = False
        self.skip_song_lock = threading.Lock()
        self.skipped_song_event = threading.Event()
        
        self.socket_handler : 'ClientSocketHandler' = None
        
        self.done_playing_next_song = threading.Event()
        self.done_playing_next_song.set()
        
    def received_next_order(self, order):
        self.next_expected_order = order
        logging.debug(f"{self.next_expected_order=}")

    def skip_to_song(self, index):
        song = self.song_queue[index]
        order = song.order
        
        logging.checkpoint(f"About to skip to song#{order}")
        self.socket_handler.send_skip_to_song_event(order)
        self.play_event.clear()
        
        self.skip_current_song()
        logging.debug(f"Updated song queue after skipping current: {self.song_queue}")
        
        self.song_queue.clear_until_order(order)
        logging.debug(f"Updated song queue ({order=}): {self.song_queue}")
        
        self.play_event.set()
        self.play_next_song()
        
    @log_calls
    def add_to_song_queue(self, song_name :str):
        song_info = self.song_name_to_info[song_name]
        new_song_buffer = SongBuffer(song_info, self.next_expected_order)
        
        self.song_queue.append(new_song_buffer)
        logging.debug(f"Appended. {self.song_queue=}")
        
        self.next_expected_order += 1
        
    def song_list_received(self, song_list : list[dict[str, str]]):
        song_info_list = [SongInfo(**song_dict) for song_dict in song_list]
        self.song_name_to_info = {info.name : info for info in song_info_list}
        
        self.main_page_emitter.song_list_recieved.emit(song_list)
        
    
    def play_next_song(self):
        if not self.song_queue:
            logging.error("No more songs to play")
            return
                
        if self.current_song_buffer:
            logging.info("Can't start playing next song, current song is playing")
            return
        
        self.current_song_buffer = self.song_queue[0]
        logging.checkpoint(f"Starting to play next song: {self.current_song_buffer}")
        
        self.setup_stream()
        self.play_song()
        logging.checkpoint("Done playing song...")
        self.song_queue.pop(0)
        
        self.current_song_buffer = None
        self.play_next_song()

    def play_song(self):
        logging.checkpoint("Playing new song...")
        self.next_sequence_number = 0
        max_seq = self.current_song_buffer.info.max_seq
        while self.next_sequence_number < max_seq:
            logging.debug(f"{self.next_sequence_number=}, {max_seq=}")
            
            with self.skip_song_lock:
                if self.skip_song_flag:
                    self.reset_skip()
                    return
            
            logging.info("Waiting on play event...")
            self.play_event.wait()
            logging.info("Done waiting on play event...")
            
            self.await_next_seq_num() 
            logging.debug("Done waiting for seq num!")   
            self.write_song_data()
            self.emit_progress_to_bar()

    def reset_skip(self):
        self.skip_song_flag = False
        logging.info("Skipping song...")
        self.skipped_song_event.set()
        logging.debug("Set skipped song event")

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
        logging.debug(f"{song_chunk=}, {self.song_queue=}")
        
        for song_buffer in self.song_queue:
            if song_buffer.order == song_chunk.order:
                
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
    def skip_current_song(self):
        logging.info("Skipping song...")
        if not self.current_song_buffer:
            logging.info("Can't skip song, no song playing")
            return
        
        with self.skip_song_lock:
            self.skip_song_flag = True
            
        logging.debug("Waiting for skipped song event...")
        self.skipped_song_event.wait()
        logging.debug("Done waiting")
        self.skipped_song_event.clear()
        
        


