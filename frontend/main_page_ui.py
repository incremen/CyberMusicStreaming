# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_page.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import font_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1180, 834)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(Qt.RightToLeft)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(132, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setMinimumSize(QSize(1100, 0))
        self.main_widget.setLayoutDirection(Qt.RightToLeft)
        self.gridLayoutWidget = QWidget(self.main_widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(70, 10, 621, 591))
        self.song_grid = QGridLayout(self.gridLayoutWidget)
        self.song_grid.setObjectName(u"song_grid")
        self.song_grid.setContentsMargins(0, 0, 0, 0)
        self.song_progress = QProgressBar(self.main_widget)
        self.song_progress.setObjectName(u"song_progress")
        self.song_progress.setGeometry(QRect(120, 680, 511, 23))
        self.song_progress.setValue(0)
        self.song_progress.setInvertedAppearance(True)
        self.skip_btn = QPushButton(self.main_widget)
        self.skip_btn.setObjectName(u"skip_btn")
        self.skip_btn.setGeometry(QRect(640, 670, 81, 61))
        self.skip_btn.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"qproperty-iconSize: 50px;\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"../../../Downloads2/play_button_right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.skip_btn.setIcon(icon)
        self.skip_btn.setFlat(True)
        self.song_queue = QListWidget(self.main_widget)
        self.song_queue.setObjectName(u"song_queue")
        self.song_queue.setGeometry(QRect(785, 20, 271, 721))
        self.back_btn = QPushButton(self.main_widget)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setGeometry(QRect(50, 660, 81, 61))
        self.back_btn.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"qproperty-iconSize: 50px;\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../../../Downloads2/play_button_left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_btn.setIcon(icon1)
        self.back_btn.setFlat(True)
        self.pause_btn = QPushButton(self.main_widget)
        self.pause_btn.setObjectName(u"pause_btn")
        self.pause_btn.setGeometry(QRect(360, 620, 81, 61))
        self.pause_btn.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"qproperty-iconSize: 50px;\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"../../../Downloads2/pause_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pause_btn.setIcon(icon2)
        self.pause_btn.setFlat(True)

        self.horizontalLayout.addWidget(self.main_widget)

        self.horizontalSpacer = QSpacerItem(132, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1180, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.skip_btn.setText("")
        self.back_btn.setText("")
        self.pause_btn.setText("")
    # retranslateUi

