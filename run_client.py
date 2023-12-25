from client.client_socket import ClientSocketHandler
import custom_logging
from PyQt5.QtWidgets import QApplication
from music_playing.audio_handler import AudioHandler
from client.main_page_emitter import MainPageEmitter
from ui.login_page.login_page import LoginWindow
import sys
import threading
import logging


def main():
    custom_logger = custom_logging.CustomLogger(log_files=["client.log"])
    custom_logger.clear_logs()
    app = QApplication(sys.argv)
    
    main_page_emitter = MainPageEmitter()
    audio_handler = AudioHandler(main_page_emitter)
    client_socket_handler = ClientSocketHandler(audio_handler)
    
    login_window = LoginWindow(client_socket_handler, audio_handler)
    
    main_page_emitter.setup_connections(login_window.main_window)
    
    client_socket_handler.connect()
    client_socket_handler.emit_to_server("song_list_request")
    app.exec_()
    
if __name__ == "__main__":
    main()

