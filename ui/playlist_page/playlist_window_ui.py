# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'playlist_window.ui'
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

        self.search_btn = QPushButton(self.left_box)
        self.search_btn.setObjectName(u"search_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy1)
        self.search_btn.setMaximumSize(QSize(16777215, 60))
        font1 = QFont()
        font1.setPointSize(13)
        self.search_btn.setFont(font1)
        self.search_btn.setStyleSheet(u" border: 2px solid gold;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.song_grid.addWidget(self.search_btn, 1, 0, 1, 1)


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
        self.song_queue_widget = QListWidget(self.right_box)
        self.song_queue_widget.setObjectName(u"song_queue_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
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
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"Find more!", None))
        self.right_box.setTitle("")
    # retranslateUi

