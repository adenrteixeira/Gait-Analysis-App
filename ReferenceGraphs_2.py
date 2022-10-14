# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReferenceGraphs.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import os
from Warning import Ui_Dialog as Form

import pandas as pd
import numpy as np
import joblib
from tensorflow import keras

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1046, 536)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(300, 20, 228, 491))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 81, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(14, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.widget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_11.setObjectName("gridLayout_11")
        spacerItem2 = QtWidgets.QSpacerItem(20, 24, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem2, 2, 0, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.checkBox_10 = QtWidgets.QCheckBox(self.frame_5)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout_12.addWidget(self.checkBox_10, 3, 0, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.frame_5)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_12.addWidget(self.checkBox_7, 2, 0, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.frame_5)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_12.addWidget(self.checkBox_9, 1, 0, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.frame_5)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_12.addWidget(self.checkBox_6, 4, 0, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.frame_5)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout_12.addWidget(self.checkBox_8, 0, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_12, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_5)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_11.addWidget(self.label_15, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_5, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 81, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 2, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(540, 20, 481, 491))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setGeometry(QtCore.QRect(0, 30, 481, 421))
        self.widget_2.setObjectName("widget_2")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 450, 481, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 10, 481, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 20, 271, 491))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget2 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(40, 30, 175, 428))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_29 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_17.addWidget(self.label_29, 1, 1, 1, 1)
        self.horizontalSlider_5 = QtWidgets.QSlider(self.layoutWidget2)
        self.horizontalSlider_5.setMinimum(1)
        self.horizontalSlider_5.setMaximum(3)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.gridLayout_17.addWidget(self.horizontalSlider_5, 3, 1, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout_17.addWidget(self.label_30, 2, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.gridLayout_17.addWidget(self.label_31, 2, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.gridLayout_17.addWidget(self.label_32, 2, 2, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_17)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_6.setMaximumSize(QtCore.QSize(21, 21))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/Icon/information.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem9, 9, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_27 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_7.addWidget(self.label_27)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_7.addWidget(self.lineEdit_7)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setMaximumSize(QtCore.QSize(21, 21))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/Icon/information.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 10, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem10, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_36 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_9.addWidget(self.label_36)
        self.spinBox_2 = QtWidgets.QSpinBox(self.layoutWidget2)
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout_9.addWidget(self.spinBox_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_9)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_8.setMaximumSize(QtCore.QSize(21, 21))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/Icon/information.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_28 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_8.addWidget(self.label_28)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_8.addWidget(self.lineEdit_8)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_5.setMaximumSize(QtCore.QSize(21, 21))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/Icon/information.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 8, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem11, 3, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_33 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.gridLayout_18.addWidget(self.label_33, 2, 2, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.gridLayout_18.addWidget(self.label_34, 2, 0, 1, 1)
        self.horizontalSlider_6 = QtWidgets.QSlider(self.layoutWidget2)
        self.horizontalSlider_6.setMaximum(1)
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.gridLayout_18.addWidget(self.horizontalSlider_6, 2, 1, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_18.addWidget(self.label_35, 1, 1, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_18)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_7.setMaximumSize(QtCore.QSize(21, 21))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/Icon/information.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem12, 5, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem13, 7, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.label_38 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.gridLayout_19.addWidget(self.label_38, 2, 2, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.gridLayout_19.addWidget(self.label_39, 2, 0, 1, 1)
        self.horizontalSlider_7 = QtWidgets.QSlider(self.layoutWidget2)
        self.horizontalSlider_7.setMaximum(1)
        self.horizontalSlider_7.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_7.setObjectName("horizontalSlider_7")
        self.gridLayout_19.addWidget(self.horizontalSlider_7, 2, 1, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.label_40.setFont(font)
        self.label_40.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.gridLayout_19.addWidget(self.label_40, 1, 1, 1, 1)
        self.horizontalLayout_9.addLayout(self.gridLayout_19)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_10.setMaximumSize(QtCore.QSize(21, 21))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/Icon/information.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(100, 0, 62, 17))
        self.label_2.setObjectName("label_2")
        self.frame.raise_()
        self.frame_2.raise_()
        self.widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.alteracoes()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reference GAIT Graphs"))
        self.checkBox_10.setText(_translate("MainWindow", "MSVR"))
        self.checkBox_7.setText(_translate("MainWindow", "RELM"))
        self.checkBox_9.setText(_translate("MainWindow", "ELM"))
        self.checkBox_6.setText(_translate("MainWindow", "CNN"))
        self.checkBox_8.setText(_translate("MainWindow", "Linear Regression"))
        self.label_15.setText(_translate("MainWindow", "Algorithm"))
        self.pushButton.setText(_translate("MainWindow", "Generate"))
        self.label.setText(_translate("MainWindow", "Graphic"))
        self.label_29.setText(_translate("MainWindow", "Speed"))
        self.label_30.setText(_translate("MainWindow", "2"))
        self.label_31.setText(_translate("MainWindow", "1"))
        self.label_32.setText(_translate("MainWindow", "3"))
        self.label_27.setText(_translate("MainWindow", "Weight"))
        self.label_36.setText(_translate("MainWindow", "Age"))
        self.label_28.setText(_translate("MainWindow", "Height"))
        self.label_33.setText(_translate("MainWindow", "M"))
        self.label_34.setText(_translate("MainWindow", "F"))
        self.label_35.setText(_translate("MainWindow", "Gender"))
        self.label_38.setText(_translate("MainWindow", "R"))
        self.label_39.setText(_translate("MainWindow", "L"))
        self.label_40.setText(_translate("MainWindow", "Side of the foot"))
        self.label_2.setText(_translate("MainWindow", "Inputs"))

    def alteracoes(self):
        # Create canvas
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
 
        self.horizontalLayout_8.addWidget(self.canvas)
        ###########################################
        self.pushButton.clicked.connect(self.open_warning_dialog)

        self.lineEdit_8.setText("0")
        self.lineEdit_7.setText("0")

        self.label_10.setToolTip("Choose to see either right or left foot")
        self.label_10.setToolTipDuration(2147483647)

        self.label_8.setToolTip("For Males: [17 ; 78] \nFor Females: [15 ; 67]")
        self.label_8.setToolTipDuration(2147483647)

        self.label_6.setToolTip("slow 0.98 m/s, \nself-selected 1.27 m/s, \nand fast 1.55 m/s")
        self.label_6.setToolTipDuration(2147483647)

        self.label_7.setToolTip("Both left and right foot of the individual will be \n presented, choose only the gender")
        self.label_7.setToolTipDuration(2147483647)

        self.label_5.setToolTip("For Males: [163.0 ; 192.0] cm\n For Females: [152.0 ; 183.0] cm")
        self.label_5.setToolTipDuration(2147483647)

        self.label_4.setToolTip("For Males: [52.6 ; 143.2] kg \n For Females: [47.7 ; 108.1] kg")
        self.label_4.setToolTipDuration(2147483647)

    def check_values(self):
        self.BandeiraErro = 0
        # Lets see if the inputs that were given are numbers for Age
        if(self.horizontalSlider_6.value() == 0):          
            if(self.spinBox_2.value() > 67 | self.spinBox_2.value() < 15):
                self.BandeiraErro = 1

            # Lets see if the inputs that were given are numbers for Height
            try:
                aux = True
            except ValueError:
                aux = False
            if(aux == True):
                if(float(self.lineEdit_8.text()) > 183.0 or float(self.lineEdit_8.text()) < 152.0):
                    self.BandeiraErro = 1
            else:
                self.BandeiraErro = 1

            # Lets see if the inputs that were given are numbers for Body Mass
            try:
                float(self.lineEdit_7.text())
                aux = True
            except ValueError:
                aux = False
            if(aux == True):
                if(float(self.lineEdit_7.text()) > 108.1 or float(self.lineEdit_7.text()) < 47.7):
                    self.BandeiraErro = 1
            else:
                self.BandeiraErro = 1
        
        else:
            if(self.spinBox_2.value() > 78 | self.spinBox_2.value() < 17):
                self.BandeiraErro = 1
            # Lets see if the inputs that were given are numbers for Height
            try:
                float(self.lineEdit_8.text())
                aux = True
            except ValueError:
                aux = False
            if(aux == True):
                if(float(self.lineEdit_8.text()) > 192.0 or float(self.lineEdit_8.text()) < 163.0):
                    self.BandeiraErro = 1
            else:
                self.BandeiraErro = 1

            # Lets see if the inputs that were given are numbers for Height
            try:
                float(self.lineEdit_7.text())
                aux = True
            except ValueError:
                aux = False
            if(aux == True):
                if(float(self.lineEdit_7.text()) > 143.2 or float(self.lineEdit_7.text()) < 52.6):
                    self.BandeiraErro = 1
            else:
                self.BandeiraErro = 1

    def loadModels(self):
        self.figure.clear()

        if(self.horizontalSlider_6.value() == 0): # Is female
            if(self.horizontalSlider_7.value() == 0): # Its left foot 
                if(self.checkBox_8.isChecked()): # Linear 

                    LR_model_AP = joblib.load('Results/LR/LR_Female_AP_Left')
                    LR_model_ML = joblib.load('Results/LR/LR_Female_ML_Left')
                    LR_model_V = joblib.load('Results/LR/LR_Female_V_Left')

                    plt.plot(list(range(0,101)),LR_model_V.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Red", linestyle='-', marker ='p', markerfacecolor='black', label="LR V")
                    plt.plot(list(range(0,101)),LR_model_ML.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Red",linestyle='-', marker ='h', markerfacecolor='green', label="LR ML")
                    plt.plot(list(range(0,101)),LR_model_AP.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Red", linestyle='-', marker ='^', markerfacecolor='white', label="LR AP")
                    plt.legend()
                    self.canvas.draw()

                if(self.checkBox_9.isChecked()): # ELM

                    aux = pd.DataFrame(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1).flatten())
                    aux.to_csv("ForELMAndRELM_app.csv",index=False)

                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_FL_V.mat\',\'Results/ELM/RELM_FL_V.mat\');exit;\"")
                    ELMResult_FL_V = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_FL_V = pd.read_csv("ResultsRELMTeste.csv")
                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_FL_AP.mat\',\'Results/ELM/RELM_FL_AP.mat\');exit;\"")
                    ELMResult_FL_AP = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_FL_AP = pd.read_csv("ResultsRELMTeste.csv")
                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_FL_ML.mat\',\'Results/ELM/RELM_FL_ML.mat\');exit;\"")
                    ELMResult_FL_ML = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_FL_ML = pd.read_csv("ResultsRELMTeste.csv")
                    plt.plot(list(range(0,101)),ELMResult_FL_V.to_numpy().flatten(), color="Green", linestyle='-', marker ='p', markerfacecolor='black', label="ELM V")
                    plt.plot(list(range(0,101)),ELMResult_FL_ML.to_numpy().flatten(), color="Green",linestyle='-', marker ='h', markerfacecolor='green', label="ELM ML")
                    plt.plot(list(range(0,101)),ELMResult_FL_AP.to_numpy().flatten(), color="Green", linestyle='-', marker ='^', markerfacecolor='white', label="ELM AP")
                    plt.legend()
                    self.canvas.draw()

                if(self.checkBox_7.isChecked()): # RELM
                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_FL_V.mat\',\'Results/ELM/RELM_FL_V.mat\');exit;\"")
                    ELMResult_FL_V = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_FL_V = pd.read_csv("ResultsRELMTeste.csv")
                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_FL_AP.mat\',\'Results/ELM/RELM_FL_AP.mat\');exit;\"")
                    ELMResult_FL_AP = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_FL_AP = pd.read_csv("ResultsRELMTeste.csv")
                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_FL_ML.mat\',\'Results/ELM/RELM_FL_ML.mat\');exit;\"")
                    ELMResult_FL_ML = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_FL_ML = pd.read_csv("ResultsRELMTeste.csv")
                    plt.plot(list(range(0,101)),RELMResult_FL_V.to_numpy().flatten(), color="Blue", linestyle='-', marker ='p', markerfacecolor='black', label="RELM V")
                    plt.plot(list(range(0,101)),RELMResult_FL_ML.to_numpy().flatten(), color="Blue",linestyle='-', marker ='h', markerfacecolor='green', label="RELM ML")
                    plt.plot(list(range(0,101)),RELMResult_FL_AP.to_numpy().flatten(), color="Blue", linestyle='-', marker ='^', markerfacecolor='white', label="RELM AP")
                    plt.legend()
                    self.canvas.draw()

                if(self.checkBox_10.isChecked()): # MSVR
                    MSVR_model_AP = joblib.load('Results/MSVR_First_teste/MSVR_Female_AP_Left')
                    MSVR_model_ML = joblib.load('Results/MSVR_First_teste/MSVR_Female_ML_Left')
                    MSVR_model_V = joblib.load('Results/MSVR_First_teste/MSVR_Female_V_Left')

                    plt.plot(list(range(0,101)),MSVR_model_V.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Yellow", linestyle='-', marker ='p', markerfacecolor='black', label="MSVR V")
                    plt.plot(list(range(0,101)),MSVR_model_ML.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Yellow",linestyle='-', marker ='h', markerfacecolor='green', label="MSVR ML")
                    plt.plot(list(range(0,101)),MSVR_model_AP.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Yellow", linestyle='-', marker ='^', markerfacecolor='white', label="MSVR AP")
                    plt.legend()
                    self.canvas.draw()

                if(self.checkBox_6.isChecked()): # CNN
                    CNN_model_AP = keras.models.load_model('Results/CNN/CNN_Female_AP_Left')
                    CNN_model_ML = keras.models.load_model('Results/CNN/CNN_Female_ML_Left')
                    CNN_model_V = keras.models.load_model('Results/CNN/CNN_Female_V_Left')
                    
                    plt.plot(CNN_model_V.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Pink", linestyle='-', marker ='p', markerfacecolor='black', label="CNN V")
                    plt.plot(CNN_model_ML.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Pink",linestyle='-', marker ='h', markerfacecolor='green', label="CNN ML")
                    plt.plot(CNN_model_AP.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Pink", linestyle='-', marker ='^', markerfacecolor='white', label="CNN AP")
                    plt.legend()
                    self.canvas.draw()
                

            else: # Female Right foot

                if(self.checkBox_8.isChecked()): # Linear 

                    LR_model_AP = joblib.load('Results/LR/LR_Female_AP_Right')
                    LR_model_ML = joblib.load('Results/LR/LR_Female_ML_Right')
                    LR_model_V = joblib.load('Results/LR/LR_Female_V_Right')

                    plt.plot(list(range(0,101)),LR_model_V.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Red", linestyle='-', marker ='p', markerfacecolor='black', label="LR V")
                    plt.plot(list(range(0,101)),LR_model_ML.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Red",linestyle='-', marker ='h', markerfacecolor='green', label="LR ML")
                    plt.plot(list(range(0,101)),LR_model_AP.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Red", linestyle='-', marker ='^', markerfacecolor='white', label="LR AP")
                    plt.legend()
                    self.canvas.draw()

                if(self.checkBox_9.isChecked()): # ELM

                    aux = pd.DataFrame(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1).flatten())
                    aux.to_csv("ForELMAndRELM_app.csv",index=False)

                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_FR_V.mat\',\'Results/ELM/RELM_FR_V.mat\');exit;\"")
                    ELMResult_FR_V = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_FR_V = pd.read_csv("ResultsRELMTeste.csv")
                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_FR_AP.mat\',\'Results/ELM/RELM_FR_AP.mat\');exit;\"")
                    ELMResult_FR_AP = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_FR_AP = pd.read_csv("ResultsRELMTeste.csv")
                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_FR_ML.mat\',\'Results/ELM/RELM_FR_ML.mat\');exit;\"")
                    ELMResult_FR_ML = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_FR_ML = pd.read_csv("ResultsRELMTeste.csv")
                    plt.plot(list(range(0,101)),ELMResult_FR_V.to_numpy().flatten(), color="Green", linestyle='-', marker ='p', markerfacecolor='black', label="ELM V")
                    plt.plot(list(range(0,101)),ELMResult_FR_ML.to_numpy().flatten(), color="Green",linestyle='-', marker ='h', markerfacecolor='green', label="ELM ML")
                    plt.plot(list(range(0,101)),ELMResult_FR_AP.to_numpy().flatten(), color="Green", linestyle='-', marker ='^', markerfacecolor='white', label="ELM AP")
                    plt.legend()
                    self.canvas.draw()

                if(self.checkBox_7.isChecked()): # RELM
                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_FR_V.mat\',\'Results/ELM/RELM_FR_V.mat\');exit;\"")
                    ELMResult_FR_V = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_FR_V = pd.read_csv("ResultsRELMTeste.csv")
                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_FR_AP.mat\',\'Results/ELM/RELM_FR_AP.mat\');exit;\"")
                    ELMResult_FR_AP = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_FR_AP = pd.read_csv("ResultsRELMTeste.csv")
                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_FR_ML.mat\',\'Results/ELM/RELM_FR_ML.mat\');exit;\"")
                    ELMResult_FR_ML = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_FR_ML = pd.read_csv("ResultsRELMTeste.csv")
                    plt.plot(list(range(0,101)),RELMResult_FR_V.to_numpy().flatten(), color="Blue", linestyle='-', marker ='p', markerfacecolor='black', label="RELM V")
                    plt.plot(list(range(0,101)),RELMResult_FR_ML.to_numpy().flatten(), color="Blue",linestyle='-', marker ='h', markerfacecolor='green', label="RELM ML")
                    plt.plot(list(range(0,101)),RELMResult_FR_AP.to_numpy().flatten(), color="Blue", linestyle='-', marker ='^', markerfacecolor='white', label="RELM AP")
                    plt.legend()
                    self.canvas.draw()

                if(self.checkBox_10.isChecked()): # MSVR
                    MSVR_model_AP = joblib.load('Results/MSVR_First_teste/MSVR_Female_AP_Right')
                    MSVR_model_ML = joblib.load('Results/MSVR_First_teste/MSVR_Female_ML_Right')
                    MSVR_model_V = joblib.load('Results/MSVR_First_teste/MSVR_Female_V_Right')

                    plt.plot(list(range(0,101)),MSVR_model_V.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Yellow", linestyle='-', marker ='p', markerfacecolor='black', label="MSVR V")
                    plt.plot(list(range(0,101)),MSVR_model_ML.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Yellow",linestyle='-', marker ='h', markerfacecolor='green', label="MSVR ML")
                    plt.plot(list(range(0,101)),MSVR_model_AP.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Yellow", linestyle='-', marker ='^', markerfacecolor='white', label="MSVR AP")
                    plt.legend()
                    self.canvas.draw()

                if(self.checkBox_6.isChecked()): # CNN
                    CNN_model_AP = keras.models.load_model('Results/CNN/CNN_Female_AP_Right')
                    CNN_model_ML = keras.models.load_model('Results/CNN/CNN_Female_ML_Right')
                    CNN_model_V = keras.models.load_model('Results/CNN/CNN_Female_V_Right')
                    
                    plt.plot(CNN_model_V.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Pink", linestyle='-', marker ='p', markerfacecolor='black', label="CNN V")
                    plt.plot(CNN_model_ML.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Pink",linestyle='-', marker ='h', markerfacecolor='green', label="CNN ML")
                    plt.plot(CNN_model_AP.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Pink", linestyle='-', marker ='^', markerfacecolor='white', label="CNN AP")
                    plt.legend()
                    self.canvas.draw()

        else: # Its male
            if(self.horizontalSlider_7.value() == 0): # Its left foot 
                if(self.checkBox_8.isChecked()): # Linear 

                    LR_model_AP = joblib.load('Results/LR/LR_Male_AP_Left')
                    LR_model_ML = joblib.load('Results/LR/LR_Male_ML_Left')
                    LR_model_V = joblib.load('Results/LR/LR_Male_V_Left')

                    plt.plot(list(range(0,101)),LR_model_V.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Red", linestyle='-', marker ='p', markerfacecolor='black', label="LR V")
                    plt.plot(list(range(0,101)),LR_model_ML.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Red",linestyle='-', marker ='h', markerfacecolor='green', label="LR ML")
                    plt.plot(list(range(0,101)),LR_model_AP.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Red", linestyle='-', marker ='^', markerfacecolor='white', label="LR AP")
                    plt.legend()
                    self.canvas.draw()

                if(self.checkBox_9.isChecked()): # ELM

                    aux = pd.DataFrame(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1).flatten())
                    aux.to_csv("ForELMAndRELM_app.csv",index=False)

                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_ML_V.mat\',\'Results/ELM/RELM_ML_V.mat\');exit;\"")
                    ELMResult_ML_V = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_ML_V = pd.read_csv("ResultsRELMTeste.csv")
                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_ML_AP.mat\',\'Results/ELM/RELM_ML_AP.mat\');exit;\"")
                    ELMResult_ML_AP = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_ML_AP = pd.read_csv("ResultsRELMTeste.csv")
                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_ML_ML.mat\',\'Results/ELM/RELM_ML_ML.mat\');exit;\"")
                    ELMResult_ML_ML = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_ML_ML = pd.read_csv("ResultsRELMTeste.csv")
                    plt.plot(list(range(0,101)),ELMResult_ML_V.to_numpy().flatten(), color="Green", linestyle='-', marker ='p', markerfacecolor='black', label="ELM V")
                    plt.plot(list(range(0,101)),ELMResult_ML_ML.to_numpy().flatten(), color="Green",linestyle='-', marker ='h', markerfacecolor='green', label="ELM ML")
                    plt.plot(list(range(0,101)),ELMResult_ML_AP.to_numpy().flatten(), color="Green", linestyle='-', marker ='^', markerfacecolor='white', label="ELM AP")
                    plt.legend()
                    self.canvas.draw()

                if(self.checkBox_7.isChecked()): # RELM
                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_ML_V.mat\',\'Results/ELM/RELM_ML_V.mat\');exit;\"")
                    ELMResult_ML_V = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_ML_V = pd.read_csv("ResultsRELMTeste.csv")
                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_ML_AP.mat\',\'Results/ELM/RELM_ML_AP.mat\');exit;\"")
                    ELMResult_ML_AP = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_ML_AP = pd.read_csv("ResultsRELMTeste.csv")
                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_ML_ML.mat\',\'Results/ELM/RELM_ML_ML.mat\');exit;\"")
                    ELMResult_ML_ML = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_ML_ML = pd.read_csv("ResultsRELMTeste.csv")
                    plt.plot(list(range(0,101)),RELMResult_ML_V.to_numpy().flatten(), color="Blue", linestyle='-', marker ='p', markerfacecolor='black', label="RELM V")
                    plt.plot(list(range(0,101)),RELMResult_ML_ML.to_numpy().flatten(), color="Blue",linestyle='-', marker ='h', markerfacecolor='green', label="RELM ML")
                    plt.plot(list(range(0,101)),RELMResult_ML_AP.to_numpy().flatten(), color="Blue", linestyle='-', marker ='^', markerfacecolor='white', label="RELM AP")
                    plt.legend()
                    self.canvas.draw()

                if(self.checkBox_10.isChecked()): # MSVR
                    MSVR_model_AP = joblib.load('Results/MSVR_First_teste/MSVR_Male_AP_Left')
                    MSVR_model_ML = joblib.load('Results/MSVR_First_teste/MSVR_Male_ML_Left')
                    MSVR_model_V = joblib.load('Results/MSVR_First_teste/MSVR_Male_V_Left')

                    plt.plot(list(range(0,101)),MSVR_model_V.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Yellow", linestyle='-', marker ='p', markerfacecolor='black', label="MSVR V")
                    plt.plot(list(range(0,101)),MSVR_model_ML.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Yellow",linestyle='-', marker ='h', markerfacecolor='green', label="MSVR ML")
                    plt.plot(list(range(0,101)),MSVR_model_AP.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Yellow", linestyle='-', marker ='^', markerfacecolor='white', label="MSVR AP")
                    plt.legend()
                    self.canvas.draw()

                if(self.checkBox_6.isChecked()): # CNN
                    CNN_model_AP = keras.models.load_model('Results/CNN/CNN_Male_AP_Left')
                    CNN_model_ML = keras.models.load_model('Results/CNN/CNN_Male_ML_Left')
                    CNN_model_V = keras.models.load_model('Results/CNN/CNN_Male_V_Left')
                    
                    plt.plot(CNN_model_V.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Pink", linestyle='-', marker ='p', markerfacecolor='black', label="CNN V")
                    plt.plot(CNN_model_ML.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Pink",linestyle='-', marker ='h', markerfacecolor='green', label="CNN ML")
                    plt.plot(CNN_model_AP.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Pink", linestyle='-', marker ='^', markerfacecolor='white', label="CNN AP")
                    plt.legend()
                    self.canvas.draw()

            else: # Male Right foot

                if(self.checkBox_8.isChecked()): # Linear 

                    LR_model_AP = joblib.load('Results/LR/LR_Male_AP_Right')
                    LR_model_ML = joblib.load('Results/LR/LR_Male_ML_Right')
                    LR_model_V = joblib.load('Results/LR/LR_Male_V_Right')

                    plt.plot(list(range(0,101)),LR_model_V.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Red", linestyle='-', marker ='p', markerfacecolor='black', label="LR V")
                    plt.plot(list(range(0,101)),LR_model_ML.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Red",linestyle='-', marker ='h', markerfacecolor='green', label="LR ML")
                    plt.plot(list(range(0,101)),LR_model_AP.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Red", linestyle='-', marker ='^', markerfacecolor='white', label="LR AP")
                    plt.legend()
                    self.canvas.draw()

                if(self.checkBox_9.isChecked()): # ELM

                    aux = pd.DataFrame(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1).flatten())
                    aux.to_csv("ForELMAndRELM_app.csv",index=False)

                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_MR_V.mat\',\'Results/ELM/RELM_MR_V.mat\');exit;\"")
                    ELMResult_MR_V = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_MR_V = pd.read_csv("ResultsRELMTeste.csv")
                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_MR_AP.mat\',\'Results/ELM/RELM_MR_AP.mat\');exit;\"")
                    ELMResult_MR_AP = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_MR_AP = pd.read_csv("ResultsRELMTeste.csv")
                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_MR_ML.mat\',\'Results/ELM/RELM_MR_ML.mat\');exit;\"")
                    ELMResult_MR_ML = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_MR_ML = pd.read_csv("ResultsRELMTeste.csv")
                    plt.plot(list(range(0,101)),ELMResult_MR_V.to_numpy().flatten(), color="Green", linestyle='-', marker ='p', markerfacecolor='black', label="ELM V")
                    plt.plot(list(range(0,101)),ELMResult_MR_ML.to_numpy().flatten(), color="Green",linestyle='-', marker ='h', markerfacecolor='green', label="ELM ML")
                    plt.plot(list(range(0,101)),ELMResult_MR_AP.to_numpy().flatten(), color="Green", linestyle='-', marker ='^', markerfacecolor='white', label="ELM AP")
                    plt.legend()
                    self.canvas.draw()

                if(self.checkBox_7.isChecked()): # RELM
                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_FL_V.mat\',\'Results/ELM/RELM_FL_V.mat\');exit;\"")
                    ELMResult_MR_V = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_MR_V = pd.read_csv("ResultsRELMTeste.csv")
                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_FL_AP.mat\',\'Results/ELM/RELM_FL_AP.mat\');exit;\"")
                    ELMResult_MR_AP = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_MR_AP = pd.read_csv("ResultsRELMTeste.csv")
                    os.system("matlab -nodesktop -nosplash -r \"LoadELM_app(\'Results/ELM/ELM_FL_ML.mat\',\'Results/ELM/RELM_FL_ML.mat\');exit;\"")
                    ELMResult_MR_ML = pd.read_csv("ResultsELMTeste.csv")
                    RELMResult_MR_ML = pd.read_csv("ResultsRELMTeste.csv")
                    plt.plot(list(range(0,101)),RELMResult_MR_V.to_numpy().flatten(), color="Blue", linestyle='-', marker ='p', markerfacecolor='black', label="RELM V")
                    plt.plot(list(range(0,101)),RELMResult_MR_ML.to_numpy().flatten(), color="Blue",linestyle='-', marker ='h', markerfacecolor='green', label="RELM ML")
                    plt.plot(list(range(0,101)),RELMResult_MR_AP.to_numpy().flatten(), color="Blue", linestyle='-', marker ='^', markerfacecolor='white', label="RELM AP")
                    plt.legend()
                    self.canvas.draw()

                if(self.checkBox_10.isChecked()): # MSVR
                    MSVR_model_AP = joblib.load('Results/MSVR_First_teste/MSVR_Male_AP_Left')
                    MSVR_model_ML = joblib.load('Results/MSVR_First_teste/MSVR_Male_ML_Left')
                    MSVR_model_V = joblib.load('Results/MSVR_First_teste/MSVR_Male_V_Left')

                    plt.plot(list(range(0,101)),MSVR_model_V.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Yellow", linestyle='-', marker ='p', markerfacecolor='black', label="MSVR V")
                    plt.plot(list(range(0,101)),MSVR_model_ML.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Yellow",linestyle='-', marker ='h', markerfacecolor='green', label="MSVR ML")
                    plt.plot(list(range(0,101)),MSVR_model_AP.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Yellow", linestyle='-', marker ='^', markerfacecolor='white', label="MSVR AP")
                    plt.legend()
                    self.canvas.draw()

                if(self.checkBox_6.isChecked()): # CNN
                    CNN_model_AP = keras.models.load_model('Results/CNN/CNN_Male_AP_Left')
                    CNN_model_ML = keras.models.load_model('Results/CNN/CNN_Male_ML_Left')
                    CNN_model_V = keras.models.load_model('Results/CNN/CNN_Male_V_Left')
                    
                    plt.plot(CNN_model_V.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Pink", linestyle='-', marker ='p', markerfacecolor='black', label="CNN V")
                    plt.plot(CNN_model_ML.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Pink",linestyle='-', marker ='h', markerfacecolor='green', label="CNN ML")
                    plt.plot(CNN_model_AP.predict(np.array([self.spinBox_2.value(), self.horizontalSlider_5.value(), round(float(self.lineEdit_7.text()) / (float(self.lineEdit_8.text()) * float(self.lineEdit_8.text()) * 0.0001),1)]).reshape(1, -1)).flatten(), color="Pink", linestyle='-', marker ='^', markerfacecolor='white', label="CNN AP")
                    plt.legend()
                    self.canvas.draw()

                    
    def open_warning_dialog(self):
        self.check_values()

        if(self.BandeiraErro == 1):
            dialog = QtWidgets.QDialog()
            dialog.ui = Form()
            dialog.ui.setupUi(dialog)
            dialog.exec_()
            dialog.show()
        else:
            self.loadModels()
            print("waitng")


import Images_rc

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

import Images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
