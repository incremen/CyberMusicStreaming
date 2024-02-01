# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_page.ui'
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
        MainWindow.resize(1123, 922)
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setStyleSheet(u"#central_widget {\n"
" background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"           stop:0 #4B0082, stop:0.5 #000000, stop:1 #4B0082);\n"
"}\n"
"QGroupBox {border: none;}")
        self.horizontalLayout_6 = QHBoxLayout(self.central_widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.albums_boxlayout = QGroupBox(self.central_widget)
        self.albums_boxlayout.setObjectName(u"albums_boxlayout")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.albums_boxlayout.sizePolicy().hasHeightForWidth())
        self.albums_boxlayout.setSizePolicy(sizePolicy)
        self.albums_boxlayout.setMaximumSize(QSize(16777215, 1000))
        self.albums_boxlayout.setStyleSheet(u"#groupBox {border: none;\n"
"}")
        self.albums_boxlayout.setFlat(True)
        self.gridLayout_2 = QGridLayout(self.albums_boxlayout)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.album_grid = QGridLayout()
        self.album_grid.setObjectName(u"album_grid")
        self.pushButton_7 = QPushButton(self.albums_boxlayout)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy1)
        self.pushButton_7.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setPointSize(40)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.pushButton_7, 0, 3, 1, 1)

        self.pushButton = QPushButton(self.albums_boxlayout)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setPointSize(30)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.albums_boxlayout)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)
        self.pushButton_6.setMaximumSize(QSize(200, 16777215))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.pushButton_6, 0, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.albums_boxlayout)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy3)
        self.pushButton_9.setMaximumSize(QSize(200, 16777215))
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.pushButton_9, 1, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.albums_boxlayout)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setMaximumSize(QSize(200, 16777215))
        font2 = QFont()
        font2.setPointSize(40)
        font2.setBold(False)
        font2.setUnderline(False)
        font2.setWeight(50)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.pushButton_4.setFlat(False)

        self.album_grid.addWidget(self.pushButton_4, 0, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.albums_boxlayout)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy1.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy1)
        self.pushButton_13.setMaximumSize(QSize(200, 16777215))
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet(u" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.pushButton_13, 1, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.albums_boxlayout)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy1.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy1)
        self.pushButton_14.setMaximumSize(QSize(200, 16777215))
        self.pushButton_14.setFont(font)
        self.pushButton_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet(u" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.pushButton_14, 1, 2, 1, 1)

        self.pushButton_12 = QPushButton(self.albums_boxlayout)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy1.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy1)
        self.pushButton_12.setMaximumSize(QSize(200, 16777215))
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet(u" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.pushButton_12, 1, 3, 1, 1)


        self.gridLayout_2.addLayout(self.album_grid, 3, 0, 1, 1)

        self.top_btns_box = QGroupBox(self.albums_boxlayout)
        self.top_btns_box.setObjectName(u"top_btns_box")
        self.top_btns_box.setMinimumSize(QSize(0, 100))
        self.top_btns_box.setStyleSheet(u"QGroupBox {border: none;}")
        self.top_btns_box.setFlat(True)
        self.horizontalLayout_3 = QHBoxLayout(self.top_btns_box)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit = QLineEdit(self.top_btns_box)
        self.lineEdit.setObjectName(u"lineEdit")
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(40)
        self.lineEdit.setFont(font3)
        self.lineEdit.setCursor(QCursor(Qt.CrossCursor))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
" background-color: rgba(255, 255, 255, 150); \n"
" color: black;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.groupBox_3 = QGroupBox(self.top_btns_box)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalLayout_3.addWidget(self.groupBox_3)


        self.gridLayout_2.addWidget(self.top_btns_box, 2, 0, 1, 1)

        self.albums_box_layout = QHBoxLayout()
        self.albums_box_layout.setObjectName(u"albums_box_layout")

        self.gridLayout_2.addLayout(self.albums_box_layout, 0, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.albums_boxlayout)

        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1123, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.albums_boxlayout.setTitle("")
        self.pushButton_7.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Dummy 1", None))
        self.pushButton_6.setText("")
        self.pushButton_9.setText("")
        self.pushButton_4.setText("")
        self.pushButton_13.setText("")
        self.pushButton_14.setText("")
        self.pushButton_12.setText("")
        self.top_btns_box.setTitle("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Your own playlists:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
    # retranslateUi

