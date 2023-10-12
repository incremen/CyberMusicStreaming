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
from typing import TYPE_CHECKING

CHUNK = 4096
if TYPE_CHECKING:
    from backend.server.server_socket import ServerSocketHandler


class ServerQueueManager:
    def __init__(self, socket_handler: 'ServerSocketHandler', songs_dir : str):
        self.socket_handler = socket_handler
        self.songs_dir = songs_dir
        self.song_list = manage_songs_in_dir.get_song_list(self.songs_dir, CHUNK)
        self.song_name_to_info = manage_songs_in_dir.get_name_to_songinfo_dict(self.songs_dir, CHUNK)
        self.songs_to_send : list[str]= []
        self.skip_song_flag : bool = False
        self.song_being_sent : str = None
        self.client_has_ack : bool = False
        
        self.emit = self.socket_handler.emit_to_client

    def get_song_path(self, song_name):
        if not song_name.endswith(".wav"):
            song_name += ".wav"
        song_path = os.path.join(self.songs_dir, song_name)
        return song_path

    def send_next_song(self, sid):
        logging.info("Sending next song!")
        
        if not self.songs_to_send:
            logging.info("No more songs to send...")
            return

        next_song_name = self.songs_to_send.pop(0)
        
        self.skip_song_flag = False
        self.send_song(next_song_name, sid)
        
        self.send_next_song(sid)
        
    def add_song_to_send_list(self, song_name, sid):
        self.songs_to_send.append(song_name)
        logging.info(f"Added {song_name} to song list")
        if len(self.songs_to_send) == 1:
            self.send_next_song(sid)
    
    def send_song(self, song_name, sid):
        song_path = self.get_song_path(song_name)
    
        song_info = self.song_name_to_info[song_name]

        self.emit("sending_new_song", sid, asdict(song_info))
        logging.info("Emitted sending_new_song event")

        logging.info("Waiting for client to acknowledge...")
        self.await_client_ack()
        
        logging.debug(f"About to send {song_path}") 
        
        self.song_being_sent = song_name
        with wave.open(song_path, 'rb') as wave_file:
            self.send_song_data(song_name, sid, wave_file)
        self.song_being_sent = None

    def await_client_ack(self):
        while not self.client_has_ack:
            eventlet.sleep(0.01)
        self.client_has_ack = False

    def send_song_data(self, song_name, sid, wf):
        sequence_number = 0
        logging.checkpoint(f"Beginning to send song: {song_name=}, {self.songs_to_send=}")
        
        while song_data := wf.readframes(CHUNK):
             if self.skip_song_flag:
                 self.skip_song_flag = False
                 return
             
             if not song_data:
                 return
             
             logging.debug("Sending audio data!")
             self.emit('audio_data', sid, (song_data, song_name, sequence_number))
             eventlet.sleep(0.01)
             sequence_number += 1
             
        logging.checkpoint(f"Done sending song: {song_name=}, {self.songs_to_send=}")
