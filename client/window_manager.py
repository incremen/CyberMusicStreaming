from ui.login_page.login_page import LoginWindow
from ui.album_page.album_window import AlbumWindow
from ui.search_page.search_window import SearchWindow
from client.shared_state import SharedState


class WindowManager:
    def __init__(self, shared_state : SharedState):
      self.shared_state = shared_state
      self.windows = {
          LoginWindow: LoginWindow(self.shared_state, self),
          AlbumWindow: AlbumWindow(self.shared_state, self),
          SearchWindow: SearchWindow(self.shared_state, self)
          # Add more windows as needed...
      }

    def start_window(self, window_class):
        window = self.windows.get(window_class)
        if window is not None:
            window.start()

    def hide_window(self, window_class):
        window = self.windows.get(window_class)
        if window is not None:
            window.hide()




