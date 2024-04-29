# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_playlist.ui'
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
        MainWindow.resize(1181, 927)
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setStyleSheet(u"#central_widget {\n"
" background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"            stop:0 #4B0082, stop:1 #000000);\n"
"}\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.central_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.vertical_box = QGroupBox(self.central_widget)
        self.vertical_box.setObjectName(u"vertical_box")
        self.vertical_box.setStyleSheet(u"QGroupBox{\n"
"   border: none;\n"
"}\n"
"")
        self.vertical_box.setFlat(True)
        self.verticalLayout_3 = QVBoxLayout(self.vertical_box)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(self.vertical_box)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 30))
        self.groupBox_2.setFlat(True)
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.profile_btn = QPushButton(self.groupBox_2)
        self.profile_btn.setObjectName(u"profile_btn")
        self.profile_btn.setMinimumSize(QSize(80, 30))
        font = QFont()
        font.setPointSize(12)
        self.profile_btn.setFont(font)
        self.profile_btn.setStyleSheet(u" border: 2px solid gold;\n"
" background-color: rgba(128, 128, 128, 128);\n"
"color: white;\n"
"border-radius:10px;\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.profile_btn)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.big_box = QGroupBox(self.vertical_box)
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
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.name_edit_box = QGroupBox(self.left_box)
        self.name_edit_box.setObjectName(u"name_edit_box")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_edit_box.sizePolicy().hasHeightForWidth())
        self.name_edit_box.setSizePolicy(sizePolicy)
        self.name_edit_box.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_5 = QHBoxLayout(self.name_edit_box)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.playlist_name_edit = QLineEdit(self.name_edit_box)
        self.playlist_name_edit.setObjectName(u"playlist_name_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.playlist_name_edit.sizePolicy().hasHeightForWidth())
        self.playlist_name_edit.setSizePolicy(sizePolicy1)
        self.playlist_name_edit.setMinimumSize(QSize(0, 100))
        self.playlist_name_edit.setMaximumSize(QSize(16777215, 100))
        font1 = QFont()
        font1.setPointSize(40)
        self.playlist_name_edit.setFont(font1)
        self.playlist_name_edit.setStyleSheet(u" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 50px;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.playlist_name_edit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.playlist_name_edit)


        self.gridLayout.addWidget(self.name_edit_box, 0, 0, 1, 1)

        self.song_grid = QGridLayout()
        self.song_grid.setObjectName(u"song_grid")
        self.label_2 = QLabel(self.left_box)
        self.label_2.setObjectName(u"label_2")

        self.song_grid.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_3 = QLabel(self.left_box)
        self.label_3.setObjectName(u"label_3")

        self.song_grid.addWidget(self.label_3, 3, 1, 1, 1)

        self.label_4 = QLabel(self.left_box)
        self.label_4.setObjectName(u"label_4")

        self.song_grid.addWidget(self.label_4, 3, 2, 1, 1)

        self.search_btn = QPushButton(self.left_box)
        self.search_btn.setObjectName(u"search_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy2)
        self.search_btn.setMaximumSize(QSize(16777215, 60))
        font2 = QFont()
        font2.setPointSize(13)
        self.search_btn.setFont(font2)
        self.search_btn.setStyleSheet(u" border: 2px solid gold;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.song_grid.addWidget(self.search_btn, 0, 0, 1, 1)

        self.search_bar = QLineEdit(self.left_box)
        self.search_bar.setObjectName(u"search_bar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.search_bar.sizePolicy().hasHeightForWidth())
        self.search_bar.setSizePolicy(sizePolicy3)
        self.search_bar.setMinimumSize(QSize(0, 70))
        self.search_bar.setStyleSheet(u" border: 2px solid gold;\n"
" background-color: rgba(128, 128, 128, 128);\n"
"color: white;\n"
"\n"
"\n"
"")

        self.song_grid.addWidget(self.search_bar, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.song_grid, 1, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)

        self.horizontalLayout.addWidget(self.left_box)

        self.right_tab_widget = QTabWidget(self.big_box)
        self.right_tab_widget.setObjectName(u"right_tab_widget")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.right_tab_widget.sizePolicy().hasHeightForWidth())
        self.right_tab_widget.setSizePolicy(sizePolicy4)
        self.right_tab_widget.setStyleSheet(u"background: transparent;")
        self.right_tab_widget.setDocumentMode(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"background: transparent;")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.play_list_widget = QListWidget(self.tab)
        self.play_list_widget.setObjectName(u"play_list_widget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.play_list_widget.sizePolicy().hasHeightForWidth())
        self.play_list_widget.setSizePolicy(sizePolicy5)
        self.play_list_widget.setStyleSheet(u" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 50px;\n"
"color: white;\n"
"\n"
"\n"
"")
        self.play_list_widget.setFrameShape(QFrame.StyledPanel)
        self.play_list_widget.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.play_list_widget)

        self.playlist_btns_box_1 = QGroupBox(self.tab)
        self.playlist_btns_box_1.setObjectName(u"playlist_btns_box_1")
        self.playlist_btns_box_1.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_4 = QHBoxLayout(self.playlist_btns_box_1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.play_btn = QPushButton(self.playlist_btns_box_1)
        self.play_btn.setObjectName(u"play_btn")
        sizePolicy2.setHeightForWidth(self.play_btn.sizePolicy().hasHeightForWidth())
        self.play_btn.setSizePolicy(sizePolicy2)
        self.play_btn.setMaximumSize(QSize(120, 60))
        self.play_btn.setFont(font2)
        self.play_btn.setStyleSheet(u" border: 2px solid #ADD8E6;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 30px;\n"
"color: white;\n"
"  \n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.play_btn)

        self.save_playlist_btn = QPushButton(self.playlist_btns_box_1)
        self.save_playlist_btn.setObjectName(u"save_playlist_btn")
        sizePolicy2.setHeightForWidth(self.save_playlist_btn.sizePolicy().hasHeightForWidth())
        self.save_playlist_btn.setSizePolicy(sizePolicy2)
        self.save_playlist_btn.setMaximumSize(QSize(300, 60))
        self.save_playlist_btn.setFont(font2)
        self.save_playlist_btn.setStyleSheet(u" border: 2px solid lime;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 30px;\n"
"color: white;\n"
"\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.save_playlist_btn)

        self.delete_btn = QPushButton(self.playlist_btns_box_1)
        self.delete_btn.setObjectName(u"delete_btn")
        sizePolicy2.setHeightForWidth(self.delete_btn.sizePolicy().hasHeightForWidth())
        self.delete_btn.setSizePolicy(sizePolicy2)
        self.delete_btn.setMaximumSize(QSize(100, 60))
        self.delete_btn.setFont(font2)
        self.delete_btn.setStyleSheet(u" border: 2px solid red;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 30px;\n"
"color: white;\n"
"  \n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.delete_btn)


        self.verticalLayout_2.addWidget(self.playlist_btns_box_1)

        self.playlist_btns_box_2 = QGroupBox(self.tab)
        self.playlist_btns_box_2.setObjectName(u"playlist_btns_box_2")
        self.playlist_btns_box_2.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_7 = QHBoxLayout(self.playlist_btns_box_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        self.verticalLayout_2.addWidget(self.playlist_btns_box_2)

        self.right_tab_widget.addTab(self.tab, "")
        self.song_queue = QWidget()
        self.song_queue.setObjectName(u"song_queue")
        self.verticalLayout = QVBoxLayout(self.song_queue)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.songs_played_widget = QListWidget(self.song_queue)
        self.songs_played_widget.setObjectName(u"songs_played_widget")
        sizePolicy5.setHeightForWidth(self.songs_played_widget.sizePolicy().hasHeightForWidth())
        self.songs_played_widget.setSizePolicy(sizePolicy5)
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

        self.song_queue_widget = QListWidget(self.song_queue)
        self.song_queue_widget.setObjectName(u"song_queue_widget")
        sizePolicy5.setHeightForWidth(self.song_queue_widget.sizePolicy().hasHeightForWidth())
        self.song_queue_widget.setSizePolicy(sizePolicy5)
        self.song_queue_widget.setStyleSheet(u" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
" border-radius: 50px;\n"
"color: white;\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout.addWidget(self.song_queue_widget)

        self.right_tab_widget.addTab(self.song_queue, "")

        self.horizontalLayout.addWidget(self.right_tab_widget)


        self.verticalLayout_3.addWidget(self.big_box)

        self.controller_box = QGroupBox(self.vertical_box)
        self.controller_box.setObjectName(u"controller_box")
        self.controller_box.setMinimumSize(QSize(0, 100))
        self.controller_box.setStyleSheet(u"#controller_box\n"
"{\n"
"border: none;\n"
"}")
        self.controller_box.setFlat(True)
        self.verticalLayout_4 = QVBoxLayout(self.controller_box)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pause_btn = QPushButton(self.controller_box)
        self.pause_btn.setObjectName(u"pause_btn")
        self.pause_btn.setStyleSheet(u"qproperty-iconSize: 80px;\n"
" border: none;\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/images/white_pause_btn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pause_btn.setIcon(icon)

        self.verticalLayout_4.addWidget(self.pause_btn)

        self.song_btns_box = QGroupBox(self.controller_box)
        self.song_btns_box.setObjectName(u"song_btns_box")
        self.song_btns_box.setMinimumSize(QSize(0, 100))
        self.song_btns_box.setStyleSheet(u"#song_btns_box{\n"
"border: none;}")
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
        self.back_btn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.back_btn)

        self.progress_slider = QScrollBar(self.song_btns_box)
        self.progress_slider.setObjectName(u"progress_slider")
        self.progress_slider.setMinimumSize(QSize(0, 50))
        self.progress_slider.setStyleSheet(u"QScrollBar {\n"
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


        self.verticalLayout_4.addWidget(self.song_btns_box)


        self.verticalLayout_3.addWidget(self.controller_box)


        self.horizontalLayout_2.addWidget(self.vertical_box)

        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1181, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.right_tab_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.vertical_box.setTitle("")
        self.groupBox_2.setTitle("")
        self.profile_btn.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.big_box.setTitle("")
        self.left_box.setTitle("")
        self.name_edit_box.setTitle("")
        self.playlist_name_edit.setText(QCoreApplication.translate("MainWindow", u"Playlist Name", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"Search for a song:", None))
        self.playlist_btns_box_1.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.play_btn.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.save_playlist_btn.setText(QCoreApplication.translate("MainWindow", u"Save playlist", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.playlist_btns_box_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.right_tab_widget.setTabText(self.right_tab_widget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Playlist", None))
        self.right_tab_widget.setTabText(self.right_tab_widget.indexOf(self.song_queue), QCoreApplication.translate("MainWindow", u"Queue", None))
        self.controller_box.setTitle("")
        self.pause_btn.setText("")
        self.song_btns_box.setTitle("")
        self.back_btn.setText("")
        self.skip_btn.setText("")
    # retranslateUi

