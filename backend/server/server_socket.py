import threading
import time
import socketio
import wave
import logging
from custom_logging import log_calls
import eventlet
from eventlet import wsgi
import os
from music_playing import manage_songs_in_dir
import pprint
from dataclasses import asdict
from backend import server_addr_tuple
from backend.server.song_queue_manager import ServerQueueManager

#sid - socket id
# environ is a dictionary that contains environmental information related to the incoming connection

class ServerSocketHandler:
    def __init__(self, songs_dir):
        self.sio = socketio.Server()
        self.song_queue_manager = ServerQueueManager(self, songs_dir)
        
    def emit_to_client(self, event_name, sid, data= None):
        self.sio.emit(event_name, data, room=sid)
        logging.debug(f"Emitted {event_name} to client {sid}")
        return

    def start(self):
        @self.sio.on('connect', namespace='/')
        def connect(sid, environ):
            logging.info('Client connected')

        @self.sio.on('audio_request')
        def on_audio_request(sid, song_name: str):
            logging.checkpoint(f"Received audio request for {song_name}")
            self.song_queue_manager.add_song_to_send_list(song_name, sid)

        @self.sio.on("song_list_request")
        def send_song_list(sid):
            song_dict_list = [asdict(song) for song in self.song_queue_manager.song_list]
            self.sio.emit("song_list", song_dict_list, room=sid)

        @self.sio.event
        def disconnect(sid):
            logging.info('Client disconnected')
            
        @self.sio.on('acknowledge')
        def client_acknowledged(sid):
            logging.debug("Client acknowledged")
            self.song_queue_manager.client_has_ack = True
        
        @self.sio.on('skip_song')
        def skip_song(sid, song_name):
            logging.info("Beginning of skip song func")
            if self.song_queue_manager.song_being_sent != song_name:
                logging.info("Not sending that anymore...")
                return
            
            logging.info("Skipping song!")
            self.song_queue_manager.skip_song_flag = True
            
        app = socketio.WSGIApp(self.sio)
        wsgi.server(eventlet.listen(server_addr_tuple), app)
            

        

            






