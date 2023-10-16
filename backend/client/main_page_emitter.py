from PyQt5.QtCore import QObject, pyqtSignal
from frontend.main_page import MainPage
from music_playing.song_class import SongBuffer

class MainPageEmitter(QObject):
    song_list_recieved = pyqtSignal(list)
    update_song_progress = pyqtSignal(int)
    add_song_to_queue = pyqtSignal(SongBuffer)
        
    def setup_connections(self, main_page : MainPage):
        self.song_list_recieved.connect(main_page.song_list_received)
        self.update_song_progress.connect(main_page.update_song_progress)
        self.add_song_to_queue.connect(main_page.add_song_to_queue)