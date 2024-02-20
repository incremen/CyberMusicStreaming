from ui import gui_funcs
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QListWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QDragEnterEvent, QDragMoveEvent, QDropEvent
from PyQt5.QtCore import QMimeData, Qt
from PyQt5.QtGui import QDragEnterEvent


"""Setting up dragging is pretty complicated. Use only the first few functions, rest are here for utility."""



def make_list_widget_accept_drops(widget : QWidget):
    """
    Sets the given widget to accept drops and assigns event handlers for drag enter, drop, and drag move events.

    """
    widget.setAcceptDrops(True)
    widget.dragEnterEvent = lambda event: drag_enter_event_to_accept_drops(widget, event)
    widget.dropEvent = lambda event: list_widget_accept_drop_event(widget, event)
    widget.dragMoveEvent = lambda event: drag_enter_event_to_accept_drops(widget, event)


def make_widget_draggable(widget : QWidget):
    """
    Create a draggable widget by connecting mouse press and mouse move events to the corresponding event handlers.
    
    :param widget: QWidget - the widget to make draggable
    """
    widget.mousePressEvent = lambda event, btn=widget: draggable_mouse_press_event(btn, event)
    widget.mouseMoveEvent = lambda event, btn=widget: draggable_mouse_move_event(btn, event)
    
    
def make_widget_not_draggable(widget : QWidget):
    """
    Disable the dragging functionality of the given QWidget by setting its mousePressEvent and mouseMoveEvent attributes to None.
    
    Args:
        widget (QWidget): The widget to make not draggable.
        
    Returns:
        None
    """
    widget.mousePressEvent = None
    widget.mouseMoveEvent = None


def draggable_mouse_press_event(widget : QWidget, event):
    """
    Handle mouse press event for the widget, and make it draggable.
    
    Args:
        widget: The widget where the mouse press event occurred.
        event: The mouse press event object.

    Returns:
        None
    """
    if event.button() == Qt.MouseButton.LeftButton:
        widget.drag_start_position = event.pos()


def draggable_mouse_move_event(widget, event):
    """
    Handle the mouse move event for the given widget, and make it draggable.

    Args:
        widget: The widget where the mouse move event occurred.
        event: The mouse move event object.

    Returns:
        None
    """
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


def drag_enter_event_to_accept_drops(widget, event : QDragEnterEvent):
    """
    Handle the widgets dragenterevent, and make it accept drops.
    """
    if event.mimeData().hasText():
        event.acceptProposedAction()


def list_widget_accept_drop_event(list_widget : QListWidget, event):
    """
    A function to handle the drop event for a list widget.
    
    Drop event uses gui_funcs.add_item_to_list_widget to add the widget.
    """
    pos = event.pos()
    text = event.mimeData().text()
    gui_funcs.add_item_to_list_widget(list_widget, text)
    event.acceptProposedAction()
    
    


