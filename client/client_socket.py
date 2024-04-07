import socketio
import logging
from backend import CLIENT_CONNECTS_TO_STR
from music_playing.audio_handler import AudioHandler
from client.window_emitter import MusicPlayingEmitter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from database.login_manager import LoginManager
    from ui.signup_page.signup_window_emitter import SignupWindowEmitter
    from ui.user_profile.profile_window_emitter import ProfileWindowEmitter
    from ui.user_playlist_page.user_playlist_emitter import PlaylistWindowEmitter

    
class ClientSocketHandler:
    def __init__(self, audio_handler :AudioHandler, music_playing_emitter : MusicPlayingEmitter):
        self.sio = socketio.Client(logger=True, engineio_logger=True)
        self.music_playing_emitter = music_playing_emitter
        self.audio_handler = audio_handler
        self.audio_handler.socket_handler = self
        self.emit_to_server= self.sio.emit
        self.login_manager : 'LoginManager' = None
        self.signup_window_emitter : 'SignupWindowEmitter'= None
        self.profile_window_emitter : 'ProfileWindowEmitter' = None
        self.playlist_window_emitter : 'PlaylistWindowEmitter' = None
    
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
            self.audio_handler.song_list_received(song_list)
            
        @self.sio.on("next_song_order")
        def received_next_song_order(order):    
            logging.recv(f"received next song order: {order}")
            
        @self.sio.on("account_create_result")
        def on_account_create_result(data):
            logging.debug(f"{data=}")
            self.signup_window_emitter.account_create_result.emit(data['result'])

        @self.sio.on("login_result")
        def on_login_result(data):
            logging.debug(f"{data=}")
            if self.login_manager:
                self.login_manager.login_response(data['result'])
                
        @self.sio.on("user_info")
        def on_user_info(data):
            logging.debug(f"{data=}")
            logging.info("About to emit to profile window")
            self.profile_window_emitter.load_user_playlists.emit(data['user'])
        
        @self.sio.on("search_result")
        def on_search_result(data):
            logging.debug(f"{data=}")
            self.playlist_window_emitter.search_result_received.emit(data['songs'])
            
        
            
        self.sio.connect(CLIENT_CONNECTS_TO_STR)
        
        

