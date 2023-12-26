import socketio
import logging
from backend import client_connects_to_str
from music_playing.audio_handler import AudioHandler
from client.window_emitter import WindowEmitter

class ClientSocketHandler:
    def __init__(self, audio_handler :AudioHandler, window_emitter : WindowEmitter):
        self.sio = socketio.Client(logger=False, engineio_logger=False)
        self.window_emitter = window_emitter
        self.audio_handler = audio_handler
        self.audio_handler.socket_handler = self
        emit_to_server= self.sio.emit
    
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

        @self.sio.event
        def disconnect():
            logging.info('Disconnected from server')
        
        @self.sio.on("song_list")
        def received_song_list(song_list):
            logging.debug(f"{song_list=}")
            self.window_emitter.song_list_recieved.emit(song_list)
            
        @self.sio.on("next_song_order")
        def received_next_song_order(order):
            logging.recv(f"received next song order: {order}")
            self.audio_handler.received_next_order(order)
            
        self.sio.connect(client_connects_to_str)
        
        

