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

import resource_file_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1130, 936)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(Qt.RightToLeft)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(132, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setMinimumSize(QSize(1100, 0))
        self.main_widget.setLayoutDirection(Qt.RightToLeft)
        self.main_widget.setStyleSheet(u" background-image: url(:images/dark_background.png);\n"
"")
        self.gridLayoutWidget = QWidget(self.main_widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(70, 10, 621, 591))
        self.song_grid = QGridLayout(self.gridLayoutWidget)
        self.song_grid.setObjectName(u"song_grid")
        self.song_grid.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget = QWidget(self.main_widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(740, 10, 331, 741))
        self.song_queue_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.song_queue_layout.setSpacing(12)
        self.song_queue_layout.setObjectName(u"song_queue_layout")
        self.song_queue_layout.setContentsMargins(0, 0, 0, 0)
        self.songs_played_widget = QListWidget(self.verticalLayoutWidget)
        self.songs_played_widget.setObjectName(u"songs_played_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.songs_played_widget.sizePolicy().hasHeightForWidth())
        self.songs_played_widget.setSizePolicy(sizePolicy1)
        self.songs_played_widget.setStyleSheet(u"border-image: url(:/images/light_background.png) 0 0 0 0 stretch stretch;")
        self.songs_played_widget.setFrameShape(QFrame.StyledPanel)
        self.songs_played_widget.setFrameShadow(QFrame.Sunken)

        self.song_queue_layout.addWidget(self.songs_played_widget)

        self.song_queue_widget = QListWidget(self.verticalLayoutWidget)
        self.song_queue_widget.setObjectName(u"song_queue_widget")
        self.song_queue_widget.setStyleSheet(u"border-image: url(:/images/light_background.png) 0 0 0 0 stretch stretch;")

        self.song_queue_layout.addWidget(self.song_queue_widget)

        self.gridLayoutWidget_2 = QWidget(self.main_widget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(140, 660, 421, 184))
        self.song_btns_layout = QGridLayout(self.gridLayoutWidget_2)
        self.song_btns_layout.setObjectName(u"song_btns_layout")
        self.song_btns_layout.setContentsMargins(0, 0, 0, 0)
        self.back_btn = QPushButton(self.gridLayoutWidget_2)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setStyleSheet(u"qproperty-iconSize: 80px;\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/images/white_play_button_left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setFlat(False)

        self.song_btns_layout.addWidget(self.back_btn, 1, 2, 1, 1)

        self.skip_btn = QPushButton(self.gridLayoutWidget_2)
        self.skip_btn.setObjectName(u"skip_btn")
        self.skip_btn.setStyleSheet(u"qproperty-iconSize: 80px;\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/images/white_play_button_right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.skip_btn.setIcon(icon1)
        self.skip_btn.setFlat(False)

        self.song_btns_layout.addWidget(self.skip_btn, 1, 0, 1, 1)

        self.pause_btn = QPushButton(self.gridLayoutWidget_2)
        self.pause_btn.setObjectName(u"pause_btn")
        self.pause_btn.setStyleSheet(u"qproperty-iconSize: 80px;\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/images/white_pause_btn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pause_btn.setIcon(icon2)
        self.pause_btn.setFlat(False)

        self.song_btns_layout.addWidget(self.pause_btn, 0, 1, 1, 1)

        self.song_progress_layout = QHBoxLayout()
        self.song_progress_layout.setObjectName(u"song_progress_layout")
        self.progress_slider = QSlider(self.gridLayoutWidget_2)
        self.progress_slider.setObjectName(u"progress_slider")
        self.progress_slider.setLayoutDirection(Qt.LeftToRight)
        self.progress_slider.setOrientation(Qt.Horizontal)

        self.song_progress_layout.addWidget(self.progress_slider)


        self.song_btns_layout.addLayout(self.song_progress_layout, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.main_widget)

        self.horizontalSpacer = QSpacerItem(132, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1130, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.back_btn.setText("")
        self.skip_btn.setText("")
        self.pause_btn.setText("")
    # retranslateUi

