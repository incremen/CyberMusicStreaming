from ui.login_page.login_page import LoginWindow
from ui.main_page.main_page import MainPage
from ui.search_page.search_page import SearchWindow
from client.shared_state import SharedState


class WindowManager:
    def __init__(self, shared_state : SharedState):
      self.shared_state = shared_state
      self.windows = {
          LoginWindow: LoginWindow(self.shared_state),
          MainPage: MainPage(self.shared_state),
          SearchWindow: SearchWindow(self.shared_state)
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




