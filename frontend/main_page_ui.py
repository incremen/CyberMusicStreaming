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
        MainWindow.resize(996, 843)
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
        self.horizontalSpacer_2 = QSpacerItem(132, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setMinimumSize(QSize(900, 0))
        self.main_widget.setLayoutDirection(Qt.RightToLeft)
        self.gridLayoutWidget = QWidget(self.main_widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(70, 10, 741, 591))
        self.song_grid = QGridLayout(self.gridLayoutWidget)
        self.song_grid.setObjectName(u"song_grid")
        self.song_grid.setContentsMargins(0, 0, 0, 0)
        self.song_progress = QProgressBar(self.main_widget)
        self.song_progress.setObjectName(u"song_progress")
        self.song_progress.setGeometry(QRect(160, 680, 511, 23))
        self.song_progress.setValue(2)
        self.song_progress.setInvertedAppearance(True)
        self.horizontalScrollBar = QScrollBar(self.main_widget)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setGeometry(QRect(150, 730, 551, 16))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy1)
        self.horizontalScrollBar.setStyleSheet(u"QScrollBar {\n"
"                background-color: transparent;\n"
"                width: 10px;\n"
"            }\n"
"            QScrollBar::handle {\n"
"                background-color: blue;\n"
"                min-height: 0;\n"
"\n"
"            }\n"
"            QScrollBar::add-line, QScrollBar::sub-line {\n"
"                background-color: transparent;\n"
"                height: 0;\n"
"            }")
        self.horizontalScrollBar.setSliderPosition(2)
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)
        self.horizontalScrollBar.setInvertedAppearance(True)
        self.horizontalScrollBar.setInvertedControls(False)
        self.pause_btn = QPushButton(self.main_widget)
        self.pause_btn.setObjectName(u"pause_btn")
        self.pause_btn.setGeometry(QRect(264, 622, 111, 41))
        self.skip_btn = QPushButton(self.main_widget)
        self.skip_btn.setObjectName(u"skip_btn")
        self.skip_btn.setGeometry(QRect(454, 622, 111, 41))

        self.horizontalLayout.addWidget(self.main_widget)

        self.horizontalSpacer = QSpacerItem(132, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 996, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pause_btn.setText(QCoreApplication.translate("MainWindow", u"pause", None))
        self.skip_btn.setText(QCoreApplication.translate("MainWindow", u"skip", None))
    # retranslateUi

