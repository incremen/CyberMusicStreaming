import pyaudio
import logging

CHUNK = 1024

class AudioHandler:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.p.get_format_from_width(2),
                             channels=1,
                             rate=44100,
                             output=True,
                             frames_per_buffer=CHUNK)

    def play_audio(self, data):
        self.stream.write(data)

    def terminate(self):
        self.stream.stop_stream()
        self.stream.close()
        
        self.p.terminate()
