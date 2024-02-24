from database.models import User, Playlist, Base, Song
import logging
from database import SQLITE_PATH
from sqlalchemy import create_engine

def log_user_and_playlists(session, user: User):
    logging.info(f"\n{user}")
    if not user.playlists:
        logging.debug("User has no playlists")
        return
    
    for playlist in user.playlists:
        logging.debug(f"\n{playlist}")
        
        for song in playlist.songs:
            logging.debug(f"{song}")
            
def log_all_songs(session):
    for song in session.query(Song).all():
        logging.debug(song)
        
        
def log_all_users_playlists(session):
    for user in session.query(User).all():
        log_user_and_playlists(session, user)
        

def reset_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def create_session():
    engine = create_engine(SQLITE_PATH)
    from sqlalchemy.orm import Session
    return Session(bind=engine)


def get_all_songs(session):
    return session.query(Song).all()
    


