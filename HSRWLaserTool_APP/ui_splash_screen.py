# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenVuwvEQ.ui'
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


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(600, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.DropShadowFrame = QFrame(self.centralwidget)
        self.DropShadowFrame.setObjectName(u"DropShadowFrame")
        self.DropShadowFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(0, 240, 112);\n"
"	border-radius: 10px;\n"
"}")
        self.DropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.DropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.DropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 40, 581, 91))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(255,255,255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_subtitle = QLabel(self.DropShadowFrame)
        self.label_subtitle.setObjectName(u"label_subtitle")
        self.label_subtitle.setGeometry(QRect(0, 130, 581, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_subtitle.setFont(font1)
        self.label_subtitle.setStyleSheet(u"color: rgb(0, 186, 84);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_subtitle.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.DropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 250, 471, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color:rgb(0, 186, 84);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 85, 127, 255), stop:1 rgba(0, 0, 0, 255));\n"
"}")
        self.progressBar.setValue(50)
        self.label_loading = QLabel(self.DropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(0, 280, 581, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.label_loading.setFont(font2)
        self.label_loading.setAutoFillBackground(False)
        self.label_loading.setStyleSheet(u"color: rgb(0, 186, 84);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.DropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(230, 350, 341, 21))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        self.label_credits.setFont(font3)
        self.label_credits.setStyleSheet(u"color: rgb(0, 186, 84);")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label = QLabel(self.DropShadowFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 0, 341, 381))
        self.label.setPixmap(QPixmap(u"Images/favpng_electrical-network-printed-circuit-board-electronic-circuit-electronics.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.DropShadowFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-60, 0, 331, 461))
        self.label_2.setStyleSheet(u"border-radius: 100px;")
        self.label_2.setPixmap(QPixmap(u"Images/5782258-circuit-png-images-vector-and-psd-files-free-download-on-pngtree-circuits-png-360_360.png"))
        self.label_2.setScaledContents(True)
        self.label_2.raise_()
        self.label.raise_()
        self.label_title.raise_()
        self.label_subtitle.raise_()
        self.progressBar.raise_()
        self.label_loading.raise_()
        self.label_credits.raise_()

        self.verticalLayout.addWidget(self.DropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"<Strong> HSRW Laser tool", None))
        self.label_subtitle.setText(QCoreApplication.translate("SplashScreen", u"<Strong>V 1.0", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.label_credits.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-weight:600;\">Created by</span> Arthur Grilo da Silva Santos</p></body></html>", None))
        self.label.setText("")
        self.label_2.setText("")
    # retranslateUi

