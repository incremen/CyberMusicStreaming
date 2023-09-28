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
        
        self.current_row = 0
        self.current_col = 0
        
        self.show()
        
    def song_list_received(self, songs : list):
        logging.debug(f"Received song list: {songs}")
        for song in songs:
            self.add_song_to_grid(song["name"])
    
    def setup_main_widget_properties(self):
        main_widget = self.main_widget
        self.song_grid = main_widget.findChild(QGridLayout, "song_grid")
        
    def add_song_to_grid(self, text):
        song_label = QLabel(text)
        self.song_grid.addWidget(song_label, self.current_row, self.current_col)
        
        self.current_col += 1
        if self.current_col >= 3:
            self.current_col = 0
            self.current_row += 1
    
    # def closeEvent(self, event):
    #     if not event.spontaneous():
    #         return

    #     wants_to_close = gui_funcs.create_yes_no_question("Are you sure you want to exit?","Exit Confirmation")

    #     if not wants_to_close:
    #         event.ignore()
    #         return
        
    #     event.accept()  


        