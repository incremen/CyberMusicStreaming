import socketio
import pyaudio
import logging
from backend import server_address
from music_playing.audio_handler import AudioHandler
import threading

class ClientSocketHandler:
    def __init__(self):
        self.sio = socketio.Client(logger=True, engineio_logger=True)
        self.audio_handler = AudioHandler()
        self.play_thread = threading.Thread(target=self.audio_handler.play_audio)
        self.play_thread.start()

    def connect(self):
        @self.sio.event
        def connect():
            logging.info('Connected to server')

        @self.sio.on('audio_data')
        def on_audio_data(data):
            self.audio_handler.add_to_buffer(data)

        @self.sio.event
        def disconnect():
            logging.info('Disconnected from server')

        self.sio.connect(server_address)
        self.sio.emit('audio_request')
        self.sio.wait()
