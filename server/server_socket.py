import threading
import time
import socketio
import wave
import logging
from custom_logging import log_calls
import eventlet
from eventlet import wsgi
import os
from server import manage_songs_in_dir
import pprint
from dataclasses import asdict
from backend import server_addr_tuple
from database import utils
from server import login_funcs
#sid - socket id
# environ is a dictionary that contains environmental information related to the incoming connection

class ServerSocketHandler:
    def __init__(self, song_dir):
        self.sio = socketio.Server()
        logging.info("Started sio server...")
        session = utils.create_session()
        self.song_list = manage_songs_in_dir.get_all_songs_in_db(session)
        logging.info(f"{self.song_list=}")
        session.close()

    def start(self):
        @self.sio.on('connect', namespace='/')
        def connect(sid, environ):
            logging.info('Client connected')

        @self.sio.on("song_list_request")
        def send_song_list(sid):
            song_dict_list = [asdict(song) for song in self.song_list]
            self.sio.emit("song_list", song_dict_list, room=sid)

        @self.sio.on("create_new_account")
        def create_new_account_handler(sid, data):
            username = data.get('username')
            password = data.get('password')
            
            result = login_funcs.create_new_account(username, password)
            
            if result.is_ok():
                with self.sio.session(sid) as session_data:
                    session_data['username'] = username
                    
            result_msg = result.value
                                
            self.sio.emit("account_create_result", {"result": result.is_ok(), "message" : result_msg},  room=sid)

        @self.sio.on("login")
        def login_handler(sid, data):
            username = data.get('username')
            password = data.get('password')
            
            result = login_funcs.login(username, password)
            
            if result.is_ok():
                with self.sio.session(sid) as session_data:
                    session_data['username'] = username
                    
            self.sio.emit("login_result", {"result": result.is_ok(), "message": result.value}, room=sid)

        @self.sio.on("logout")
        def logout_handler(sid):
            with self.sio.session(sid) as session_data:
                session_data.clear()
            # self.sio.emit("logout_success", {"message": "Logged out successfully"}, room=sid)
            
            
        app = socketio.WSGIApp(self.sio)
        wsgi.server(eventlet.listen(server_addr_tuple), app)

            

        

            






