import time
import socketio
import wave
import logging
import eventlet
from eventlet import wsgi
import os
from music_playing import manage_songs_in_dir
import pprint
from dataclasses import asdict
from backend import server_addr_tuple
CHUNK = 4096

#sid - socket id
# environ is a dictionary that contains environmental information related to the incoming connection


class ServerSocketHandler:
    def __init__(self, songs_dir):
        self.sio = socketio.Server()
        self.songs_dir = songs_dir
        self.song_list = manage_songs_in_dir.get_song_list(songs_dir)
        self.song_name_to_info = manage_songs_in_dir.get_name_to_songinfo_dict(songs_dir)
        
        self.songs_to_send : list[str]= []
        self.skip_song_flag : bool = False
        logging.debug(pprint.pformat(self.song_list))

    def get_song_path(self, song_name):
        if not song_name.endswith(".wav"):
            song_name += ".wav"
        song_path = os.path.join(self.songs_dir, song_name)
        return song_path
    
    def send_next_song(self, sid):
        if not self.songs_to_send:
            logging.info("No more songs to send...")
            return

        next_song_name = self.songs_to_send.pop(0)
        
        self.send_song(next_song_name, sid)
        
        self.send_next_song(sid)
        
    def add_song_to_send_list(self, song_name, sid):
        self.songs_to_send.append(song_name)
        
        if len(self.songs_to_send) == 1:
            self.send_next_song(sid)
    
    def send_song(self, song_name, sid):
        song_path = self.get_song_path(song_name)
    
        song_info = self.song_name_to_info[song_name]

        self.sio.emit("sending_new_song", asdict(song_info), room=sid)
        logging.debug(f"About to send {song_path}")
            
        with wave.open(song_path, 'rb') as wave_file:
            self.send_song_data(song_name, sid, wave_file)

    def send_song_data(self, song_name, sid, wf):
        while True:
            if self.skip_song_flag:
                self.skip_song_flag = False
                logging.debug("Quitting loop because skip")
                break
            song_data = wf.readframes(CHUNK)
            if not song_data:
                break
            logging.debug("Sending audio data!")
            self.sio.emit('audio_data', (song_data, song_name), room=sid)

    def start(self):
        @self.sio.on('connect', namespace='/')
        def connect(sid, environ):
            logging.info('Client connected')

        @self.sio.on('audio_request')
        def on_audio_request(sid, song_name: str):
            self.add_song_to_send_list(song_name, sid)

        @self.sio.on("song_list_request")
        def send_song_list(sid):
            song_dict_list = [asdict(song) for song in self.song_list]
            self.sio.emit("song_list", song_dict_list, room=sid)

        @self.sio.event
        def disconnect(sid):
            logging.info('Client disconnected')
            
        @self.sio.on('skip_song')
        def skip_song():
            logging.info("Skipping song!")
            self.skip_song_flag = True

        app = socketio.WSGIApp(self.sio)
        wsgi.server(eventlet.listen(server_addr_tuple), app)
        

            






