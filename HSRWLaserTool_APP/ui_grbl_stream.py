# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'grbl_streamZAKZUB.ui'
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


class Ui_GrblStream(object):
    def setupUi(self, GrblStream):
        if GrblStream.objectName():
            GrblStream.setObjectName(u"GrblStream")
        GrblStream.resize(478, 483)
        self.centralwidget = QWidget(GrblStream)
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
"	border-radius: 220px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(0, 170, 0, 0), stop:0.750 rgba(0, 85, 127, 255));\n"
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
        self.send_label.setGeometry(QRect(80, 30, 241, 41))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.send_label.setFont(font)
        self.send_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: #FFFFFFFF")
        self.send_label.setAlignment(Qt.AlignCenter)
        self.gcode_label = QLabel(self.container)
        self.gcode_label.setObjectName(u"gcode_label")
        self.gcode_label.setGeometry(QRect(50, 70, 301, 31))
        self.gcode_label.setFont(font)
        self.gcode_label.setLayoutDirection(Qt.LeftToRight)
        self.gcode_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: #FFFFFFFF")
        self.gcode_label.setAlignment(Qt.AlignCenter)
        self.progress_label = QLabel(self.container)
        self.progress_label.setObjectName(u"progress_label")
        self.progress_label.setGeometry(QRect(40, 90, 321, 181))
        font1 = QFont()
        font1.setFamily(u"Agency FB")
        font1.setPointSize(100)
        self.progress_label.setFont(font1)
        self.progress_label.setLayoutDirection(Qt.LeftToRight)
        self.progress_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: #FFFFFFFF")
        self.progress_label.setAlignment(Qt.AlignCenter)
        self.engrave_label = QLabel(self.container)
        self.engrave_label.setObjectName(u"engrave_label")
        self.engrave_label.setGeometry(QRect(120, 270, 161, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.engrave_label.setFont(font2)
        self.engrave_label.setLayoutDirection(Qt.LeftToRight)
        self.engrave_label.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(127, 240, 180);\n"
"color: #FFFFFFFF")
        self.engrave_label.setAlignment(Qt.AlignCenter)
        self.play_pause_button = QPushButton(self.container)
        self.play_pause_button.setObjectName(u"play_pause_button")
        self.play_pause_button.setGeometry(QRect(120, 310, 70, 70))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Black")
        font3.setPointSize(20)
        self.play_pause_button.setFont(font3)
        self.play_pause_button.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(0, 255, 119);\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 35px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(0, 240, 112);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(0, 143, 66);\n"
"}")
        icon = QIcon()
        icon.addFile(u"Images/PinClipart.com_barcode-clipart_2064177.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"Images/PinClipart.com_empty-refrigerator-clipart_1968920.png", QSize(), QIcon.Normal, QIcon.On)
        self.play_pause_button.setIcon(icon)
        self.play_pause_button.setIconSize(QSize(130, 200))
        self.play_pause_button.setCheckable(True)
        self.play_pause_button.setChecked(False)
        self.play_pause_button.setAutoExclusive(False)
        self.stop_button = QPushButton(self.container)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setGeometry(QRect(200, 310, 70, 70))
        self.stop_button.setFont(font3)
        self.stop_button.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(0, 255, 119);\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 35px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(0, 240, 112);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(0, 143, 66);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"Images/pngwing.com.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_button.setIcon(icon1)
        self.stop_button.setIconSize(QSize(120, 200))
        self.stop_button.setCheckable(True)
        self.stop_button.setChecked(False)
        self.stop_button.setAutoExclusive(False)
        self.circularBig.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        GrblStream.setCentralWidget(self.centralwidget)

        self.retranslateUi(GrblStream)

        QMetaObject.connectSlotsByName(GrblStream)
    # setupUi

    def retranslateUi(self, GrblStream):
        GrblStream.setWindowTitle(QCoreApplication.translate("GrblStream", u"MainWindow", None))
        self.send_label.setText(QCoreApplication.translate("GrblStream", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:400;\">PRESS </span>PLAY<span style=\" font-weight:400;\"> TO START</span></p></body></html>", None))
        self.gcode_label.setText(QCoreApplication.translate("GrblStream", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.progress_label.setText(QCoreApplication.translate("GrblStream", u"<html><head/><body><p align=\"center\">0<span style=\" font-size:72pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.engrave_label.setText(QCoreApplication.translate("GrblStream", u"<html><head/><body><p align=\"center\">Ready to engrave<br/></p></body></html>", None))
        self.play_pause_button.setText("")
        self.stop_button.setText("")
    # retranslateUi

