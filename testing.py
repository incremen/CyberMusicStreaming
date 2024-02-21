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
    user1 = User(username="user1")
    user2 = User(username="user2")

    playlist1 = Playlist(name="playlist1")
    playlist2 = Playlist(name="playlist2")
    playlist3 = Playlist(name="playlist3")
    playlist4 = Playlist(name="playlist4")

    user1.playlists.append(playlist1)
    user1.playlists.append(playlist2)
    user2.playlists.append(playlist1)
    user2.playlists.append(playlist2)

    session.add_all([user1, user2, playlist1, playlist2, playlist3, playlist4])
        
    session.commit()


if __name__ == "__main__":
    main()
