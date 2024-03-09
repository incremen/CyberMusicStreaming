

from database.models import User, Playlist, Base, Song
import database.utils as utils
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from custom_logging import CustomLogger
from database import client_db_funcs
import logging
import os
from server.manage_songs_in_dir import load_songs_to_db, get_song_list
from server import manage_songs_in_dir

# default_songs = [{'name': 'american', 'length': 62.13451247165533, 'nframes': 2740132, 'framerate': 44100, 'nchannels': 2, 'id': 0},
# {'name': 'beats', 'length': 64.0, 'nframes': 2822400, 'framerate': 44100, 'nchannels': 2, 'id': 1},
# {'name': 'cant_keep_getting_away', 'length': 5.01825, 'nframes': 240876, 'framerate': 48000, 'nchannels': 2, 'id': 2},
# {'name': 'No_38', 'length': 11.97938775510204, 'nframes': 528291, 'framerate': 44100, 'nchannels': 2, 'id': 3}
# ]

def main():
    custom_logger = CustomLogger(log_files=["testing.log"]) 
    custom_logger.clear_logs()
    song_dir = os.path.abspath(r"songs")
    songs_list = get_song_list(song_dir)
    session = utils.create_session()
    session.close()


def create_default_playlist(songs_list):
    playlist1 = Playlist(name="default_playlist")
    for song in songs_list:
        playlist1.songs.append(song)


if __name__ == "__main__":
    main()
