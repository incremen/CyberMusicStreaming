import logging
import pyaudio
import queue
from backend.client.main_page_emitter import MainPageEmitter
from music_playing.song_class import SongData, return_as_songdata
import threading


CHUNK = 1024


class AudioHandler:
    def __init__(self, main_page_emitter :MainPageEmitter):
        self.p = pyaudio.PyAudio()
        
        self.stream = self.p.open(format=self.p.get_format_from_width(2),
                             channels=1,
                             rate=44100,
                             output=True,
                             frames_per_buffer=CHUNK,
                             stream_callback=self.callback)
        
        self.buffer = queue.Queue()
        self.main_page_emitter = main_page_emitter
        self.frames_played = 0
        self.lock = threading.Lock()

    def callback(self, in_data, frame_count, time_info, status):
        with self.lock:
            data = self.buffer.get()
        self.frames_played += CHUNK
        self.update_progress()
        return (data, pyaudio.paContinue)

    def update_progress(self):
        progress = self.calculate_progress()
        logging.debug(f"Emitting {progress=}")
        self.main_page_emitter.update_song_progress.emit(progress)

    def add_to_buffer(self, data):
        with self.lock:
            self.buffer.put(data)

    def calculate_progress(self):
        progress = (self.frames_played / self.song_data.nframes) * 100
        logging.debug(f"{self.frames_played=} / {self.song_data.nframes=} = {progress}")
        return progress

    def terminate(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.frames_played = 0  


