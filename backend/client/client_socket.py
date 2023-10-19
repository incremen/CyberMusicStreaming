import eventlet
import socketio
import logging
from backend import client_connects_to_str
from music_playing.audio_handler import AudioHandler
import threading
from backend.client.main_page_emitter import MainPageEmitter
from frontend.main_page import MainPage
from music_playing.song_class import SongInfo, SongChunk


class ClientSocketHandler:
    def __init__(self, audio_handler :AudioHandler):
        self.sio = socketio.Client(logger=False, engineio_logger=False)
        self.audio_handler = audio_handler
        self.audio_handler.socket_handler = self
        self.emit_to_server= self.sio.emit

    def request_song(self, song_name : str):
        self.emit_to_server('audio_request', song_name)
    
    def send_skip_to_song_event(self, song_order):
        self.emit_to_server("skip_to_song" ,song_order)
    
    def send_skip_song_event(self):
        if not self.audio_handler.current_song_buffer:
            logging.error("No current song playing...")
            return
        
        order = self.audio_handler.current_song_buffer.order
        self.emit_to_server('skip_song', order)
        
    def connect(self):
        
        @self.sio.event
        def connect():
            logging.info('Connected to server')
            
        @self.sio.on("sending_new_song")
        def new_song_stream(song_info_dict, song_order):
            song_info = SongInfo(**song_info_dict)
            logging.recv(f"Received sending_new_song event! {song_info=}")
            self.audio_handler.play_next_song()

        @self.sio.on('audio_data')
        def on_audio_data(song_chunk_dict):
            song_chunk = SongChunk(**song_chunk_dict)
            logging.recv(f"Received audio data ({song_chunk})")
            self.audio_handler.add_to_buffer(song_chunk)

        @self.sio.event
        def disconnect():
            logging.info('Disconnected from server')
        
        @self.sio.on("song_list")
        def received_song_list(song_list):
            logging.debug(f"{song_list=}")
            self.audio_handler.song_list_received(song_list)
            
        @self.sio.on("next_song_order")
        def received_next_song_order(order):
            logging.recv(f"received next song order: {order}")
            self.audio_handler.received_next_order(order)
            
        self.sio.connect(client_connects_to_str)
        
        

