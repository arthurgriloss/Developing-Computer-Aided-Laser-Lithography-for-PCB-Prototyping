# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainLpNvti.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.DropShadowFrame = QFrame(self.centralwidget)
        self.DropShadowFrame.setObjectName(u"DropShadowFrame")
        self.DropShadowFrame.setStyleSheet(u"background-color: rgb(0, 240, 112);")
        self.DropShadowFrame.setFrameShape(QFrame.NoFrame)
        self.DropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.DropShadowFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-120, 0, 441, 581))
        font = QFont()
        font.setFamily(u"Calibri Light")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_2.setPixmap(QPixmap(u"Images/5782258-circuit-png-images-vector-and-psd-files-free-download-on-pngtree-circuits-png-360_360.png"))
        self.label_2.setScaledContents(True)
        self.label = QLabel(self.DropShadowFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(420, 0, 381, 471))
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label.setPixmap(QPixmap(u"Images/favpng_electrical-network-printed-circuit-board-electronic-circuit-electronics.png"))
        self.label.setScaledContents(True)
        self.label_3 = QLabel(self.DropShadowFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 88, 561, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.browse_button = QPushButton(self.DropShadowFrame)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setGeometry(QRect(650, 30, 121, 61))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.browse_button.setFont(font2)
        self.browse_button.setLayoutDirection(Qt.LeftToRight)
        self.browse_button.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(0, 240, 112);\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border-color: white;\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(0, 255, 119);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(0, 143, 66);\n"
"}")
        icon = QIcon()
        icon.addFile(u"Images/clipart1547514.png", QSize(), QIcon.Normal, QIcon.Off)
        self.browse_button.setIcon(icon)
        self.browse_button.setIconSize(QSize(30, 30))
        self.next_button = QPushButton(self.DropShadowFrame)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setGeometry(QRect(580, 400, 191, 71))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        self.next_button.setFont(font3)
        self.next_button.setLayoutDirection(Qt.LeftToRight)
        self.next_button.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(0, 240, 112);\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(0, 255, 119);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(0, 143, 66);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"Images/pngfind.com-start-button-png-3164705.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_button.setIcon(icon1)
        self.next_button.setIconSize(QSize(190, 80))
        self.next_button.setCheckable(False)
        self.groupBox = QGroupBox(self.DropShadowFrame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(210, 130, 561, 261))
        self.groupBox.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, -2, 541, 261))
        self.gridLayout_10 = QGridLayout(self.layoutWidget)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.b2 = QCheckBox(self.layoutWidget)
        self.b2.setObjectName(u"b2")

        self.gridLayout_7.addWidget(self.b2, 0, 1, 1, 1)

        self.d2 = QCheckBox(self.layoutWidget)
        self.d2.setObjectName(u"d2")

        self.gridLayout_7.addWidget(self.d2, 0, 3, 1, 1)

        self.h2 = QCheckBox(self.layoutWidget)
        self.h2.setObjectName(u"h2")

        self.gridLayout_7.addWidget(self.h2, 0, 7, 1, 1)

        self.j2 = QCheckBox(self.layoutWidget)
        self.j2.setObjectName(u"j2")

        self.gridLayout_7.addWidget(self.j2, 0, 9, 1, 1)

        self.k2 = QCheckBox(self.layoutWidget)
        self.k2.setObjectName(u"k2")

        self.gridLayout_7.addWidget(self.k2, 0, 10, 1, 1)

        self.a2 = QCheckBox(self.layoutWidget)
        self.a2.setObjectName(u"a2")

        self.gridLayout_7.addWidget(self.a2, 0, 0, 1, 1)

        self.i2 = QCheckBox(self.layoutWidget)
        self.i2.setObjectName(u"i2")

        self.gridLayout_7.addWidget(self.i2, 0, 8, 1, 1)

        self.g2 = QCheckBox(self.layoutWidget)
        self.g2.setObjectName(u"g2")

        self.gridLayout_7.addWidget(self.g2, 0, 6, 1, 1)

        self.f2 = QCheckBox(self.layoutWidget)
        self.f2.setObjectName(u"f2")

        self.gridLayout_7.addWidget(self.f2, 0, 5, 1, 1)

        self.e2 = QCheckBox(self.layoutWidget)
        self.e2.setObjectName(u"e2")

        self.gridLayout_7.addWidget(self.e2, 0, 4, 1, 1)

        self.c2 = QCheckBox(self.layoutWidget)
        self.c2.setObjectName(u"c2")

        self.gridLayout_7.addWidget(self.c2, 0, 2, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_7, 2, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.a7 = QCheckBox(self.layoutWidget)
        self.a7.setObjectName(u"a7")

        self.gridLayout_2.addWidget(self.a7, 0, 0, 1, 1)

        self.b7 = QCheckBox(self.layoutWidget)
        self.b7.setObjectName(u"b7")

        self.gridLayout_2.addWidget(self.b7, 0, 1, 1, 1)

        self.c7 = QCheckBox(self.layoutWidget)
        self.c7.setObjectName(u"c7")

        self.gridLayout_2.addWidget(self.c7, 0, 2, 1, 1)

        self.d7 = QCheckBox(self.layoutWidget)
        self.d7.setObjectName(u"d7")

        self.gridLayout_2.addWidget(self.d7, 0, 3, 1, 1)

        self.e7 = QCheckBox(self.layoutWidget)
        self.e7.setObjectName(u"e7")

        self.gridLayout_2.addWidget(self.e7, 0, 4, 1, 1)

        self.f7 = QCheckBox(self.layoutWidget)
        self.f7.setObjectName(u"f7")

        self.gridLayout_2.addWidget(self.f7, 0, 5, 1, 1)

        self.g7 = QCheckBox(self.layoutWidget)
        self.g7.setObjectName(u"g7")

        self.gridLayout_2.addWidget(self.g7, 0, 6, 1, 1)

        self.h7 = QCheckBox(self.layoutWidget)
        self.h7.setObjectName(u"h7")

        self.gridLayout_2.addWidget(self.h7, 0, 7, 1, 1)

        self.i7 = QCheckBox(self.layoutWidget)
        self.i7.setObjectName(u"i7")

        self.gridLayout_2.addWidget(self.i7, 0, 8, 1, 1)

        self.j7 = QCheckBox(self.layoutWidget)
        self.j7.setObjectName(u"j7")

        self.gridLayout_2.addWidget(self.j7, 0, 9, 1, 1)

        self.k7 = QCheckBox(self.layoutWidget)
        self.k7.setObjectName(u"k7")

        self.gridLayout_2.addWidget(self.k7, 0, 10, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_2, 7, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.a3 = QCheckBox(self.layoutWidget)
        self.a3.setObjectName(u"a3")

        self.gridLayout_6.addWidget(self.a3, 0, 0, 1, 1)

        self.b3 = QCheckBox(self.layoutWidget)
        self.b3.setObjectName(u"b3")

        self.gridLayout_6.addWidget(self.b3, 0, 1, 1, 1)

        self.c3 = QCheckBox(self.layoutWidget)
        self.c3.setObjectName(u"c3")

        self.gridLayout_6.addWidget(self.c3, 0, 2, 1, 1)

        self.d3 = QCheckBox(self.layoutWidget)
        self.d3.setObjectName(u"d3")

        self.gridLayout_6.addWidget(self.d3, 0, 3, 1, 1)

        self.e3 = QCheckBox(self.layoutWidget)
        self.e3.setObjectName(u"e3")

        self.gridLayout_6.addWidget(self.e3, 0, 4, 1, 1)

        self.f3 = QCheckBox(self.layoutWidget)
        self.f3.setObjectName(u"f3")

        self.gridLayout_6.addWidget(self.f3, 0, 5, 1, 1)

        self.g3 = QCheckBox(self.layoutWidget)
        self.g3.setObjectName(u"g3")

        self.gridLayout_6.addWidget(self.g3, 0, 6, 1, 1)

        self.h3 = QCheckBox(self.layoutWidget)
        self.h3.setObjectName(u"h3")

        self.gridLayout_6.addWidget(self.h3, 0, 7, 1, 1)

        self.i3 = QCheckBox(self.layoutWidget)
        self.i3.setObjectName(u"i3")

        self.gridLayout_6.addWidget(self.i3, 0, 8, 1, 1)

        self.j3 = QCheckBox(self.layoutWidget)
        self.j3.setObjectName(u"j3")

        self.gridLayout_6.addWidget(self.j3, 0, 9, 1, 1)

        self.k3 = QCheckBox(self.layoutWidget)
        self.k3.setObjectName(u"k3")

        self.gridLayout_6.addWidget(self.k3, 0, 10, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_6, 3, 0, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.a1 = QCheckBox(self.layoutWidget)
        self.a1.setObjectName(u"a1")

        self.gridLayout_8.addWidget(self.a1, 0, 0, 1, 1)

        self.b1 = QCheckBox(self.layoutWidget)
        self.b1.setObjectName(u"b1")

        self.gridLayout_8.addWidget(self.b1, 0, 1, 1, 1)

        self.c1 = QCheckBox(self.layoutWidget)
        self.c1.setObjectName(u"c1")

        self.gridLayout_8.addWidget(self.c1, 0, 2, 1, 1)

        self.d1 = QCheckBox(self.layoutWidget)
        self.d1.setObjectName(u"d1")

        self.gridLayout_8.addWidget(self.d1, 0, 3, 1, 1)

        self.e1 = QCheckBox(self.layoutWidget)
        self.e1.setObjectName(u"e1")

        self.gridLayout_8.addWidget(self.e1, 0, 4, 1, 1)

        self.f1 = QCheckBox(self.layoutWidget)
        self.f1.setObjectName(u"f1")

        self.gridLayout_8.addWidget(self.f1, 0, 5, 1, 1)

        self.g1 = QCheckBox(self.layoutWidget)
        self.g1.setObjectName(u"g1")

        self.gridLayout_8.addWidget(self.g1, 0, 6, 1, 1)

        self.h1 = QCheckBox(self.layoutWidget)
        self.h1.setObjectName(u"h1")

        self.gridLayout_8.addWidget(self.h1, 0, 7, 1, 1)

        self.i1 = QCheckBox(self.layoutWidget)
        self.i1.setObjectName(u"i1")

        self.gridLayout_8.addWidget(self.i1, 0, 8, 1, 1)

        self.j1 = QCheckBox(self.layoutWidget)
        self.j1.setObjectName(u"j1")

        self.gridLayout_8.addWidget(self.j1, 0, 9, 1, 1)

        self.k1 = QCheckBox(self.layoutWidget)
        self.k1.setObjectName(u"k1")

        self.gridLayout_8.addWidget(self.k1, 0, 10, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_8, 1, 0, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.a0 = QCheckBox(self.layoutWidget)
        self.a0.setObjectName(u"a0")

        self.gridLayout_9.addWidget(self.a0, 0, 0, 1, 1)

        self.b0 = QCheckBox(self.layoutWidget)
        self.b0.setObjectName(u"b0")

        self.gridLayout_9.addWidget(self.b0, 0, 1, 1, 1)

        self.c0 = QCheckBox(self.layoutWidget)
        self.c0.setObjectName(u"c0")

        self.gridLayout_9.addWidget(self.c0, 0, 2, 1, 1)

        self.d0 = QCheckBox(self.layoutWidget)
        self.d0.setObjectName(u"d0")

        self.gridLayout_9.addWidget(self.d0, 0, 3, 1, 1)

        self.e0 = QCheckBox(self.layoutWidget)
        self.e0.setObjectName(u"e0")

        self.gridLayout_9.addWidget(self.e0, 0, 4, 1, 1)

        self.f0 = QCheckBox(self.layoutWidget)
        self.f0.setObjectName(u"f0")

        self.gridLayout_9.addWidget(self.f0, 0, 5, 1, 1)

        self.g0 = QCheckBox(self.layoutWidget)
        self.g0.setObjectName(u"g0")

        self.gridLayout_9.addWidget(self.g0, 0, 6, 1, 1)

        self.h0 = QCheckBox(self.layoutWidget)
        self.h0.setObjectName(u"h0")

        self.gridLayout_9.addWidget(self.h0, 0, 7, 1, 1)

        self.i0 = QCheckBox(self.layoutWidget)
        self.i0.setObjectName(u"i0")

        self.gridLayout_9.addWidget(self.i0, 0, 8, 1, 1)

        self.j0 = QCheckBox(self.layoutWidget)
        self.j0.setObjectName(u"j0")

        self.gridLayout_9.addWidget(self.j0, 0, 9, 1, 1)

        self.k0 = QCheckBox(self.layoutWidget)
        self.k0.setObjectName(u"k0")

        self.gridLayout_9.addWidget(self.k0, 0, 10, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.e6 = QCheckBox(self.layoutWidget)
        self.e6.setObjectName(u"e6")

        self.gridLayout_3.addWidget(self.e6, 0, 4, 1, 1)

        self.k6 = QCheckBox(self.layoutWidget)
        self.k6.setObjectName(u"k6")

        self.gridLayout_3.addWidget(self.k6, 0, 10, 1, 1)

        self.j6 = QCheckBox(self.layoutWidget)
        self.j6.setObjectName(u"j6")

        self.gridLayout_3.addWidget(self.j6, 0, 9, 1, 1)

        self.i6 = QCheckBox(self.layoutWidget)
        self.i6.setObjectName(u"i6")

        self.gridLayout_3.addWidget(self.i6, 0, 8, 1, 1)

        self.g6 = QCheckBox(self.layoutWidget)
        self.g6.setObjectName(u"g6")

        self.gridLayout_3.addWidget(self.g6, 0, 6, 1, 1)

        self.d6 = QCheckBox(self.layoutWidget)
        self.d6.setObjectName(u"d6")

        self.gridLayout_3.addWidget(self.d6, 0, 3, 1, 1)

        self.b6 = QCheckBox(self.layoutWidget)
        self.b6.setObjectName(u"b6")

        self.gridLayout_3.addWidget(self.b6, 0, 1, 1, 1)

        self.h6 = QCheckBox(self.layoutWidget)
        self.h6.setObjectName(u"h6")

        self.gridLayout_3.addWidget(self.h6, 0, 7, 1, 1)

        self.f6 = QCheckBox(self.layoutWidget)
        self.f6.setObjectName(u"f6")

        self.gridLayout_3.addWidget(self.f6, 0, 5, 1, 1)

        self.a6 = QCheckBox(self.layoutWidget)
        self.a6.setObjectName(u"a6")

        self.gridLayout_3.addWidget(self.a6, 0, 0, 1, 1)

        self.c6 = QCheckBox(self.layoutWidget)
        self.c6.setObjectName(u"c6")

        self.gridLayout_3.addWidget(self.c6, 0, 2, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_3, 6, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.a5 = QCheckBox(self.layoutWidget)
        self.a5.setObjectName(u"a5")

        self.gridLayout_4.addWidget(self.a5, 0, 0, 1, 1)

        self.b5 = QCheckBox(self.layoutWidget)
        self.b5.setObjectName(u"b5")

        self.gridLayout_4.addWidget(self.b5, 0, 1, 1, 1)

        self.c5 = QCheckBox(self.layoutWidget)
        self.c5.setObjectName(u"c5")

        self.gridLayout_4.addWidget(self.c5, 0, 2, 1, 1)

        self.d5 = QCheckBox(self.layoutWidget)
        self.d5.setObjectName(u"d5")

        self.gridLayout_4.addWidget(self.d5, 0, 3, 1, 1)

        self.e5 = QCheckBox(self.layoutWidget)
        self.e5.setObjectName(u"e5")

        self.gridLayout_4.addWidget(self.e5, 0, 4, 1, 1)

        self.f5 = QCheckBox(self.layoutWidget)
        self.f5.setObjectName(u"f5")

        self.gridLayout_4.addWidget(self.f5, 0, 5, 1, 1)

        self.g5 = QCheckBox(self.layoutWidget)
        self.g5.setObjectName(u"g5")

        self.gridLayout_4.addWidget(self.g5, 0, 6, 1, 1)

        self.h5 = QCheckBox(self.layoutWidget)
        self.h5.setObjectName(u"h5")

        self.gridLayout_4.addWidget(self.h5, 0, 7, 1, 1)

        self.i5 = QCheckBox(self.layoutWidget)
        self.i5.setObjectName(u"i5")

        self.gridLayout_4.addWidget(self.i5, 0, 8, 1, 1)

        self.j5 = QCheckBox(self.layoutWidget)
        self.j5.setObjectName(u"j5")

        self.gridLayout_4.addWidget(self.j5, 0, 9, 1, 1)

        self.k5 = QCheckBox(self.layoutWidget)
        self.k5.setObjectName(u"k5")

        self.gridLayout_4.addWidget(self.k5, 0, 10, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_4, 5, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.a4 = QCheckBox(self.layoutWidget)
        self.a4.setObjectName(u"a4")

        self.gridLayout_5.addWidget(self.a4, 0, 0, 1, 1)

        self.b4 = QCheckBox(self.layoutWidget)
        self.b4.setObjectName(u"b4")

        self.gridLayout_5.addWidget(self.b4, 0, 1, 1, 1)

        self.c4 = QCheckBox(self.layoutWidget)
        self.c4.setObjectName(u"c4")

        self.gridLayout_5.addWidget(self.c4, 0, 2, 1, 1)

        self.d4 = QCheckBox(self.layoutWidget)
        self.d4.setObjectName(u"d4")
        self.d4.setChecked(True)

        self.gridLayout_5.addWidget(self.d4, 0, 3, 1, 1)

        self.e4 = QCheckBox(self.layoutWidget)
        self.e4.setObjectName(u"e4")

        self.gridLayout_5.addWidget(self.e4, 0, 4, 1, 1)

        self.f4 = QCheckBox(self.layoutWidget)
        self.f4.setObjectName(u"f4")

        self.gridLayout_5.addWidget(self.f4, 0, 5, 1, 1)

        self.g4 = QCheckBox(self.layoutWidget)
        self.g4.setObjectName(u"g4")

        self.gridLayout_5.addWidget(self.g4, 0, 6, 1, 1)

        self.h4 = QCheckBox(self.layoutWidget)
        self.h4.setObjectName(u"h4")
        self.h4.setChecked(True)

        self.gridLayout_5.addWidget(self.h4, 0, 7, 1, 1)

        self.i4 = QCheckBox(self.layoutWidget)
        self.i4.setObjectName(u"i4")

        self.gridLayout_5.addWidget(self.i4, 0, 8, 1, 1)

        self.j4 = QCheckBox(self.layoutWidget)
        self.j4.setObjectName(u"j4")

        self.gridLayout_5.addWidget(self.j4, 0, 9, 1, 1)

        self.k4 = QCheckBox(self.layoutWidget)
        self.k4.setObjectName(u"k4")

        self.gridLayout_5.addWidget(self.k4, 0, 10, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_5, 4, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.a8 = QCheckBox(self.layoutWidget)
        self.a8.setObjectName(u"a8")

        self.gridLayout.addWidget(self.a8, 0, 0, 1, 1)

        self.b8 = QCheckBox(self.layoutWidget)
        self.b8.setObjectName(u"b8")

        self.gridLayout.addWidget(self.b8, 0, 1, 1, 1)

        self.c8 = QCheckBox(self.layoutWidget)
        self.c8.setObjectName(u"c8")

        self.gridLayout.addWidget(self.c8, 0, 2, 1, 1)

        self.d8 = QCheckBox(self.layoutWidget)
        self.d8.setObjectName(u"d8")

        self.gridLayout.addWidget(self.d8, 0, 3, 1, 1)

        self.e8 = QCheckBox(self.layoutWidget)
        self.e8.setObjectName(u"e8")

        self.gridLayout.addWidget(self.e8, 0, 4, 1, 1)

        self.f8 = QCheckBox(self.layoutWidget)
        self.f8.setObjectName(u"f8")

        self.gridLayout.addWidget(self.f8, 0, 5, 1, 1)

        self.g8 = QCheckBox(self.layoutWidget)
        self.g8.setObjectName(u"g8")

        self.gridLayout.addWidget(self.g8, 0, 6, 1, 1)

        self.h8 = QCheckBox(self.layoutWidget)
        self.h8.setObjectName(u"h8")

        self.gridLayout.addWidget(self.h8, 0, 7, 1, 1)

        self.i8 = QCheckBox(self.layoutWidget)
        self.i8.setObjectName(u"i8")

        self.gridLayout.addWidget(self.i8, 0, 8, 1, 1)

        self.j8 = QCheckBox(self.layoutWidget)
        self.j8.setObjectName(u"j8")

        self.gridLayout.addWidget(self.j8, 0, 9, 1, 1)

        self.k8 = QCheckBox(self.layoutWidget)
        self.k8.setObjectName(u"k8")

        self.gridLayout.addWidget(self.k8, 0, 10, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout, 8, 0, 1, 1)

        self.directory_edit = QTextBrowser(self.DropShadowFrame)
        self.directory_edit.setObjectName(u"directory_edit")
        self.directory_edit.setGeometry(QRect(30, 50, 611, 41))
        font4 = QFont()
        font4.setFamily(u"Courier")
        font4.setPointSize(24)
        self.directory_edit.setFont(font4)
        self.directory_edit.setStyleSheet(u"color: rgb(0,0,0);\n"
"border-radius: 10px;\n"
"border-color: rgb(0, 0, 0);\n"
"background-color:rgb(255,255,255);")
        self.adv_label = QLabel(self.DropShadowFrame)
        self.adv_label.setObjectName(u"adv_label")
        self.adv_label.setGeometry(QRect(310, -20, 181, 61))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(10)
        self.adv_label.setFont(font5)
        self.adv_label.setStyleSheet(u"background-color: rgb(2, 2, 2);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.adv_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.advMenu = QFrame(self.DropShadowFrame)
        self.advMenu.setObjectName(u"advMenu")
        self.advMenu.setGeometry(QRect(0, 0, 800, 5))
        self.advMenu.setMaximumSize(QSize(16777215, 16777215))
        self.advMenu.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.advMenu.setFrameShape(QFrame.StyledPanel)
        self.advMenu.setFrameShadow(QFrame.Raised)
        self.root_button = QPushButton(self.advMenu)
        self.root_button.setObjectName(u"root_button")
        self.root_button.setGeometry(QRect(30, 20, 121, 61))
        self.root_button.setFont(font2)
        self.root_button.setLayoutDirection(Qt.LeftToRight)
        self.root_button.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(0, 0, 0);\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border-color: white;\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(50, 50, 50);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(100, 100, 100);\n"
"}")
        self.root_button.setIcon(icon)
        self.root_button.setIconSize(QSize(30, 30))
        self.default_check = QCheckBox(self.advMenu)
        self.default_check.setObjectName(u"default_check")
        self.default_check.setGeometry(QRect(620, 10, 141, 41))
        self.default_check.setFont(font5)
        self.default_check.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.default_check.setIconSize(QSize(25, 25))
        self.label_4 = QLabel(self.advMenu)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(520, 150, 161, 61))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(14)
        self.label_4.setFont(font6)
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.advMenu)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(510, 260, 151, 31))
        self.label_5.setFont(font6)
        self.label_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.advMenu)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(410, 370, 221, 43))
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.feed_rate = QDoubleSpinBox(self.advMenu)
        self.feed_rate.setObjectName(u"feed_rate")
        self.feed_rate.setGeometry(QRect(400, 370, 321, 81))
        font7 = QFont()
        font7.setPointSize(24)
        self.feed_rate.setFont(font7)
        self.feed_rate.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.feed_rate.setWrapping(False)
        self.feed_rate.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.feed_rate.setReadOnly(False)
        self.feed_rate.setAccelerated(True)
        self.feed_rate.setDecimals(0)
        self.feed_rate.setMinimum(10.000000000000000)
        self.feed_rate.setMaximum(2000.000000000000000)
        self.feed_rate.setSingleStep(10.000000000000000)
        self.feed_rate.setValue(2000.000000000000000)
        self.pcb_width = QDoubleSpinBox(self.advMenu)
        self.pcb_width.setObjectName(u"pcb_width")
        self.pcb_width.setGeometry(QRect(290, 160, 211, 81))
        self.pcb_width.setFont(font7)
        self.pcb_width.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pcb_width.setWrapping(False)
        self.pcb_width.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.pcb_width.setReadOnly(False)
        self.pcb_width.setAccelerated(True)
        self.pcb_width.setDecimals(0)
        self.pcb_width.setMinimum(5.000000000000000)
        self.pcb_width.setMaximum(300.000000000000000)
        self.pcb_width.setSingleStep(5.000000000000000)
        self.pcb_width.setValue(160.000000000000000)
        self.overlap = QDoubleSpinBox(self.advMenu)
        self.overlap.setObjectName(u"overlap")
        self.overlap.setGeometry(QRect(510, 160, 211, 81))
        self.overlap.setFont(font7)
        self.overlap.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.overlap.setWrapping(False)
        self.overlap.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.overlap.setReadOnly(False)
        self.overlap.setAccelerated(True)
        self.overlap.setDecimals(0)
        self.overlap.setMaximum(100.000000000000000)
        self.overlap.setSingleStep(10.000000000000000)
        self.overlap.setValue(90.000000000000000)
        self.tool_diameter = QDoubleSpinBox(self.advMenu)
        self.tool_diameter.setObjectName(u"tool_diameter")
        self.tool_diameter.setGeometry(QRect(70, 370, 321, 81))
        self.tool_diameter.setFont(font7)
        self.tool_diameter.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tool_diameter.setWrapping(False)
        self.tool_diameter.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.tool_diameter.setReadOnly(False)
        self.tool_diameter.setAccelerated(True)
        self.tool_diameter.setSingleStep(0.010000000000000)
        self.tool_diameter.setValue(0.100000000000000)
        self.label_7 = QLabel(self.advMenu)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 370, 221, 43))
        self.label_7.setFont(font6)
        self.label_7.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.advMenu)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(300, 150, 161, 61))
        self.label_8.setFont(font6)
        self.label_8.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.pin_gap = QDoubleSpinBox(self.advMenu)
        self.pin_gap.setObjectName(u"pin_gap")
        self.pin_gap.setGeometry(QRect(510, 260, 211, 81))
        self.pin_gap.setFont(font7)
        self.pin_gap.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pin_gap.setWrapping(False)
        self.pin_gap.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.pin_gap.setReadOnly(False)
        self.pin_gap.setAccelerated(True)
        self.pin_gap.setDecimals(0)
        self.pin_gap.setMinimum(5.000000000000000)
        self.pin_gap.setMaximum(100.000000000000000)
        self.pin_gap.setSingleStep(5.000000000000000)
        self.pin_gap.setValue(30.000000000000000)
        self.passes_iso = QDoubleSpinBox(self.advMenu)
        self.passes_iso.setObjectName(u"passes_iso")
        self.passes_iso.setGeometry(QRect(290, 260, 211, 81))
        self.passes_iso.setFont(font7)
        self.passes_iso.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.passes_iso.setWrapping(False)
        self.passes_iso.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.passes_iso.setReadOnly(False)
        self.passes_iso.setAccelerated(True)
        self.passes_iso.setDecimals(0)
        self.passes_iso.setMaximum(100.000000000000000)
        self.passes_iso.setSingleStep(1.000000000000000)
        self.passes_iso.setValue(2.000000000000000)
        self.label_9 = QLabel(self.advMenu)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(300, 260, 151, 31))
        self.label_9.setFont(font6)
        self.label_9.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.root_browse = QTextBrowser(self.advMenu)
        self.root_browse.setObjectName(u"root_browse")
        self.root_browse.setGeometry(QRect(30, 100, 741, 41))
        self.root_browse.setFont(font4)
        self.root_browse.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.label_10 = QLabel(self.advMenu)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(80, 260, 151, 31))
        self.label_10.setFont(font6)
        self.label_10.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.spin_speed = QDoubleSpinBox(self.advMenu)
        self.spin_speed.setObjectName(u"spin_speed")
        self.spin_speed.setGeometry(QRect(70, 260, 211, 81))
        self.spin_speed.setFont(font7)
        self.spin_speed.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spin_speed.setWrapping(False)
        self.spin_speed.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.spin_speed.setReadOnly(False)
        self.spin_speed.setAccelerated(True)
        self.spin_speed.setDecimals(0)
        self.spin_speed.setMaximum(1000.000000000000000)
        self.spin_speed.setSingleStep(10.000000000000000)
        self.spin_speed.setValue(100.000000000000000)
        self.keep_check = QCheckBox(self.advMenu)
        self.keep_check.setObjectName(u"keep_check")
        self.keep_check.setGeometry(QRect(530, 50, 241, 41))
        self.keep_check.setFont(font5)
        self.keep_check.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.keep_check.setIconSize(QSize(25, 25))
        self.pcb_height = QDoubleSpinBox(self.advMenu)
        self.pcb_height.setObjectName(u"pcb_height")
        self.pcb_height.setGeometry(QRect(70, 160, 211, 81))
        self.pcb_height.setFont(font7)
        self.pcb_height.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pcb_height.setWrapping(False)
        self.pcb_height.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.pcb_height.setReadOnly(False)
        self.pcb_height.setAccelerated(True)
        self.pcb_height.setDecimals(0)
        self.pcb_height.setMinimum(5.000000000000000)
        self.pcb_height.setMaximum(300.000000000000000)
        self.pcb_height.setSingleStep(5.000000000000000)
        self.pcb_height.setValue(100.000000000000000)
        self.label_11 = QLabel(self.advMenu)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(70, 150, 161, 61))
        self.label_11.setFont(font6)
        self.label_11.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.pcb_width.raise_()
        self.spin_speed.raise_()
        self.label_10.raise_()
        self.pin_gap.raise_()
        self.label_8.raise_()
        self.root_button.raise_()
        self.default_check.raise_()
        self.feed_rate.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.overlap.raise_()
        self.label_4.raise_()
        self.tool_diameter.raise_()
        self.label_7.raise_()
        self.passes_iso.raise_()
        self.label_9.raise_()
        self.root_browse.raise_()
        self.keep_check.raise_()
        self.pcb_height.raise_()
        self.label_11.raise_()
        self.advanced_button = QPushButton(self.DropShadowFrame)
        self.advanced_button.setObjectName(u"advanced_button")
        self.advanced_button.setGeometry(QRect(310, 0, 181, 41))
        self.advanced_button.setFont(font2)
        self.advanced_button.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: none")
        self.shutdown_button = QPushButton(self.DropShadowFrame)
        self.shutdown_button.setObjectName(u"shutdown_button")
        self.shutdown_button.setGeometry(QRect(370, 400, 70, 70))
        self.shutdown_button.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(0, 240, 112);\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 35px;\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(0, 255, 119);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(0, 143, 66);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"Images/shutdown.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shutdown_button.setIcon(icon2)
        self.shutdown_button.setIconSize(QSize(40, 40))
        self.splitter = QSplitter(self.DropShadowFrame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(30, 120, 151, 331))
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setHandleWidth(10)
        self.gcode_button = QPushButton(self.splitter)
        self.gcode_button.setObjectName(u"gcode_button")
        font8 = QFont()
        font8.setFamily(u"Segoe UI Black")
        font8.setPointSize(20)
        self.gcode_button.setFont(font8)
        self.gcode_button.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(0, 143, 66);\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border-color: white;\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(0, 255, 119);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(0, 240, 112);\n"
