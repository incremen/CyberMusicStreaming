from sqlalchemy.orm import sessionmaker
from database.models import Base, User, Playlist, Song
import logging
from sqlalchemy import create_engine
from database import SQLITE_PATH


class DatabaseManager:
    def __init__(self, db_path):
        self.engine = create_engine(SQLITE_PATH)
        self.session = sessionmaker(bind=self.engine)

    def log_users_playlists(self, user: User):
        logging.info(f"\n{user}")
        if not user.playlists:
            logging.debug("User has no playlists")
            return
        
        for playlist in user.playlists:
            self.log_playlist(playlist)

    def log_playlist(self, playlist):
        logging.debug(f"\n{playlist}")
        
        if not playlist.songs:
            logging.debug("Playlist has no songs")
            return
        for song in playlist.songs:
            logging.debug(f"{song}")

    def log_all_users_playlists(self):
        self.session = self.self.session()
        for user in self.session.query(User).all():
            self.log_users_playlists(user)
        self.session.close()

    def add_new_playlist(self, username, playlist_name):
        self.session = self.self.session()
        user = self.session.query(User).filter_by(username=username).first()
        
        if not user:
            logging.error(f"User with username {username} not found.")
        
        new_playlist = Playlist(name=playlist_name)
        self.session.add(new_playlist)
        user.playlists.append(new_playlist)
        self.session.commit()
        logging.info(f"New playlist '{playlist_name}' added for user {username}.")
        self.session.close()

    def add_song_to_playlist(self, playlist_id, song_id):
        playlist = self.session.query(Playlist).filter_by(id=playlist_id).first()
        song = self.session.query(Song).filter_by(id=song_id).first()
        
        if not playlist:
            logging.error(f"Playlist with id {playlist_id} not found.")
            self.session.close()
            return
        
        if not song:
            logging.error(f"Song with id {song_id} not found.")
            self.session.close()
            return
        
        playlist.songs.append(song)
        self.session.commit()
        logging.info(f"Song with id {song_id} added to playlist with id {playlist_id}.")
        self.session.close()
