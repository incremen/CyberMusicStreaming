import pyaudio
import logging

CHUNK = 1024

class AudioHandler:
    def __init__(self):
        self.p = pyaudio.PyAudio()

    def play_audio(self, data):
        stream = self.p.open(format=self.p.get_format_from_width(2),
                             channels=1,
                             rate=44100,
                             output=True,
                             frames_per_buffer=CHUNK)

        stream.write(data)

        stream.stop_stream()
        stream.close()

    def terminate(self):
        self.p.terminate()
