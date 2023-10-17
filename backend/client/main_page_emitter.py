from PyQt5.QtCore import QObject, pyqtSignal
from frontend.main_page import MainPage
from music_playing.song_class import SongBuffer

class MainPageEmitter(QObject):
    song_list_recieved = pyqtSignal(list)
    update_song_progress = pyqtSignal(int)
    update_song_queue = pyqtSignal(list)
        
    def setup_connections(self, main_page : MainPage):
        self.song_list_recieved.connect(main_page.song_list_received)
        self.update_song_progress.connect(main_page.update_song_progress)
        self.update_song_queue.connect(main_page.update_song_queue)