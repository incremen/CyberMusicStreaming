from PyQt5.QtWidgets import QMessageBox
def create_message_box(text, title):
    msg_box = QMessageBox()
    msg_box.setText(text)
    msg_box.setWindowTitle(title)
    msg_box.exec_()
    
def create_yes_no_question(text, title):
        btn_clicked = QMessageBox.question(None, title, text ,QMessageBox.Yes | QMessageBox.No)
        return btn_clicked == QMessageBox.Yes 
    