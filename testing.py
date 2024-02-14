from database.models import User, Playlist, Base
from database.operations import add_song_to_playlist, remove_song_from_playlist
import database.utils as utils
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from custom_logging import CustomLogger

def main():
    custom_logger = CustomLogger(log_files=["testing.log"])
    database_url = "sqlite:///database/test_db.db"
    engine = create_engine(database_url)
    # utils.reset_tables(engine)
    session = Session(bind=engine)

    # user1 = User(username="Itamar", password="password")
    # session.add(user1)
    # session.commit()
    utils.log_all_users_playlists(session)


if __name__ == "__main__":
    main()
