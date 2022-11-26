# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_organizer.ui'
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
        MainWindow.resize(510, 445)
        MainWindow.setStyleSheet(u"background-color: rgb(215, 248, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_path = QLineEdit(self.frame)
        self.txt_path.setObjectName(u"txt_path")
        self.txt_path.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.txt_path)

        self.btn_open = QPushButton(self.frame)
        self.btn_open.setObjectName(u"btn_open")

        self.horizontalLayout_2.addWidget(self.btn_open)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.btn_organize = QPushButton(self.frame)
        self.btn_organize.setObjectName(u"btn_organize")

        self.horizontalLayout.addWidget(self.btn_organize)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"_imgs/icone2.png\"/></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#000000;\">ORGANIZADORZINHO</span></p></body></html>", None))
        self.txt_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_2.setText("")
        self.btn_organize.setText(QCoreApplication.translate("MainWindow", u"Organizar", None))
        self.label_3.setText("")
    # retranslateUi

