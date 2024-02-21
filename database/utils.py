from database.models import User, Playlist, Base
import logging


def log_user_and_playlists(session, user: User):
    logging.info(f"User: {user.username}")
    if not user.playlists:
        logging.debug("User has no playlists")
        return
    
    for playlist in user.playlists:
        logging.debug(f"Playlist ID: {playlist.id}")
        
        # Iterate through the songs in the playlist
        for song in playlist.songs:
            logging.debug(f"Song ID: {song.id}, Name: {song.name}, Length: {song.length}")
        
        
def log_all_users_playlists(session):
    for user in session.query(User).all():
        log_user_and_playlists(session, user)
        

def reset_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    
    


