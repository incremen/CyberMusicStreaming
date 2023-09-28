from PyQt5.QtCore import QObject, pyqtSignal
from frontend.main_page import MainPage

class MainPageEmitter(QObject):
    song_dict_received = pyqtSignal(dict)
        
    def setup_connections(self, main_page : MainPage):
        self.song_dict_received.connect(main_page.add_song_to_grid)