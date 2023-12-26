import sys
import logging
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor
from PyQt5.QtCore import QMimeData, Qt

def mouse_press_event(widget, event):
    if event.button() == Qt.MouseButton.LeftButton:
        widget.drag_start_position = event.pos()


def mouse_move_event(widget, event):
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


def drop_event(list_widget, event):
    pos = event.pos()
    text = event.mimeData().text()
    item = QListWidgetItem(item_text)
    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
    gui_funcs.set_custom_font(item, "Helvetica", 15)
    song_list_widget.addItem(item)
    list_widget.addItem(text)
    event.acceptProposedAction()


