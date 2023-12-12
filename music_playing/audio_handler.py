import eventlet
import logging
import pyaudio
from queue import Queue
from backend.client.main_page_emitter import MainPageEmitter
from music_playing.song_class import SongInfo
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
        self.player = mpv.MPV(
            player_operation_mode='pseudo-gui',
            script_opts='osc-layout=box,osc-seekbarstyle=bar,osc-deadzonesize=0,osc-minmousemove=3,osc-visibility=always',
            input_default_bindings=True,
            input_vo_keyboard=True,
            osc=True
        )
        self.next_expected_order = 0
        self.play_next_song_thread = PlayNextSongThread(self)
        self.playing_song = False
        
    def start_play_next_song_thread(self):
        if self.play_next_song_thread.isRunning():
            logging.error("play next song thread already running")
            return
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
        song_info.order = self.next_expected_order
        
        self.song_queue.append(song_info)
        logging.debug(f"Appended. {self.song_queue=}")
        self.next_expected_order += 1
        self.start_play_next_song_thread()
        
    def song_list_received(self, song_list : list[dict[str, str]]):
        song_info_list = [SongInfo(**song_dict) for song_dict in song_list]
        self.song_name_to_info = {info.name : info for info in song_info_list}
        
        self.main_page_emitter.song_list_recieved.emit(song_list)
    
    def play_next_song(self):
        if self.playing_song:
            logging.error("Already playing a song.")
            return
        if not self.song_queue:
            logging.error("No songs in queue to play...")
            return
        song_to_play = self.song_queue[0]
        self.play_song(song_to_play)
        self.song_queue.pop(0)
        self.songs_played.append(song_to_play)
        self.play_next_song()
        
    @log_calls
    def play_song(self, song : SongInfo):
        self.playing_song = True
        print("Playing song!")
        # url = f'http://{self.host}:{self.port}/{song_name}/index.m3u8'
        url = f'songs/{song.name}'
        logging.debug(f"Playing {url=}")
        self.player.play(url)
        self.player.wait_for_playback()
        self.playing_song = False
        
    @log_calls
    def skip_current_song(self):
        logging.info("Skipping song...")
        self.player.stop()
        
    @log_calls
    def pause_or_resume_song(self):
        if not self.playing_song:
            logging.error("No song is currently playing.")
            return
        self.player.pause = not self.player.pause
        logging.info("Song paused.")

        
        
        


