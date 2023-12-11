import logging
import wave
import os
from music_playing.song_class import SongInfo
import math
from pydub import AudioSegment

def get_song_list(song_dir):
    return [get_song_info(song_dir, song_name) for song_name in os.listdir(song_dir)]

def get_name_to_songinfo_dict(song_dir):
    song_list = get_song_list(song_dir)
    return {song_data.name : song_data for song_data in song_list}

def get_song_info(song_dir, song_name):
    song_path = os.path.join(song_dir, song_name)
    audio = AudioSegment.from_wav(song_path)
    nframes = audio.frame_count()
    framerate = audio.frame_rate
    nchannels = audio.channels

    length = nframes / framerate
    song_info = SongInfo(name=song_name, nframes=nframes, framerate=framerate, nchannels=nchannels, length=length)
    logging.debug(f"{song_info=}")
    return song_info

    