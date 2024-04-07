from client.client_socket import ClientSocketHandler
import custom_logging
from PyQt5.QtWidgets import QApplication
from music_playing.audio_handler import AudioHandler
from client.window_emitter import MusicPlayingEmitter
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
from ui.user_profile.user_profile_window import UserProfileWindow
from ui.user_profile.profile_window_emitter import ProfileWindowEmitter
import logging
from ui.signup_page.signup_window_emitter import SignupWindowEmitter
from ui.login_page.login_window_emitter import LoginWindowEmitter
from ui.user_playlist_page.user_playlist_emitter import PlaylistWindowEmitter

def main():
    logging.getLogger('sqlalchemy').setLevel(logging.ERROR)

    custom_logger = custom_logging.CustomLogger(log_files=["client.log"], log_to_console = True)
    custom_logger.clear_logs()
    app = QApplication(sys.argv)
    
    album_emitter, audio_handler, client_socket_handler, login_manager, window_manager = create_main_objs()
    
    audio_handler.window_manager = window_manager
    album_window = window_manager.get_window(AlbumWindow)
    album_emitter.setup_connections(album_window)
    
    login_manager.create_new_account("a", "a")
    login_manager.login("a", "a")
    
    signup_window = window_manager.get_window(SignupWindow)
    signup_window_emitter = SignupWindowEmitter(signup_window)
    signup_window_emitter.setup_connections(signup_window)
    client_socket_handler.signup_window_emitter = signup_window_emitter
    
    
    login_window_emitter = LoginWindowEmitter()
    login_window_emitter.setup_connections(window_manager.get_window(LoginWindow))
    login_manager.login_window_emitter = login_window_emitter
    
    
    profile_window = window_manager.get_window(UserProfileWindow)
    profile_window_emitter = ProfileWindowEmitter(profile_window)
    profile_window_emitter.setup_connections(profile_window)
    client_socket_handler.profile_window_emitter = profile_window_emitter
    
    playlist_window = window_manager.get_window(UserPlaylistWindow)
    playlist_window_emitter = PlaylistWindowEmitter(playlist_window)
    playlist_window_emitter.setup_connections(playlist_window)
    client_socket_handler.playlist_window_emitter = playlist_window_emitter
    
    
    window_manager.start_window(SignupWindow)
    logging.getLogger('sqlalchemy').setLevel(logging.ERROR)
    
    app.exec_()

def create_main_objs():
    album_emitter = MusicPlayingEmitter()
    audio_handler = AudioHandler(album_emitter)
    client_socket_handler = ClientSocketHandler(audio_handler, album_emitter)
    client_socket_handler.connect()
    
    login_manager = LoginManager(SQLITE_PATH, client_socket_handler)
    client_socket_handler.login_manager = login_manager
    
    shared_state = SharedState(socket_handler=client_socket_handler, audio_handler=audio_handler, login_manager=login_manager)
    window_manager = WindowManager(shared_state)
    return album_emitter,audio_handler,client_socket_handler,login_manager,window_manager
  
  
if __name__ == "__main__":
    main()


