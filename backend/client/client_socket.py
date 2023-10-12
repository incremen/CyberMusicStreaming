import eventlet
import socketio
import logging
from backend import client_connects_to_str
from music_playing.audio_handler import AudioHandler
import threading
from backend.client.main_page_emitter import MainPageEmitter
from frontend.main_page import MainPage
from music_playing.song_class import SongInfo


class ClientSocketHandler:
    def __init__(self, audio_handler :AudioHandler, main_page_emitter: MainPageEmitter):
        self.sio = socketio.Client(logger=True, engineio_logger=True)
        self.audio_handler = audio_handler
        self.audio_handler.socket_handler = self
        self.main_page_emitter = main_page_emitter
    
    def emit_to_server(self, event_name : str, data = None):
        self.sio.emit(event_name, data)

    def request_song(self, song_name : str):
        self.sio.emit('audio_request', song_name)
        
    def send_skip_song_event(self):
        current_song_id = self.audio_handler.current_song_buffer.info.id
        self.sio.emit('skip_song', current_song_id)
        
    def connect(self):
        self.sio.connect(client_connects_to_str)
        
        @self.sio.event
        def connect():
            logging.info('Connected to server')
            
        @self.sio.on("sending_new_song")
        def new_song_stream(song_info_dict):
            logging.info("Received sending_new_song event!")
            song_info = SongInfo(**song_info_dict)
            logging.debug(f"{song_info=}")
            logging.info("About to add a new song to the queue!")
            self.audio_handler.add_to_song_queue(song_info)
            self.audio_handler.start_playing_next_song()

        @self.sio.on('audio_data')
        def on_audio_data(song_data, song_name, sequence_number):
            logging.info("Received audio data")
            self.audio_handler.add_to_buffer(song_data, song_name, sequence_number)

        @self.sio.event
        def disconnect():
            logging.info('Disconnected from server')
        
        @self.sio.on("song_list")
        def received_song_list(song_list):
            logging.debug(f"{song_list=}")
            self.main_page_emitter.song_list_recieved.emit(song_list)
        

