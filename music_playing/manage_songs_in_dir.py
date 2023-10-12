import logging
import wave
import os
from music_playing.song_class import SongInfo
import math


def get_song_list(song_dir, chunk):
    return [get_song_info(song_dir, song_name, chunk) for song_name in os.listdir(song_dir)]

def get_name_to_songinfo_dict(song_dir, chunk):
    song_list = get_song_list(song_dir, chunk)
    return {song_data.name : song_data for song_data in song_list}

def get_song_info(song_dir, song_name, chunk):
    song_path = os.path.join(song_dir, song_name)
    with wave.open(song_path) as mywav:
        nframes = mywav.getnframes()
        framerate = mywav.getframerate()
        nchannels = mywav.getnchannels()
        
    length = nframes / framerate
    max_seq = math.ceil(nframes / chunk)
    song_data = SongInfo(name=song_name, nframes=nframes, framerate=framerate, nchannels=nchannels, length=length, max_seq=max_seq)
    logging.debug(f"{song_data=}")
    return song_data

def get_song_path(self, song_name):
        if not song_name.endswith(".wav"):
            song_name += ".wav"
        song_path = os.path.join(self.songs_dir, song_name)
        return song_path
    
    