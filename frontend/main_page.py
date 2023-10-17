from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget, QGridLayout, QProgressBar, QListWidget
from PyQt5 import uic, QtGui
from PyQt5.QtCore import Qt, QThread, pyqtSlot
import logging
from music_playing.song_class import SongInfo, SongBuffer
from typing import TYPE_CHECKING
import threading

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
        self.setup_main_widget_properties()
        
        self.show()
        
        self.last_row = 0
        self.last_col = -1
        
        self.skip_lock = threading.Lock()
        
    def song_list_received(self, songs : list):
        logging.debug(f"Received song list: {songs}")
        self.btn_to_data = {}
        
        for song_dict in songs:
            logging.debug(f"{song_dict=}")
            song_data = SongInfo(**song_dict)
            logging.debug(f"{song_data=}")
            song_text = f"{song_data.name}\n {song_data.length} seconds"
            song_btn = QPushButton(song_text)
            
            self.btn_to_data.update({song_btn : song_data})
            self.add_song_to_grid(song_btn)
            
    def setup_main_widget_properties(self):
        main_widget = self.main_widget
        self.song_grid = main_widget.findChild(QGridLayout, "song_grid")
        
        self.song_progress = main_widget.findChild(QProgressBar, "song_progress")
        
        self.skip_btn = main_widget.findChild(QPushButton, "skip_btn")
        self.skip_btn.clicked.connect(self.skip_btn_click)
        
        self.pause_btn = main_widget.findChild(QPushButton, "pause_btn")
        self.pause_btn.clicked.connect(self.pause_btn_click)  
        
        self.song_queue = main_widget.findChild(QListWidget, "song_queue")  
        self.song_queue.itemClicked.connect(self.song_in_queue_click)
        
    def song_in_queue_click(self):
        song_clicked = self.song_queue.currentItem()
        index = self.song_queue.row(song_clicked)
        logging.info(f"Index of song clicked {index}")    
        self.audio_handler.skip_to_song(index)
    
    def add_song_to_queue(self, song_buffer : SongBuffer):
        song_text = song_buffer.__repr__()
        self.song_queue.addItem(song_text)
    
    def update_song_queue(self, song_list : list[SongBuffer]):
        self.song_queue.clear()
        for song in song_list:
            self.add_song_to_queue(song)

    def skip_song_thread(self):
        self.audio_handler.skip_song()
        self.socket_handler.send_skip_song_event()

    def skip_btn_click(self):
        self.skip_btn.setEnabled(False)
        self.audio_handler.skip_song() 
        self.socket_handler.send_skip_song_event()
        self.skip_btn.setEnabled(True)

    def enable_skip_button(self):
        self.skip_btn.setEnabled(True)
        
    def pause_btn_click(self):
        self.audio_handler.pause_or_resume()
        
    def update_song_progress(self, progress):
        logging.info(f"updating progress to {progress}")
        self.song_progress.setValue(progress)
        
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
        

        
    



        