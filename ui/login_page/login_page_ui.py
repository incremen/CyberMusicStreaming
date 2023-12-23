# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_page.ui'
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
        MainWindow.resize(1081, 803)
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setStyleSheet(u"#central_widget {\n"
" background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"            stop:0 #4B0082, stop:1 #000000);\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.central_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.central_widget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(16777215, 100))
        self.label.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white;\n"
"")

        self.verticalLayout.addWidget(self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(120, 100))
        self.label_2.setStyleSheet(u" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
"color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"\n"
"\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 100))
        self.lineEdit.setBaseSize(QSize(0, 100))
        font1 = QFont()
        font1.setPointSize(80)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
"color: white;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"\n"
"\n"
"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMinimumSize(QSize(120, 100))
        self.label_6.setStyleSheet(u" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
"color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(120, 100))
        self.label_5.setStyleSheet(u" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
"color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 100))
        self.lineEdit_2.setBaseSize(QSize(0, 100))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
"color: white;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"\n"
"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 100))
        self.lineEdit_3.setBaseSize(QSize(0, 100))
        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setStyleSheet(u" border: 2px solid white;\n"
" background-color: rgba(128, 128, 128, 128);\n"
"color: white;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"\n"
"")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout.setItem(0, QFormLayout.LabelRole, self.horizontalSpacer)


        self.verticalLayout.addLayout(self.formLayout)


        self.verticalLayout_2.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1081, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"If you dont log in, who will?", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enter username:", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"asdf", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Enter password: ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Insert profile picture", None))
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
    # retranslateUi

