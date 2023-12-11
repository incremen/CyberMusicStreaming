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
from music_playing.song_queue import EmittingSongList
from music_playing.play_song_thread import PlayNextSongThread
import mpv
if TYPE_CHECKING:
    from backend.client.client_socket import ClientSocketHandler

CHUNK = 4096

class AudioHandler:
    def __init__(self, main_page_emitter: 'MainPageEmitter'):
        self.main_page_emitter = main_page_emitter
        self.song_queue = EmittingSongList(main_page_emitter.update_song_queue)
        self.songs_played = EmittingSongList(main_page_emitter.update_songs_played)
        self.current_song_index = 0
        self.player = mpv.MPV(
            player_operation_mode='pseudo-gui',
            script_opts='osc-layout=box,osc-seekbarstyle=bar,osc-deadzonesize=0,osc-minmousemove=3,osc-visibility=always',
            input_default_bindings=True,
            input_vo_keyboard=True,
            osc=True
        )
        
        self.play_next_song_thread = PlayNextSongThread(self)
        self.play_next_song_thread.start()
        
    def received_next_order(self, order):
        self.next_expected_order = order
        logging.debug(f"{self.next_expected_order=}")

    def skip_to_song(self, index):
        song = self.song_queue[index]
        order = song.order
        logging.debug(f"{self.next_expected_order=}")
        logging.checkpoint(f"About to skip to song#{order}")
        self.skip_current_song()
        
        logging.debug(f"Updated song queue after skipping current: {self.song_queue}")
        
        self.song_queue.clear_until_order(order)
        logging.debug(f"Updated song queue ({order=}): {self.song_queue}")
        
        self.continue_playing = True
        logging.debug(f"Trying to restart the thread...:")
        self.start_play_songs_thread()
        
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
        if self.current_song_index >= len(self.song_queue):
            print("Reached the end of the song queue.")
            return
        song_name = self.song_queue[self.current_song_index].info.name
        self.play_song(song_name)
        self.current_song_index += 1
        if self.current_song_index < len(self.song_queue):
            self.play_next_song()
        
    @log_calls
    def play_song(self, song_name):
        print("Playing song!")
        # url = f'http://{self.host}:{self.port}/{song_name}/index.m3u8'
        url = f'songs/{song_name}'
        logging.debug(f"Playing {url=}")
        self.player.play(url)
        
    @log_calls
    def skip_current_song(self):
        logging.info("Skipping song...")
        self.stop_song()
        
        self.socket_handler.send_skip_song_event()
        
        with self.skip_song_lock:
            self.skip_song_flag = True
            #play_song will get stuck forever in the loop if this event isn't set:
            self.play_event.set()
        logging.debug("Waiting for skipped song event...")
        self.skipped_song_event.wait()
        logging.debug("Done waiting")
        self.skipped_song_event.clear()
        
    def stop_song(self):
        self.player.stop()
        
        
        


