import pprint
from database.models import User, Playlist, Base, Song
import database.utils as utils
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from custom_logging import CustomLogger, debug_vars
from database import client_db_funcs
import logging
import os
from server.manage_songs_in_dir import load_songs_to_db, get_all_songs_in_db
from server import manage_songs_in_dir
from database.login_manager import LoginManager
from database import SQLITE_PATH
from result import Ok, Err, Result, is_ok, is_err

def main():
    custom_logger = CustomLogger(log_files=["testing.log"]) 
    custom_logger.clear_logs()
    song_dir = os.path.abspath(r"songs")
    session = utils.create_session()
    login_manager = LoginManager(SQLITE_PATH)
    
    create_dummy_user_playlist(session)


def test_creating_accounts(session, login_manager):
    username = 'testuser'
    password = 'testpassword'
    result = login_manager.create_new_account(username, password)
    if is_ok(result):
        logging.info("New account created successfully.")
    else:
        logging.error(f"Failed to create account: {result.unwrap_err()}")

    result = login_manager.login(username, password)
    if is_ok(result):
        logging.info("Login successful.")
    else:
        logging.error(f"Login failed: {result.unwrap_err()}")

    result = login_manager.logout()
    if is_ok(result):
        logging.info("Logout successful.")
    else:
        logging.error(f"Logout failed: {result.unwrap_err()}")
    utils.log_all_songs(session)   


def create_dummy_user_playlist(session : Session):
    user1 = User(username="1", password="1")
    session.add(user1)
    playlist1 = Playlist(name="playlist1")
    user1.playlists.append(playlist1)
    song1 = Song(name="Song 1", length=3.5, nframes=300, framerate=44100, nchannels=2)
    song2 = Song(name="Song 2", length=4.0, nframes=400, framerate=44100, nchannels=2)
    playlist1.songs.extend([song1, song2])
    session.add(user1)
    session.commit()


def create_dummy_data(session):
    user1 = User(username="user1")
    user2 = User(username="user2")

    playlist1 = Playlist(name="playlist1")
    playlist2 = Playlist(name="playlist2")
    playlist3 = Playlist(name="playlist3")
    playlist4 = Playlist(name="playlist4")

    # Associate playlists with users
    user1.playlists.append(playlist1)
    user1.playlists.append(playlist2)
    user2.playlists.append(playlist1)
    user2.playlists.append(playlist2)
    user2.playlists.append(playlist4)

    song1 = Song(name="Song 1", length=3.5, nframes=300, framerate=44100, nchannels=2)
    song2 = Song(name="Song 2", length=4.0, nframes=400, framerate=44100, nchannels=2)
    song3 = Song(name="Song 3", length=5.0, nframes=500, framerate=44100, nchannels=2)
    song4 = Song(name="Song 4", length=6.0, nframes=600, framerate=44100, nchannels=2)
    song5 = Song(name="Song 5", length=7.0, nframes=700, framerate=44100, nchannels=2)

    playlist1.songs.extend([song1, song2, song3])
    playlist2.songs.extend([song2, song3, song4])
    playlist3.songs.extend([song3, song4, song5])
    playlist4.songs.extend([song4, song5, song1])

    session.add_all([user1, user2, playlist1, playlist2, playlist3, playlist4, song1, song2, song3, song4, song5])

    session.commit()



if __name__ == "__main__":
    main()
