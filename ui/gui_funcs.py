from PyQt5.QtWidgets import QMessageBox
import logging
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QListWidgetItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt



def add_item_to_list_widget(list_widget, text, unique = True):
    if unique:
        existing_items = list_widget.findItems(text, Qt.MatchExactly)
        if existing_items:
            return

    item = QListWidgetItem(text)
    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
    set_custom_font(item, "Helvetica", 15)
    item.text = lambda : text

    list_widget.addItem(item)
    

def set_custom_font(widget : QWidget, font_family, font_size):
    font = QFont(font_family, font_size)
    widget.setFont(font)



def create_message_box(text, title):
    msg_box = QMessageBox()
    msg_box.setText(text)
    msg_box.setWindowTitle(title)
    msg_box.exec_()
    
    
def create_yes_no_question(text, title):
        btn_clicked = QMessageBox.question(None, title, text ,QMessageBox.Yes | QMessageBox.No)
        return btn_clicked == QMessageBox.Yes 
    
    
def get_name_to_item_from_gridlayout(grid_layout):
    name_to_item = {}
    for row in range(3):
        for column in range(3):
            item = grid_layout.itemAtPosition(row, column)
            if not item:
                continue

            if widget := item.widget():
                name = widget.objectName()
                name_to_item[name] = widget
                
            elif layout := item.layout():
                name = layout.objectName()
                name_to_item[name] = layout
    logging.debug(f"{name_to_item=}")

    return name_to_item



def get_objects_from_boxlayout(box_layout):
    objects = []
    for i in range(box_layout.count()):
        item = box_layout.itemAt(i)
        if not item:
            continue

        if widget := item.widget():
            objects.append(widget)
                
        elif layout := item.layout():
            objects.append(layout)
    logging.debug(f"{objects=}")

    return objects



def get_name_to_item_from_boxlayout(box_layout):
    name_to_item = {}
    for i in range(box_layout.count()):
        item = box_layout.itemAt(i)
        if not item:
            continue

        if widget := item.widget():
            name = widget.objectName()
            name_to_item[name] = widget
                
        elif layout := item.layout():
            name = layout.objectName()
            name_to_item[name] = layout
    logging.debug(f"{name_to_item=}")

    return name_to_item


def get_name_to_item_from_widget_children(widget):
    name_to_item = {}
    for child in widget.children():
        name = child.objectName()
        name_to_item[name] = child
    logging.debug(f"{name_to_item=}")

    return name_to_item


def get_name_to_item_recursive(item):
    if not item:
       return {}
    
    name_to_item = {}
    name_to_item[item.objectName()] = item
    
    
    if isinstance(item, QtWidgets.QWidget):
        new_name_to_item = get_name_to_item_from_widget_children(item)

    elif isinstance(item, QtWidgets.QBoxLayout):
        new_name_to_item = get_name_to_item_from_boxlayout(item)
        
    elif isinstance(item, QtWidgets.QGridLayout):
        new_name_to_item = get_name_to_item_from_gridlayout(item)

    name_to_item.update(new_name_to_item)
    for new_item in new_name_to_item.values():
        name_to_item.update(get_name_to_item_recursive(new_item))

    logging.info(f"{name_to_item=}")
    return name_to_item








                
    