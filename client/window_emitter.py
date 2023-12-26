from PyQt5.QtCore import QObject, pyqtSignal
from ui.album_page.album_window import AlbumWindow

class WindowEmitter(QObject):
    song_list_recieved = pyqtSignal(list)
    update_song_progress = pyqtSignal(int)
    update_song_queue = pyqtSignal(list, int)
    update_songs_played = pyqtSignal(list, int)
        
    def setup_main_page_connections(self, main_page : AlbumWindow):
        self.song_list_recieved.connect(main_page.song_list_received)
        self.update_song_progress.connect(main_page.update_song_progress)
        self.update_song_queue.connect(main_page.update_song_queue)
        self.update_songs_played.connect(main_page.update_songs_played)