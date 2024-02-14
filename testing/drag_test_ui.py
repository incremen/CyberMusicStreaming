# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drag_test.ui'
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
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drag_widget = QLabel(self.centralwidget)
        self.drag_widget.setObjectName(u"drag_widget")
        self.drag_widget.setGeometry(QRect(150, 130, 47, 13))
        self.drop_widget = QLabel(self.centralwidget)
        self.drop_widget.setObjectName(u"drop_widget")
        self.drop_widget.setGeometry(QRect(510, 300, 81, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.drag_widget.setText(QCoreApplication.translate("MainWindow", u"drag me", None))
        self.drop_widget.setText(QCoreApplication.translate("MainWindow", u"drop_widget", None))
    # retranslateUi

