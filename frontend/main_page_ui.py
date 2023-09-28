# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_page.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import font_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(526, 766)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(Qt.RightToLeft)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(132, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setMinimumSize(QSize(485, 0))
        self.main_widget.setLayoutDirection(Qt.RightToLeft)
        self.player_msg = QLabel(self.main_widget)
        self.player_msg.setObjectName(u"player_msg")
        self.player_msg.setGeometry(QRect(-30, 530, 531, 161))
        font = QFont()
        font.setFamily(u"Voltage")
        font.setPointSize(70)
        self.player_msg.setFont(font)
        self.player_msg.setStyleSheet(u"")
        self.player_msg.setAlignment(Qt.AlignCenter)
        self.gridLayoutWidget = QWidget(self.main_widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 50, 441, 351))
        self.song_grid = QGridLayout(self.gridLayoutWidget)
        self.song_grid.setSpacing(0)
        self.song_grid.setObjectName(u"song_grid")
        self.song_grid.setSizeConstraint(QLayout.SetMinimumSize)
        self.song_grid.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.main_widget)

        self.horizontalSpacer_2 = QSpacerItem(132, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 526, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.player_msg.setText(QCoreApplication.translate("MainWindow", u"Good luck!", None))
    # retranslateUi

