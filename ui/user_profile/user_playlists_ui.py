# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_playlists.ui'
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
        self.albums_boxlayout.setMinimumSize(QSize(0, 100))
        self.albums_boxlayout.setMaximumSize(QSize(16777215, 1000))
        self.albums_boxlayout.setStyleSheet(u"#groupBox {border: none;\n"
"}")
        self.albums_boxlayout.setFlat(True)
        self.gridLayout_2 = QGridLayout(self.albums_boxlayout)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.sign_out_btn_box = QGroupBox(self.albums_boxlayout)
        self.sign_out_btn_box.setObjectName(u"sign_out_btn_box")
        self.sign_out_btn_box.setMinimumSize(QSize(0, 80))
        self.sign_out_btn_box.setStyleSheet(u"#groupBox {border: none;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.sign_out_btn_box)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.sign_out_btn = QPushButton(self.sign_out_btn_box)
        self.sign_out_btn.setObjectName(u"sign_out_btn")
        font = QFont()
        font.setPointSize(18)
        self.sign_out_btn.setFont(font)
        self.sign_out_btn.setStyleSheet(u" border: 2px solid gold;\n"
" background-color: rgba(128, 128, 128, 128);\n"
"color: white;\n"
"border-radius:12px;\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.sign_out_btn)

        self.home_btn = QPushButton(self.sign_out_btn_box)
        self.home_btn.setObjectName(u"home_btn")
        font1 = QFont()
        font1.setPointSize(20)
        self.home_btn.setFont(font1)
        self.home_btn.setStyleSheet(u" border: 2px solid gold;\n"
" background-color: rgba(128, 128, 128, 128);\n"
"color: white;\n"
"border-radius:12px;\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.home_btn)


        self.gridLayout_2.addWidget(self.sign_out_btn_box, 1, 0, 1, 1)

        self.album_grid = QGridLayout()
        self.album_grid.setObjectName(u"album_grid")
        self.btn_4 = QPushButton(self.albums_boxlayout)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy1)
        self.btn_4.setMaximumSize(QSize(200, 16777215))
        font2 = QFont()
        font2.setPointSize(40)
        self.btn_4.setFont(font2)
        self.btn_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_4.setStyleSheet(u" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.btn_4, 0, 3, 1, 1)

        self.btn_1 = QPushButton(self.albums_boxlayout)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy2)
        self.btn_1.setMaximumSize(QSize(200, 16777215))
        font3 = QFont()
        font3.setPointSize(30)
        self.btn_1.setFont(font3)
        self.btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_1.setStyleSheet(u" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.btn_1, 0, 0, 1, 1)

        self.btn_3 = QPushButton(self.albums_boxlayout)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy1.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy1)
        self.btn_3.setMaximumSize(QSize(200, 16777215))
        self.btn_3.setFont(font2)
        self.btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_3.setStyleSheet(u" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.btn_3, 0, 2, 1, 1)

        self.btn_5 = QPushButton(self.albums_boxlayout)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy3)
        self.btn_5.setMaximumSize(QSize(200, 16777215))
        self.btn_5.setFont(font2)
        self.btn_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_5.setStyleSheet(u" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.btn_5, 1, 0, 1, 1)

        self.btn_2 = QPushButton(self.albums_boxlayout)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy1.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy1)
        self.btn_2.setMaximumSize(QSize(200, 16777215))
        font4 = QFont()
        font4.setPointSize(40)
        font4.setBold(False)
        font4.setUnderline(False)
        font4.setWeight(50)
        font4.setKerning(True)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.btn_2.setFont(font4)
        self.btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_2.setStyleSheet(u" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.btn_2.setFlat(False)

        self.album_grid.addWidget(self.btn_2, 0, 1, 1, 1)

        self.btn_6 = QPushButton(self.albums_boxlayout)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy1.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy1)
        self.btn_6.setMaximumSize(QSize(200, 16777215))
        self.btn_6.setFont(font2)
        self.btn_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_6.setStyleSheet(u" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.btn_6, 1, 1, 1, 1)

        self.btn_7 = QPushButton(self.albums_boxlayout)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy1.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy1)
        self.btn_7.setMaximumSize(QSize(200, 16777215))
        self.btn_7.setFont(font2)
        self.btn_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_7.setStyleSheet(u" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.album_grid.addWidget(self.btn_7, 1, 2, 1, 1)

        self.groupBox = QGroupBox(self.albums_boxlayout)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QGroupBox{ \n"
"border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"font-size: 30px;\n"
"color:white;\n"
"background-color: transparent;")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 90))
        self.pushButton_2.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_2.setStyleSheet(u"background-color:transparent;\n"
"qproperty-iconSize: 80px;\n"
" border-radius: 30px;\n"
"\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/images/white_play_button_transparent.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.album_grid.addWidget(self.groupBox, 1, 3, 1, 1)


        self.gridLayout_2.addLayout(self.album_grid, 5, 0, 1, 1)

        self.top_btns_box = QGroupBox(self.albums_boxlayout)
        self.top_btns_box.setObjectName(u"top_btns_box")
        self.top_btns_box.setMinimumSize(QSize(0, 100))
        self.top_btns_box.setStyleSheet(u"QGroupBox {border: none;}")
        self.top_btns_box.setFlat(True)
        self.horizontalLayout_3 = QHBoxLayout(self.top_btns_box)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit = QLineEdit(self.top_btns_box)
        self.lineEdit.setObjectName(u"lineEdit")
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(40)
        self.lineEdit.setFont(font5)
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


        self.gridLayout_2.addWidget(self.top_btns_box, 3, 0, 1, 1)

        self.user_info_label = QLabel(self.albums_boxlayout)
        self.user_info_label.setObjectName(u"user_info_label")
        self.user_info_label.setMinimumSize(QSize(0, 100))
        font6 = QFont()
        font6.setPointSize(22)
        self.user_info_label.setFont(font6)
        self.user_info_label.setStyleSheet(u" border: 2px solid white; \n"
"border-radius: 30px;\n"
"color: white;")

        self.gridLayout_2.addWidget(self.user_info_label, 4, 0, 1, 1)

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
        self.sign_out_btn_box.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.sign_out_btn.setText(QCoreApplication.translate("MainWindow", u"Sign out", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_4.setText("")
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"Dummy 1", None))
        self.btn_3.setText("")
        self.btn_5.setText("")
        self.btn_2.setText("")
        self.btn_6.setText("")
        self.btn_7.setText("")
        self.groupBox.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Playlist name", None))
        self.pushButton_2.setText("")
        self.top_btns_box.setTitle("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Your own playlists:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.user_info_label.setText(QCoreApplication.translate("MainWindow", u"username: idk \n"
" password: idk", None))
    # retranslateUi

