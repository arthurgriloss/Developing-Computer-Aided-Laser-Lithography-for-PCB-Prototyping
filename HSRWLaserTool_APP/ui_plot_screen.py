# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plot_screenhKtjJK.ui'
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


class Ui_PlotScreen(object):
    def setupUi(self, PlotScreen):
        if PlotScreen.objectName():
            PlotScreen.setObjectName(u"PlotScreen")
        PlotScreen.resize(800, 480)
        self.centralwidget = QWidget(PlotScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.DropShadowFrame = QFrame(self.centralwidget)
        self.DropShadowFrame.setObjectName(u"DropShadowFrame")
        self.DropShadowFrame.setGeometry(QRect(0, 0, 800, 480))
        self.DropShadowFrame.setStyleSheet(u"background-color: rgb(0, 240, 112);")
        self.DropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.DropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.DropShadowFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(-120, 0, 441, 581))
        font = QFont()
        font.setFamily(u"Calibri Light")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_4.setPixmap(QPixmap(u"Images/5782258-circuit-png-images-vector-and-psd-files-free-download-on-pngtree-circuits-png-360_360.png"))
        self.label_4.setScaledContents(True)
        self.label_5 = QLabel(self.DropShadowFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(420, 0, 381, 471))
        self.label_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_5.setPixmap(QPixmap(u"Images/favpng_electrical-network-printed-circuit-board-electronic-circuit-electronics.png"))
        self.label_5.setScaledContents(True)
        self.text = QTextBrowser(self.DropShadowFrame)
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(20, 360, 541, 111))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.text.setFont(font1)
        self.text.setStyleSheet(u"color: rgb(0,0,0);\n"
"border-radius: 10px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color:rgb(255,255,255);")
        self.text.setFrameShape(QFrame.NoFrame)
        self.text.setFrameShadow(QFrame.Sunken)
        self.text.setLineWidth(1)
        self.text.setMidLineWidth(0)
        self.text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.text.setTabChangesFocus(False)
        self.text.setUndoRedoEnabled(False)
        self.text.setOverwriteMode(True)
        self.text.setTabStopDistance(80.000000000000000)
        self.text.setAcceptRichText(False)
        self.text.setTextInteractionFlags(Qt.NoTextInteraction)
        self.text.setOpenLinks(False)
        self.plot_box = QGraphicsView(self.DropShadowFrame)
        self.plot_box.setObjectName(u"plot_box")
        self.plot_box.setGeometry(QRect(20, 10, 761, 341))
        self.plot_box.setStyleSheet(u"color: rgb(0,0,0);\n"
"border-radius: 10px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color:rgb(255,255,255);")
        self.plot_box.setFrameShape(QFrame.Box)
        self.plot_box.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.play_pause_button = QPushButton(self.DropShadowFrame)
        self.play_pause_button.setObjectName(u"play_pause_button")
        self.play_pause_button.setGeometry(QRect(580, 370, 91, 91))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Black")
        font2.setPointSize(20)
        self.play_pause_button.setFont(font2)
        self.play_pause_button.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(0, 255, 119);\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
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
        self.play_pause_button.setIconSize(QSize(150, 200))
        self.play_pause_button.setCheckable(True)
        self.play_pause_button.setChecked(False)
        self.play_pause_button.setAutoExclusive(False)
        self.stop_button = QPushButton(self.DropShadowFrame)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setGeometry(QRect(680, 370, 91, 91))
        self.stop_button.setFont(font2)
        self.stop_button.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(0, 255, 119);\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
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
        self.stop_button.setIconSize(QSize(150, 200))
        self.stop_button.setCheckable(True)
        self.stop_button.setChecked(False)
        self.stop_button.setAutoExclusive(False)
        self.label_5.raise_()
        self.label_4.raise_()
        self.text.raise_()
        self.plot_box.raise_()
        self.play_pause_button.raise_()
        self.stop_button.raise_()
        PlotScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(PlotScreen)

        QMetaObject.connectSlotsByName(PlotScreen)
    # setupUi

    def retranslateUi(self, PlotScreen):
        PlotScreen.setWindowTitle(QCoreApplication.translate("PlotScreen", u"MainWindow", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.text.setMarkdown(QCoreApplication.translate("PlotScreen", u"***PRESS THE PLAY BUTTON TO START THE PROCESS ***\n"
"\n"
"", None))
        self.text.setHtml(QCoreApplication.translate("PlotScreen", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:14pt; font-weight:600; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PRESS THE PLAY BUTTON TO START THE PROCESS </p></body></html>", None))
        self.play_pause_button.setText("")
        self.stop_button.setText("")
    # retranslateUi

