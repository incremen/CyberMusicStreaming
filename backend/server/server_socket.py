import socketio
import pyaudio
import wave
import logging
import eventlet
from eventlet import wsgi
import os
from music_playing import manage_songs_in_dir
import pprint
from dataclasses import asdict

CHUNK = 4096

#sid - socket id
# environ is a dictionary that contains environmental information related to the incoming connection


class ServerSocketHandler:
    def __init__(self, songs_dir):
        self.sio = socketio.Server()
        self.songs_dir = songs_dir
        self.song_list = manage_songs_in_dir.get_song_list(songs_dir)
        self.song_name_to_data = manage_songs_in_dir.get_name_to_song_data_dict(songs_dir)
        logging.debug(pprint.pformat(self.song_list))

    def start(self):
        @self.sio.on('connect', namespace='/')
        def connect(sid, environ):
            logging.info('Client connected')

        @self.sio.on('audio_request')
        def on_audio_request(sid, song_name: str):
            if not song_name.endswith(".wav"):
                song_name += ".wav"
            
            song_data = self.song_name_to_data[song_name]

            song_path = os.path.join(self.songs_dir, song_name)
            logging.debug(f"About to play {song_path}")
            wf = wave.open(song_path, 'rb')

            p = pyaudio.PyAudio()
            stream = self.setup_audio_stream(wf, p)

            self.sio.emit("beginning_play", asdict(song_data), room=sid)
            
            while True:
                data = wf.readframes(CHUNK)
                if not data:
                    break

                self.sio.emit('audio_data', data, room=sid)
                stream.write(data)

            self.cleanup_audio_stream(stream, p)
            
        @self.sio.on("song_list_request")
        def send_song_list(sid):
            song_dict_list = [asdict(song) for song in self.song_list]
            self.sio.emit("song_list", song_dict_list, room=sid)

        @self.sio.event
        def disconnect(sid):
            logging.info('Client disconnected')

        app = socketio.WSGIApp(self.sio)
        wsgi.server(eventlet.listen(('localhost', 5000)), app)
        
    def setup_audio_stream(self, wf, p):
            stream = p.open(
                format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
            )
            return stream

    def cleanup_audio_stream(self, stream, p):
        stream.stop_stream()
        stream.close()
        p.terminate()





