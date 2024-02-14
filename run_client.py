from client.client_socket import ClientSocketHandler
import custom_logging
from PyQt5.QtWidgets import QApplication
from music_playing.audio_handler import AudioHandler
from client.album_window_emitter import AlbumWindowEmitter
from ui.login_page.login_page import LoginWindow
import sys
from client.shared_state import SharedState
from client.window_manager import WindowManager
from ui.album_page.album_window import AlbumWindow



def connect_and_request_song_list(client_socket_handler):
    client_socket_handler.connect()
    client_socket_handler.emit_to_server("song_list_request")
    
    
def main():
    custom_logger = custom_logging.CustomLogger(log_files=["client.log"])
    custom_logger.clear_logs()
    app = QApplication(sys.argv)
    
    album_window_emitter = AlbumWindowEmitter()
    audio_handler = AudioHandler(album_window_emitter)
    client_socket_handler = ClientSocketHandler(audio_handler, album_window_emitter)
    client_socket_handler.connect()
    
    shared_state = SharedState(socket_handler=client_socket_handler, audio_handler=audio_handler)
    window_manager = WindowManager(shared_state)
    
    album_window = window_manager.get_window(AlbumWindow)
    album_window_emitter.setup_album_page_connections(album_window)
    
    window_manager.start_window(AlbumWindow)
    
    app.exec_()
  
  
if __name__ == "__main__":
    main()