"}")
        self.gcode_button.setCheckable(True)
        self.gcode_button.setChecked(True)
        self.gcode_button.setAutoExclusive(True)
        self.splitter.addWidget(self.gcode_button)
        self.isolate_button = QPushButton(self.splitter)
        self.isolate_button.setObjectName(u"isolate_button")
        self.isolate_button.setFont(font8)
        self.isolate_button.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(0, 240, 112);\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border-color: white;\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(0, 255, 119);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(0, 143, 66);\n"
"}")
        self.isolate_button.setCheckable(True)
        self.isolate_button.setAutoExclusive(True)
        self.splitter.addWidget(self.isolate_button)
        self.remove_button = QPushButton(self.splitter)
        self.remove_button.setObjectName(u"remove_button")
        self.remove_button.setFont(font8)
        self.remove_button.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(0, 240, 112);\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border-color: white;\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(0, 255, 119);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(0, 143, 66);\n"
"}")
        self.remove_button.setCheckable(True)
        self.remove_button.setAutoExclusive(True)
        self.splitter.addWidget(self.remove_button)
        self.soldermask_button = QPushButton(self.splitter)
        self.soldermask_button.setObjectName(u"soldermask_button")
        self.soldermask_button.setFont(font8)
        self.soldermask_button.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(0, 240, 112);\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border-color: white;\n"
