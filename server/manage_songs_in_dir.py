import logging
import wave
import os
from music_playing.song_class import SongInfo, song_orm_to_songinfo
from pathlib import Path
from pydub import AudioSegment
from database.models import Song
from dataclasses import asdict
from database import utils


def get_song_list():
    session = utils.create_session()
    songs = session.query(Song).all()
    return [song_orm_to_songinfo(song) for song in songs]


def load_songs_to_db(song_dir):
    session = utils.create_session()
    for id, song in enumerate(os.listdir(song_dir)):
        song_info = get_song_info(song_dir, song, id)
        song = Song(**asdict(song_info))
        session.add(song)
    session.commit()


def get_song_info(song_dir, song_name, id : int):
    song_path = Path(song_dir) / song_name
    audio = AudioSegment.from_wav(str(song_path))
    nframes = audio.frame_count()
    framerate = audio.frame_rate
    nchannels = audio.channels

    length = nframes / framerate
    song_info = SongInfo(name=song_path.stem, nframes=nframes, framerate=framerate, nchannels=nchannels, length=length, id = id)
    logging.debug(f"{song_info=}")
    return song_info


    