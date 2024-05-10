import logging
from ui.miniplayer.miniplayer_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QListWidget, QListWidgetItem
from ui import gui_funcs
from ui.window_interface import WindowInterface
from typing import TYPE_CHECKING
from ui.album_page import album_window
import threading
from ui.user_playlist_page.user_playlist_config import PROGRESS_BAR_MAXIMUM
from music_playing.song_class import SongInfo
if TYPE_CHECKING:
    from client.shared_state import SharedState
    from client.window_manager import WindowManager


class MiniplayerWindow(Ui_MainWindow, WindowInterface, QMainWindow): 
    def __init__(self, shared_state :'SharedState', window_manager :'WindowManager'):
        super(MiniplayerWindow, self).__init__()

        self.setupUi(self)
        self.socket_handler = shared_state.socket_handler
        self.audio_handler = shared_state.audio_handler
        self.window_manager = window_manager
        self.login_manager = shared_state.login_manager
        self.setup_widgets()

        self.last_song_grid_row = 3
        self.last_song_grid_col = -1

        self.skip_lock = threading.Lock()

        self.last_queue_emit_num = -1
        self.last_songs_played_emit_num = -1
        
        self.last_playlist_emit_num = -1
        
    def start(self):
        self.show()
    
    def setup_widgets(self):
        self.skip_btn.clicked.connect(self.skip_btn_click)
        self.back_btn.clicked.connect(self.back_btn_click)
        self.pause_btn.clicked.connect(self.pause_btn_click)  
        self.song_queue_widget.itemClicked.connect(self.song_in_queue_click)
        
        self.progress_slider.setMaximum(PROGRESS_BAR_MAXIMUM)
        self.progress_slider.sliderPressed.connect(self.audio_handler.pause_or_resume_song)
        self.progress_slider.sliderReleased.connect(self.seek_in_song)
        
    def skip_btn_click(self):
        self.skip_btn.setEnabled(False)
        self.audio_handler.stop_playing_song() 
        self.skip_btn.setEnabled(True)
        
    def back_btn_click(self):
        self.audio_handler.play_last_song()
        
    def pause_btn_click(self):
        self.audio_handler.pause_or_resume_song()
        
    def song_in_queue_click(self):
        song_clicked = self.song_queue_widget.currentItem()
        index = self.song_queue_widget.row(song_clicked)
        logging.info(f"Index of song clicked {index}")    
        self.audio_handler.skip_to_song(index)
        self.socket_handler.send_skip_to_song_event(index)
      
    def update_song_progress(self, progress):
        self.progress_slider.setValue(progress)
        
    def update_song_queue(self, song_list : list[SongInfo], emit_num : int):
        if emit_num < self.last_queue_emit_num:
            logging.debug(f"{emit_num=}, {self.last_queue_emit_num=} so returning")
            return
        
        if song_list:
            self.song_name_label.setText(song_list[0].name)
        self.update_list_widget(song_list, self.song_queue_widget)
        self.last_queue_emit_num = emit_num

    def update_list_widget(self, song_list : list[SongInfo], song_list_widget : QListWidget):
        song_list_widget.clear()
        for song in song_list:
            gui_funcs.add_item_to_list_widget(song_list_widget, song.name)
            
    def update_songs_played(self, song_list : list[SongInfo], emit_num : int):
        if emit_num < self.last_songs_played_emit_num:
            logging.debug(f"{emit_num=}, {self.last_songs_played_emit_num=} so returning")
            return
        
        self.update_list_widget(song_list, self.songs_played_widget)
        self.last_songs_played_emit_num = emit_num
        
        
    def seek_in_song(self):
        self.audio_handler.seek_value(self.progress_slider.value())