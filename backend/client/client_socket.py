import socketio
import logging
from backend import server_address
from music_playing.audio_handler import AudioHandler
import threading
from frontend.main_page import MainPage
from backend.client.main_page_emitter import MainPageEmitter

class ClientSocketHandler:
    def __init__(self):
        self.sio = socketio.Client(reconnection=True, logger=True, engineio_logger=True, reconnection_attempts=1024)
        self.audio_handler = AudioHandler()
        # self.main_page = MainPage()
        # self.main_page_emitter = MainPageEmitter()
        self.play_thread = threading.Thread(target=self.audio_handler.play_audio)
        self.play_thread.start()

    def connect(self):
        @self.sio.event
        def connect():
            logging.info('Connected to server')

        @self.sio.on('audio_data')
        def on_audio_data(data):
            self.audio_handler.add_to_buffer(data)

        @self.sio.event
        def disconnect():
            logging.info('Disconnected from server')

        self.sio.connect(server_address)
        
        @self.sio.on("song_list")
        def received_song_list(song_list):
            logging.debug(f"{song_list=}")
        
    def emit_to_server(self, event_name : str, data : dict = None):
        self.sio.emit(event_name, data)

    def request_song(self, song_name : str):
        self.sio.emit('audio_request', song_name)