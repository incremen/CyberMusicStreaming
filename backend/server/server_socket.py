import socketio
import pyaudio
import wave
import logging
import eventlet
from eventlet import wsgi
import os
CHUNK = 4096


#sid - socket id
# environ is a dictionary that contains environmental information related to the incoming connection


class ServerSocketHandler:
    def __init__(self, songs_dir):
        self.sio = socketio.Server()
        self.songs_dir = songs_dir

    def start(self):
        @self.sio.on('connect', namespace='/')
        def connect(sid, environ):
            logging.info('Client connected')

        @self.sio.on('audio_request')
        def on_audio_request(sid, song_name: str):
            if not song_name.endswith(".wav"):
                song_name += ".wav"

            song_path = os.path.join(self.songs_dir, song_name)
            wf = wave.open(song_path, 'rb')

            p = pyaudio.PyAudio()

            stream = p.open(
                format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
            )

            data = wf.readframes(CHUNK)

            while data != b'':
                self.sio.emit('audio_data', data, room=sid)
                stream.write(data)
                data = wf.readframes(CHUNK)

            stream.stop_stream()
            stream.close()
            p.terminate()
            
        @self.sio.on("song_list_request")
        def send_song_list(sid):
            song_list = os.listdir(self.songs_dir)
            self.sio.emit("song_list", song_list, room=sid)

        @self.sio.event
        def disconnect(sid):
            logging.info('Client disconnected')

        app = socketio.WSGIApp(self.sio)
        wsgi.server(eventlet.listen(('localhost', 5000)), app)




