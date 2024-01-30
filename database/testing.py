# test.py
from database.models import User, Playlist, Base
from database.operations import add_song_to_playlist, remove_song_from_playlist
from database.utils import log_user_and_playlists
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

def main():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    # Create users and playlists
    user1 = User(username="user1", password="pass1")
    session.add(user1)
    session.commit()

    playlist1 = Playlist(items="['song1', 'song2']", user=user1)
    session.add(playlist1)
    session.commit()

    # Test logging in
    log_user_and_playlists(session, user1.id)

    # Test editing playlists
    add_song_to_playlist(session, playlist1.id, 'song3')
    log_user_and_playlists(session, user1.id)

    remove_song_from_playlist(session, playlist1.id, 'song1')
    log_user_and_playlists(session, user1.id)

if __name__ == "__main__":
    main()
