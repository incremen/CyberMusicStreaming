from PyQt5.QtWidgets import QMessageBox
import logging

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

                
    