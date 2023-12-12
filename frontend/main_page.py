from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget, QGridLayout, QProgressBar, QListWidget, QVBoxLayout
from PyQt5 import uic, QtGui
from PyQt5.QtCore import Qt, QThread, pyqtSlot
import logging
from music_playing.song_class import SongInfo
from typing import TYPE_CHECKING
import threading
from custom_logging import log_calls
from frontend.main_page_ui import Ui_MainWindow
import pprint
if TYPE_CHECKING:
    from backend.client.client_socket import ClientSocketHandler
    from music_playing.audio_handler import AudioHandler
    
class MainPage(Ui_MainWindow, QMainWindow): 
    def __init__(self, socket_handler :'ClientSocketHandler', audio_handler :'AudioHandler'):
       super(MainPage, self).__init__()
       self.setupUi(self)
       self.socket_handler = socket_handler
       self.audio_handler = audio_handler
       self.setup_main_widget_properties()
       self.show()

       self.last_row = 0
       self.last_col = -1

       self.skip_lock = threading.Lock()

       self.last_queue_emit_num = -1
       self.last_songs_played_emit_num = -1
       
    def setup_main_widget_properties(self):
        self.skip_btn.clicked.connect(self.skip_btn_click)
        
        self.pause_btn.clicked.connect(self.pause_btn_click)  
        self.song_queue_widget.itemClicked.connect(self.song_in_queue_click)
        
    def song_list_received(self, songs : list):
        logging.debug(f"Received song list: {songs}")
        self.btn_to_info = {}
        
        for song_dict in songs:
            song_info = SongInfo(**song_dict)
            song_text = f"{song_info.name}\n {song_info.length} seconds"
            song_btn = QPushButton(song_text)
            
            self.btn_to_info.update({song_btn : song_info})
            self.add_song_to_grid(song_btn)
        
    def get_full_song_queue(self):
        item_text_list = [self.song_queue_widget.item(i).text() for i in range(self.song_queue_widget.count())]
        return item_text_list
        
    def song_in_queue_click(self):
        song_clicked = self.song_queue_widget.currentItem()
        index = self.song_queue_widget.row(song_clicked)
        logging.info(f"Index of song clicked {index}")    
        self.audio_handler.skip_to_song(index)
        self.socket_handler.send_skip_to_song_event(index)
        
    def update_songs_played(self, song_list : list[SongInfo], emit_num : int):
        if emit_num < self.last_songs_played_emit_num:
            logging.debug(f"{emit_num=}, {self.last_songs_played_emit_num=} so returning")
            return
        
        self.update_list_widget(song_list, self.songs_played_widget)
        self.last_songs_played_emit_num = emit_num
        
    def update_song_queue(self, song_list : list[SongInfo], emit_num : int):
        if emit_num < self.last_queue_emit_num:
            logging.debug(f"{emit_num=}, {self.last_queue_emit_num=} so returning")
            return
        
        self.update_list_widget(song_list, self.song_queue_widget)
        self.last_queue_emit_num = emit_num

    @log_calls    
    def update_list_widget(self, song_list : list[SongInfo], song_list_widget : QListWidget):
        song_list_widget.clear()
        for song in song_list:
            self.add_song_to_queue(song_list_widget, song)
            
        logging.info(f"{self.get_full_song_queue()=}")
        logging.info(f"{song_list=}")
        
    def add_song_to_queue(self, song_list_widget : QListWidget, song_buffer : SongInfo):
        song_text = song_buffer.__repr__()
        song_list_widget.addItem(song_text)

    def skip_btn_click(self):
        self.skip_btn.setEnabled(False)
        self.audio_handler.skip_current_song() 
        self.skip_btn.setEnabled(True)

    def enable_skip_button(self):
        self.skip_btn.setEnabled(True)
        
    def pause_btn_click(self):
        self.audio_handler.pause_or_resume_song()
        
    def update_song_progress(self, progress):
        logging.info(f"updating progress to {progress}")
        self.song_progress_bar.setValue(progress)
        
    def add_song_to_grid(self, song_btn):
        song_btn.setFixedSize(200, 100)
        song_btn.clicked.connect(self.song_btn_click)
        self.last_col += 1
        if self.last_col == 3:
            self.last_col = 0
            self.last_row += 1
        self.song_grid.addWidget(song_btn, self.last_row, self.last_col)
        
    def song_btn_click(self):
        btn_clicked_data = self.btn_to_info[self.sender()]
        self.audio_handler.add_to_song_queue(btn_clicked_data.name)

        
    



        