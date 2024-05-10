# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\user_profile\user_profile.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 922)
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setStyleSheet("#central_widget {\n"
" background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"           stop:0 #4B0082, stop:0.5 #000000, stop:1 #4B0082);\n"
"}\n"
"QGroupBox {border: none;}")
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.albums_boxlayout = QtWidgets.QGroupBox(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.albums_boxlayout.sizePolicy().hasHeightForWidth())
        self.albums_boxlayout.setSizePolicy(sizePolicy)
        self.albums_boxlayout.setMinimumSize(QtCore.QSize(0, 100))
        self.albums_boxlayout.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.albums_boxlayout.setStyleSheet("#groupBox {border: none;\n"
"}")
        self.albums_boxlayout.setTitle("")
        self.albums_boxlayout.setFlat(True)
        self.albums_boxlayout.setObjectName("albums_boxlayout")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.albums_boxlayout)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.album_grid = QtWidgets.QGridLayout()
        self.album_grid.setObjectName("album_grid")
        self.groupBox_6 = QtWidgets.QGroupBox(self.albums_boxlayout)
        self.groupBox_6.setMinimumSize(QtCore.QSize(0, 250))
        self.groupBox_6.setStyleSheet("QGroupBox{ \n"
"border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.playlist_btn_4 = QtWidgets.QPushButton(self.groupBox_6)
        self.playlist_btn_4.setStyleSheet("font-size: 30px;\n"
"color:white;\n"
"background-color: transparent;")
        self.playlist_btn_4.setObjectName("playlist_btn_4")
        self.verticalLayout_9.addWidget(self.playlist_btn_4)
        self.play_btn_4 = QtWidgets.QPushButton(self.groupBox_6)
        self.play_btn_4.setMinimumSize(QtCore.QSize(0, 0))
        self.play_btn_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.play_btn_4.setStyleSheet("background-color:transparent;\n"
"qproperty-iconSize: 80px;\n"
" border-radius: 30px;\n"
"\n"
"\n"
"\n"
"")
        self.play_btn_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/white_play_button_transparent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_btn_4.setIcon(icon)
        self.play_btn_4.setObjectName("play_btn_4")
        self.verticalLayout_9.addWidget(self.play_btn_4)
        self.album_grid.addWidget(self.groupBox_6, 0, 3, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.albums_boxlayout)
        self.groupBox_7.setStyleSheet("QGroupBox{ \n"
"border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.playlist_btn_3 = QtWidgets.QPushButton(self.groupBox_7)
        self.playlist_btn_3.setStyleSheet("font-size: 30px;\n"
"color:white;\n"
"background-color: transparent;")
        self.playlist_btn_3.setObjectName("playlist_btn_3")
        self.verticalLayout_8.addWidget(self.playlist_btn_3)
        self.play_btn_3 = QtWidgets.QPushButton(self.groupBox_7)
        self.play_btn_3.setMinimumSize(QtCore.QSize(0, 0))
        self.play_btn_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.play_btn_3.setStyleSheet("background-color:transparent;\n"
"qproperty-iconSize: 80px;\n"
" border-radius: 30px;\n"
"\n"
"\n"
"\n"
"")
        self.play_btn_3.setText("")
        self.play_btn_3.setIcon(icon)
        self.play_btn_3.setObjectName("play_btn_3")
        self.verticalLayout_8.addWidget(self.play_btn_3)
        self.album_grid.addWidget(self.groupBox_7, 0, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.albums_boxlayout)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 250))
        self.groupBox.setStyleSheet("QGroupBox{ \n"
"border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.playlist_btn_8 = QtWidgets.QPushButton(self.groupBox)
        self.playlist_btn_8.setMinimumSize(QtCore.QSize(0, 0))
        self.playlist_btn_8.setStyleSheet("font-size: 30px;\n"
"color:white;\n"
"background-color: transparent;")
        self.playlist_btn_8.setObjectName("playlist_btn_8")
        self.verticalLayout_2.addWidget(self.playlist_btn_8)
        self.play_btn_8 = QtWidgets.QPushButton(self.groupBox)
        self.play_btn_8.setMinimumSize(QtCore.QSize(0, 90))
        self.play_btn_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.play_btn_8.setStyleSheet("background-color:transparent;\n"
"qproperty-iconSize: 80px;\n"
" border-radius: 30px;\n"
"\n"
"\n"
"\n"
"")
        self.play_btn_8.setText("")
        self.play_btn_8.setIcon(icon)
        self.play_btn_8.setObjectName("play_btn_8")
        self.verticalLayout_2.addWidget(self.play_btn_8)
        self.album_grid.addWidget(self.groupBox, 1, 3, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.albums_boxlayout)
        self.groupBox_4.setStyleSheet("QGroupBox{ \n"
"border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.playlist_btn_6 = QtWidgets.QPushButton(self.groupBox_4)
        self.playlist_btn_6.setStyleSheet("font-size: 30px;\n"
"color:white;\n"
"background-color: transparent;")
        self.playlist_btn_6.setObjectName("playlist_btn_6")
        self.verticalLayout_4.addWidget(self.playlist_btn_6)
        self.play_btn_6 = QtWidgets.QPushButton(self.groupBox_4)
        self.play_btn_6.setMinimumSize(QtCore.QSize(0, 90))
        self.play_btn_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.play_btn_6.setStyleSheet("background-color:transparent;\n"
"qproperty-iconSize: 80px;\n"
" border-radius: 30px;\n"
"\n"
"\n"
"\n"
"")
        self.play_btn_6.setText("")
        self.play_btn_6.setIcon(icon)
        self.play_btn_6.setObjectName("play_btn_6")
        self.verticalLayout_4.addWidget(self.play_btn_6)
        self.album_grid.addWidget(self.groupBox_4, 1, 1, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(self.albums_boxlayout)
        self.groupBox_8.setStyleSheet("QGroupBox{ \n"
"border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.playlist_btn_2 = QtWidgets.QPushButton(self.groupBox_8)
        self.playlist_btn_2.setStyleSheet("font-size: 30px;\n"
"color:white;\n"
"background-color: transparent;")
        self.playlist_btn_2.setObjectName("playlist_btn_2")
        self.verticalLayout_7.addWidget(self.playlist_btn_2)
        self.play_btn_2 = QtWidgets.QPushButton(self.groupBox_8)
        self.play_btn_2.setMinimumSize(QtCore.QSize(0, 90))
        self.play_btn_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.play_btn_2.setStyleSheet("background-color:transparent;\n"
"qproperty-iconSize: 80px;\n"
" border-radius: 30px;\n"
"\n"
"\n"
"\n"
"")
        self.play_btn_2.setText("")
        self.play_btn_2.setIcon(icon)
        self.play_btn_2.setObjectName("play_btn_2")
        self.verticalLayout_7.addWidget(self.play_btn_2)
        self.album_grid.addWidget(self.groupBox_8, 0, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.albums_boxlayout)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox_2.setStyleSheet("QGroupBox{ \n"
"border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.playlist_btn_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.playlist_btn_7.setStyleSheet("font-size: 30px;\n"
"color:white;\n"
"background-color: transparent;")
        self.playlist_btn_7.setObjectName("playlist_btn_7")
        self.verticalLayout_5.addWidget(self.playlist_btn_7)
        self.play_btn_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.play_btn_7.setMinimumSize(QtCore.QSize(0, 90))
        self.play_btn_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.play_btn_7.setStyleSheet("background-color:transparent;\n"
"qproperty-iconSize: 80px;\n"
" border-radius: 30px;\n"
"\n"
"\n"
"\n"
"")
        self.play_btn_7.setText("")
        self.play_btn_7.setIcon(icon)
        self.play_btn_7.setObjectName("play_btn_7")
        self.verticalLayout_5.addWidget(self.play_btn_7)
        self.album_grid.addWidget(self.groupBox_2, 1, 2, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.albums_boxlayout)
        self.groupBox_5.setStyleSheet("QGroupBox{ \n"
"border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.playlist_btn_5 = QtWidgets.QPushButton(self.groupBox_5)
        self.playlist_btn_5.setStyleSheet("font-size: 30px;\n"
"color:white;\n"
"background-color: transparent;")
        self.playlist_btn_5.setObjectName("playlist_btn_5")
        self.verticalLayout_3.addWidget(self.playlist_btn_5)
        self.play_btn_5 = QtWidgets.QPushButton(self.groupBox_5)
        self.play_btn_5.setMinimumSize(QtCore.QSize(0, 90))
        self.play_btn_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.play_btn_5.setStyleSheet("background-color:transparent;\n"
"qproperty-iconSize: 80px;\n"
" border-radius: 30px;\n"
"\n"
"\n"
"\n"
"")
        self.play_btn_5.setText("")
        self.play_btn_5.setIcon(icon)
        self.play_btn_5.setObjectName("play_btn_5")
        self.verticalLayout_3.addWidget(self.play_btn_5)
        self.album_grid.addWidget(self.groupBox_5, 1, 0, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.albums_boxlayout)
        self.groupBox_9.setStyleSheet("QGroupBox{ \n"
"border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.playlist_btn_1 = QtWidgets.QPushButton(self.groupBox_9)
        self.playlist_btn_1.setStyleSheet("font-size: 30px;\n"
"color:white;\n"
"background-color: transparent;")
        self.playlist_btn_1.setObjectName("playlist_btn_1")
        self.verticalLayout_6.addWidget(self.playlist_btn_1)
        self.play_btn_1 = QtWidgets.QPushButton(self.groupBox_9)
        self.play_btn_1.setMinimumSize(QtCore.QSize(0, 90))
        self.play_btn_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.play_btn_1.setStyleSheet("background-color:transparent;\n"
"qproperty-iconSize: 80px;\n"
" border-radius: 30px;\n"
"\n"
"\n"
"\n"
"")
        self.play_btn_1.setText("")
        self.play_btn_1.setIcon(icon)
        self.play_btn_1.setObjectName("play_btn_1")
        self.verticalLayout_6.addWidget(self.play_btn_1)
        self.album_grid.addWidget(self.groupBox_9, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.album_grid, 6, 0, 1, 1)
        self.sign_out_btn_box = QtWidgets.QGroupBox(self.albums_boxlayout)
        self.sign_out_btn_box.setMinimumSize(QtCore.QSize(0, 80))
        self.sign_out_btn_box.setStyleSheet("#groupBox {border: none;\n"
"}")
        self.sign_out_btn_box.setObjectName("sign_out_btn_box")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.sign_out_btn_box)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.sign_out_btn_box)
        self.label.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
" background-color: rgba(255, 255, 255, 150); \n"
" color: black;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gridLayout_2.addWidget(self.sign_out_btn_box, 2, 0, 1, 1)
        self.albums_box_layout = QtWidgets.QHBoxLayout()
        self.albums_box_layout.setObjectName("albums_box_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.albums_box_layout.addItem(spacerItem)
        self.sign_out_btn = QtWidgets.QPushButton(self.albums_boxlayout)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sign_out_btn.setFont(font)
        self.sign_out_btn.setStyleSheet(" border: 2px solid red;\n"
" background-color: rgba(128, 128, 128, 128);\n"
"color: white;\n"
"border-radius:12px;\n"
"\n"
"")
        self.sign_out_btn.setObjectName("sign_out_btn")
        self.albums_box_layout.addWidget(self.sign_out_btn)
        self.home_btn = QtWidgets.QPushButton(self.albums_boxlayout)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.home_btn.setFont(font)
        self.home_btn.setStyleSheet(" border: 2px solid lime;\n"
" background-color: rgba(128, 128, 128, 128);\n"
"color: white;\n"
"border-radius:12px;\n"
"\n"
"")
        self.home_btn.setObjectName("home_btn")
        self.albums_box_layout.addWidget(self.home_btn)
        self.gridLayout_2.addLayout(self.albums_box_layout, 0, 0, 1, 1)
        self.top_btns_box = QtWidgets.QGroupBox(self.albums_boxlayout)
        self.top_btns_box.setMinimumSize(QtCore.QSize(0, 100))
        self.top_btns_box.setStyleSheet("QGroupBox {border: none;}")
        self.top_btns_box.setTitle("")
        self.top_btns_box.setFlat(True)
        self.top_btns_box.setObjectName("top_btns_box")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.top_btns_box)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.top_btns_box)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.user_info_label = QtWidgets.QLabel(self.groupBox_3)
        self.user_info_label.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.user_info_label.setFont(font)
        self.user_info_label.setStyleSheet(" border: 2px solid gold; \n"
"border-radius: 30px;\n"
"color: white;")
        self.user_info_label.setObjectName("user_info_label")
        self.verticalLayout.addWidget(self.user_info_label)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.gridLayout_2.addWidget(self.top_btns_box, 4, 0, 1, 1)
        self.horizontalLayout_6.addWidget(self.albums_boxlayout)
        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1123, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.playlist_btn_4.setText(_translate("MainWindow", "4"))
        self.playlist_btn_3.setText(_translate("MainWindow", "3"))
        self.playlist_btn_8.setText(_translate("MainWindow", "8"))
        self.playlist_btn_6.setText(_translate("MainWindow", "6"))
        self.playlist_btn_2.setText(_translate("MainWindow", "2"))
        self.playlist_btn_7.setText(_translate("MainWindow", "7"))
        self.playlist_btn_5.setText(_translate("MainWindow", "5"))
        self.playlist_btn_1.setText(_translate("MainWindow", "1"))
        self.sign_out_btn_box.setTitle(_translate("MainWindow", "GroupBox"))
        self.label.setText(_translate("MainWindow", "Your playlists:"))
        self.sign_out_btn.setText(_translate("MainWindow", " Sign out "))
        self.home_btn.setText(_translate("MainWindow", " Home "))
        self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))
        self.user_info_label.setText(_translate("MainWindow", "username: idk \n"
" password: idk"))
import resource_file_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())