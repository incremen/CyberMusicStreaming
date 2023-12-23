# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_file.ui'
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
        MainWindow.resize(1230, 871)
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setStyleSheet(u"#central_widget {\n"
" background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"            stop:0 #4B0082, stop:1 #000000);\n"
"}\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.central_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.big_box = QGroupBox(self.central_widget)
        self.big_box.setObjectName(u"big_box")
        self.big_box.setStyleSheet(u"QGroupBox{\n"
"   border: none;\n"
"}\n"
"")
        self.big_box.setFlat(True)
        self.horizontalLayout = QHBoxLayout(self.big_box)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_box = QGroupBox(self.big_box)
        self.left_box.setObjectName(u"left_box")
        self.left_box.setFlat(True)
        self.gridLayout = QGridLayout(self.left_box)
        self.gridLayout.setObjectName(u"gridLayout")
        self.song_grid = QGridLayout()
        self.song_grid.setObjectName(u"song_grid")
        self.label_2 = QLabel(self.left_box)
        self.label_2.setObjectName(u"label_2")

        self.song_grid.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(self.left_box)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setStyleSheet(u" border: 2px solid pink;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 50px;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.label.setLineWidth(3)
        self.label.setAlignment(Qt.AlignCenter)

        self.song_grid.addWidget(self.label, 0, 0, 1, 3)

        self.label_4 = QLabel(self.left_box)
        self.label_4.setObjectName(u"label_4")

        self.song_grid.addWidget(self.label_4, 2, 2, 1, 1)

        self.label_3 = QLabel(self.left_box)
        self.label_3.setObjectName(u"label_3")

        self.song_grid.addWidget(self.label_3, 2, 1, 1, 1)

        self.label_5 = QLabel(self.left_box)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMaximumSize(QSize(16777215, 80))
        font1 = QFont()
        font1.setPointSize(15)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u" border: 2px solid gold;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.song_grid.addWidget(self.label_5, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.song_grid, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)

        self.horizontalLayout.addWidget(self.left_box)

        self.right_box = QGroupBox(self.big_box)
        self.right_box.setObjectName(u"right_box")
        self.right_box.setFlat(True)
        self.verticalLayout = QVBoxLayout(self.right_box)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.songs_played_widget = QListWidget(self.right_box)
        self.songs_played_widget.setObjectName(u"songs_played_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.songs_played_widget.sizePolicy().hasHeightForWidth())
        self.songs_played_widget.setSizePolicy(sizePolicy2)
        self.songs_played_widget.setStyleSheet(u" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 50px;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.songs_played_widget.setFrameShape(QFrame.StyledPanel)
        self.songs_played_widget.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.songs_played_widget)

        self.song_queue_widget = QListWidget(self.right_box)
        __qlistwidgetitem = QListWidgetItem(self.song_queue_widget)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        self.song_queue_widget.setObjectName(u"song_queue_widget")
        sizePolicy2.setHeightForWidth(self.song_queue_widget.sizePolicy().hasHeightForWidth())
        self.song_queue_widget.setSizePolicy(sizePolicy2)
        self.song_queue_widget.setStyleSheet(u" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 50px;\n"
"color: white;\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout.addWidget(self.song_queue_widget)

        self.pause_btn = QPushButton(self.right_box)
        self.pause_btn.setObjectName(u"pause_btn")
        self.pause_btn.setStyleSheet(u"qproperty-iconSize: 80px;\n"
" border: none;\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/images/white_pause_btn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pause_btn.setIcon(icon)

        self.verticalLayout.addWidget(self.pause_btn)

        self.song_btns_box = QGroupBox(self.right_box)
        self.song_btns_box.setObjectName(u"song_btns_box")
        self.song_btns_box.setMinimumSize(QSize(0, 100))
        self.song_btns_box.setFlat(True)
        self.horizontalLayout_3 = QHBoxLayout(self.song_btns_box)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.back_btn = QPushButton(self.song_btns_box)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setStyleSheet(u"qproperty-iconSize: 80px;\n"
" border: none;\n"
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/images/white_play_button_left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_btn.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.back_btn)

        self.progress_slider = QScrollBar(self.song_btns_box)
        self.progress_slider.setObjectName(u"progress_slider")
        self.progress_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.progress_slider)

        self.skip_btn = QPushButton(self.song_btns_box)
        self.skip_btn.setObjectName(u"skip_btn")
        self.skip_btn.setStyleSheet(u"qproperty-iconSize: 80px;\n"
" border: none;\n"
"\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/images/white_play_button_right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.skip_btn.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.skip_btn)


        self.verticalLayout.addWidget(self.song_btns_box)


        self.horizontalLayout.addWidget(self.right_box)


        self.horizontalLayout_2.addWidget(self.big_box)

        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1230, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.big_box.setTitle("")
        self.left_box.setTitle("")
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Demo Album", None))
        self.label_4.setText("")
        self.label_3.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Find more albums!", None))
        self.right_box.setTitle("")

        __sortingEnabled = self.song_queue_widget.isSortingEnabled()
        self.song_queue_widget.setSortingEnabled(False)
        ___qlistwidgetitem = self.song_queue_widget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"dummy item", None));
        self.song_queue_widget.setSortingEnabled(__sortingEnabled)

        self.pause_btn.setText("")
        self.song_btns_box.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.back_btn.setText("")
        self.skip_btn.setText("")
    # retranslateUi

