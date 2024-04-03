# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\user_playlists\user_playlists.ui'
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
        self.sign_out_btn_box = QtWidgets.QGroupBox(self.albums_boxlayout)
        self.sign_out_btn_box.setMinimumSize(QtCore.QSize(0, 80))
        self.sign_out_btn_box.setStyleSheet("#groupBox {border: none;\n"
"}")
        self.sign_out_btn_box.setObjectName("sign_out_btn_box")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.sign_out_btn_box)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.sign_out_btn = QtWidgets.QPushButton(self.sign_out_btn_box)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sign_out_btn.setFont(font)
        self.sign_out_btn.setStyleSheet(" border: 2px solid pink;\n"
" border-radius: 5px;\n"
"color: black;\n"
"background-color: white;\n"
"\n"
"")
        self.sign_out_btn.setObjectName("sign_out_btn")
        self.horizontalLayout.addWidget(self.sign_out_btn)
        self.gridLayout_2.addWidget(self.sign_out_btn_box, 1, 0, 1, 1)
        self.album_grid = QtWidgets.QGridLayout()
        self.album_grid.setObjectName("album_grid")
        self.btn_4 = QtWidgets.QPushButton(self.albums_boxlayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.btn_4.setFont(font)
        self.btn_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_4.setStyleSheet(" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.btn_4.setText("")
        self.btn_4.setObjectName("btn_4")
        self.album_grid.addWidget(self.btn_4, 0, 3, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.albums_boxlayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.btn_1.setFont(font)
        self.btn_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1.setStyleSheet(" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.btn_1.setObjectName("btn_1")
        self.album_grid.addWidget(self.btn_1, 0, 0, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.albums_boxlayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.btn_3.setFont(font)
        self.btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_3.setStyleSheet(" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.btn_3.setText("")
        self.btn_3.setObjectName("btn_3")
        self.album_grid.addWidget(self.btn_3, 0, 2, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.albums_boxlayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.btn_5.setFont(font)
        self.btn_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_5.setStyleSheet(" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.btn_5.setText("")
        self.btn_5.setObjectName("btn_5")
        self.album_grid.addWidget(self.btn_5, 1, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.albums_boxlayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_2.setFont(font)
        self.btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2.setStyleSheet(" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.btn_2.setText("")
        self.btn_2.setFlat(False)
        self.btn_2.setObjectName("btn_2")
        self.album_grid.addWidget(self.btn_2, 0, 1, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.albums_boxlayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.btn_6.setFont(font)
        self.btn_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_6.setStyleSheet(" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.btn_6.setText("")
        self.btn_6.setObjectName("btn_6")
        self.album_grid.addWidget(self.btn_6, 1, 1, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.albums_boxlayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.btn_7.setFont(font)
        self.btn_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_7.setStyleSheet(" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.btn_7.setText("")
        self.btn_7.setObjectName("btn_7")
        self.album_grid.addWidget(self.btn_7, 1, 2, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.albums_boxlayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.btn_8.setFont(font)
        self.btn_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_8.setStyleSheet(" border: 2px solid white;\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.btn_8.setText("")
        self.btn_8.setObjectName("btn_8")
        self.album_grid.addWidget(self.btn_8, 1, 3, 1, 1)
        self.gridLayout_2.addLayout(self.album_grid, 5, 0, 1, 1)
        self.top_btns_box = QtWidgets.QGroupBox(self.albums_boxlayout)
        self.top_btns_box.setMinimumSize(QtCore.QSize(0, 100))
        self.top_btns_box.setStyleSheet("QGroupBox {border: none;}")
        self.top_btns_box.setTitle("")
        self.top_btns_box.setFlat(True)
        self.top_btns_box.setObjectName("top_btns_box")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.top_btns_box)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.top_btns_box)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
" background-color: rgba(255, 255, 255, 150); \n"
" color: black;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.groupBox_3 = QtWidgets.QGroupBox(self.top_btns_box)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.gridLayout_2.addWidget(self.top_btns_box, 3, 0, 1, 1)
        self.user_info_label = QtWidgets.QLabel(self.albums_boxlayout)
        self.user_info_label.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.user_info_label.setFont(font)
        self.user_info_label.setStyleSheet(" border: 2px solid white; \n"
"border-radius: 30px;\n"
"color: white;")
        self.user_info_label.setObjectName("user_info_label")
        self.gridLayout_2.addWidget(self.user_info_label, 4, 0, 1, 1)
        self.albums_box_layout = QtWidgets.QHBoxLayout()
        self.albums_box_layout.setObjectName("albums_box_layout")
        self.gridLayout_2.addLayout(self.albums_box_layout, 0, 0, 1, 1)
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
        self.sign_out_btn_box.setTitle(_translate("MainWindow", "GroupBox"))
        self.sign_out_btn.setText(_translate("MainWindow", "Sign out"))
        self.btn_1.setText(_translate("MainWindow", "Dummy 1"))
        self.lineEdit.setText(_translate("MainWindow", "Your own playlists:"))
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