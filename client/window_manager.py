from ui.login_page.login_page import LoginWindow
from ui.main_page.main_window import MainWindow
from ui.search_page.search_window import SearchWindow
from client.shared_state import SharedState


class WindowManager:
    def __init__(self, shared_state : SharedState):
      self.shared_state = shared_state
      self.windows = {
          LoginWindow: LoginWindow(self.shared_state, self),
          MainWindow: MainWindow(self.shared_state, self),
          SearchWindow: SearchWindow(self.shared_state, self)
          # Add more windows as needed...
      }

    def show_window(self, window_class):
        window = self.windows.get(window_class)
        if window is not None:
            window.show()

    def hide_window(self, window_class):
        window = self.windows.get(window_class)
        if window is not None:
            window.hide()




