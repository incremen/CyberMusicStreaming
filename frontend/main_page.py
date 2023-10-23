from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget, QGridLayout, QProgressBar, QListWidget, QVBoxLayout
from PyQt5 import uic, QtGui
from PyQt5.QtCore import Qt, QThread, pyqtSlot
import logging
from music_playing.song_class import SongInfo, SongBuffer
from typing import TYPE_CHECKING
import threading
from custom_logging import log_calls
from frontend import gui_funcs
import pprint
if TYPE_CHECKING:
    from backend.client.client_socket import ClientSocketHandler
    from music_playing.audio_handler import AudioHandler
    

class MainPage(QMainWindow):
    def __init__(self, socket_handler :'ClientSocketHandler', audio_handler :'AudioHandler'):
        super(MainPage, self).__init__()
        self.socket_handler = socket_handler
        self.audio_handler = audio_handler
        
        uic.loadUi(r"frontend\main_page.ui", self)
        self.setWindowTitle(f"Stream music!")
        
        self.main_widget = self.findChild(QWidget, "main_widget")
        self.name_to_item = gui_funcs.get_name_to_item_recursive(self.main_widget)
        pprint.pprint(self.name_to_item)
        
        self.setup_main_widget_properties()
        
        self.show()
        
        self.last_row = 0
        self.last_col = -1
        
        self.skip_lock = threading.Lock()
        
        self.last_signal_num = -1
        
    def song_list_received(self, songs : list):
        logging.debug(f"Received song list: {songs}")
        self.btn_to_data = {}
        
        for song_dict in songs:
            song_data = SongInfo(**song_dict)
            song_text = f"{song_data.name}\n {song_data.length} seconds"
            song_btn = QPushButton(song_text)
            
            self.btn_to_data.update({song_btn : song_data})
            self.add_song_to_grid(song_btn)
            
    def setup_main_widget_properties(self):
        self.song_grid = self.name_to_item["song_grid"]
        
        self.song_btns_layout = self.name_to_item["song_btns_layout"]
        self.init_song_btns_layout()
        
        self.song_lists_layout = self.name_to_item["song_queue_layout"]
        self.init_song_list_widgets()


    def init_song_btns_layout(self):
        name_to_item = self.name_to_item
        
        self.skip_btn = name_to_item["skip_btn"]
        self.skip_btn.clicked.connect(self.skip_btn_click)
        
        self.pause_btn = name_to_item["pause_btn"]
        self.pause_btn.clicked.connect(self.pause_btn_click)
        
        self.back_btn = name_to_item["back_btn"]
        
        self.song_progress_layout = name_to_item["song_progress_layout"]
        self.song_progress_bar = name_to_item["song_progress_bar"]

    def init_song_list_widgets(self):
        self.song_queue_widget = self.name_to_item["song_queue_widget"]
        self.song_queue_widget.itemClicked.connect(self.song_in_queue_click)
        
        self.songs_played_widget = self.name_to_item["songs_played_widget"]
        
    def get_full_song_queue(self):
        item_text_list = [self.song_queue_widget.item(i).text() for i in range(self.song_queue_widget.count())]
        return item_text_list
        
    def song_in_queue_click(self):
        song_clicked = self.song_queue_widget.currentItem()
        index = self.song_queue_widget.row(song_clicked)
        logging.info(f"Index of song clicked {index}")    
        self.audio_handler.skip_to_song(index)
        self.socket_handler.send_skip_to_song_event(index)
    
    def add_song_to_queue(self, song_buffer : SongBuffer):
        song_text = song_buffer.__repr__()
        self.song_queue_widget.addItem(song_text)
    
    @log_calls    
    def update_song_queue(self, song_list : list[SongBuffer], signal_num : int):
        if signal_num < self.last_signal_num:
            logging.info("Ignoring this signal cuz it wasnt the last")
            logging.debug(f"{signal_num=}, {self.last_signal_num=}")
            return
        
        self.song_queue_widget.clear()
        for song in song_list:
            self.add_song_to_queue(song)
            
        logging.info(f"{self.get_full_song_queue()=}")
        logging.info(f"{song_list=}")
        
        self.last_signal_num = signal_num

    def skip_btn_click(self):
        self.skip_btn.setEnabled(False)
        self.audio_handler.skip_current_song() 
        self.skip_btn.setEnabled(True)

    def enable_skip_button(self):
        self.skip_btn.setEnabled(True)
        
    def pause_btn_click(self):
        self.audio_handler.pause_or_resume()
        
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
        btn_clicked_data = self.btn_to_data[self.sender()]
        self.audio_handler.add_to_song_queue(btn_clicked_data.name)
        self.socket_handler.request_song(btn_clicked_data.name)
        

        
    



        