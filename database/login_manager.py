import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import User  # Assuming you have a User model defined elsewhere
from log_db import log_db
from result import Ok, Err, Result, is_ok, is_err
from typing import TYPE_CHECKING
from ui.login_page.login_window_emitter import LoginWindowEmitter


if TYPE_CHECKING:
    from client.client_socket import ClientSocketHandler
class LoginManager:
    def __init__(self, db_url, client_socket_handler : 'ClientSocketHandler'):
        self.socket_handler = client_socket_handler
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        self.current_user_id = None
        self.login_window_emitter : LoginWindowEmitter = None
        
        self.signed_in = False
        self.username = None
        self.password = None
        self.playlists : dict[str, str] = None

    def get_current_user(self):
        if self.current_user_id is None:
            return None

        session = self.Session()
        user = session.query(User).get(self.current_user_id)
        session.close()
        return user

    def create_new_account(self, username, password):
        logging.info(f"Attempting to create a new account for user: {username}")
        self.socket_handler.emit_to_server('create_new_account', {'username': username, 'password': password})

    def login(self, username, password):
        logging.info(f"Attempting to log in user: {username}")
        self.socket_handler.emit_to_server('login', {'username': username, 'password': password})

    def login_response(self, result):
        if not result:
            self.username = None
            self.password = None
        else:
            self.signed_in = True

        self.login_window_emitter.login_response.emit(result)

    def logout(self) -> Result[bool, str]:
        if self.current_user_id is None:
            error_message = "No user is currently logged in"
            logging.error(error_message)
            return Err(error_message)

        current_user = self.get_current_user()
        logging.info(f"Logging out user: {current_user.username}")
        self.current_user_id = None
        logging.info("User logged out successfully")
        return Ok(True)