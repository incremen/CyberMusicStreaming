from client.client_socket import ClientSocketHandler
import custom_logging
from PyQt5.QtWidgets import QApplication
from music_playing.audio_handler import AudioHandler
from client.window_emitter import WindowEmitter
from ui.login_page.login_page import LoginWindow
import sys
from client.shared_state import SharedState
from client.window_manager import WindowManager
from ui.album_page.album_window import AlbumWindow

def main():
    custom_logger = custom_logging.CustomLogger(log_files=["client.log"])
    custom_logger.clear_logs()
    app = QApplication(sys.argv)
    
    window_emitter = WindowEmitter()
    audio_handler = AudioHandler(window_emitter)
    client_socket_handler = ClientSocketHandler(audio_handler, window_emitter)
    
    shared_state = SharedState(socket_handler=client_socket_handler, audio_handler=audio_handler)
    window_manager = WindowManager(shared_state)
    
    album_window = window_manager.get_window(AlbumWindow)
    window_emitter.setup_album_page_connections(album_window)
    
    window_manager.start_window(LoginWindow)
    
    client_socket_handler.connect()
    app.exec_()
  
  
if __name__ == "__main__":
    main()


