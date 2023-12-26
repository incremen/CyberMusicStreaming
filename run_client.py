from client.client_socket import ClientSocketHandler
import custom_logging
from PyQt5.QtWidgets import QApplication
from music_playing.audio_handler import AudioHandler
from client.main_page_emitter import WindowEmitter
from ui.login_page.login_page import LoginWindow
import sys
from client.shared_state import SharedState
from client.window_manager import WindowManager


def main():
  custom_logger = custom_logging.CustomLogger(log_files=["client.log"])
  custom_logger.clear_logs()
  app = QApplication(sys.argv)
  
  window_emitter = WindowEmitter()
  audio_handler = AudioHandler(window_emitter)
  client_socket_handler = ClientSocketHandler(audio_handler)
  
  shared_state = SharedState(socket_handler=client_socket_handler, audio_handler=audio_handler)
  window_manager = WindowManager(shared_state)
  
  window_manager.start_window(LoginWindow)
  
  client_socket_handler.connect()
  client_socket_handler.emit_to_server("song_list_request")
  app.exec_()
  
  
if __name__ == "__main__":
  main()


