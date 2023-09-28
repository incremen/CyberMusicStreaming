from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget, QGridLayout
from PyQt5 import uic, QtGui
import logging

class MainPage(QMainWindow):
    def __init__(self):
        super(MainPage, self).__init__()
        uic.loadUi(r"frontend\main_page.ui", self)
        self.setWindowTitle(f"Stream music!")
        self.main_widget = self.findChild(QWidget, "main_widget")
        self.setup_main_widget_properties()
        
        self.show()
        self.last_row = 0
        self.last_col = -1
        
    def song_list_received(self, songs : list):
        logging.debug(f"Received song list: {songs}")
        for song in songs:
            self.add_song_to_grid(song["name"])
    
    def setup_main_widget_properties(self):
        main_widget = self.main_widget
        self.song_grid = main_widget.findChild(QGridLayout, "song_grid")
        
    def add_song_to_grid(self, text):
        song_label = QLabel(text)
        self.last_col += 1
        if self.last_col == 3:
            self.last_col = 0
            self.last_row += 1
        logging.debug(f"About to add {text} to grid at {self.last_row=}, {self.last_col=}")
        self.song_grid.addWidget(song_label, self.last_row, self.last_col)

        
    



        