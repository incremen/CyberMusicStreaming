from PyQt5.QtCore import QObject, pyqtSignal
from ui.login_page.login_window import LoginWindow

class LoginWindowEmitter(QObject):
    login_response = pyqtSignal(bool)
        
    def setup_connections(self, login_window : LoginWindow):
        self.login_response.connect(login_window.handle_login_response)