from database.models import User, Playlist, Base, Song
import logging
from database import SQLITE_PATH
from sqlalchemy import create_engine

def log_user_and_playlists(user: User):
    logging.info(f"\n{user}")
    if not user.playlists:
        logging.debug("User has no playlists")
        return
    
    for playlist in user.playlists:
        log_playlist(playlist)

def log_playlist(playlist):
    logging.debug(f"\n{playlist}")
        
    for song in playlist.songs:
        logging.debug(f"{song}")
            
def log_all_songs(session):
    logging.debug("Logging all songs")
    for song in session.query(Song).all():
        logging.debug(song)
        
        
def log_all_users_playlists(session):
    for user in session.query(User).all():
        log_user_and_playlists(user)
        
def log_all_users(session):
    logging.debug("Logging all users")
    all_users = session.query(User).all()
    for user in all_users:
        logging.debug(user)
    if not all_users:
        logging.debug("No users") 
        
               
def log_all_playlists():
    session = create_session()
    logging.debug("Logging all playlists")
    logging.debug("Playlist count: " + str(session.query(Playlist).count()))
    all_playlists = session.query(Playlist).all()
    for playlist in all_playlists:
        log_playlist(playlist)
    if not all_playlists:
        logging.debug("No playlists")

def reset_tables():
    engine = create_engine(SQLITE_PATH)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def create_session():
    engine = create_engine(SQLITE_PATH)
    engine.echo = False
    from sqlalchemy.orm import Session
    return Session(bind=engine)


def get_all_songs(session):
    return session.query(Song).all()
    


