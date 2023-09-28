from PyQt5.QtCore import QObject, pyqtSignal
from frontend.main_page import MainPage

class MainPageEmitter(QObject):
    song_list_recieved = pyqtSignal(list)
        
    def setup_connections(self, main_page : MainPage):
        self.song_list_recieved.connect(main_page.song_list_received)