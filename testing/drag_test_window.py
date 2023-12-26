from PyQt5 import QtCore, QtGui, QtWidgets
from testing.drag_test_ui import Ui_MainWindow
from PyQt5.QtWidgets import QWidget
from testing.working_dummy import *




from PyQt5 import QtCore, QtGui, QtWidgets
from testing.drag_test_ui import Ui_MainWindow
from PyQt5.QtWidgets import QWidget
from testing.working_dummy import *

class TestWindow(QtWidgets.QMainWindow, Ui_MainWindow):
 def __init__(self,):
    super(TestWindow, self).__init__()
    self.setupUi(self)
    
    self.drag_widget.mousePressEvent = lambda event: mouse_press_event(self.drag_widget, event)
    self.drag_widget.mouseMoveEvent = lambda event: mouseMoveEvent(self.drag_widget, event)
    
    self.drop_widget.setAcceptDrops(True)
    self.drop_widget.dragEnterEvent = lambda event: dragEnterEvent(self.drop_widget, event)
    self.drop_widget.dropEvent = lambda event: dropEvent(self.drop_widget, event)

       


