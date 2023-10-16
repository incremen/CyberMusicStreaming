import wave
import math
import os
from custom_logging import CustomLogger
import logging
from pydub import AudioSegment

testing_logger = CustomLogger(log_files=["testing.log"])

CHUNK = 4096

def calc_total_chunks(song_dir, song_name, chunk):
    song_path = os.path.join(song_dir, song_name)
    audio = AudioSegment.from_wav(song_path)
    return math.ceil(audio.frame_count() / chunk)

songs = ["american.wav", "beats.wav", "No_38.wav"]


def count_chunks_in_song(song_dir, song_name, chunk):
    song_path = os.path.join(song_dir, song_name)
    chunk_count = 0

    with wave.open(song_path) as mywav:
        while True:
            song_data_chunk = mywav.readframes(chunk)
            if not song_data_chunk:
                break
            chunk_count += 1

    return chunk_count


songs = ["warm_hall.wav", "hall.wav", "american.wav", "beats.wav", "No_38.wav"]

for song in songs:
    print(f"total chunks calc for {song}: {calc_total_chunks('songs', song, CHUNK)}")
    print(f"total chunks read for {song}: {count_chunks_in_song('songs', song, CHUNK)}")


