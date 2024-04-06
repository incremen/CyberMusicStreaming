from database.models import Base
from custom_logging import CustomLogger
from database.utils import log_all_users_playlists, create_session, log_all_songs, log_all_playlists

def log_db():
    CustomLogger()
    log_all_users_playlists(create_session())
    log_all_songs(create_session())
    log_all_playlists()
    


if __name__ == "__main__":
    log_db()
