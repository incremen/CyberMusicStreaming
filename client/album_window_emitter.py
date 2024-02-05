from PyQt5.QtCore import QObject, pyqtSignal
from ui.album_page.album_window import AlbumWindow

class AlbumWindowEmitter(QObject):
    song_list_received = pyqtSignal(list)
    update_song_progress = pyqtSignal(int)
    update_song_queue = pyqtSignal(list, int)
    update_songs_played = pyqtSignal(list, int)
        
    def setup_album_page_connections(self, album_window : AlbumWindow):
        self.song_list_received.connect(album_window.song_list_received)
        self.update_song_progress.connect(album_window.update_song_progress)
        self.update_song_queue.connect(album_window.update_song_queue)
        self.update_songs_played.connect(album_window.update_songs_played)