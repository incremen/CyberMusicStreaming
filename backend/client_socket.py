import socketio
import pyaudio
import logging

CHUNK = 1024

class ClientSocketHandler:
    def __init__(self, audio_handler):
        self.sio = socketio.Client(logger=True, engineio_logger=True)
        self.audio_handler = audio_handler

    def connect(self):
        @self.sio.event
        def connect():
            logging.info('Connected to server')

        @self.sio.on('audio_data')
        def on_audio_data(data):
            self.audio_handler.play_audio(data)

        @self.sio.event
        def disconnect():
            logging.info('Disconnected from server')

        self.sio.connect('http://localhost:5000')
        self.sio.emit('audio_request')
        self.sio.wait()
