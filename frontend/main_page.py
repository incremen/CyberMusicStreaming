from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget, QGridLayout
from PyQt5 import uic, QtGui
import logging
import random
from PyQt5.QtGui import QTransform
from PyQt5.QtCore import QTimer
import gui_funcs
from PyQt5.QtGui import QFont


class MainPage(QMainWindow):
    def __init__(self):
        super(MainPage, self).__init__()
        uic.loadUi(r"frontend\tictactoe_gui.ui", self)
        self.setWindowTitle(f"Stream music!")
        self.main_widget = self.findChild(QWidget, "main_widget")
        self.setup_main_widget_properties()
        
        self.show()
        
    def song_dict_received(self, songs : dict):
        for song in songs:
            self.add_song_to_grid(song["name"])
    
    def setup_main_widget_properties(self):
        main_widget = self.main_widget
        self.song_grid = main_widget.findChild(QGridLayout, "song_grid")
        
    def add_song_to_grid(self, text):
        song_label = QLabel(text)
        row = self.song_grid.rowCount()
        col = self.song_grid.columnCount()
    
        if col > 1:
            row += 1
            col = 0
        
        self.song_grid.addWidget(song_label, row, col)
    
    def closeEvent(self, event):
        if not event.spontaneous():
            return

        wants_to_close = gui_funcs.create_yes_no_question("Are you sure you want to exit?","Exit Confirmation")

        if not wants_to_close:
            event.ignore()
            return
        
        event.accept()  


        