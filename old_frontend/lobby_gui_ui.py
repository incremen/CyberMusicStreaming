# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lobby_gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 788)
        self.main_widget = QWidget(MainWindow)
        self.main_widget.setObjectName(u"main_widget")
        self.list_widget = QListWidget(self.main_widget)
        self.list_widget.setObjectName(u"list_widget")
        self.list_widget.setGeometry(QRect(170, 140, 441, 551))
        font = QFont()
        font.setPointSize(40)
        self.list_widget.setFont(font)
        self.list_widget.setStyleSheet(u"background-color: white;\n"
"QListWidget::item {\n"
"    text-align: center;\n"
"background-color: white;\n"
"}\n"
"")
        self.list_widget.setTextElideMode(Qt.ElideLeft)
        self.join_btn = QPushButton(self.main_widget)
        self.join_btn.setObjectName(u"join_btn")
        self.join_btn.setGeometry(QRect(40, 30, 121, 81))
        font1 = QFont()
        font1.setFamily(u"Voltage")
        font1.setPointSize(40)
        self.join_btn.setFont(font1)
        self.join_btn.setAutoFillBackground(False)
        self.join_btn.setStyleSheet(u"background-color: white;\n"
"")
        self.leave_btn = QPushButton(self.main_widget)
        self.leave_btn.setObjectName(u"leave_btn")
        self.leave_btn.setGeometry(QRect(600, 30, 141, 81))
        self.leave_btn.setFont(font1)
        self.leave_btn.setStyleSheet(u"background-color: white;\n"
"")
        self.label = QLabel(self.main_widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 10, 311, 71))
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: white;")
        self.label.setAlignment(Qt.AlignCenter)
        self.username_label = QLabel(self.main_widget)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(230, 70, 311, 51))
        font2 = QFont()
        font2.setFamily(u"Sitka Display")
        font2.setPointSize(30)
        self.username_label.setFont(font2)
        self.username_label.setStyleSheet(u"background-color: white;")
        self.username_label.setAlignment(Qt.AlignCenter)
        self.game_end_msg = QLabel(self.main_widget)
        self.game_end_msg.setObjectName(u"game_end_msg")
        self.game_end_msg.setGeometry(QRect(190, 720, 391, 31))
        font3 = QFont()
        font3.setPointSize(20)
        self.game_end_msg.setFont(font3)
        self.game_end_msg.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.main_widget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.join_btn.setText(QCoreApplication.translate("MainWindow", u"Join", None))
        self.leave_btn.setText(QCoreApplication.translate("MainWindow", u"leave", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"You are:", None))
        self.username_label.setText(QCoreApplication.translate("MainWindow", u"Not in lobby", None))
        self.game_end_msg.setText("")
    # retranslateUi

