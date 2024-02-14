from database.models import User, Playlist, Base
from database.operations import add_song_to_playlist, remove_song_from_playlist
import database.utils as utils
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from custom_logging import CustomLogger
from database import client_db_funcs
def main():
    custom_logger = CustomLogger(log_files=["testing.log"])
    session = client_db_funcs.create_session()
    client_db_funcs.clear_user_playlists(session)
    utils.log_all_users_playlists(session)


if __name__ == "__main__":
    main()
