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
        self.horizontalSpacer_2 = QSpacerItem(132, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setMinimumSize(QSize(485, 0))
        self.main_widget.setLayoutDirection(Qt.RightToLeft)
        self.gridLayoutW_idget = QWidget(self.main_widget)
        self.gridLayoutW_idget.setObjectName(u"gridLayoutW_idget")
        self.gridLayoutW_idget.setGeometry(QRect(50, 10, 381, 304))
        self.gridLayout_3 = QGridLayout(self.gridLayoutW_idget)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_1 = QPushButton(self.gridLayoutW_idget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(100)
        sizePolicy1.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy1)
        self.btn_1.setMinimumSize(QSize(100, 100))
        font = QFont()
        font.setFamily(u"MV Boli")
        font.setPointSize(48)
        self.btn_1.setFont(font)

        self.gridLayout_3.addWidget(self.btn_1, 0, 0, 1, 1)

        self.btn_5 = QPushButton(self.gridLayoutW_idget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy1.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy1)
        self.btn_5.setMinimumSize(QSize(100, 100))
        self.btn_5.setFont(font)

        self.gridLayout_3.addWidget(self.btn_5, 1, 1, 1, 1)

        self.btn_9 = QPushButton(self.gridLayoutW_idget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy1.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy1)
        self.btn_9.setMinimumSize(QSize(100, 100))
        self.btn_9.setFont(font)

        self.gridLayout_3.addWidget(self.btn_9, 2, 2, 1, 1)

        self.btn_4 = QPushButton(self.gridLayoutW_idget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy1.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy1)
        self.btn_4.setMinimumSize(QSize(100, 100))
        self.btn_4.setFont(font)

        self.gridLayout_3.addWidget(self.btn_4, 0, 1, 1, 1)

        self.btn_3 = QPushButton(self.gridLayoutW_idget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy1.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy1)
        self.btn_3.setMinimumSize(QSize(100, 100))
        self.btn_3.setFont(font)

        self.gridLayout_3.addWidget(self.btn_3, 2, 0, 1, 1)

        self.btn_8 = QPushButton(self.gridLayoutW_idget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy1.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy1)
        self.btn_8.setMinimumSize(QSize(100, 100))
        self.btn_8.setFont(font)

        self.gridLayout_3.addWidget(self.btn_8, 1, 2, 1, 1)

        self.btn_2 = QPushButton(self.gridLayoutW_idget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy1.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy1)
        self.btn_2.setMinimumSize(QSize(100, 100))
        self.btn_2.setFont(font)

        self.gridLayout_3.addWidget(self.btn_2, 1, 0, 1, 1)

        self.btn_7 = QPushButton(self.gridLayoutW_idget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy1.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy1)
        self.btn_7.setMinimumSize(QSize(100, 100))
        self.btn_7.setFont(font)

        self.gridLayout_3.addWidget(self.btn_7, 0, 2, 1, 1)

        self.btn_6 = QPushButton(self.gridLayoutW_idget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy1.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy1)
        self.btn_6.setMinimumSize(QSize(100, 100))
        self.btn_6.setFont(font)

        self.gridLayout_3.addWidget(self.btn_6, 2, 1, 1, 1)

        self.player_msg = QLabel(self.main_widget)
        self.player_msg.setObjectName(u"player_msg")
        self.player_msg.setGeometry(QRect(-30, 530, 531, 161))
        font1 = QFont()
        font1.setFamily(u"Voltage")
        font1.setPointSize(70)
        self.player_msg.setFont(font1)
        self.player_msg.setStyleSheet(u"")
        self.player_msg.setAlignment(Qt.AlignCenter)
        self.btn_reset = QPushButton(self.main_widget)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setGeometry(QRect(75, 460, 301, 71))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_reset.sizePolicy().hasHeightForWidth())
        self.btn_reset.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamily(u"Courier")
        font2.setPointSize(50)
        self.btn_reset.setFont(font2)
        self.btn_reset.setStyleSheet(u"")
        self.opponents_symbol_text = QLabel(self.main_widget)
        self.opponents_symbol_text.setObjectName(u"opponents_symbol_text")
        self.opponents_symbol_text.setGeometry(QRect(260, 340, 181, 41))
        font3 = QFont()
        font3.setFamily(u"Voltage")
        font3.setPointSize(14)
        self.opponents_symbol_text.setFont(font3)
        self.opponents_symbol_text.setAlignment(Qt.AlignCenter)
        self.your_symbol_text = QLabel(self.main_widget)
        self.your_symbol_text.setObjectName(u"your_symbol_text")
        self.your_symbol_text.setGeometry(QRect(65, 340, 111, 41))
        self.your_symbol_text.setFont(font3)
        self.your_symbol_text.setAlignment(Qt.AlignCenter)
        self.player_symbol_label = QLabel(self.main_widget)
        self.player_symbol_label.setObjectName(u"player_symbol_label")
        self.player_symbol_label.setGeometry(QRect(90, 380, 61, 61))
        font4 = QFont()
        font4.setFamily(u"MV Boli")
        font4.setPointSize(40)
        self.player_symbol_label.setFont(font4)
        self.player_symbol_label.setStyleSheet(u"border: 1px solid black;")
        self.player_symbol_label.setAlignment(Qt.AlignCenter)
        self.opponent_symbol_label = QLabel(self.main_widget)
        self.opponent_symbol_label.setObjectName(u"opponent_symbol_label")
        self.opponent_symbol_label.setGeometry(QRect(320, 380, 61, 61))
        self.opponent_symbol_label.setFont(font4)
        self.opponent_symbol_label.setStyleSheet(u"border: 1px solid black; \n"
"")
        self.opponent_symbol_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.main_widget)

        self.horizontalSpacer = QSpacerItem(132, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

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
        self.btn_1.setText("")
        self.btn_5.setText("")
        self.btn_9.setText("")
        self.btn_4.setText("")
        self.btn_3.setText("")
        self.btn_8.setText("")
        self.btn_2.setText("")
        self.btn_7.setText("")
        self.btn_6.setText("")
        self.player_msg.setText(QCoreApplication.translate("MainWindow", u"Good luck!", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"Start Over", None))
        self.opponents_symbol_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Opponent's symbol:</p></body></html>", None))
        self.your_symbol_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Your symbol:</p></body></html>", None))
        self.player_symbol_label.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.opponent_symbol_label.setText(QCoreApplication.translate("MainWindow", u"O", None))
    # retranslateUi

