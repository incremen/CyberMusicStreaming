# reset_tables.py
from sqlalchemy import create_engine
from database.models import Base
from custom_logging import CustomLogger
from database.utils import log_all_users_playlists, create_session
DATABASE_URL = "sqlite:///database/test_db.db"

def reset_tables():
    CustomLogger()
    log_all_users_playlists(create_session())
    engine = create_engine(DATABASE_URL)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    reset_tables()
