from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt, QThread, pyqtSlot
from music_playing.song_class import SongInfo
from typing import TYPE_CHECKING
from custom_logging import log_calls
from ui.playlist_page.playlist_window_ui import Ui_MainWindow
from ui.album_page.album_window_config import PROGRESS_BAR_MAXIMUM
from functools import partial

from testing.working_dummy import *

from ui.window_interface import WindowInterface


if TYPE_CHECKING:
    from client.client_socket import ClientSocketHandler
    from music_playing.audio_handler import AudioHandler
    from client.shared_state import SharedState
    from client.window_manager import WindowManager


class PlaylistWindow(Ui_MainWindow, QMainWindow): 
    def __init__(self):
        super(PlaylistWindow, self).__init__()

        self.setupUi(self)
        self.setup_widgets()
        
    def mouse_press_event(self, widget, event):
        if event.button() == Qt.MouseButton.LeftButton:
            widget.drag_start_position = event.pos()
            
    def mouse_move_event(self, widget, event):
        if not (event.buttons() & Qt.MouseButton.LeftButton):
            return
        if (event.pos() - widget.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        drag = QDrag(widget)
        mimedata = QMimeData()
        mimedata.setText(widget.text())
        drag.setMimeData(mimedata)
        pixmap = QPixmap(widget.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(widget.rect(), widget.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.DropAction.CopyAction | Qt.DropAction.MoveAction)
        
    def drag_enter_event(widget, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()
        
    def setup_widgets(self):
        self.song_label.mousePressEvent = lambda event: self.mouse_press_event(self.song_label, event)
        self.song_label.mouseMoveEvent = lambda event: self.mouse_move_event(self.song_label, event)

        self.song_queue_widget.setAcceptDrops(True)
        self.song_queue_widget.dragEnterEvent = lambda event: drag_enter_event(self.song_queue_widget, event)
        self.song_queue_widget.dropEvent = lambda event: drop_event(self.song_queue_widget, event)
        self.song_queue_widget.dragMoveEvent = lambda event: drag_enter_event(self.song_queue_widget, event)
        
        
