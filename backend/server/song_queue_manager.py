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
from music_playing.song_class import SongInfo, SongToSend
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
        
        self.songs_to_send : list[SongToSend]= []
        self.skip_song_flag : bool = False
        self.song_being_sent : SongToSend = None
        self.client_has_ack : bool = False
        
        self.emit = self.socket_handler.emit_to_client
        
        self.next_song_id = 0
        
    def get_song_path(self, song_name :str):
        if not song_name.endswith(".wav"):
            song_name += ".wav"
        song_path = os.path.join(self.songs_dir, song_name)
        return song_path
    
    def skip_song(self, sid, song_id):
        if not self.song_being_sent:
            logging.info("No song being sent, skipping")
            return
        
        logging.info("Beginning of skip song func")
        if self.song_being_sent and self.song_being_sent.id == song_id:
            logging.info("Setting skip song flag to true")
            self.skip_song_flag = True
            return
            
        logging.info("Nothing to skip server-side")
    
    def send_next_song(self, sid):
        logging.info("Sending next song!")
        
        if not self.songs_to_send:
            logging.info("No more songs to send...")
            return

        next_song = self.songs_to_send.pop(0)
        
        self.skip_song_flag = False
        self.send_song(next_song, sid)
        
        self.send_next_song(sid)
        
    def create_new_songtosend(self, song_name):
        songtosend = SongToSend(song_name, self.next_song_id)
        self.next_song_id += 1
        return songtosend
        
    def add_song_to_send_list(self, song_name, sid):
        song_to_send = self.create_new_songtosend(song_name)
        self.songs_to_send.append(song_to_send)
        logging.info(f"Added {song_name} to song list")
        if len(self.songs_to_send) == 1:
            self.send_next_song(sid)
    
    def send_song(self, song_to_send : SongToSend, sid):
        song_path = self.get_song_path(song_to_send.name)
    
        song_info = self.song_name_to_info[song_to_send.name]
        song_info.id = song_to_send.id

        self.emit("sending_new_song", sid, (asdict(song_info)) )
        logging.info("Emitted sending_new_song event")

        logging.info("Waiting for client to acknowledge...")
        self.await_client_ack()
        
        logging.debug(f"About to send {song_path}") 
        
        self.song_being_sent = song_to_send
        with wave.open(song_path, 'rb') as wave_file:
            self.send_song_data(song_to_send, sid, wave_file)
        self.song_being_sent = None

    def await_client_ack(self):
        while not self.client_has_ack:
            eventlet.sleep(0.01)
        self.client_has_ack = False

    def send_song_data(self, song_to_send : SongToSend, sid, wf):
        song_name = song_to_send.name
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
