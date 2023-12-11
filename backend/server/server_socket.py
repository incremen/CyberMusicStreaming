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

#sid - socket id
# environ is a dictionary that contains environmental information related to the incoming connection

class ServerSocketHandler:
    def __init__(self):
        self.sio = socketio.Server()
        self.next_song_order = 0

    def start(self):
        @self.sio.on('connect', namespace='/')
        def connect(sid, environ):
            logging.info('Client connected')
            logging.send("Sending next song order...")

        @self.sio.on('audio_request')
        def on_audio_request(sid, song_name: str):
            logging.recv(f"Received audio request for {song_name}")
            self.song_queue_manager.add_song_to_send_list(song_name, sid)

        @self.sio.on("song_list_request")
        def send_song_list(sid):
            song_dict_list = [asdict(song) for song in self.song_queue_manager.song_list]
            self.sio.emit("song_list", song_dict_list, room=sid)

        @self.sio.event
        def disconnect(sid):
            logging.info('Client disconnected')
        
        @self.sio.on('skip_song')
        def skip_song(sid, song_name):
            self.song_queue_manager.skip_song(sid, song_name)
            
        @self.sio.on("skip_to_song")
        def on_skip_to_song(sid, song_name):
            logging.checkpoint("Skipping to song...")
            self.song_queue_manager.skip_to_song(sid, song_name)
            
        app = socketio.WSGIApp(self.sio)
        wsgi.server(eventlet.listen(server_addr_tuple), app)

            

        

            






