from database.models import User, Playlist, Base, Song
import database.utils as utils
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from custom_logging import CustomLogger
from database import SQLITE_PATH


def update_playlist(session : Session, playlist : Playlist, to_add : list[Song] | Song):
    playlist.songs = []
    if isinstance(to_add, Song):
        new_playlist_items = [to_add]
    for song in new_playlist_items:
        playlist.songs.append(song)
    session.commit()
    

def clear_user_playlists(session):
    session.query(Playlist).delete()
    session.commit()
    
    
def create_session():
    engine = create_engine(SQLITE_PATH)
    session = Session(bind=engine)
    return session


def get_first_user(session):
    return session.query(User).first()


def get_first_playlist(session):
    return session.query(Playlist).first()


def get_engine():
    return create_engine(SQLITE_PATH)
    
