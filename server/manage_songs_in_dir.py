import logging
import wave
import os
from music_playing.song_class import SongInfo, song_orm_to_songinfo
from pathlib import Path
from pydub import AudioSegment
from database.models import Song
from dataclasses import asdict
from database import utils


def get_all_songs_in_db(session):
    songs = session.query(Song).all()
    return [song_orm_to_songinfo(song) for song in songs]


def get_all_song_info_dicts_in_dir(song_dir) -> list[dict]:
    song_dicts = []
    for song in os.listdir(song_dir):
        song_dict = get_song_info_dict(song_dir, song)
        song_dicts.append(song_dict)
    return song_dicts


def load_songs_to_db(song_dir, session):
    for id, song in enumerate(os.listdir(song_dir)):
        song_dict = get_song_info_dict(song_dir, song)
        song = Song(**song_dict)
        session.add(song)
    session.commit()


def get_song_info_dict(song_dir, song_name) -> dict:
    song_path = Path(song_dir) / song_name
    audio = AudioSegment.from_wav(str(song_path))
    nframes = audio.frame_count()
    framerate = audio.frame_rate
    nchannels = audio.channels

    length = nframes / framerate
    song_dict =  {"name": song_path.stem, "nframes": nframes, "framerate": framerate, "nchannels": nchannels, "length": length}
    return song_dict


    