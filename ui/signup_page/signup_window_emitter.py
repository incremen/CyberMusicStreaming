from PyQt5.QtCore import QObject, pyqtSignal
from ui.signup_page.signup_window import SignupWindow

class SignupWindowEmitter(QObject):
    account_create_result = pyqtSignal(bool, str)
        
    def setup_connections(self, signup_window : SignupWindow):
        self.account_create_result.connect(signup_window.handle_new_acc_response)