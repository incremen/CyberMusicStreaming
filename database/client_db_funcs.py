from database.models import User, Playlist, Base
from database.operations import add_song_to_playlist, remove_song_from_playlist
import database.utils as utils
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from custom_logging import CustomLogger

DATABASE_URL = "sqlite:///database/test_db.db"


def create_playlist_for_user(session, playlist_items : list):
    user = session.query(User).first()
    playlist_str = repr(playlist_items)
    playlist = Playlist(items=playlist_str, user=user)
    session.add(playlist)
    session.commit()
    
    
def update_user_playlist(session, new_playlist_items: list):
    user = session.query(User).first()
    playlist = user.playlists[0]
    playlist.items = repr(new_playlist_items)
    session.commit()
    

def clear_user_playlists(session):
    session.query(Playlist).delete()
    session.commit()
    
    
def create_session():
    engine = create_engine(DATABASE_URL)
    session = Session(bind=engine)
    return session
    
