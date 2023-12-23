from ui.search_page.search_page_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QListWidget, QListWidgetItem


class SearchWindow(Ui_MainWindow, QMainWindow): 
    def __init__(self):
       super(SearchWindow, self).__init__()
       self.setupUi(self)
       self.show()
