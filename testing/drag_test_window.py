from PyQt5 import QtCore, QtGui, QtWidgets
from testing.drag_test_ui import Ui_MainWindow


class TestWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   def __init__(self,):
       super(TestWindow, self).__init__()
       self.setupUi(self)
