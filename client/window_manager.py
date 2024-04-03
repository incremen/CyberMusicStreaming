from ui.login_page.login_window import LoginWindow
from ui.album_page.album_window import AlbumWindow
from ui.search_page.search_window import SearchWindow
from client.shared_state import SharedState
from ui.window_interface import WindowInterface
from ui.user_profile.user_profile_window import UserProfileWindow
from ui.signup_page.signup_window import SignupWindow
from ui.user_playlist_page.user_playlist_window import UserPlaylistWindow
import logging

class WindowManager:
    def __init__(self, shared_state : SharedState):
         self.shared_state = shared_state
         self.windows: dict[type[WindowInterface], WindowInterface] = {
           LoginWindow: LoginWindow(self.shared_state, self),
           AlbumWindow: AlbumWindow(self.shared_state, self),
           SearchWindow: SearchWindow(self.shared_state, self),
           UserProfileWindow: UserProfileWindow(self.shared_state, self),
           SignupWindow: SignupWindow(self.shared_state, self),
           UserPlaylistWindow: UserPlaylistWindow(self.shared_state, self)
       }
         
    def get_window(self, window_class):
        return self.windows[window_class]

    def start_window(self, window_class):
        window = self.windows.get(window_class)
        if window is None:
            error_msg = f"Window of class {window_class.__name__} not found"
            logging.error(error_msg)
            raise Exception(error_msg)
        
        window.start()

    def hide_window(self, window_class):
        window = self.windows.get(window_class)
        if window is not None:
            window.hide()




