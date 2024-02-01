from database.models import User, Playlist, Base
from database.operations import add_song_to_playlist, remove_song_from_playlist
from database.utils import log_user_and_playlists
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from custom_logging import CustomLogger

def main():
    custom_logger = CustomLogger(log_files=["testing.log"])
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    user1 = User(username="user1", password="pass1")
    session.add(user1)
    session.commit()

    playlist1 = Playlist(items="['song1', 'song2']", user=user1)
    session.add(playlist1)
    session.commit()

    log_user_and_playlists(session, user1.id)

    add_song_to_playlist(session, playlist1.id, 'song3')
    remove_song_from_playlist(session, playlist1.id, 'song1')
    log_user_and_playlists(session, user1.id)

if __name__ == "__main__":
    main()
