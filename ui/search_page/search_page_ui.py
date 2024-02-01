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
        MainWindow.resize(1120, 922)
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setStyleSheet(u"#central_widget {\n"
" background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"           stop:0 #4B0082, stop:0.5 #000000, stop:1 #4B0082);\n"
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
        font = QFont()
        font.setPointSize(40)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u" border: 2px solid white;\n"
" background-image: url(:/album_pics/img_4.png);\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.pushButton_7, 0, 3, 1, 1)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setMaximumSize(QSize(200, 16777215))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u" border: 2px solid white;\n"
" background-image: url(:/album_pics/img_1.png);\n"
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
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u" border: 2px solid white;\n"
" background-image: url(:/album_pics/img_3.png);\n"
" border-radius: 30px;\n"
"color: white;\n"
"text-shadow: 2px 2px 2px black;	\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.pushButton_6, 0, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.groupBox)
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
" background-image: url(:/album_pics/img_5.png);\n"
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
        font1 = QFont()
        font1.setPointSize(40)
        font1.setBold(False)
        font1.setUnderline(False)
        font1.setWeight(50)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u" border: 2px solid white;\n"
" background-image: url(:/album_pics/img_2.png);\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.pushButton_4.setFlat(False)

        self.album_grid.addWidget(self.pushButton_4, 0, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.groupBox)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy1.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy1)
        self.pushButton_13.setMaximumSize(QSize(200, 16777215))
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet(u" border: 2px solid white;\n"
" background-image: url(:/album_pics/img_6.png);\n"
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
        self.pushButton_14.setFont(font)
        self.pushButton_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet(u" border: 2px solid white;\n"
" background-image: url(:/album_pics/img_7.png);\n"
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
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet(u" border: 2px solid white;\n"
" background-image: url(:/album_pics/img_8.png);\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.pushButton_12, 1, 3, 1, 1)


        self.gridLayout_2.addLayout(self.album_grid, 3, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(40)
        self.lineEdit.setFont(font2)
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

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font3 = QFont()
        font3.setPointSize(20)
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
" background-color: rgba(255, 255, 255, 150); \n"
" color: black;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.groupBox_3)


        self.gridLayout_2.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1120, 21))
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
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"    Made for Itamar. ", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"See your own playlists", None))
    # retranslateUi

