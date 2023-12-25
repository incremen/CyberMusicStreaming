from ui.login_page.login_page import LoginWindow
from ui.main_page.main_page import MainPage
from ui.search_page.search_page import SearchWindow


class WindowManager:
  def __init__(self, shared_state):
      self.shared_state = shared_state
      self.windows = {
          LoginWindow: LoginWindow(self.shared_state.socket_handler, self.shared_state.audio_handler)
          # Add more windows as needed...
      }

  def show_window(self, window_class):
      window = next((window for window in self.windows.values() if isinstance(window, window_class)), None)
      if window is not None:
          window.show()

  def hide_window(self, window_class):
      window = next((window for window in self.windows.values() if isinstance(window, window_class)), None)
      if window is not None:
          window.hide()

  def get_socket_handler(self):
      return self.shared_state.socket_handler

  def get_audio_handler(self):
      return self.shared_state.audio_handler

  # Add more methods as needed to manage your windows...
