import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import User  # Assuming you have a User model defined elsewhere
from returns.result import Result, Success, Failure

import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import User
from result import Ok, Err, Result, is_ok, is_err

class LoginManager:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        self.current_user = None

    def create_new_account(self, username, password) -> Result[User, str]:
        logging.info(f"Attempting to create a new account for user: {username}")
        session = self.Session()
        existing_user = session.query(User).filter_by(username=username).first()
        if existing_user:
            error_message = f"User {username} already exists"
            logging.error(error_message)
            return Err(error_message)
        new_user = User(username=username, password=password)
        
        self.current_user = new_user
        session.add(new_user)
        session.expunge(new_user)
        session.commit()
        session.close()
        
        logging.info(f"Account for user {username} created successfully")
        return Ok(new_user)

    def login(self, username, password) -> Result[User, str]:
        logging.info(f"Attempting to log in user: {username}")
        session = self.Session()
        user: User = session.query(User).filter_by(username=username).first()
        if not user:
            error_message = f"User {username} not found"
            logging.error(error_message)
            return Err(error_message)
        if user.password != password:
            error_message = f"Wrong password"
            logging.error(error_message)
            return Err(error_message)
        self.current_user = user
        session.expunge(user)
        session.close()
        logging.info(f"User {username} logged in successfully")
        return Ok(user)

    def logout(self) -> Result[bool, str]:
        if not self.current_user:
            raise Exception("User is not logged in")
        logging.info(f"Logging out user: {self.current_user.username}")
        self.current_user = None
        logging.info("User logged out successfully")
        return Ok(True)


