from database.models import User, Playlist, Base, Song
from database.operations import add_song_to_playlist, remove_song_from_playlist
import database.utils as utils
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from custom_logging import CustomLogger
from database import client_db_funcs
import logging
def main():
    custom_logger = CustomLogger(log_files=["testing.log"])
    custom_logger.clear_logs()
    session = client_db_funcs.create_session()
    utils.reset_tables(client_db_funcs.get_engine())
    create_dummy_data(session)
    
    utils.log_all_users_playlists(session)

def create_dummy_data(session):
    users = [User(username=f"user{i}") for i in range(1,   5)]
    for user in users:
        session.add(user)
    session.commit()

    songs = [
        Song(name=f"song{i}", length=i *   0.5, nframes=i *   100, framerate=i *   44100, nchannels=i)
        for i in range(1,   7)
    ]
    for song in songs:
        session.add(song)
    session.commit()

    playlists = [Playlist(name=f"playlist{i}") for i in range(1,   7)]
    for i, playlist in enumerate(playlists):
        for song in songs[i:i+3]:
            logging.debug(f"Adding {song.name} to {playlist.name}")
            playlist.songs.append(song)
        logging.debug(f"{playlist} has {len(playlist.songs)} songs")
        
        user = users[i %  4]
        playlist.user = user
        
        session.add(playlist)
        
    session.commit()


if __name__ == "__main__":
    main()
