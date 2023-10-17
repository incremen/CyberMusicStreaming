import logging
import wave
import os
from music_playing.song_class import SongInfo
import math
from pydub import AudioSegment

def get_song_list(song_dir, chunk):
    return [get_song_info(song_dir, song_name, chunk) for song_name in os.listdir(song_dir)]

def get_name_to_songinfo_dict(song_dir, chunk):
    song_list = get_song_list(song_dir, chunk)
    return {song_data.name : song_data for song_data in song_list}

def get_song_info(song_dir, song_name, chunk):
    song_path = os.path.join(song_dir, song_name)
    audio = AudioSegment.from_wav(song_path)
    nframes = audio.frame_count()
    framerate = audio.frame_rate
    nchannels = audio.channels

    length = nframes / framerate
    max_seq = math.ceil(nframes / chunk)
    song_info = SongInfo(name=song_name, nframes=nframes, framerate=framerate, nchannels=nchannels, length=length, max_seq=max_seq)
    logging.debug(f"{song_info=}")
    return song_info


def calc_total_chunks(song_dir, song_name, chunk):
    song_path = os.path.join(song_dir, song_name)
    audio = AudioSegment.from_wav(song_path)
    return math.ceil(audio.frame_count() / chunk)
    