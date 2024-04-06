import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import User  # Assuming you have a User model defined elsewhere
from returns.result import Result, Success, Failure
from log_db import log_db

class LoginManager:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        self.current_user_id = None

    def get_current_user(self):
        if self.current_user_id is None:
            return None

        session = self.Session()
        user = session.query(User).get(self.current_user_id)
        session.close()
        return user

    def create_new_account(self, username, password) -> Result[User, str]:
        logging.info(f"Attempting to create a new account for user: {username}")
        session = self.Session()
        existing_user = session.query(User).filter_by(username=username).first()

        if existing_user:
            error_message = f"User {username} already exists"
            logging.error(error_message)
            session.close()
            return Failure(error_message)

        new_user = User(username=username, password=password)
        self.current_user_id = new_user.id
        session.add(new_user)
        session.commit()
        logging.info(f"Account for user {username} created successfully")
        log_db()
        session.close()
        return Success(new_user)

    def login(self, username, password) -> Result[User, str]:
        logging.info(f"Attempting to log in user: {username}")
        session = self.Session()
        user: User = session.query(User).filter_by(username=username).first()

        if not user:
            error_message = f"User {username} not found"
            logging.error(error_message)
            session.close()
            return Failure(error_message)

        if user.password != password:
            error_message = f"Wrong password"
            logging.error(error_message)
            session.close()
            return Failure(error_message)

        self.current_user_id = user.id
        logging.info(f"User {username} logged in successfully")
        log_db()
        session.close()
        return Success(user)

    def logout(self) -> Result[bool, str]:
        if self.current_user_id is None:
            error_message = "No user is currently logged in"
            logging.error(error_message)
            return Failure(error_message)

        current_user = self.get_current_user()
        logging.info(f"Logging out user: {current_user.username}")
        self.current_user_id = None
        logging.info("User logged out successfully")
        return Success(True)