"	color:rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(0, 255, 119);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(0, 143, 66);\n"
"}")
        self.soldermask_button.setCheckable(True)
        self.soldermask_button.setChecked(False)
        self.soldermask_button.setAutoExclusive(True)
        self.splitter.addWidget(self.soldermask_button)
        self.shutdown_button.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.browse_button.raise_()
        self.next_button.raise_()
        self.groupBox.raise_()
        self.label_3.raise_()
        self.directory_edit.raise_()
        self.splitter.raise_()
        self.advMenu.raise_()
        self.adv_label.raise_()
        self.advanced_button.raise_()

        self.verticalLayout.addWidget(self.DropShadowFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>SELECT THE EMPLOYED PINS:</p></body></html>", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.next_button.setText("")
        self.b2.setText(QCoreApplication.translate("MainWindow", u"B2", None))
        self.d2.setText(QCoreApplication.translate("MainWindow", u"D2", None))
        self.h2.setText(QCoreApplication.translate("MainWindow", u"H2", None))
        self.j2.setText(QCoreApplication.translate("MainWindow", u"J2", None))
        self.k2.setText(QCoreApplication.translate("MainWindow", u"K2", None))
        self.a2.setText(QCoreApplication.translate("MainWindow", u"A2", None))
        self.i2.setText(QCoreApplication.translate("MainWindow", u"I2", None))
        self.g2.setText(QCoreApplication.translate("MainWindow", u"G2", None))
        self.f2.setText(QCoreApplication.translate("MainWindow", u"F2", None))
        self.e2.setText(QCoreApplication.translate("MainWindow", u"E2", None))
        self.c2.setText(QCoreApplication.translate("MainWindow", u"C2", None))
        self.a7.setText(QCoreApplication.translate("MainWindow", u"A7", None))
        self.b7.setText(QCoreApplication.translate("MainWindow", u"B7", None))
        self.c7.setText(QCoreApplication.translate("MainWindow", u"C7", None))
        self.d7.setText(QCoreApplication.translate("MainWindow", u"D7", None))
        self.e7.setText(QCoreApplication.translate("MainWindow", u"E7", None))
        self.f7.setText(QCoreApplication.translate("MainWindow", u"F7", None))
        self.g7.setText(QCoreApplication.translate("MainWindow", u"G7", None))
        self.h7.setText(QCoreApplication.translate("MainWindow", u"H7", None))
        self.i7.setText(QCoreApplication.translate("MainWindow", u"I7", None))
        self.j7.setText(QCoreApplication.translate("MainWindow", u"J7", None))
        self.k7.setText(QCoreApplication.translate("MainWindow", u"K7", None))
        self.a3.setText(QCoreApplication.translate("MainWindow", u"A3", None))
        self.b3.setText(QCoreApplication.translate("MainWindow", u"B3", None))
        self.c3.setText(QCoreApplication.translate("MainWindow", u"C3", None))
        self.d3.setText(QCoreApplication.translate("MainWindow", u"D3", None))
        self.e3.setText(QCoreApplication.translate("MainWindow", u"E3", None))
        self.f3.setText(QCoreApplication.translate("MainWindow", u"F3", None))
        self.g3.setText(QCoreApplication.translate("MainWindow", u"G3", None))
        self.h3.setText(QCoreApplication.translate("MainWindow", u"H3", None))
        self.i3.setText(QCoreApplication.translate("MainWindow", u"I3", None))
        self.j3.setText(QCoreApplication.translate("MainWindow", u"J3", None))
        self.k3.setText(QCoreApplication.translate("MainWindow", u"K3", None))
        self.a1.setText(QCoreApplication.translate("MainWindow", u"A1", None))
        self.b1.setText(QCoreApplication.translate("MainWindow", u"B1", None))
        self.c1.setText(QCoreApplication.translate("MainWindow", u"C1", None))
        self.d1.setText(QCoreApplication.translate("MainWindow", u"D1", None))
        self.e1.setText(QCoreApplication.translate("MainWindow", u"E1", None))
        self.f1.setText(QCoreApplication.translate("MainWindow", u"F1", None))
        self.g1.setText(QCoreApplication.translate("MainWindow", u"G1", None))
        self.h1.setText(QCoreApplication.translate("MainWindow", u"H1", None))
        self.i1.setText(QCoreApplication.translate("MainWindow", u"I1", None))
        self.j1.setText(QCoreApplication.translate("MainWindow", u"J1", None))
        self.k1.setText(QCoreApplication.translate("MainWindow", u"K1", None))
        self.a0.setText(QCoreApplication.translate("MainWindow", u"A0", None))
        self.b0.setText(QCoreApplication.translate("MainWindow", u"B0", None))
        self.c0.setText(QCoreApplication.translate("MainWindow", u"C0", None))
        self.d0.setText(QCoreApplication.translate("MainWindow", u"D0", None))
        self.e0.setText(QCoreApplication.translate("MainWindow", u"E0", None))
        self.f0.setText(QCoreApplication.translate("MainWindow", u"F0", None))
        self.g0.setText(QCoreApplication.translate("MainWindow", u"G0", None))
        self.h0.setText(QCoreApplication.translate("MainWindow", u"H0", None))
        self.i0.setText(QCoreApplication.translate("MainWindow", u"I0", None))
        self.j0.setText(QCoreApplication.translate("MainWindow", u"J0", None))
        self.k0.setText(QCoreApplication.translate("MainWindow", u"K0", None))
        self.e6.setText(QCoreApplication.translate("MainWindow", u"E6", None))
        self.k6.setText(QCoreApplication.translate("MainWindow", u"K6", None))
        self.j6.setText(QCoreApplication.translate("MainWindow", u"J6", None))
        self.i6.setText(QCoreApplication.translate("MainWindow", u"I6", None))
        self.g6.setText(QCoreApplication.translate("MainWindow", u"G6", None))
        self.d6.setText(QCoreApplication.translate("MainWindow", u"D6", None))
        self.b6.setText(QCoreApplication.translate("MainWindow", u"B6", None))
        self.h6.setText(QCoreApplication.translate("MainWindow", u"H6", None))
        self.f6.setText(QCoreApplication.translate("MainWindow", u"F6", None))
        self.a6.setText(QCoreApplication.translate("MainWindow", u"A6", None))
        self.c6.setText(QCoreApplication.translate("MainWindow", u"C6", None))
        self.a5.setText(QCoreApplication.translate("MainWindow", u"A5", None))
        self.b5.setText(QCoreApplication.translate("MainWindow", u"B5", None))
        self.c5.setText(QCoreApplication.translate("MainWindow", u"C5", None))
        self.d5.setText(QCoreApplication.translate("MainWindow", u"D5", None))
        self.e5.setText(QCoreApplication.translate("MainWindow", u"E5", None))
        self.f5.setText(QCoreApplication.translate("MainWindow", u"F5", None))
        self.g5.setText(QCoreApplication.translate("MainWindow", u"G5", None))
        self.h5.setText(QCoreApplication.translate("MainWindow", u"H5", None))
        self.i5.setText(QCoreApplication.translate("MainWindow", u"I5", None))
        self.j5.setText(QCoreApplication.translate("MainWindow", u"J5", None))
        self.k5.setText(QCoreApplication.translate("MainWindow", u"K5", None))
        self.a4.setText(QCoreApplication.translate("MainWindow", u"A4", None))
        self.b4.setText(QCoreApplication.translate("MainWindow", u"B4", None))
        self.c4.setText(QCoreApplication.translate("MainWindow", u"C4", None))
        self.d4.setText(QCoreApplication.translate("MainWindow", u"D4", None))
        self.e4.setText(QCoreApplication.translate("MainWindow", u"E4", None))
        self.f4.setText(QCoreApplication.translate("MainWindow", u"F4", None))
        self.g4.setText(QCoreApplication.translate("MainWindow", u"G4", None))
        self.h4.setText(QCoreApplication.translate("MainWindow", u"H4", None))
        self.i4.setText(QCoreApplication.translate("MainWindow", u"I4", None))
        self.j4.setText(QCoreApplication.translate("MainWindow", u"J4", None))
        self.k4.setText(QCoreApplication.translate("MainWindow", u"K4", None))
        self.a8.setText(QCoreApplication.translate("MainWindow", u"A8", None))
        self.b8.setText(QCoreApplication.translate("MainWindow", u"B8", None))
        self.c8.setText(QCoreApplication.translate("MainWindow", u"C8", None))
        self.d8.setText(QCoreApplication.translate("MainWindow", u"D8", None))
        self.e8.setText(QCoreApplication.translate("MainWindow", u"E8", None))
        self.f8.setText(QCoreApplication.translate("MainWindow", u"F8", None))
        self.g8.setText(QCoreApplication.translate("MainWindow", u"G8", None))
        self.h8.setText(QCoreApplication.translate("MainWindow", u"H8", None))
        self.i8.setText(QCoreApplication.translate("MainWindow", u"I8", None))
        self.j8.setText(QCoreApplication.translate("MainWindow", u"J8", None))
        self.k8.setText(QCoreApplication.translate("MainWindow", u"K8", None))
        self.directory_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Courier'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.adv_label.setText("")
        self.root_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.default_check.setText(QCoreApplication.translate("MainWindow", u"Save as default", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Overlap [%]:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u" Pin Gap [mm]:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Feed Rate [mm/min]:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tool Diameter [mm]:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"PCB w. [mm]:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"#Passes(iso):", None))
        self.root_browse.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Courier'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Root directory</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Spin.S [rpm]: ", None))
        self.keep_check.setText(QCoreApplication.translate("MainWindow", u"Keep values for further files", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u" PCB h. [mm]:", None))
        self.advanced_button.setText(QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.shutdown_button.setText("")
        self.gcode_button.setText(QCoreApplication.translate("MainWindow", u"G-Code", None))
        self.isolate_button.setText(QCoreApplication.translate("MainWindow", u"Isolate", None))
        self.remove_button.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.soldermask_button.setText(QCoreApplication.translate("MainWindow", u"Mask", None))
    # retranslateUi

