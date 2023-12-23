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
        MainWindow.resize(1266, 871)
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
        self.horizontalLayout = QHBoxLayout(self.big_box)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(self.big_box)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.song_grid = QGridLayout()
        self.song_grid.setObjectName(u"song_grid")

        self.gridLayout.addLayout(self.song_grid, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white;\n"
"		")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.right_box = QGroupBox(self.big_box)
        self.right_box.setObjectName(u"right_box")
        self.verticalLayout = QVBoxLayout(self.right_box)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.songs_played_widget = QListWidget(self.right_box)
        self.songs_played_widget.setObjectName(u"songs_played_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songs_played_widget.sizePolicy().hasHeightForWidth())
        self.songs_played_widget.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.song_queue_widget.sizePolicy().hasHeightForWidth())
        self.song_queue_widget.setSizePolicy(sizePolicy)
        self.song_queue_widget.setStyleSheet(u" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 50px;\n"
"color: white;\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout.addWidget(self.song_queue_widget)

        self.pushButton = QPushButton(self.right_box)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"qproperty-iconSize: 80px;\n"
" border: none;\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/images/white_pause_btn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.verticalLayout.addWidget(self.pushButton)

        self.groupBox = QGroupBox(self.right_box)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"qproperty-iconSize: 80px;\n"
" border: none;\n"
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/images/white_play_button_left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.horizontalScrollBar = QScrollBar(self.groupBox)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.horizontalScrollBar)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"qproperty-iconSize: 80px;\n"
" border: none;\n"
"\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/images/white_play_button_right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.pushButton_3)


        self.verticalLayout.addWidget(self.groupBox)


        self.horizontalLayout.addWidget(self.right_box)


        self.horizontalLayout_2.addWidget(self.big_box)

        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1266, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.big_box.setTitle(QCoreApplication.translate("MainWindow", u"big box", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"left box", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"dummy song 2", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"dummy song 1", None))
        self.right_box.setTitle(QCoreApplication.translate("MainWindow", u"right box", None))

        __sortingEnabled = self.song_queue_widget.isSortingEnabled()
        self.song_queue_widget.setSortingEnabled(False)
        ___qlistwidgetitem = self.song_queue_widget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"dummy item", None));
        self.song_queue_widget.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
    # retranslateUi

