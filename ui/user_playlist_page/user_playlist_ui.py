# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\user_playlist_page\user_playlist.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1181, 933)
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setStyleSheet("#central_widget {\n"
" background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"            stop:0 #4B0082, stop:1 #000000);\n"
"}\n"
"")
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.vertical_box = QtWidgets.QGroupBox(self.central_widget)
        self.vertical_box.setTitle("")
        self.vertical_box.setObjectName("vertical_box")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.vertical_box)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.big_box = QtWidgets.QGroupBox(self.vertical_box)
        self.big_box.setStyleSheet("QGroupBox{\n"
"   border: none;\n"
"}\n"
"")
        self.big_box.setTitle("")
        self.big_box.setFlat(True)
        self.big_box.setObjectName("big_box")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.big_box)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_box = QtWidgets.QGroupBox(self.big_box)
        self.left_box.setTitle("")
        self.left_box.setFlat(True)
        self.left_box.setObjectName("left_box")
        self.gridLayout = QtWidgets.QGridLayout(self.left_box)
        self.gridLayout.setObjectName("gridLayout")
        self.song_grid = QtWidgets.QGridLayout()
        self.song_grid.setObjectName("song_grid")
        self.label_3 = QtWidgets.QLabel(self.left_box)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.song_grid.addWidget(self.label_3, 4, 1, 1, 1)
        self.search_btn = QtWidgets.QPushButton(self.left_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy)
        self.search_btn.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.search_btn.setFont(font)
        self.search_btn.setStyleSheet(" border: 2px solid gold;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.search_btn.setObjectName("search_btn")
        self.song_grid.addWidget(self.search_btn, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.left_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setStyleSheet(" border: 2px solid pink;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 50px;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.label.setLineWidth(3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.song_grid.addWidget(self.label, 0, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.left_box)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.song_grid.addWidget(self.label_4, 4, 2, 1, 1)
        self.search_bar = QtWidgets.QLineEdit(self.left_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_bar.sizePolicy().hasHeightForWidth())
        self.search_bar.setSizePolicy(sizePolicy)
        self.search_bar.setMinimumSize(QtCore.QSize(0, 70))
        self.search_bar.setStyleSheet(" border: 2px solid gold;\n"
" background-color: rgba(128, 128, 128, 128);\n"
"color: white;\n"
"\n"
"\n"
"")
        self.search_bar.setObjectName("search_bar")
        self.song_grid.addWidget(self.search_bar, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.left_box)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.song_grid.addWidget(self.label_2, 3, 0, 1, 1)
        self.gridLayout.addLayout(self.song_grid, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.horizontalLayout.addWidget(self.left_box)
        self.right_tab = QtWidgets.QTabWidget(self.big_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_tab.sizePolicy().hasHeightForWidth())
        self.right_tab.setSizePolicy(sizePolicy)
        self.right_tab.setStyleSheet("background: transparent;")
        self.right_tab.setDocumentMode(True)
        self.right_tab.setObjectName("right_tab")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("background: transparent;")
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.play_list_widget = QtWidgets.QListWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play_list_widget.sizePolicy().hasHeightForWidth())
        self.play_list_widget.setSizePolicy(sizePolicy)
        self.play_list_widget.setStyleSheet(" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 50px;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.play_list_widget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.play_list_widget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.play_list_widget.setObjectName("play_list_widget")
        self.verticalLayout_2.addWidget(self.play_list_widget)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.save_playlist_btn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_playlist_btn.sizePolicy().hasHeightForWidth())
        self.save_playlist_btn.setSizePolicy(sizePolicy)
        self.save_playlist_btn.setMaximumSize(QtCore.QSize(300, 60))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.save_playlist_btn.setFont(font)
        self.save_playlist_btn.setStyleSheet(" border: 2px solid gold;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.save_playlist_btn.setObjectName("search_btn_2")
        self.horizontalLayout_4.addWidget(self.save_playlist_btn)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.right_tab.addTab(self.tab, "")
        self.song_queue = QtWidgets.QWidget()
        self.song_queue.setObjectName("song_queue")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.song_queue)
        self.verticalLayout.setObjectName("verticalLayout")
        self.songs_played_widget = QtWidgets.QListWidget(self.song_queue)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songs_played_widget.sizePolicy().hasHeightForWidth())
        self.songs_played_widget.setSizePolicy(sizePolicy)
        self.songs_played_widget.setStyleSheet(" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 50px;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.songs_played_widget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.songs_played_widget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.songs_played_widget.setObjectName("songs_played_widget")
        self.verticalLayout.addWidget(self.songs_played_widget)
        self.song_queue_widget = QtWidgets.QListWidget(self.song_queue)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.song_queue_widget.sizePolicy().hasHeightForWidth())
        self.song_queue_widget.setSizePolicy(sizePolicy)
        self.song_queue_widget.setStyleSheet(" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 50px;\n"
"color: white;\n"
"\n"
"\n"
"\n"
"")
        self.song_queue_widget.setObjectName("song_queue_widget")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.song_queue_widget.addItem(item)
        self.verticalLayout.addWidget(self.song_queue_widget)
        self.right_tab.addTab(self.song_queue, "")
        self.horizontalLayout.addWidget(self.right_tab)
        self.verticalLayout_3.addWidget(self.big_box)
        self.controller_box = QtWidgets.QGroupBox(self.vertical_box)
        self.controller_box.setMinimumSize(QtCore.QSize(0, 100))
        self.controller_box.setStyleSheet("#controller_box\n"
"{\n"
"border: none;\n"
"}")
        self.controller_box.setFlat(True)
        self.controller_box.setObjectName("controller_box")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.controller_box)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pause_btn = QtWidgets.QPushButton(self.controller_box)
        self.pause_btn.setStyleSheet("qproperty-iconSize: 80px;\n"
" border: none;\n"
"\n"
"\n"
"")
        self.pause_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/white_pause_btn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_btn.setIcon(icon)
        self.pause_btn.setObjectName("pause_btn")
        self.verticalLayout_4.addWidget(self.pause_btn)
        self.song_btns_box = QtWidgets.QGroupBox(self.controller_box)
        self.song_btns_box.setMinimumSize(QtCore.QSize(0, 100))
        self.song_btns_box.setStyleSheet("#song_btns_box{\n"
"border: none;}")
        self.song_btns_box.setFlat(True)
        self.song_btns_box.setObjectName("song_btns_box")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.song_btns_box)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.back_btn = QtWidgets.QPushButton(self.song_btns_box)
        self.back_btn.setStyleSheet("qproperty-iconSize: 80px;\n"
" border: none;\n"
"\n"
"\n"
"")
        self.back_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/white_play_button_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon1)
        self.back_btn.setFlat(True)
        self.back_btn.setObjectName("back_btn")
        self.horizontalLayout_3.addWidget(self.back_btn)
        self.progress_slider = QtWidgets.QScrollBar(self.song_btns_box)
        self.progress_slider.setMinimumSize(QtCore.QSize(0, 50))
        self.progress_slider.setStyleSheet("QScrollBar {\n"
"background-color:   rgba(128, 128, 128, 60);\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
" background-color:  rgba(255, 105, 180, 100);\n"
" min-width: 20px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.progress_slider.setOrientation(QtCore.Qt.Horizontal)
        self.progress_slider.setObjectName("progress_slider")
        self.horizontalLayout_3.addWidget(self.progress_slider)
        self.skip_btn = QtWidgets.QPushButton(self.song_btns_box)
        self.skip_btn.setStyleSheet("qproperty-iconSize: 80px;\n"
" border: none;\n"
"\n"
"\n"
"")
        self.skip_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/white_play_button_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.skip_btn.setIcon(icon2)
        self.skip_btn.setObjectName("skip_btn")
        self.horizontalLayout_3.addWidget(self.skip_btn)
        self.verticalLayout_4.addWidget(self.song_btns_box)
        self.verticalLayout_3.addWidget(self.controller_box)
        self.horizontalLayout_2.addWidget(self.vertical_box)
        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1181, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.right_tab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_btn.setText(_translate("MainWindow", "Search for a song:"))
        self.label.setText(_translate("MainWindow", "Demo Album"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.save_playlist_btn.setText(_translate("MainWindow", "Save playlist"))
        self.right_tab.setTabText(self.right_tab.indexOf(self.tab), _translate("MainWindow", "Page"))
        __sortingEnabled = self.song_queue_widget.isSortingEnabled()
        self.song_queue_widget.setSortingEnabled(False)
        item = self.song_queue_widget.item(0)
        item.setText(_translate("MainWindow", "dummy item"))
        self.song_queue_widget.setSortingEnabled(__sortingEnabled)
        self.controller_box.setTitle(_translate("MainWindow", "GroupBox"))
        self.song_btns_box.setTitle(_translate("MainWindow", "GroupBox"))
import resource_file_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
