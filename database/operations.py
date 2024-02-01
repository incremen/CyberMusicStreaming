from database.models import Playlist
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
