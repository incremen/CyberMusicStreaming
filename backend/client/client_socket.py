import eventlet
import socketio
import logging
from backend import client_connects_to_str
from music_playing.audio_handler import AudioHandler
import threading
from backend.client.main_page_emitter import MainPageEmitter
from frontend.main_page import MainPage
from music_playing.song_classes import SongInfo, SongChunk


class ClientSocketHandler:
    def __init__(self, audio_handler :AudioHandler, main_page_emitter: MainPageEmitter):
        self.sio = socketio.Client(logger=False, engineio_logger=False)
        self.audio_handler = audio_handler
        self.audio_handler.socket_handler = self
        self.main_page_emitter = main_page_emitter
        
        self.emit_to_server= self.sio.emit
        
        self.got_response = threading.Event()
        self.await_response_lock = threading.Semaphore(2)
        

    def request_song(self, song_name : str):
        self.sio.emit('audio_request', song_name)
    
    def ack_received(self):
        with self.await_response_lock:
            self.got_response.set()
    
    def send_skip_song_event(self):
        with self.await_response_lock:
            if not self.audio_handler.current_song_buffer:
                logging.info("No current song playing...")
                return
            
            order = self.audio_handler.current_song_buffer.order
            self.sio.emit('skip_song', order,callback=self.ack_received)
            
            self.got_response.wait()
            self.got_response.clear()
        
    def connect(self):
        self.sio.connect(client_connects_to_str)
        
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
            self.main_page_emitter.song_list_recieved.emit(song_list)
        

