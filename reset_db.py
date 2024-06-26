# reset_tables.py
from sqlalchemy import create_engine
from database.models import Base
from custom_logging import CustomLogger
from database.utils import log_all_users_playlists, create_session
from database import SQLITE_PATH, SONG_DIR
from make_default_db_playlist import load_songs_to_db
def reset_tables():
    CustomLogger()
    log_all_users_playlists(create_session())
    engine = create_engine(SQLITE_PATH)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    load_songs_to_db(SONG_DIR, create_session())

if __name__ == "__main__":
    reset_tables()
