import logging
import wave
import os
from music_playing.song_class import SongInfo

def get_song_list(song_dir):
    return [get_song_data(song_dir, song_name) for song_name in os.listdir(song_dir)]

def get_name_to_song_data_dict(song_dir):
    song_list = get_song_list(song_dir)
    return {song_data.name : song_data for song_data in song_list}

def get_song_data(song_dir, song_name):
    song_path = os.path.join(song_dir, song_name)
    with wave.open(song_path) as mywav:
        nframes, framerate = mywav.getnframes(), mywav.getframerate()
    
    total_secs = nframes / framerate
            
    song_data = SongInfo(name=song_name, length=total_secs, nframes=nframes, framerate=framerate)
    logging.debug(f"{song_data=}")
    return song_data
    
    