from ui.login_page.login_page_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QListWidget, QListWidgetItem
import ui.main_page.main_page
from ui import gui_funcs


class LoginWindow(Ui_MainWindow, QMainWindow): 
   def __init__(self, socket_handler, audio_handler):
       super(LoginWindow, self).__init__()
       self.socket_handler = socket_handler
       self.audio_handler = audio_handler
       self.main_window = ui.main_page.main_page.MainPage(self.socket_handler, self.audio_handler)
       self.setupUi(self)
       self.setup_btns()
       self.show()
       
   def setup_btns(self):
       self.ready_btn.clicked.connect(self.ready_btn_click)
           
   def ready_btn_click(self, btn_clicked):
      self.main_window.show()
           
    
       
        
