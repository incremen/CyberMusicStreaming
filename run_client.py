from client.client_socket import ClientSocketHandler
import custom_logging
from PyQt5.QtWidgets import QApplication
from music_playing.audio_handler import AudioHandler
from client.window_emitter import WindowEmitter
from ui.login_page.login_window import LoginWindow
import sys
from client.shared_state import SharedState
from client.window_manager import WindowManager
from ui.album_page.album_window import AlbumWindow
from ui.search_page.search_window import SearchWindow
from ui.signup_page.signup_window import SignupWindow
from database.login_manager import LoginManager
from database import SQLITE_PATH
from ui.user_playlist_page.user_playlist_window import UserPlaylistWindow


def main():
    custom_logger = custom_logging.CustomLogger(log_files=["client.log"], log_to_console = False)
    custom_logger.clear_logs()
    app = QApplication(sys.argv)
    
    album_emitter = WindowEmitter()
    audio_handler = AudioHandler(album_emitter)
    client_socket_handler = ClientSocketHandler(audio_handler, album_emitter)
    
    login_manager = LoginManager(SQLITE_PATH)
    shared_state = SharedState(socket_handler=client_socket_handler, audio_handler=audio_handler, login_manager=login_manager)
    window_manager = WindowManager(shared_state)
    
    audio_handler.window_manager = window_manager
    album_window = window_manager.get_window(AlbumWindow)
    album_emitter.setup_connections(album_window)
    user_playlist_window = window_manager.get_window(UserPlaylistWindow)
    
    window_manager.start_window(SignupWindow)
    
    app.exec_()
  
  
if __name__ == "__main__":
    main()


