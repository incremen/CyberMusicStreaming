# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'albums_page.ui'
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
        MainWindow.resize(1086, 922)
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setStyleSheet(u"#central_widget {\n"
" background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"            stop:0 #4B0082, stop:1 #000000);\n"
"}\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(self.central_widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox = QGroupBox(self.central_widget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QSize(16777215, 1000))
        self.groupBox.setStyleSheet(u"#groupBox {border: none;\n"
"}")
        self.groupBox.setFlat(True)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(60)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
" border: 2px solid gold;\n"
" background-color: rgba(255, 255, 0, 80); \n"
" border-radius: 30px;\n"
" color: gold;\n"
" font-family: Arial;\n"
" padding: 30px;\n"
" box-shadow: 0px 0px 10px gold;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
" outline: 2px solid gold;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.album_grid = QGridLayout()
        self.album_grid.setObjectName(u"album_grid")
        self.pushButton_7 = QPushButton(self.groupBox)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy1)
        self.pushButton_7.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setPointSize(40)
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setStyleSheet(u" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.pushButton_7, 0, 3, 1, 1)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setMaximumSize(QSize(200, 16777215))
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.groupBox)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)
        self.pushButton_6.setMaximumSize(QSize(200, 16777215))
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setStyleSheet(u" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.pushButton_6, 0, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.groupBox)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy1.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy1)
        self.pushButton_9.setMaximumSize(QSize(200, 16777215))
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setStyleSheet(u" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.pushButton_9, 1, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setMaximumSize(QSize(200, 16777215))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.pushButton_4, 0, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.groupBox)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy1.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy1)
        self.pushButton_13.setMaximumSize(QSize(200, 16777215))
        self.pushButton_13.setFont(font1)
        self.pushButton_13.setStyleSheet(u" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.pushButton_13, 1, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.groupBox)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy1.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy1)
        self.pushButton_14.setMaximumSize(QSize(200, 16777215))
        self.pushButton_14.setFont(font1)
        self.pushButton_14.setStyleSheet(u" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.pushButton_14, 1, 2, 1, 1)

        self.pushButton_12 = QPushButton(self.groupBox)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy1.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy1)
        self.pushButton_12.setMaximumSize(QSize(200, 16777215))
        self.pushButton_12.setFont(font1)
        self.pushButton_12.setStyleSheet(u" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.pushButton_12, 1, 3, 1, 1)


        self.gridLayout_2.addLayout(self.album_grid, 2, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1086, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Find a song...", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Summer \n"
"\n"
"\n"
"hits", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Popular \n"
"\n"
"\n"
"albums", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Summer \n"
"\n"
"\n"
"albums", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"asdf \n"
"\n"
"\n"
"asdf", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Top \n"
"\n"
"\n"
"hits", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"asdf \n"
"\n"
"\n"
"asdf", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"asdf \n"
"\n"
"\n"
"asdf", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"asdf \n"
"\n"
"\n"
"asdf", None))
    # retranslateUi

