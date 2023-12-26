import sys
import logging
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor
from PyQt5.QtCore import QMimeData, Qt


def mouse_press_event(self, event):
    if event.button() == Qt.MouseButton.LeftButton:
        self.drag_start_position = event.pos()


def mouseMoveEvent(self, event):
    if not (event.buttons() & Qt.MouseButton.LeftButton):
        return
    if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
        return
    drag = QDrag(self)
    mimedata = QMimeData()
    mimedata.setText(self.text())
    drag.setMimeData(mimedata)
    pixmap = QPixmap(self.size())
    painter = QPainter(pixmap)
    painter.drawPixmap(self.rect(), self.grab())
    painter.end()
    drag.setPixmap(pixmap)
    drag.setHotSpot(event.pos())
    drag.exec_(Qt.DropAction.CopyAction | Qt.DropAction.MoveAction)


def dragEnterEvent(self, event):
    if event.mimeData().hasText():
        event.acceptProposedAction()


def dropEvent(self, event):
    pos = event.pos()
    text = event.mimeData().text()
    self.setText(text)
    print(f'Dropped label with text: {text} at position: {pos}')
    event.acceptProposedAction()


