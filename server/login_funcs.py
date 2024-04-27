import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import User, Song, Playlist
from log_db import log_db
from result import Ok, Err, Result, is_ok, is_err
from database.utils import create_session

def create_new_account(username, password) -> Result[str, User]:
    logging.info(f"Attempting to create a new account for user: {username}")
    session = create_session()
    existing_user = session.query(User).filter_by(username=username).first()

    if existing_user:
        error_message = f"User {username} already exists"
        logging.error(error_message)
        session.close()
        return Err(error_message)

    new_user = User(username=username, password=password)
    session.add(new_user)
    session.commit()
    ok_message = f"Account for user {username} created successfully"
    logging.info(ok_message)
    session.close()
    return Ok(new_user)

def login(username, password) -> Result[User, str]:
    logging.info(f"Attempting to log in user: {username}")
    session = create_session()
    user: User = session.query(User).filter_by(username=username).first()

    if not user:
        error_message = f"User {username} not found"
        logging.error(error_message)
        session.close()
        return Err(error_message)

    if user.password != password:
        error_message = f"Wrong password"
        logging.error(error_message)
        session.close()
        return Err(error_message)

    ok_msg = f"User {username} logged in successfully"
    logging.info(ok_msg)
    session.close()
    return Ok(user)

def save_playlist(username, playlist_dict: dict):
    session = create_session()
    user = session.query(User).filter_by(username=username).first()
    session.add(user)

    playlist_to_edit = find_matching_user_playlist(playlist_dict, user)
    if not playlist_to_edit:
        playlist_to_edit = Playlist(name=playlist_dict["name"])
        user.playlists.append(playlist_to_edit)
        session.add(playlist_to_edit)

    playlist_to_edit.songs = []

    for song_name in playlist_dict["songs"]:
        song = session.query(Song).filter_by(name=song_name).first()
        playlist_to_edit.songs.append(song)
        
    from database.utils import log_user_and_playlists
    log_user_and_playlists(user)

    logging.checkpoint(f"{playlist_dict=}, {playlist_to_edit.songs=}")
    session.commit()
    session.close()
    return user

def find_matching_user_playlist(playlist_dict, user):
    for user_playlist in user.playlists:
        if user_playlist.name == playlist_dict["name"]:
            return user_playlist
        
    return None

def query_user(username):
    session = create_session()
    user = session.query(User).filter_by(username=username).first()
    session.close()
    return user


    

def search_for_term(search_term : str):
    session = create_session()
    songs_found = session.query(Song).filter(Song.name.like(f'{search_term}%')).all()
    session.close()
    return songs_found