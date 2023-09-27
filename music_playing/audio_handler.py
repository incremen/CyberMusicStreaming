import pyaudio
import logging
import queue

CHUNK = 1024

class AudioHandler:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.p.get_format_from_width(2),
                             channels=1,
                             rate=44100,
                             output=True,
                             frames_per_buffer=CHUNK)
        self.buffer = queue.Queue()

    def add_to_buffer(self, data):
        self.buffer.put(data)

    def play_audio(self):
        while not self.buffer.empty():
            data = self.buffer.get()
            self.stream.write(data)

    def terminate(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
