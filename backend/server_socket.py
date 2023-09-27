import socketio
import pyaudio
import wave
import logging
import eventlet
from eventlet import wsgi

CHUNK = 4096

class ServerSocketHandler:
    def __init__(self, song_path):
        self.sio = socketio.Server()
        self.song_path = song_path

    def start(self):
        logging.debug(f"{self.song_path=}")
        wf = wave.open(self.song_path, 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True,
                        frames_per_buffer=CHUNK)

        @self.sio.on('connect', namespace='/')
        def connect(sid, environ):
            print('Client connected')


        @self.sio.on('audio_request')
        def on_audio_request(sid):
            data = wf.readframes(CHUNK)
            while data != b'':
                self.sio.emit('audio_data', data, room=sid)
                stream.write(data)
                data = wf.readframes(CHUNK)

        @self.sio.event
        def disconnect(sid):
            print('Client disconnected')
            stream.stop_stream()
            stream.close()
            p.terminate()

        app = socketio.WSGIApp(self.sio)
        wsgi.server(eventlet.listen(('localhost', 5000)), app)



