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
from music_playing.song_class import SongInfo, SongToSend, SongChunk
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
        self.song_being_sent : SongToSend = None
        
        self.emit = self.socket_handler.sio.emit
        
        self.next_song_id = 0
        
        self.songs_to_skip : dict[int, bool] = {}
        
        self.check_skip_lock = threading.Semaphore(3)
        
    def get_song_path(self, song_name :str):
        if not song_name.endswith(".wav"):
            song_name += ".wav"
        song_path = os.path.join(self.songs_dir, song_name)
        return song_path
    
    def skip_song(self, sid, song_order):
        with self.check_skip_lock:
            logging.recv(f"Received skip song req for {song_order=}, {self.songs_to_send=}")
            if not self.songs_to_send:
                logging.info("No more songs to skip...")
                return
            
            if self.songs_to_send[0].order == song_order:
                self.songs_to_skip[song_order] = True
                logging.debug(f"Set skip to true for {song_order}")
                return
            
            for i, song in enumerate(self.songs_to_send,1):
                if song.order == song_order:
                    self.songs_to_send.pop(i)
                    logging.debug(f"Popped {song_order}")
                    return
                
            logging.error(f"Song order to skip not found: {song_order}")
            
    def skip_to_song(self, sid, order_to_skip_to):
        with self.check_skip_lock:
            logging.recv(f"Received skip to song req for {order_to_skip_to=}, {self.songs_to_send=}")
            if not self.songs_to_send:
                logging.info("No more songs to skip...")
                return
            
            if self.song_being_sent.order == order_to_skip_to:
                logging.info("Already playing song to skip to")
                return
            
            
            logging.info(f"Skipping song to {order_to_skip_to}")
            self.songs_to_skip[self.song_being_sent.order] = True
            del self.songs_to_skip[0:order_to_skip_to]
            logging.info(f"Updated songs to skip: {pprint.pformat(self.songs_to_skip)}")
    
    def send_next_song(self, sid):
        logging.info("Sending next song!")
        
        if not self.songs_to_send:
            logging.info("No more songs to send...")
            return

        next_song = self.songs_to_send[0]
        
        self.send_song(next_song, sid)
        self.songs_to_send.pop(0)
        #you cant pop it earlier because it needs to stay in the list
        self.send_next_song(sid)
        
    def create_new_songtosend(self, song_name):
        songtosend = SongToSend(song_name, self.next_song_id)
        self.next_song_id += 1
        return songtosend
        
    def add_song_to_send_list(self, song_name, sid):
        logging.checkpoint(f"Received audio request for {song_name}")
        song_to_send = self.create_new_songtosend(song_name)
        self.songs_to_send.append(song_to_send)
        logging.info(f"Added {song_name} to song list")
        if len(self.songs_to_send) == 1:
            self.send_next_song(sid)
    
    def send_song(self, song_to_send : SongToSend, sid):
        song_path = self.get_song_path(song_to_send.name)
    
        song_info = self.song_name_to_info[song_to_send.name]

        self.emit("sending_new_song", ((asdict(song_info)), song_to_send.order) ,room=sid )
        logging.send(f"Emitted sending_new_song event for {song_to_send.name}(id={song_to_send.order})")
        
        logging.debug(f"About to send {song_path}") 
        
        self.song_being_sent = song_to_send
        with wave.open(song_path, 'rb') as wave_file:
            self.send_song_data(song_to_send, sid, wave_file)
        self.song_being_sent = None

    def send_song_data(self, song_to_send : SongToSend, sid, wf):
        song_name = song_to_send.name
        sequence_number = 0
        logging.checkpoint(f"Beginning to send song: {song_name=}, {self.songs_to_send=}")
        
        while song_data_chunk := wf.readframes(CHUNK):
            with self.check_skip_lock:
                eventlet.sleep(0.01)
                
            if self.songs_to_skip.get(song_to_send.order):
                 logging.checkpoint(f"Song skipped: {song_to_send}")
                 self.songs_to_skip[song_to_send.order] = False
                 return
             
            if not song_data_chunk:
                 return
            song_chunk = SongChunk(chunk=song_data_chunk, name=song_to_send.name, order=song_to_send.order, seq=sequence_number)
            logging.send(f"Sending audio data for {song_to_send.name}(id={song_to_send.order}, seq = {sequence_number})")
            self.emit('audio_data', asdict(song_chunk), room=sid)
             

            sequence_number += 1
             
        logging.checkpoint(f"Done sending song: {song_name=}, {self.songs_to_send=}")
