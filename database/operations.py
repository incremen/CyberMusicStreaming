from database.models import Playlist, User
from sqlalchemy.orm import Session
import logging


def add_song_to_playlist(session, playlist : Playlist, song : Playlist):
    items = eval(playlist.items)
    logging.debug(f"{items=}")
    items.append(song)
    logging.debug(f"items after appending: {items}")
    playlist.items = str(items)
    session.commit()

def remove_song_from_playlist(session, playlist: Playlist, song : str):
    items = eval(playlist.items)
    items.remove(song)
    playlist.items = str(items)
    session.commit()
    
    

def add_playlist_to_user(session: Session, user: User, playlist: Playlist) -> None:
    user.playlists.append(playlist)
    session.commit()
