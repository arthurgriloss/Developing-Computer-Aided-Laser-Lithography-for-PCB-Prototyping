# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gcode_loaderjbRdrg.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_GcodeLoader(object):
    def setupUi(self, GcodeLoader):
        if GcodeLoader.objectName():
            GcodeLoader.setObjectName(u"GcodeLoader")
        GcodeLoader.resize(479, 484)
        self.centralwidget = QWidget(GcodeLoader)
        self.centralwidget.setObjectName(u"centralwidget")
        self.circularProgressBarBase = QFrame(self.centralwidget)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setGeometry(QRect(10, 10, 460, 460))
        self.circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Raised)
        self.circularProgress = QFrame(self.circularProgressBarBase)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(10, 10, 440, 440))
        self.circularProgress.setStyleSheet(u"QFrame{\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0 rgba(0, 85, 127, 255), stop:1 rgba(255, 255, 255, 0));\n"
"	border-radius: 220px;\n"
"}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularBig = QFrame(self.circularProgressBarBase)
        self.circularBig.setObjectName(u"circularBig")
        self.circularBig.setGeometry(QRect(10, 10, 440, 440))
        self.circularBig.setStyleSheet(u"QFrame{\n"
"	border-radius: 220px;\n"
"	background-color: rgba(0, 240, 112, 120);\n"
"}")
        self.circularBig.setFrameShape(QFrame.NoFrame)
        self.circularBig.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circularProgressBarBase)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(30, 30, 400, 400))
        self.container.setStyleSheet(u"QFrame{\n"
"	border-radius: 200px;\n"
"	background-color: rgb(0, 240, 112);\n"
"}")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.send_label = QLabel(self.container)
        self.send_label.setObjectName(u"send_label")
        self.send_label.setGeometry(QRect(0, 120, 401, 131))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.send_label.setFont(font)
        self.send_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: #FFFFFFFF")
        self.send_label.setAlignment(Qt.AlignCenter)
        self.engrave_label = QLabel(self.container)
        self.engrave_label.setObjectName(u"engrave_label")
        self.engrave_label.setGeometry(QRect(100, 80, 191, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(18)
        self.engrave_label.setFont(font1)
        self.engrave_label.setLayoutDirection(Qt.LeftToRight)
        self.engrave_label.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(127, 240, 180);\n"
"color: #FFFFFFFF")
        self.engrave_label.setAlignment(Qt.AlignCenter)
        self.send_label_2 = QLabel(self.container)
        self.send_label_2.setObjectName(u"send_label_2")
        self.send_label_2.setGeometry(QRect(30, 290, 341, 81))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.send_label_2.setFont(font2)
        self.send_label_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: #FFFFFFFF")
        self.send_label_2.setAlignment(Qt.AlignCenter)
        self.circularBig.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        GcodeLoader.setCentralWidget(self.centralwidget)

        self.retranslateUi(GcodeLoader)

        QMetaObject.connectSlotsByName(GcodeLoader)
    # setupUi

    def retranslateUi(self, GcodeLoader):
        GcodeLoader.setWindowTitle(QCoreApplication.translate("GcodeLoader", u"MainWindow", None))
        self.send_label.setText(QCoreApplication.translate("GcodeLoader", u"<html><head/><body><p align=\"center\">Generating<span style=\" font-weight:400;\"> the G-code...</span></p></body></html>", None))
        self.engrave_label.setText(QCoreApplication.translate("GcodeLoader", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Please wait</span></p></body></html>", None))
        self.send_label_2.setText(QCoreApplication.translate("GcodeLoader", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">It may take a few minutes</span></p></body></html>", None))
    # retranslateUi

