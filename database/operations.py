# operations.py
def add_song_to_playlist(session, playlist_id, song):
    playlist = session.query(Playlist).filter_by(id=playlist_id).first()
    items = eval(playlist.items)
    items.append(song)
    playlist.items = str(items)
    session.commit()

def remove_song_from_playlist(session, playlist_id, song):
    playlist = session.query(Playlist).filter_by(id=playlist_id).first()
    items = eval(playlist.items)
    items.remove(song)
    playlist.items = str(items)
    session.commit()
