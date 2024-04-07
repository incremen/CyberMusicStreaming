import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import User, Song
from log_db import log_db
from result import Ok, Err, Result, is_ok, is_err
from database.utils import create_session

def create_new_account(username, password) -> Result:
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
    return Ok(ok_message)

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

def search_for_term(search_term : str):
    session = create_session()
    songs_found = session.query(Song).filter(Song.name.like(f'{search_term}%')).all()
    return songs_found