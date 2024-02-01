from database.models import User, Playlist
import logging


def log_user_and_playlists(session, user_id):
    user = session.query(User).filter_by(id=user_id).first()
    logging.info(f"User: {user.username}")
    for playlist in user.playlists:
        logging.debug(f"Playlist ID: {playlist.id}, Items: {playlist.items}")
