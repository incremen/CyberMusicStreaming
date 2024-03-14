import os
from ui.album_page.album_window_config import PROGRESS_BAR_MAXIMUM
import logging
from client.window_emitter import WindowEmitter
from music_playing.song_class import SongInfo
from custom_logging import log_calls
from typing import TYPE_CHECKING
from music_playing.emitting_list import EmittingList
from music_playing.play_song_thread import PlayNextSongThread
from music_playing.update_progress_thread import SongProgressThread
import mpv
from backend import HLS_HOST, HLS_PORT
if TYPE_CHECKING:
    from client.client_socket import ClientSocketHandler

CHUNK = 4096

class AudioHandler:
    def __init__(self, main_page_emitter: 'WindowEmitter'):
        self.main_page_emitter = main_page_emitter
        self.song_queue = EmittingList(main_page_emitter.update_song_queue)
        self.songs_played = EmittingList(main_page_emitter.update_songs_played)
        self.player = mpv.MPV(
            # player_operation_mode='pseudo-gui',
            # script_opts='osc-layout=box,osc-seekbarstyle=bar,osc-deadzonesize=0,osc-minmousemove=3,osc-visibility=always',
            # input_default_bindings=True,
            # input_vo_keyboard=True,
            # osc=True,
        )
        
        self.song_name_to_info = {}
        
        self.play_next_song_thread = PlayNextSongThread(self)
        self.song_progress_thread = SongProgressThread(self)
        self.song_progress_thread.start()
        
        
    def start_play_next_song_thread(self):
        self.play_next_song_thread.killed = False
        if self.play_next_song_thread.isRunning():
            logging.error("play next song thread already running")
            return
        self.play_next_song_thread.start()


    def skip_to_song(self, index):
        logging.checkpoint(f"About to skip to song at index{index}")
        logging.checkpoint(f"Before skipping current\n{self.song_queue}\n")
        self.play_next_song_thread.pause_playing()
        self.stop_playing_song()
        logging.checkpoint(f"After skipping current\n{self.song_queue}\n")
        #drops one index because it skipped the current song.
        for _ in range(index-1):
            self.songs_played.append(self.song_queue.pop(0))
        logging.checkpoint(f"After\n{self.song_queue=}\n{self.songs_played=}\n")
        self.play_next_song_thread.resume_playing()
        
    def song_list_received(self, song_list : list[dict[str, str]]):
        song_info_list = [SongInfo(**song_dict) for song_dict in song_list]
        self.song_name_to_info = {info.name : info for info in song_info_list}
        
        self.main_page_emitter.song_list_recieved.emit(song_list)
        
    @log_calls
    def add_to_song_queue(self, song_name :str):
        try: 
            song_info = self.song_name_to_info[song_name]
        except KeyError:
            raise KeyError(f"Song not found: {song_name}")
        #     default_song_dict = {'framerate': 44100, 'length': 62.13451247165533, 'name': 'american', 'nchannels': 2, 'nframes': 2740132.0}
        #     song_info = SongInfo(**default_song_dict)
        
        self.song_queue.append(song_info)
        logging.debug(f"Appended. {self.song_queue=}")
        self.start_play_next_song_thread()
        
    def play_last_song(self):
        queue_length_before = len(self.song_queue)
        self.play_next_song_thread.kill_and_wait()
        self.player.stop()
        self.play_next_song_thread = PlayNextSongThread(self)
        logging.checkpoint(f"Before\n{self.song_queue=}\n{self.songs_played=}\n")
        if not self.songs_played:
            logging.error("No songs played")
            return
        
        times_to_queue = 2 if queue_length_before > 0 else 1
        
        for _ in range(times_to_queue):
            self.queue_last_played_song()
            
        logging.checkpoint(f"After\n{self.song_queue=}\n{self.songs_played=}\n")
        self.play_next_song_thread.start()

    def queue_last_played_song(self):
        last_song = self.songs_played.pop()
        self.song_queue.insert(0, last_song)
        
    @log_calls
    def play_song(self, song : SongInfo):
        url = f'http://{HLS_HOST}:{HLS_PORT}/{song.name}/index.m3u8'
        # url = f'songs/{song.name}'
        logging.checkpoint(f"\nPlaying {url=} because: \n{self.song_queue=}\n{self.songs_played=}\n")
        self.player.play(url)
        self.player.wait_for_playback()
        
    @log_calls
    def stop_playing_song(self):
        logging.info("Stopping song...")
        self.player.stop()
        
    @log_calls
    def pause_or_resume_song(self):
        self.player.pause = not self.player.pause
        
        logging.info("Song paused.")
        
    def seek_value(self, percentage):
        if not self.player.time_pos:
            if not self.songs_played:
                logging.error("Nothing to seek")
                return
            self.play_last_song()
        
        seek_position = self.player.duration * percentage / PROGRESS_BAR_MAXIMUM
        self.player.time_pos = seek_position
        self.player.pause = False
        logging.debug(f"Player now seeking {seek_position}")
        logging.debug(f"{self.player.time_pos=}")


        
        
        

