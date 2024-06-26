from PyQt5.QtCore import QObject, pyqtSignal
from ui.user_profile.user_profile_window import UserProfileWindow

class ProfileWindowEmitter(QObject):
    load_user_playlists = pyqtSignal(dict)
        
    def setup_connections(self, profile_window : UserProfileWindow):
        self.load_user_playlists.connect(profile_window.load_user_playlists)