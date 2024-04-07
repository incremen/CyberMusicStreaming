from PyQt5.QtCore import QObject, pyqtSignal
from ui.user_profile.user_profile_window import UserProfileWindow

class ProfileWindowEmitter(QObject):
    user_info_received = pyqtSignal(list)
        
    def setup_connections(self, profile_window : UserProfileWindow):
        self.user_info_received.connect(profile_window.load_user_playlists)