import socketio
import logging
from backend import server_address
from music_playing.audio_handler import AudioHandler
import threading
from backend.client.main_page_emitter import MainPageEmitter
from frontend.main_page import MainPage
from music_playing.song_class import SongData

class ClientSocketHandler:
    def __init__(self, audio_handler :AudioHandler, main_page_emitter: MainPageEmitter):
        self.sio = socketio.Client(logger=True, engineio_logger=True)
        self.audio_handler = audio_handler
        self.main_page_emitter = main_page_emitter

    def connect(self):
        self.sio.connect(server_address)
        
        @self.sio.event
        def connect():
            logging.info('Connected to server')

        @self.sio.on('audio_data')
        def on_audio_data(data):
            self.audio_handler.add_to_buffer(data)

        @self.sio.event
        def disconnect():
            logging.info('Disconnected from server')
        
        @self.sio.on("song_list")
        def received_song_list(song_list):
            logging.debug(f"{song_list=}")
            self.main_page_emitter.song_list_recieved.emit(song_list)
        
    def emit_to_server(self, event_name : str, data : dict = None):
        self.sio.emit(event_name, data)

    def request_song(self, song_name : str):
        self.sio.emit('audio_request', song_name)
