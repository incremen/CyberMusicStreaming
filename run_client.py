from backend.client.client_socket import ClientSocketHandler
import custom_logging
from PyQt5.QtWidgets import QApplication
from music_playing.audio_handler import AudioHandler
from backend.client.main_page_emitter import MainPageEmitter
from frontend.main_page import MainPage
import sys
from music_playing.song_classes import SongBuffer
from music_playing.song_queue import SongQueue
import threading
import logging


def main():
    custom_logger = custom_logging.CustomLogger(log_files=["client.log"])
    custom_logger.clear_logs()
    app = QApplication(sys.argv)
    
    main_page_emitter = MainPageEmitter()
    song_queue : list[SongBuffer]= SongQueue(main_page_emitter.update_song_queue)
    
    audio_handler = AudioHandler(main_page_emitter, song_queue)
    client_socket_handler = ClientSocketHandler(audio_handler, main_page_emitter)
    
    main_page = MainPage(client_socket_handler, audio_handler, song_queue)
    
    main_page_emitter.setup_connections(main_page)
    
    client_socket_handler.connect()
    client_socket_handler.emit_to_server("song_list_request")
    app.exec_()
    
if __name__ == "__main__":
    main()

