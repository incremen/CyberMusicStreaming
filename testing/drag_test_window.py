from PyQt5 import QtCore, QtGui, QtWidgets
from testing.drag_test_ui import Ui_MainWindow
from PyQt5.QtWidgets import QWidget
from testing.working_dummy import *


def replace_widget(old_widget, new_widget):
   # Copy properties from the old widget to the new widget
   new_widget.setGeometry(old_widget.geometry())
   new_widget.setText(old_widget.text())
   new_widget.setObjectName(old_widget.objectName())
   
   # Delete the old widget
   old_widget.deleteLater()



class TestWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   def __init__(self,):
       super(TestWindow, self).__init__()
       self.setupUi(self)
       
       # Create new draggable and droppable labels
       self.new_drag_widget = DraggableLabel(self.centralwidget)
       self.new_drop_widget = DropLabel(self.centralwidget)
       
       # Replace old widgets with new widgets
       replace_widget(self.drag_widget, self.new_drag_widget)
       replace_widget(self.drop_widget, self.new_drop_widget)
       self.drag_widget = self.new_drag_widget
       self.drop_widget = self.new_drop_widget

