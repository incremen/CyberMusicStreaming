from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt, QThread, pyqtSlot
import logging
from music_playing.song_class import SongInfo
from typing import TYPE_CHECKING
import threading
from custom_logging import log_calls
from ui.album_page.album_window_ui import Ui_MainWindow
from ui.album_page.album_window_config import PROGRESS_BAR_MAXIMUM
from ui.search_page.search_window import SearchWindow
from ui.drag_drop_funcs import drag_enter_event, drop_event, mouse_move_event, mouse_press_event
from functools import partial

from ui.window_interface import WindowInterface


if TYPE_CHECKING:
    from client.client_socket import ClientSocketHandler
    from music_playing.audio_handler import AudioHandler
    from client.shared_state import SharedState
    from client.window_manager import WindowManager


class AlbumWindow(Ui_MainWindow, WindowInterface, QMainWindow): 
    def __init__(self, shared_state :'SharedState', window_manager :'WindowManager'):
        super(AlbumWindow, self).__init__()

        self.setupUi(self)
        self.socket_handler = shared_state.socket_handler
        self.audio_handler = shared_state.audio_handler
        self.window_manager = window_manager
        self.setup_widgets()
        

        self.last_song_grid_row = 2
        self.last_song_grid_col = -1

        self.skip_lock = threading.Lock()

        self.last_queue_emit_num = -1
        self.last_songs_played_emit_num = -1
       
    def start(self):
       self.socket_handler.emit_to_server("song_list_request")
       self.show()
       
    def setup_widgets(self):
        self.skip_btn.clicked.connect(self.skip_btn_click)
        self.back_btn.clicked.connect(self.back_btn_click)
        self.pause_btn.clicked.connect(self.pause_btn_click)  
        self.song_queue_widget.itemClicked.connect(self.song_in_queue_click)
        
        self.progress_slider.setMaximum(PROGRESS_BAR_MAXIMUM)
        self.progress_slider.sliderPressed.connect(self.audio_handler.pause_or_resume_song)
        self.progress_slider.sliderReleased.connect(self.seek_in_song)
        
        self.search_btn.clicked.connect(self.search_btn_click)
        self.play_list_widget.setAcceptDrops(True)
        self.song_queue_widget.dragEnterEvent = lambda event: drag_enter_event(self.song_queue_widget, event)
        self.song_queue_widget.dropEvent = lambda event: drop_event(self.song_queue_widget, event)
        self.song_queue_widget.dragMoveEvent = lambda event: drag_enter_event(self.song_queue_widget, event)
        
    def search_btn_click(self):
        self.window_manager.start_window(SearchWindow)
        self.hide()
        
    def seek_in_song(self):
        self.audio_handler.seek_value(self.progress_slider.value())
        
    def song_list_received(self, songs : list):
        logging.debug(f"Received song list: {songs}")
        self.btn_to_info = {}
        
        for song_dict in songs:
            song_info = SongInfo(**song_dict)
            song_text = f"{song_info.name}\n {song_info.length} seconds"
            song_btn = self.create_song_btn(song_text)
            song_btn.mousePressEvent = lambda event: mouse_press_event(song_btn, event)
            song_btn.mouseMoveEvent = lambda event: mouse_move_event(song_btn, event)
            
            self.btn_to_info.update({song_btn : song_info})
            self.add_song_btn_to_grid(song_btn)

    def create_song_btn(self, song_text):
        song_btn = QPushButton(song_text)
            
        song_btn.setStyleSheet(""" 
                    border: 2px solid pink;
                    background-color: rgba(128, 128, 128, 128);
                    border-radius: 50px;
                    color: white; 
                    """)
            
        self.set_custom_font(song_btn, "Helvetica", 10)
        return song_btn
            
    def set_custom_font(self, widget : QWidget, font_family, font_size):
        font = QFont(font_family, font_size)
        widget.setFont(font)
        
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

    def update_list_widget(self, song_list : list[SongInfo], song_list_widget : QListWidget):
        song_list_widget.clear()
        for song in song_list:
            self.add_item_to_queue(song_list_widget, str(song))
            
        # logging.info(f"{self.get_full_song_queue()=}")
        # logging.info(f"{song_list=}")
        
    def add_item_to_queue(self, song_list_widget : QListWidget, item_text):
        item = QListWidgetItem(item_text)
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.set_custom_font(item, "Helvetica", 15)
        song_list_widget.addItem(item)


    def skip_btn_click(self):
        self.skip_btn.setEnabled(False)
        self.audio_handler.stop_playing_song() 
        self.skip_btn.setEnabled(True)
        
    def back_btn_click(self):
        self.audio_handler.play_last_song()
        
    def pause_btn_click(self):
        self.audio_handler.pause_or_resume_song()
        
    def update_song_progress(self, progress):
        # logging.info(f"updating progress to {progress}")
        self.progress_slider.setValue(progress)
        
    def add_song_btn_to_grid(self, song_btn : QPushButton):
        song_btn.setFixedSize(200, 100)
        song_btn.clicked.connect(self.song_btn_click)
        self.last_song_grid_col += 1
        if self.last_song_grid_col == 3:
            self.last_song_grid_col = 0
            self.last_song_grid_row += 1
        self.song_grid.addWidget(song_btn, self.last_song_grid_row, self.last_song_grid_col)
        
    def song_btn_click(self):
        btn_clicked_data = self.btn_to_info[self.sender()]
        self.audio_handler.add_to_song_queue(btn_clicked_data.name)

        
    



        