import pyaudio
import queue
from backend.client.main_page_emitter import MainPageEmitter
from music_playing.song_class import SongData

CHUNK = 1024

class AudioHandler:
    def __init__(self, main_page_emitter :MainPageEmitter):
        self.p = pyaudio.PyAudio()
        
        self.stream = self.p.open(format=self.p.get_format_from_width(2),
                             channels=1,
                             rate=44100,
                             output=True,
                             frames_per_buffer=CHUNK)
        
        self.buffer = queue.Queue()
        self.main_page_emitter = main_page_emitter

    def add_to_buffer(self, data):
        self.buffer.put(data)

    def play_audio(self, song_data: SongData):
        self.frames_played = 0
        
        while not self.buffer.empty():
            data = self.buffer.get()
            self.stream.write(data)
            self.frames_played += CHUNK
            progress = self.calculate_progress(song_data)
            self.main_page_emitter.update_song_progress.emit(progress) 

    def calculate_progress(self, song_data: SongData):
        return self.frames_played / song_data.nframes  

    def terminate(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.frames_played = 0  

