import sqlalchemy
import time
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QListWidget, QListWidgetItem, QApplication
from PyQt5.QtCore import Qt, QThread, pyqtSlot
import logging
from music_playing.song_class import SongInfo
from typing import TYPE_CHECKING
import threading
from custom_logging import log_calls
from ui.user_playlist_page.user_playlist_ui import Ui_MainWindow
from ui.user_playlist_page.user_playlist_config import PROGRESS_BAR_MAXIMUM
from ui.drag_drop_funcs import make_widget_draggable, make_widget_not_draggable, make_list_widget_accept_drops
from functools import partial
from ui import gui_funcs
from ui.window_interface import WindowInterface
from database import client_db_funcs
from dataclasses import asdict
from database.models import User, Playlist, Song
from database import utils
from ui.user_profile import user_profile_window
from ui.user_playlist_page.playlist_widget_emitter import PlaylistWidgetEmitter
from music_playing.emitting_list import EmittingList
from result import Ok, Err, Result, is_ok, is_err

if TYPE_CHECKING:
    from client.client_socket import ClientSocketHandler
    from music_playing.audio_handler import AudioHandler
    from client.shared_state import SharedState
    from client.window_manager import WindowManager
    


class UserPlaylistWindow(Ui_MainWindow, WindowInterface, QMainWindow): 
    def __init__(self, shared_state :'SharedState', window_manager :'WindowManager'):
        super(UserPlaylistWindow, self).__init__()

        self.setupUi(self)
        self.socket_handler = shared_state.socket_handler
        self.audio_handler = shared_state.audio_handler
        self.window_manager = window_manager
        self.login_manager = shared_state.login_manager
        self.setup_widgets()

        self.last_song_grid_row = 3
        self.last_song_grid_col = -1

        self.skip_lock = threading.Lock()
        self.song_list = []
            
        self.last_queue_emit_num = -1
        self.last_songs_played_emit_num = -1
        
        self.last_playlist_emit_num = -1
        
        self.song_btn_to_song_info : dict[QPushButton, SongInfo] = {}
        self.song_btn_text_to_song_info : dict[str, SongInfo] = {}
        
        self.playlist_widget_emitter = PlaylistWidgetEmitter()
        self.playlist_widget_emitter.setup_connections(self)
        
        self.songs_btns_text_in_playlist = EmittingList(self.playlist_widget_emitter.update_playlist)
        
    def start(self):
        self.right_tab_widget.setCurrentIndex(0)
        self.songs_btns_text_in_playlist = EmittingList(self.playlist_widget_emitter.update_playlist)
        self.playlist_name_edit.setText("New Playlist")
        self.play_list_widget.clear()
        self.play_list_widget.itemPressed.connect(self.item_pressed_with_button)
        self.play_list_widget.currentItemChanged.connect(self.playlist_item_changed)
        self.load_playlist_clicked()
        self.show()
        
    
    def setup_widgets(self):
        self.profile_btn.clicked.connect(self.profile_btn_click)
        
        self.search_bar.returnPressed.connect(self.search_bar_text_changed)
        self.skip_btn.clicked.connect(self.skip_btn_click)
        self.back_btn.clicked.connect(self.back_btn_click)
        self.pause_btn.clicked.connect(self.pause_btn_click)  
        self.song_queue_widget.itemClicked.connect(self.song_in_queue_click)
        
        self.progress_slider.setMaximum(PROGRESS_BAR_MAXIMUM)
        self.progress_slider.sliderPressed.connect(self.audio_handler.pause_or_resume_song)
        self.progress_slider.sliderReleased.connect(self.seek_in_song)
        
        make_list_widget_accept_drops(self.play_list_widget, self.add_btn_text_to_playlist)
        
        self.right_tab_widget.currentChanged.connect(self.tab_changed)
        self.on_change_to_queue_tab()
        self.right_tab_widget.setCurrentIndex(1)
        
        self.save_playlist_btn.clicked.connect(self.save_playlist_btn_clicked)
        
        self.play_btn.clicked.connect(self.play_btn_click)
        
        self.delete_btn.clicked.connect(self.delete_btn_click)
    
    def delete_btn_click(self):
        self.socket_handler.emit_to_server("delete_playlist", self.playlist_name_edit.text())
        self.hide()
        self.window_manager.start_window(user_profile_window.UserProfileWindow)
        
    def update_playlist_widget(self, songs : list, emit_num : int):
        if emit_num < self.last_playlist_emit_num:
            return
        
        self.play_list_widget.clear()
        for song in songs:
            gui_funcs.add_item_to_list_widget(self.play_list_widget, song)
        
    def playlist_item_changed(self, item):
        if item is not None:
            self.current_item = item

    def item_pressed_with_button(self, item):
        current_item = self.current_item
        logging.checkpoint(f"{current_item=}, {current_item.text()=}")
        text = current_item.text()
        
        button = QApplication.mouseButtons()
        if button == Qt.LeftButton:
            logging.info(f"Left clicked: {text}")
            song_info = self.song_btn_text_to_song_info[text]
            self.audio_handler.add_to_song_queue(song_info.name)
        elif button == Qt.RightButton:
            logging.info(f"Right clicked: {text}")
            self.remove_song_from_playlist_widget(text)

    def remove_song_from_playlist_widget(self, song_text):
        logging.checkpoint(f"Before: {self.songs_btns_text_in_playlist=}")
        try:
            self.songs_btns_text_in_playlist.remove(song_text)
        except:
            logging.error("Couldn't remove item unfortunately :(")
        logging.checkpoint(f"After: {self.songs_btns_text_in_playlist=}")
        
    def search_db(self, search_term : str = ""):
        logging.info(f"Searching db for {search_term}")
        self.socket_handler.emit_to_server("search_for_term", search_term)

    def search_result_received(self, songs_found : list[dict]):
        logging.debug(f"{songs_found=}")
        self.add_songs_to_btns(songs_found, enable_drag = True)
        self.audio_handler.setup_song_name_to_info(songs_found)
        
    def load_playlist_clicked(self):
        logging.debug("Showing users playlist...")
        profile_window = self.window_manager.get_window(user_profile_window.UserProfileWindow)
        last_playlist_result : Result = profile_window.get_last_clicked_playlist_name()
        
        logging.debug(f"{last_playlist_result=}")
        if last_playlist_result.is_err():
            self.playlist_name_edit.setText("New Playlist")
            return
        
        playlist_name = last_playlist_result.ok_value["name"]
        
        logging.debug(f"Last playlist: {playlist_name}")
        self.playlist_name_edit.setText(playlist_name)
        self.playlist_name_edit.setDisabled(True)
        
        to_load = None
        for user_playlist in self.login_manager.playlists:
            if user_playlist["name"] == playlist_name:
                to_load = user_playlist
        
        if not to_load:
            return
        self.add_loaded_songs_to_list(to_load)
        
    def play_btn_click(self):
        logging.info("Play button clicked...")
        for song in self.songs_btns_text_in_playlist:
            song_name = self.get_song_name_from_text(song)
            self.audio_handler.add_to_song_queue(song_name)
        
    def add_loaded_songs_to_list(self, playlist : Playlist):
        self.songs_btns_text_in_playlist.clear()
        self.play_list_widget.clear()
        
        for song in playlist["songs"]:
            song_text = self.get_song_widget_text(SongInfo(**song))
            self.songs_btns_text_in_playlist.append(song_text)
            self.song_btn_text_to_song_info[song_text] = SongInfo(**song)
            logging.checkpoint(f"Mid add: {self.songs_btns_text_in_playlist}")
        logging.checkpoint(f"After adding: {self.songs_btns_text_in_playlist=}")

    def query_db_for_song_list(self):
        session = client_db_funcs.create_session()
        user_playlist = client_db_funcs.get_first_playlist(session)
        logging.checkpoint(f"got {user_playlist=} from db")
        self.load_playlist(user_playlist)
        session.close()

    def load_playlist(self, playlist : Playlist):
        song_dict_list = [song.as_dict() for song in playlist.songs]
        self.audio_handler.setup_song_name_to_info(song_dict_list)
        self.song_list = song_dict_list
        self.add_songs_to_btns(self.song_list)
        
        self.right_tab_widget.setCurrentIndex(self.right_tab_widget.currentIndex)
        
    def log_thread(self):
        while True:
            time.sleep(4)
            logging.info(f"Currently: {self.songs_btns_text_in_playlist=}")
        
    def profile_btn_click(self):
        logging.info("Profile button clicked...")
        self.audio_handler.play_next_song_thread.kill_and_wait()
        self.audio_handler.clear_queue_and_played()
        self.audio_handler.stop_playing_song()
        self.window_manager.hide_window(UserPlaylistWindow)
        self.window_manager.start_window(user_profile_window.UserProfileWindow)
        
    def save_playlist_btn_clicked(self):
        playlist_name = self.playlist_name_edit.text()
        if playlist_name == "New Playlist":
            gui_funcs.create_message_box("Please enter a name for your new playlist.", "Can't save playlist")
        
        songs_in_playlist = [self.song_btn_text_to_song_info[btn_text] for btn_text in self.songs_btns_text_in_playlist]
        song_names = [song.name for song in songs_in_playlist]
        logging.checkpoint(f"Sending {song_names=}")
        self.socket_handler.emit_to_server("save_playlist", {"username" : self.login_manager.username, "songs" : song_names, "name" : playlist_name})
        
        
    def search_bar_text_changed(self):
        search_text = self.search_bar.text()
        logging.info(f"Search bar just searched for {search_text}")
        self.search_db(search_text)
        
    def add_btn_text_to_playlist(self, song_btn_text : str):
        if song_btn_text in self.songs_btns_text_in_playlist:
            logging.info("Already in playlist, not appending")
            return
        self.songs_btns_text_in_playlist.append(song_btn_text)
        logging.info("Added button to playlist...")
        logging.debug(f"{self.songs_btns_text_in_playlist=}")
        
    def tab_changed(self, index):
        #This is called initially befoer esongs are loaded
        if not self.song_list:
            return
        
        logging.debug(f"{index=}")
        if index == 0:
            self.add_songs_to_btns(self.song_list, enable_drag = True)
            
        elif index == 1:
            self.add_songs_to_btns(self.song_list, enable_drag = False)
            
        self.right_tab_widget.setCurrentIndex(index)

    def get_grid_btns(self):
        grid_widgets = gui_funcs.get_objects_from_boxlayout(self.song_grid)
        return [widget for widget in grid_widgets if isinstance(widget, QPushButton)]
    
    def on_change_to_queue_tab(self):
        logging.checkpoint("On change to main tab")
        grid_btns = self.get_grid_btns()
        for btn in grid_btns:
            make_widget_not_draggable(btn)
                
    def on_change_to_playlist_tab(self):
        logging.checkpoint("On change to playlist tab")
        grid_btns = self.get_grid_btns()
        for btn in grid_btns:
            make_widget_draggable(btn)
        
    def seek_in_song(self):
        self.audio_handler.seek_value(self.progress_slider.value())
        
    def add_songs_to_btns(self, songs : list, enable_drag = False):
        logging.debug(f"Received song list: {songs}")
        self.clear_all_song_btns(songs)
        
        for song_dict in songs:
            self.add_song_btn(enable_drag, song_dict)

    def add_song_btn(self, enable_drag, song_dict):
        song_info = SongInfo(**song_dict)
        song_text = self.get_song_widget_text(song_info)
        song_btn = self.create_song_btn(song_text)
        self.song_btn_text_to_song_info.update({song_text : song_info})
        
        if enable_drag:
            make_widget_draggable(song_btn)
                
        self.song_btn_to_song_info.update({song_btn : song_info})
        self.add_song_btn_to_grid(song_btn)

    def get_song_widget_text(self, song : Song | SongInfo):
        song_text = f"{song.name}\n {song.length} seconds"
        return song_text
    
    def get_song_name_from_text(self, text : str):
        return text.split("\n")[0]

    def clear_all_song_btns(self, songs):
        self.delete_from_grid(5)
        self.last_song_grid_row = 3
        self.last_song_grid_col = -1
        self.song_list = songs
        self.song_btn_to_song_info = {}

    def create_song_btn(self, song_text):
        song_btn = QPushButton(song_text)
            
        song_btn.setStyleSheet(""" 
                    border: 2px solid pink;
                    background-color: rgba(128, 128, 128, 128);
                    border-radius: 50px;
                    color: white; 
                    """)
            
        gui_funcs.set_custom_font(song_btn, "Helvetica", 10)
        return song_btn
            

        
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
            gui_funcs.add_item_to_list_widget(song_list_widget, song.name)

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
        
    def delete_from_grid(self, start_index):
        while self.song_grid.count() > start_index:
            item = self.song_grid.takeAt(start_index)
            widget = item.widget()
            if widget:
                widget.deleteLater()


        
    def song_btn_click(self):
        btn_clicked_data = self.song_btn_to_song_info[self.sender()]
        self.audio_handler.add_to_song_queue(btn_clicked_data.name)

        
    



        