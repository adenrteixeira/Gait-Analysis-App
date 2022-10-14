# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GlobalAnalyzis.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from unittest.util import strclass
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from Warning_2 import Ui_Dialog as Form
from Warning_3 import Ui_Dialog as Form2

import pandas as pd
import numpy as np
import os
from dtw import *
import statistics
import glob
import math
import FFT
from sklearn.linear_model import LinearRegression

class Ui_GlobalAnalyzis(object):
    def setupUi(self, GlobalAnalyzis,Idpp):
        self.Idpp = Idpp
        GlobalAnalyzis.setObjectName("GlobalAnalyzis")
        GlobalAnalyzis.resize(1303, 688)
        self.centralwidget = QtWidgets.QWidget(GlobalAnalyzis)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_3.setGeometry(QtCore.QRect(40, 80, 681, 571))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget_3.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_3.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_3.addTab(self.tab, "")
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(40, 20, 1221, 41))
        self.widget_5.setObjectName("widget_5")
        self.layoutWidget_2 = QtWidgets.QWidget(self.widget_5)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 0, 1211, 41))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_19.setScaledContents(True)
        self.label_19.setWordWrap(False)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_8.addWidget(self.label_19)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_8.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap(":/Icon/led_n_pre.png"))
        self.label_24.setScaledContents(False)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_8.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_8.addWidget(self.label_25)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_8.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_8.addWidget(self.label_27)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_8.addWidget(self.label_28)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_8.addWidget(self.label_29)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.widget_7 = QtWidgets.QWidget(self.centralwidget)
        self.widget_7.setGeometry(QtCore.QRect(760, 110, 501, 241))
        self.widget_7.setObjectName("widget_7")
        self.layoutWidget_4 = QtWidgets.QWidget(self.widget_7)
        self.layoutWidget_4.setGeometry(QtCore.QRect(0, 0, 501, 41))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem5)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_14.addWidget(self.label_32)
        self.label_33 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_33.setMaximumSize(QtCore.QSize(20, 20))
        self.label_33.setToolTipDuration(2147483647)
        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap(":/Icon/information.png"))
        self.label_33.setScaledContents(True)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_14.addWidget(self.label_33)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem6)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_14)
        self.treeWidget_4 = QtWidgets.QTreeWidget(self.widget_7)
        self.treeWidget_4.setGeometry(QtCore.QRect(0, 40, 501, 201))
        self.treeWidget_4.setObjectName("treeWidget_4")
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setGeometry(QtCore.QRect(760, 370, 501, 231))
        self.widget_6.setObjectName("widget_6")
        self.layoutWidget_3 = QtWidgets.QWidget(self.widget_6)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 0, 501, 41))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.label_30 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_12.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_31.setMaximumSize(QtCore.QSize(20, 20))
        self.label_31.setToolTipDuration(2147483647)
        self.label_31.setText("")
        self.label_31.setPixmap(QtGui.QPixmap(":/Icon/information.png"))
        self.label_31.setScaledContents(True)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_12.addWidget(self.label_31)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem8)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_12)
        self.treeWidget_3 = QtWidgets.QTreeWidget(self.widget_6)
        self.treeWidget_3.setGeometry(QtCore.QRect(0, 40, 501, 191))
        self.treeWidget_3.setObjectName("treeWidget_3")
        self.layoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_6.setGeometry(QtCore.QRect(760, 620, 501, 31))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem9)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget_6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_10.addWidget(self.pushButton_2)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem10)
        GlobalAnalyzis.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(GlobalAnalyzis)
        self.statusbar.setObjectName("statusbar")
        GlobalAnalyzis.setStatusBar(self.statusbar)

        self.retranslateUi(GlobalAnalyzis)
        self.tabWidget_3.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(GlobalAnalyzis)
        self.Uploadstuff()
        self.Change_Labels_And_Leds(self.Idpp)
        self.ChangesToGUI()
        self.DoDTW(self.Idpp)
        self.DoGE(self.Idpp)

    def retranslateUi(self, GlobalAnalyzis):
        _translate = QtCore.QCoreApplication.translate
        GlobalAnalyzis.setWindowTitle(_translate("GlobalAnalyzis", "Global Analyzis"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), _translate("GlobalAnalyzis", "Dtw(ML) vs SI"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), _translate("GlobalAnalyzis", "DTW(M) vs SI"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), _translate("GlobalAnalyzis", "GE(ML) vs SI"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab), _translate("GlobalAnalyzis", "GE(M) vs SI"))
        self.label_19.setText(_translate("GlobalAnalyzis", "<html><head/><body><p><img src=\":/Icon/led_pre.png\"/></p></body></html>"))
        self.label_23.setText(_translate("GlobalAnalyzis", "M"))
        self.label_25.setText(_translate("GlobalAnalyzis", "F"))
        self.label_26.setText(_translate("GlobalAnalyzis", "Class:"))
        self.label_27.setText(_translate("GlobalAnalyzis", "-"))
        self.label.setText(_translate("GlobalAnalyzis", "Affected Side: "))
        self.label_2.setText(_translate("GlobalAnalyzis", "-"))
        self.label_28.setText(_translate("GlobalAnalyzis", "# of Readmission:"))
        self.label_29.setText(_translate("GlobalAnalyzis", "00"))
        self.label_32.setText(_translate("GlobalAnalyzis", "Global Error (GE) and Symmetry (SI) evolution in function of sessions"))
        self.label_33.setToolTip(_translate("GlobalAnalyzis", "<html><head/><body><p>Here are presented the values of the GE and SI. 4 entrys for analyzing with machine learning reference and 4 entrys for analyzing with mean reference</p></body></html>"))
        self.treeWidget_4.headerItem().setText(0, _translate("GlobalAnalyzis", "Date"))
        self.treeWidget_4.headerItem().setText(1, _translate("GlobalAnalyzis", "Comment"))
        self.treeWidget_4.headerItem().setText(2, _translate("GlobalAnalyzis", "Side"))
        self.treeWidget_4.headerItem().setText(3, _translate("GlobalAnalyzis", "SI"))
        self.treeWidget_4.headerItem().setText(4, _translate("GlobalAnalyzis", "GE (ML)"))
        self.treeWidget_4.headerItem().setText(5, _translate("GlobalAnalyzis", "GE (M)"))
        self.label_30.setText(_translate("GlobalAnalyzis", "Parameters used in the Gait Error(GE) and Symmetry Index (SI) in function of sessions"))
        self.label_31.setToolTip(_translate("GlobalAnalyzis", "<html><head/><body><p>Parameters used in GE and the SI. 4 entrys for analyzing with machine learning reference and 4 entrys for analyzing with mean reference </p></body></html>"))
        self.treeWidget_3.headerItem().setText(0, _translate("GlobalAnalyzis", "Date"))
        self.treeWidget_3.headerItem().setText(1, _translate("GlobalAnalyzis", "Comment"))
        self.treeWidget_3.headerItem().setText(2, _translate("GlobalAnalyzis", "Side"))
        self.treeWidget_3.headerItem().setText(3, _translate("GlobalAnalyzis", "F(1)"))
        self.treeWidget_3.headerItem().setText(4, _translate("GlobalAnalyzis", "F(2)"))
        self.treeWidget_3.headerItem().setText(5, _translate("GlobalAnalyzis", "F(3)"))
        self.treeWidget_3.headerItem().setText(6, _translate("GlobalAnalyzis", "Loading Rate"))
        self.treeWidget_3.headerItem().setText(7, _translate("GlobalAnalyzis", "Push off Rate"))
        self.treeWidget_3.headerItem().setText(8, _translate("GlobalAnalyzis", "Area(density)"))
        self.treeWidget_3.headerItem().setText(9, _translate("GlobalAnalyzis", "Area(Derivative)"))
        self.treeWidget_3.headerItem().setText(10, _translate("GlobalAnalyzis", "SI"))
        self.treeWidget_3.headerItem().setText(11, _translate("GlobalAnalyzis", "GVS(ML)"))
        self.treeWidget_3.headerItem().setText(12, _translate("GlobalAnalyzis", "GVS(M)"))
        self.treeWidget_3.headerItem().setText(13, _translate("GlobalAnalyzis", "DTW(ML)"))
        self.treeWidget_3.headerItem().setText(14, _translate("GlobalAnalyzis", "DTW(M)"))
        self.pushButton_2.setText(_translate("GlobalAnalyzis", "Generate Report"))

    def Uploadstuff(self):
        # Left lower extremity
        self.GRF_F_V_PRO_left = pd.read_csv(r'../../GaitRec/GRF_F_V_PRO_left.csv')
        self.GRF_F_AP_PRO_left = pd.read_csv(r'../../GaitRec/GRF_F_AP_PRO_left.csv')
        self.GRF_F_ML_PRO_left = pd.read_csv(r'../../GaitRec/GRF_F_ML_PRO_left.csv')

        # Right lower extremity
        self.GRF_F_V_PRO_right = pd.read_csv(r'../../GaitRec/GRF_F_V_PRO_right.csv')
        self.GRF_F_AP_PRO_right = pd.read_csv(r'../../GaitRec/GRF_F_AP_PRO_right.csv')
        self.GRF_F_ML_PRO_right = pd.read_csv(r'../../GaitRec/GRF_F_ML_PRO_right.csv')

        # Annotations and Metadata
        self.GRF_Annotation = pd.read_csv(r'../../GaitRec/GRF_metadata.csv')

        self.df = self.GRF_Annotation[self.GRF_Annotation.CLASS_LABEL.values!="HC"]
        #self.df = self.GRF_Annotation[(self.GRF_Annotation.SPEED.values==2) &  (self.GRF_Annotation.SHOD_CONDITION==1)]
        # Just beacuse i dont want to change every line of code im going to constructed and aux variable to save information that i
        # though it wasnt necessary, but now i want it.
        self.auxInfo = self.df
        self.df = self.df.drop(['CLASS_LABEL_DETAILED', 'BODY_WEIGHT', 'SHOE_SIZE', 'ORTHOPEDIC_INSOLE', 'TRAIN', 'TRAIN_BALANCED', 'TEST', 'AFFECTED_SIDE', 'SHOD_CONDITION'],axis=1)
        self.df = self.df[(self.df.AGE.values < 78) & (self.df.AGE.values > 15) & (self.df.HEIGHT.values > 152.0) & (self.df.HEIGHT.values < 183.0) & (self.df.BODY_MASS.values > 47.7 ) & (self.df.BODY_MASS.values < 143.2)]
        self.auxInfo = self.auxInfo[(self.auxInfo.AGE.values < 78) & (self.auxInfo.AGE.values > 15) & (self.auxInfo.HEIGHT.values > 152.0) & (self.auxInfo.HEIGHT.values < 183.0) & (self.auxInfo.BODY_MASS.values > 47.7 ) & (self.auxInfo.BODY_MASS.values < 143.2)]
        self.df["BODY_MASS_INDEX"] = round(self.df["BODY_MASS"] / (self.df["HEIGHT"] * self.df["HEIGHT"] * 0.0001),1)
        self.auxInfo["BODY_MASS_INDEX"] = round(self.auxInfo["BODY_MASS"] / (self.auxInfo["HEIGHT"] * self.auxInfo["HEIGHT"] * 0.0001),1)
        self.df = self.df.drop(['HEIGHT','BODY_MASS'],axis=1)
        self.auxInfo = self.auxInfo.drop(['HEIGHT','BODY_MASS'],axis=1)
        self.df = self.df.reset_index(drop=True)
        self.auxInfo = self.auxInfo.reset_index(drop=True)
        self.ReferencialiterariaV = pd.read_csv("ReferenciaVLiteratura.csv",names=[*range(1,102)])
        self.ReferencialiterariaAP = pd.read_csv("ReferenciaAPLiteratura.csv",names=[*range(1,102)])

    def Change_Labels_And_Leds(self,Idpp):

        pp = self.df[self.df.SUBJECT_ID == int(Idpp)]
        auxpp = self.auxInfo[self.auxInfo.SUBJECT_ID == int(Idpp)]
        print(auxpp)
        if(str(pp.CLASS_LABEL.unique()[0]) == 'H'):
            self.label_27.setText('Hip')
        elif(str(pp.CLASS_LABEL.unique()[0]) == 'A'):
            self.label_27.setText('Ankle')
        elif(str(pp.CLASS_LABEL.unique()[0]) == 'C'):
            self.label_27.setText('Calcaneus')
        elif(str(pp.CLASS_LABEL.unique()[0]) == 'K'):
            self.label_27.setText('Knee')


        if(pp.SEX.unique()[0] == 1):
            self.label_19.setText("<html><head/><body><p><img src=\":/Icon/led_pre.png\"/></p></body></html>")
            self.label_24.setText("<html><head/><body><p><img src=\":/Icon/led_n_pre.png\"/></p></body></html>")
            self.gender = "male"
        else:
            self.label_19.setText("<html><head/><body><p><img src=\":/Icon/led_n_pre.png\"/></p></body></html>")
            self.label_24.setText("<html><head/><body><p><img src=\":/Icon/led_pre.png\"/></p></body></html>")
            self.gender = "female"
        
        # Altough we have only one value, this is way is just a cheat to get the value
        if(auxpp.AFFECTED_SIDE.unique().max()==2):
            side = 'both'
        elif(auxpp.AFFECTED_SIDE.unique().max()==1):
            side = 'right'
        else:
            side = 'left'
        
        self.label_2.setText(side)
        self.label_29.setText(str(pp.READMISSION.unique().max()))

    def ChangesToGUI(self):
        ## Canvas for graphs
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")

        self.figureDTWML = plt.figure()
        plt.title("DTW(ML) vs SI")
        self.canvasDTWML = FigureCanvas(self.figureDTWML)
        
        self.horizontalLayout_15.addWidget(self.canvasDTWML)

        #-----------------------------------------------------------------------------------

        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")

        self.figureDTWM = plt.figure()
        plt.title("DTW(M) vs SI")
        self.canvasDTWM = FigureCanvas(self.figureDTWM)
        
        self.horizontalLayout_16.addWidget(self.canvasDTWM)

        #-----------------------------------------------------------------------------------

        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")

        self.figureGEML = plt.figure()
        plt.title("GE(ML) vs SI")
        self.canvasGEML = FigureCanvas(self.figureGEML)
        
        self.horizontalLayout_17.addWidget(self.canvasGEML)

        #-----------------------------------------------------------------------------------

        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")

        self.figureGEM = plt.figure()
        plt.title("GE(M) vs SI")
        self.canvasGEM = FigureCanvas(self.figureGEM)
        
        self.horizontalLayout_18.addWidget(self.canvasGEM)

    def CalculateIS(self,arrLeft,arrRight):
        model = LinearRegression()
        model.fit(np.array(arrRight).reshape((-1, 1)),np.array(arrLeft)) # here the 2º argument was pandas dataframe, lets see if it works like this
        angulo = math.atan(model.coef_[0])
        ISPP = (angulo-(math.pi/4))*100/(0.5*(angulo+(math.pi/4)))
        return(ISPP)

    def ATN(self,value,media):
        """Adapat to normalize"""
        return(value/media)

    def CalculateDtw(self,Given,Reference):
        return(dtw(np.array(Given).flatten().tolist(),np.array(Reference).flatten().tolist()).distance)

    def ProduceELMRef(self,Given):
        """Here the parameter Given needs 
        to be panda dataframe!"""

        Given.to_csv('ForELMAndRELM_V.csv',index=False)
        os.system("matlab -nodesktop -nosplash -r \"LoadELM(\'V\',\'Results/ELM/ELM_MR_V.mat\',\'Results/ELM/RELM_MR_V.mat\');exit;\"")
        
        return(pd.read_csv("ResultsELMTeste.csv"))

    def calculateTaxas(self,arr,T1,T3):
        #Following the article between 10% and 90%
        loadingrate = arr[:T1]
        TenPindex = round(len(loadingrate)*0.10)
        NintyPindex = round(len(loadingrate)*0.90)
        LoadingRateSlop = (loadingrate[NintyPindex]-loadingrate[TenPindex])/(NintyPindex-TenPindex)

        pushoffrate = arr[T3:]
        TenPindex = round(len(pushoffrate)*0.10)
        NintyPindex = round(len(pushoffrate)*0.90)
        PushOffRateSlop = (pushoffrate[TenPindex]-pushoffrate[NintyPindex])/(TenPindex-NintyPindex)
        return(np.array([LoadingRateSlop,PushOffRateSlop]))

    def Calculate2Areas(self,arr):
        dft = np.real(FFT.FFT(arr,len(arr)))
        dft = dft[:round(len(dft)/2)] #so parte positiva
        #para fazer plot
        #freq = np.fft.fftfreq(len(arr))
        #freq = freq[:round(len(freq)/2)] #so parte positiva
        #plt.fill_between(freq,dft)
        area = 0
        for i in range(0,round(len(dft)/2)-1):
            area = area + (abs(dft[i]) + abs(dft[i+1]))/2 #(ver area de um trapézio, h=1 porque andamos de 1 em 1)
        #-----------------------------------------------------------------------------------------------------
        dx=1
        DerivadaForce = np.gradient(arr, dx)
        area2 = 0
        for i in range(0,101-1):
            area2 = area2 + (abs(DerivadaForce[i]) + abs(DerivadaForce[i+1]))/2 #(ver area de um trapézio, h=1 porque andamos de 1 em 1)
        #plt.fill_between(np.array(MaleVRight.iloc[1,6:]),DerivadaForce)
        return(round(area,2),round(area2,2))

    def CalculateGVS(self,Given,Reference):
        return(math.sqrt(np.mean(np.square(np.subtract(np.array(Given),np.array(Reference))))))

    def CalculateGE(self,arrLeft,arrRight,Sex,ReferenceR,ReferenceL,LReference,IS,Mean,date,Type):
        """
            GE is Gait error
        """
        # First we need to find the T1 and T3 for the left and right
        Times = pd.read_csv('T1T2T3.csv', names=['T1ML','T2ML','T3ML','T1MR','T2MR','T3MR','T1FL','T2FL','T3FL','T1FR','T2FR','T3FR'])

        leftParameteres = []
        rightParameteres = []
        leftReferenceParameteres = []
        rightReferenceParameteres = []

        AreasLeft = self.Calculate2Areas(arrLeft)
        AreasRight = self.Calculate2Areas(arrRight)

        RAreasLeft = self.Calculate2Areas(ReferenceL) # R before a variable means reference
        RAreasRight = self.Calculate2Areas(ReferenceR)

        GVSLeft = self.CalculateGVS(arrLeft,ReferenceL)
        GVSRight = self.CalculateGVS(arrRight,ReferenceR)

        LRefGVSLeft = self.CalculateGVS(ReferenceL,LReference)
        LRefGVSRight = self.CalculateGVS(ReferenceR,LReference)

        DtwLeft = self.CalculateDtw(arrLeft,ReferenceL)
        DtwRight = self.CalculateDtw(arrRight,ReferenceR)

        LRefDtwLeft = self.CalculateDtw(ReferenceL,LReference)
        LRefDtwRight = self.CalculateDtw(ReferenceR,LReference)

        # Second the forces
        if(Sex == 0):
            F1left = arrLeft[Times.loc[0,'T1ML']]
            F2left = arrLeft[Times.loc[0,'T2ML']]
            F3left = arrLeft[Times.loc[0,'T3ML']]

            F1right = arrRight[Times.loc[0,'T1MR']]
            F2right = arrRight[Times.loc[0,'T2MR']]
            F3right = arrRight[Times.loc[0,'T3MR']]

            RF1left = ReferenceL[Times.loc[0,'T1ML']]
            RF2left = ReferenceL[Times.loc[0,'T2ML']]
            RF3left = ReferenceL[Times.loc[0,'T3ML']]
            
            RF1right = ReferenceR[Times.loc[0,'T1MR']]
            RF2right = ReferenceR[Times.loc[0,'T2MR']]
            RF3right = ReferenceR[Times.loc[0,'T3MR']]

            TaxasML = self.calculateTaxas(arrLeft,Times.loc[0,'T1ML'],Times.loc[0,'T3ML'])
            TaxasMR = self.calculateTaxas(arrRight,Times.loc[0,'T1MR'],Times.loc[0,'T3MR'])

            RTaxasML = self.calculateTaxas(ReferenceL,Times.loc[0,'T1ML'],Times.loc[0,'T3ML'])
            RTaxasMR = self.calculateTaxas(ReferenceR,Times.loc[0,'T1MR'],Times.loc[0,'T3MR'])
            
            leftParameteres.append([F1left,F2left,F3left,TaxasML[0],TaxasML[1],AreasLeft[0],AreasLeft[1],GVSLeft,DtwLeft])
            rightParameteres.append([F1right,F2right,F3right,TaxasMR[0],TaxasMR[1],AreasRight[0],AreasRight[1],GVSRight,DtwRight])

            leftReferenceParameteres.append([RF1left,RF2left,RF3left,RTaxasML[0],RTaxasML[1],RAreasLeft[0],RAreasLeft[1],LRefGVSLeft,LRefDtwLeft])
            rightReferenceParameteres.append([RF1right,RF2right,RF3right,RTaxasMR[0],RTaxasMR[1],RAreasRight[0],RAreasRight[1],LRefGVSRight,LRefDtwRight])
            


        else:
            F1left = arrLeft[Times.loc[0,'T1FL']]
            F2left = arrLeft[Times.loc[0,'T2FL']]
            F3left = arrLeft[Times.loc[0,'T3FL']]

            F1right = arrRight[Times.loc[0,'T1FR']]
            F2right = arrRight[Times.loc[0,'T2FR']]
            F3right = arrRight[Times.loc[0,'T3FR']]

            RF1left = ReferenceL[Times.loc[0,'T1FL']]
            RF2left = ReferenceL[Times.loc[0,'T2FL']]
            RF3left = ReferenceL[Times.loc[0,'T3FL']]
            
            RF1right = ReferenceR[Times.loc[0,'T1FR']]
            RF2right = ReferenceR[Times.loc[0,'T2FR']]
            RF3right = ReferenceR[Times.loc[0,'T3FR']]

            TaxasFL = self.calculateTaxas(arrLeft,Times.loc[0,'T1FL'],Times.loc[0,'T3FL'])
            TaxasFR = self.calculateTaxas(arrRight,Times.loc[0,'T1FR'],Times.loc[0,'T3FR'])

            RTaxasFL = self.calculateTaxas(ReferenceL,Times.loc[0,'T1FL'],Times.loc[0,'T3FL'])
            RTaxasFR = self.calculateTaxas(ReferenceR,Times.loc[0,'T1FR'],Times.loc[0,'T3FR'])
            
            leftParameteres.append([F1left,F2left,F3left,TaxasFL[0],TaxasFL[1],AreasLeft[0],AreasLeft[1],GVSLeft,DtwLeft])
            rightParameteres.append([F1right,F2right,F3right,TaxasFR[0],TaxasFR[1],AreasRight[0],AreasRight[1],GVSRight,DtwRight])

            leftReferenceParameteres.append([RF1left,RF2left,RF3left,RTaxasFL[0],RTaxasFL[1],RAreasLeft[0],RAreasLeft[1],LRefGVSLeft,LRefDtwLeft])
            rightReferenceParameteres.append([RF1right,RF2right,RF3right,RTaxasFR[0],RTaxasFR[1],RAreasRight[0],RAreasRight[1],LRefGVSRight,LRefDtwRight])
        
        leftParameteres = np.array(leftParameteres).flatten()
        rightParameteres = np.array(rightParameteres).flatten()
        leftReferenceParameteres = np.array(leftReferenceParameteres).flatten()
        rightReferenceParameteres = np.array(rightReferenceParameteres).flatten()

        EMLeft = math.sqrt(math.sqrt(np.mean(np.square(np.divide(np.subtract(leftParameteres,leftReferenceParameteres),leftReferenceParameteres)))))
        EMRight = math.sqrt(math.sqrt(np.mean(np.square(np.divide(np.subtract(rightParameteres,rightReferenceParameteres),rightReferenceParameteres)))))


        if(Mean == 0):
            root = QtWidgets.QTreeWidgetItem([date, Type, 'Left', str(round(leftParameteres[0],3)), str(round(leftParameteres[1],3)), str(round(leftParameteres[2],3)), str(round(leftParameteres[3],3)), str(round(leftParameteres[4],3)), str(round(leftParameteres[5],3)),str(round(leftParameteres[6],3)),str(round(IS,3)),str(round(leftParameteres[7],3)),'-',str(round(leftParameteres[8],3)),'-'])
            self.treeWidget_3.addTopLevelItem(root)
            root = QtWidgets.QTreeWidgetItem([date, Type, 'Right', str(round(rightParameteres[0],3)), str(round(rightParameteres[1],3)), str(round(rightParameteres[2],3)), str(round(rightParameteres[3],3)), str(round(rightParameteres[4],3)), str(round(rightParameteres[5],3)),str(round(rightParameteres[6],3)),str(round(IS,3)),str(round(rightParameteres[7],3)),'-',str(round(rightParameteres[8],3)),'-'])
            self.treeWidget_3.addTopLevelItem(root)
            root = QtWidgets.QTreeWidgetItem([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '])
            self.treeWidget_3.addTopLevelItem(root)

            root = QtWidgets.QTreeWidgetItem([date, Type, 'Left', str(round(IS,3)), str(round(EMLeft,3)), '-'])
            self.treeWidget_4.addTopLevelItem(root)
            root = QtWidgets.QTreeWidgetItem([date, Type, 'Right', str(round(IS,3)), str(round(EMRight,3)), '-'])
            self.treeWidget_4.addTopLevelItem(root)
            root = QtWidgets.QTreeWidgetItem([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '])
            self.treeWidget_4.addTopLevelItem(root)



        else:
            root = QtWidgets.QTreeWidgetItem([date, Type, 'Left', str(round(leftParameteres[0],3)), str(round(leftParameteres[1],3)), str(round(leftParameteres[2],3)), str(round(leftParameteres[3],3)), str(round(leftParameteres[4],3)), str(round(leftParameteres[5],3)),str(round(leftParameteres[6],3)),str(round(IS,3)),'-',str(round(leftParameteres[7],3)),'-',str(round(leftParameteres[8],3))])
            self.treeWidget_3.addTopLevelItem(root)
            root = QtWidgets.QTreeWidgetItem([date, Type, 'Right', str(round(rightParameteres[0],3)), str(round(rightParameteres[1],3)), str(round(rightParameteres[2],3)), str(round(rightParameteres[3],3)), str(round(rightParameteres[4],3)), str(round(rightParameteres[5],3)),str(round(rightParameteres[6],3)),str(round(IS,3)),'-',str(round(rightParameteres[7],3)),'-',str(round(rightParameteres[8],3))])
            self.treeWidget_3.addTopLevelItem(root)
            root = QtWidgets.QTreeWidgetItem([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '])
            self.treeWidget_3.addTopLevelItem(root)

            root = QtWidgets.QTreeWidgetItem([date, Type, 'Left', str(round(IS,3)), '-', str(round(EMLeft,3))])
            self.treeWidget_4.addTopLevelItem(root)
            root = QtWidgets.QTreeWidgetItem([date, Type, 'Right', str(round(IS,3)), '-', str(round(EMRight,3))])
            self.treeWidget_4.addTopLevelItem(root)
            root = QtWidgets.QTreeWidgetItem([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '])
            self.treeWidget_4.addTopLevelItem(root)

        return(np.array([EMLeft,EMRight]))

    def DoDTW(self,Idpp):
        pp = self.df[self.df.SUBJECT_ID == int(Idpp)]
        
        path = "Patients/" + str(Idpp)

        cores = ['tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan','tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan']
        
        self.horizontalLayout_15.removeWidget(self.canvasDTWML)

        self.figureDTWML = plt.figure()
        plt.title("DTW(ML) vs SI")
        self.canvasDTWML = FigureCanvas(self.figureDTWML)
        
        self.horizontalLayout_15.addWidget(self.canvasDTWML)

        a = self.GRF_F_V_PRO_left.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)
        PP_VL = a.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)

        b = self.GRF_F_V_PRO_right.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)
        PP_VR = b.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)

        # MDTWML, MDTWMR, MDTWFL, MDTWFR, SDTWML, SDTWMR, SDTWFL, SDTWFR
        DtwLimits = np.loadtxt('DTWLimits.csv',delimiter=',')
        # MMN, MMP, MFN, MFP, SMN, SMP, SFN, SFP
        ISLimits = np.loadtxt('ISLimits.csv',delimiter=',')

        print(np.array(PP_VL.iloc[0,1:102]).flatten())

        ISPP_First = self.CalculateIS(np.array(PP_VL.iloc[0,1:102]).flatten(),np.array(PP_VR.iloc[0,1:102]).flatten())
        ISPP_Last = self.CalculateIS(np.array(PP_VL.iloc[PP_VL.shape[0]-1,1:102]).flatten(),np.array(PP_VR.iloc[PP_VR.shape[0]-1,1:102]).flatten()) # PP_VL.shape[0]returns the o numero de rows

        ELMResult_V_L = pd.read_csv(path+'/V_L_S2_'+'ResultsELMTeste.csv')
        ELMResult_V_R = pd.read_csv(path+'/V_R_S2_'+'ResultsELMTeste.csv')


        if(pp.SEX.unique()[0] == 0): # female
        
            distanceL_First_L = dtw(np.array(PP_VL.iloc[0,1:102]).flatten().tolist(),np.array(ELMResult_V_L).flatten().tolist()).distance
            distanceR_First_R = dtw(np.array(PP_VR.iloc[0,1:102]).flatten().tolist(),np.array(ELMResult_V_R).flatten().tolist()).distance
            distanceL_Last_L = dtw(np.array(PP_VL.iloc[PP_VL.shape[0]-1,1:102]).flatten().tolist(),np.array(ELMResult_V_L).flatten().tolist()).distance
            distanceR_Last_R = dtw(np.array(PP_VR.iloc[PP_VR.shape[0]-1,1:102]).flatten().tolist(),np.array(ELMResult_V_R).flatten().tolist()).distance

            plt.xlabel("Symetry index")
            plt.ylabel("DTW(ML)")
            plt.xlim([-10,10])
            plt.ylim([0,10])

            if(ISPP_First<0):
                Media = abs(ISLimits[2])

            else:
                Media = ISLimits[3]

            stdP = ISLimits[7] + ISLimits[7]
            stdN = ISLimits[6] + ISLimits[6]

            plt.plot([-1,-1,1,1], [0,1,1,0], color="black",linestyle='--', label="Limit box of healthy people (based on mean) (right & left)")
            plt.plot([-1+self.ATN(stdN,ISLimits[2]),-1+self.ATN(stdN,ISLimits[2]),1+self.ATN(stdP,ISLimits[3]),1+self.ATN(stdP,ISLimits[3])], [0,1+self.ATN(DtwLimits[6],DtwLimits[2]),1+self.ATN(DtwLimits[6],DtwLimits[2]),0], color="red",linestyle='-.', label="Limit box of healthy people (based on  2x Standart Dev (left))")
            plt.plot([-1+self.ATN(stdN,ISLimits[2]),-1+self.ATN(stdN,ISLimits[2]),1+self.ATN(stdP,ISLimits[3]),1+self.ATN(stdP,ISLimits[3])], [0,1+self.ATN(DtwLimits[7],DtwLimits[3]),1+self.ATN(DtwLimits[7],DtwLimits[3]),0], color="red",linestyle=':', label="Limit box of healthy people (based on  2x Standart Dev (right))")
            plt.scatter([self.ATN(ISPP_First,Media)], [self.ATN(distanceL_First_L,DtwLimits[2])],color='blue', marker="x",label="DTW(ML) First session left side")
            plt.scatter([self.ATN(ISPP_First,Media)], [self.ATN(distanceR_First_R,DtwLimits[3])],color='red', marker="x", label="DTW(ML) First session right side")
            
            if(ISPP_Last<0):
                Media = abs(ISLimits[2])

            else:
                Media = ISLimits[3]

            plt.scatter([self.ATN(ISPP_Last,Media)], [self.ATN(distanceL_Last_L,DtwLimits[2])],color='blue', marker="o",label="DTW(ML) Last session left side")
            plt.scatter([self.ATN(ISPP_Last,Media)], [self.ATN(distanceR_Last_R,DtwLimits[3])],color='red', marker="o", label="DTW(ML) Last session right side")

        else:
            
            distanceL_First_L = dtw(np.array(PP_VL.iloc[0,1:102]).flatten().tolist(),np.array(ELMResult_V_L).flatten().tolist()).distance
            distanceR_First_R = dtw(np.array(PP_VR.iloc[0,1:102]).flatten().tolist(),np.array(ELMResult_V_R).flatten().tolist()).distance
            distanceL_Last_L = dtw(np.array(PP_VL.iloc[PP_VL.shape[0]-1,1:102]).flatten().tolist(),np.array(ELMResult_V_L).flatten().tolist()).distance
            distanceR_Last_R = dtw(np.array(PP_VR.iloc[PP_VR.shape[0]-1,1:102]).flatten().tolist(),np.array(ELMResult_V_R).flatten().tolist()).distance

            plt.xlabel("Symetry index")
            plt.ylabel("DTW(ML)")
            plt.xlim([-10,10])
            plt.ylim([0,10])

            if(ISPP_First<0):
                Media = abs(ISLimits[0])

            else:
                Media = ISLimits[1]

            stdP = ISLimits[5] + ISLimits[5]
            stdN = ISLimits[4] + ISLimits[4]

            plt.plot([-1,-1,1,1], [0,1,1,0], color="black",linestyle='--', label="Limit box of healthy people (based on mean) (right & left)")
            plt.plot([-1+self.ATN(stdN,ISLimits[0]),-1+self.ATN(stdN,ISLimits[0]),1+self.ATN(stdP,ISLimits[1]),1+self.ATN(stdP,ISLimits[1])], [0,1+self.ATN(DtwLimits[4],DtwLimits[0]),1+self.ATN(DtwLimits[4],DtwLimits[0]),0], color="red",linestyle='-.', label="Limit box of healthy people (based on  2x Standart Dev (left))")
            plt.plot([-1+self.ATN(stdN,ISLimits[0]),-1+self.ATN(stdN,ISLimits[0]),1+self.ATN(stdP,ISLimits[1]),1+self.ATN(stdP,ISLimits[1])], [0,1+self.ATN(DtwLimits[5],DtwLimits[1]),1+self.ATN(DtwLimits[5],DtwLimits[1]),0], color="red",linestyle=':', label="Limit box of healthy people (based on  2x Standart Dev (right))")
            plt.scatter([self.ATN(ISPP_First,Media)], [self.ATN(distanceL_First_L,DtwLimits[0])],color='blue',marker="x",label="DTW(ML) First session left side")
            plt.scatter([self.ATN(ISPP_First,Media)], [self.ATN(distanceR_First_R,DtwLimits[1])],color='red',marker="x",label="DTW(ML) First session right side")
            
            if(ISPP_Last<0):
                Media = abs(ISLimits[0])

            else:
                Media = ISLimits[1]
            
            plt.scatter([self.ATN(ISPP_Last,Media)], [self.ATN(distanceL_Last_L,DtwLimits[0])],color='blue',marker="o",label="DTW(ML) Last session left side")
            plt.scatter([self.ATN(ISPP_Last,Media)], [self.ATN(distanceR_Last_R,DtwLimits[1])],color='red',marker="o",label="DTW(ML) Last session right side")

        plt.legend()

    # Vamos fazer agora o grafico da media!

        self.horizontalLayout_16.removeWidget(self.canvasDTWM)

        self.figureDTWM = plt.figure()
        plt.title("DTW(M) vs SI")
        self.canvasDTWM = FigureCanvas(self.figureDTWM)
        
        self.horizontalLayout_16.addWidget(self.canvasDTWM)


        if(pp.SEX.unique()[0] == 0): # female
        
            FemaleLeftMean = pd.read_csv("HFemaleVMeanLeft.csv")
            FemaleRightMean = pd.read_csv("HFemaleVMeanRight.csv")

            distanceL_First_L = dtw(np.array(PP_VL.iloc[0,1:102]).flatten().tolist(),np.array(FemaleLeftMean).flatten().tolist()).distance
            distanceR_First_R = dtw(np.array(PP_VR.iloc[0,1:102]).flatten().tolist(),np.array(FemaleRightMean).flatten().tolist()).distance
            distanceL_Last_L = dtw(np.array(PP_VL.iloc[PP_VL.shape[0]-1,1:102]).flatten().tolist(),np.array(FemaleLeftMean).flatten().tolist()).distance
            distanceR_Last_R = dtw(np.array(PP_VR.iloc[PP_VR.shape[0]-1,1:102]).flatten().tolist(),np.array(FemaleRightMean).flatten().tolist()).distance

            plt.xlabel("Symetry index")
            plt.ylabel("DTW(M)")
            plt.xlim([-10,10])
            plt.ylim([0,10])

            if(ISPP_First<0):
                Media = abs(ISLimits[2])

            else:
                Media = ISLimits[3]

            stdP = ISLimits[7] + ISLimits[7]
            stdN = ISLimits[6] + ISLimits[6]

            plt.plot([-1,-1,1,1], [0,1,1,0], color="black",linestyle='--', label="Limit box of healthy people (based on mean) (right & left)")
            plt.plot([-1+self.ATN(stdN,ISLimits[2]),-1+self.ATN(stdN,ISLimits[2]),1+self.ATN(stdP,ISLimits[3]),1+self.ATN(stdP,ISLimits[3])], [0,1+self.ATN(DtwLimits[6],DtwLimits[2]),1+self.ATN(DtwLimits[6],DtwLimits[2]),0], color="red",linestyle='-.', label="Limit box of healthy people (based on 2x Standart Dev (left))")
            plt.plot([-1+self.ATN(stdN,ISLimits[2]),-1+self.ATN(stdN,ISLimits[2]),1+self.ATN(stdP,ISLimits[3]),1+self.ATN(stdP,ISLimits[3])], [0,1+self.ATN(DtwLimits[7],DtwLimits[3]),1+self.ATN(DtwLimits[7],DtwLimits[3]),0], color="red",linestyle=':', label="Limit box of healthy people (based on 2x Standart Dev (right))")
            plt.scatter([self.ATN(ISPP_First,Media)], [self.ATN(distanceL_First_L,DtwLimits[2])],color='blue', marker="x",label="DTW(ML) First session left side")
            plt.scatter([self.ATN(ISPP_First,Media)], [self.ATN(distanceR_First_R,DtwLimits[3])],color='red', marker="x", label="DTW(ML) First session right side")

            if(ISPP_Last<0):
                Media = abs(ISLimits[2])

            else:
                Media = ISLimits[3]

            plt.scatter([self.ATN(ISPP_Last,Media)], [self.ATN(distanceL_Last_L,DtwLimits[2])],color='blue', marker="o",label="DTW(ML) Last session left side")
            plt.scatter([self.ATN(ISPP_Last,Media)], [self.ATN(distanceR_Last_R,DtwLimits[3])],color='red', marker="o", label="DTW(ML) Last session right side")

        else:

            MaleLeftMean = pd.read_csv("HMaleVMeanLeft.csv")
            MaleRightMean = pd.read_csv("HMaleVMeanRight.csv")
            
            distanceL_First_L = dtw(np.array(PP_VL.iloc[0,1:102]).flatten().tolist(),np.array(MaleLeftMean).flatten().tolist()).distance
            distanceR_First_R = dtw(np.array(PP_VR.iloc[0,1:102]).flatten().tolist(),np.array(MaleRightMean).flatten().tolist()).distance
            distanceL_Last_L = dtw(np.array(PP_VL.iloc[PP_VL.shape[0]-1,1:102]).flatten().tolist(),np.array(MaleLeftMean).flatten().tolist()).distance
            distanceR_Last_R = dtw(np.array(PP_VR.iloc[PP_VR.shape[0]-1,1:102]).flatten().tolist(),np.array(MaleRightMean).flatten().tolist()).distance

            plt.xlabel("Symetry index")
            plt.ylabel("DTW(M)")
            plt.xlim([-10,10])
            plt.ylim([0,10])

            if(ISPP_First<0):
                Media = ISLimits[0]

            else:
                Media = ISLimits[1]

            stdP = ISLimits[5] + ISLimits[5]
            stdN = ISLimits[4] + ISLimits[4]

            plt.plot([-1,-1,1,1], [0,1,1,0], color="black",linestyle='--', label="Limit box of healthy people (based on mean) (right & left)")
            plt.plot([-1+self.ATN(stdN,ISLimits[0]),-1+self.ATN(stdN,ISLimits[0]),1+self.ATN(stdP,ISLimits[1]),1+self.ATN(stdP,ISLimits[1])], [0,1+self.ATN(DtwLimits[4],DtwLimits[0]),1+self.ATN(DtwLimits[4],DtwLimits[0]),0], color="red",linestyle='-.', label="Limit box of healthy people (based on  2x Standart Dev (left))")
            plt.plot([-1+self.ATN(stdN,ISLimits[0]),-1+self.ATN(stdN,ISLimits[0]),1+self.ATN(stdP,ISLimits[1]),1+self.ATN(stdP,ISLimits[1])], [0,1+self.ATN(DtwLimits[5],DtwLimits[1]),1+self.ATN(DtwLimits[5],DtwLimits[1]),0], color="red",linestyle=':', label="Limit box of healthy people (based on  2x Standart Dev (right))")
            plt.scatter([self.ATN(ISPP_First,Media)], [self.ATN(distanceL_First_L,DtwLimits[0])],color='blue',marker="x",label="DTW(ML) First session left side")
            plt.scatter([self.ATN(ISPP_First,Media)], [self.ATN(distanceR_First_R,DtwLimits[1])],color='red',marker="x",label="DTW(ML) First session right side")

            if(ISPP_Last<0):
                Media = abs(ISLimits[0])

            else:
                Media = ISLimits[1]
            
            plt.scatter([self.ATN(ISPP_Last,Media)], [self.ATN(distanceL_Last_L,DtwLimits[0])],color='blue',marker="o",label="DTW(ML) Last session left side")
            plt.scatter([self.ATN(ISPP_Last,Media)], [self.ATN(distanceR_Last_R,DtwLimits[1])],color='red',marker="o",label="DTW(ML) Last session right side")

        plt.legend()

    def DoGE(self,Idpp):
        pp = self.df[self.df.SUBJECT_ID == int(Idpp)]
        
        path = "Patients/" + str(Idpp)

        cores = ['tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan','tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan']
        
        self.horizontalLayout_17.removeWidget(self.canvasGEML)

        self.figureGEML = plt.figure()
        plt.title("GE(ML) vs SI")
        self.canvasGEML = FigureCanvas(self.figureGEML)
        
        self.horizontalLayout_17.addWidget(self.canvasGEML)

        a = self.GRF_F_V_PRO_left.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)
        PP_VL = a.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)

        b = self.GRF_F_V_PRO_right.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)
        PP_VR = b.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)

        # MMN, MMP, MFN, MFP, SMN, SMP, SFN, SFP
        ISLimits = np.loadtxt('ISLimits.csv',delimiter=',')
        # GEMLM, GEMRM, GEFLM, GEFRM, GEMLSTD, GEMRSTD, GEFLSTD, GEFRSTD
        GELimits = np.loadtxt('GELimits.csv',delimiter=',')

        print(np.array(PP_VL.iloc[0,1:102]).flatten())

        ISPP_First = self.CalculateIS(np.array(PP_VL.iloc[0,1:102]).flatten(),np.array(PP_VR.iloc[0,1:102]).flatten())
        ISPP_Last = self.CalculateIS(np.array(PP_VL.iloc[PP_VL.shape[0]-1,1:102]).flatten(),np.array(PP_VR.iloc[PP_VR.shape[0]-1,1:102]).flatten()) # PP_VL.shape[0]returns the o numero de rows

        ELMResult_V_L = pd.read_csv(path+'/V_L_S2_'+'ResultsELMTeste.csv')
        ELMResult_V_R = pd.read_csv(path+'/V_R_S2_'+'ResultsELMTeste.csv')

        if(pp.SEX.unique()[0] == 0): # female
        
            GE_First = self.CalculateGE(np.array(PP_VL.iloc[0,1:102]).flatten().tolist(),np.array(PP_VR.iloc[0,1:102]).flatten().tolist(),1,np.array(ELMResult_V_R).flatten(),np.array(ELMResult_V_L).flatten(),np.array(self.ReferencialiterariaV),ISPP_First,0,str(pp.iloc[0,8]),'First Session')            
            GE_Last = self.CalculateGE(np.array(PP_VL.iloc[PP_VL.shape[0]-1,1:102]).flatten().tolist(),np.array(PP_VR.iloc[PP_VR.shape[0]-1,1:102]).flatten().tolist(),1,np.array(ELMResult_V_R).flatten(),np.array(ELMResult_V_L).flatten(),np.array(self.ReferencialiterariaV),ISPP_Last,0,str(pp.iloc[-1,8]),'Last Session')

            plt.xlabel("Symetry index")
            plt.ylabel("GE(ML)")
            plt.xlim([-10,10])
            plt.ylim([0,10])

            if(ISPP_First<0):
                Media = abs(ISLimits[2])

            else:
                Media = ISLimits[3]

            stdP = ISLimits[7] + ISLimits[7]
            stdN = ISLimits[6] + ISLimits[6]

            plt.plot([-1,-1,1,1], [0,1,1,0], color="black",linestyle='--', label="Limit box of healthy people (based on mean) (right & left)")
            plt.plot([-1+self.ATN(stdN,ISLimits[2]),-1+self.ATN(stdN,ISLimits[2]),1+self.ATN(stdP,ISLimits[3]),1+self.ATN(stdP,ISLimits[3])], [0,1+self.ATN(GELimits[6],GELimits[2]),1+self.ATN(GELimits[6],GELimits[2]),0], color="red",linestyle='-.', label="Limit box of healthy people (based on  2x Standart Dev (left))")
            plt.plot([-1+self.ATN(stdN,ISLimits[2]),-1+self.ATN(stdN,ISLimits[2]),1+self.ATN(stdP,ISLimits[3]),1+self.ATN(stdP,ISLimits[3])], [0,1+self.ATN(GELimits[7],GELimits[3]),1+self.ATN(GELimits[7],GELimits[3]),0], color="red",linestyle=':', label="Limit box of healthy people (based on  2x Standart Dev (right))")
            plt.scatter([self.ATN(ISPP_First,Media)], [self.ATN(GE_First[0],GELimits[2])],color='blue', marker="x",label="GE(ML) First session left side")
            plt.scatter([self.ATN(ISPP_First,Media)], [self.ATN(GE_First[1],GELimits[3])],color='red', marker="x", label="GE(ML) First session right side")
            
            if(ISPP_Last<0):
                Media = abs(ISLimits[2])

            else:
                Media = ISLimits[3]
            
            plt.scatter([self.ATN(ISPP_Last,Media)], [self.ATN(GE_Last[0],GELimits[2])],color='blue', marker="o",label="GE(ML) Last session left side")
            plt.scatter([self.ATN(ISPP_Last,Media)], [self.ATN(GE_Last[1],GELimits[3])],color='red', marker="o", label="GE(ML) Last session right side")

        else:
            
            GE_First = self.CalculateGE(np.array(PP_VL.iloc[0,1:102]).flatten().tolist(),np.array(PP_VR.iloc[0,1:102]).flatten().tolist(),0,np.array(ELMResult_V_R).flatten(),np.array(ELMResult_V_L).flatten(),np.array(self.ReferencialiterariaV),ISPP_First,0,str(pp.iloc[0,8]),'First Session')
            GE_Last = self.CalculateGE(np.array(PP_VL.iloc[PP_VL.shape[0]-1,1:102]).flatten().tolist(),np.array(PP_VR.iloc[PP_VR.shape[0]-1,1:102]).flatten().tolist(),0,np.array(ELMResult_V_R).flatten(),np.array(ELMResult_V_L).flatten(),np.array(self.ReferencialiterariaV),ISPP_Last,0,str(pp.iloc[-1,8]),'Last Session')

            plt.xlabel("Symetry index")
            plt.ylabel("GE(ML)")
            plt.xlim([-10,10])
            plt.ylim([0,10])

            if(ISPP_First<0):
                Media = abs(ISLimits[0])

            else:
                Media = ISLimits[1]

            stdP = ISLimits[5] + ISLimits[5]
            stdN = ISLimits[4] + ISLimits[4]

            plt.plot([-1,-1,1,1], [0,1,1,0], color="black",linestyle='--', label="Limit box of healthy people (based on mean) (right & left)")
            plt.plot([-1+self.ATN(stdN,ISLimits[0]),-1+self.ATN(stdN,ISLimits[0]),1+self.ATN(stdP,ISLimits[1]),1+self.ATN(stdP,ISLimits[1])], [0,1+self.ATN(GELimits[4],GELimits[0]),1+self.ATN(GELimits[4],GELimits[0]),0], color="red",linestyle='-.', label="Limit box of healthy people (based on  2x Standart Dev (left))")
            plt.plot([-1+self.ATN(stdN,ISLimits[0]),-1+self.ATN(stdN,ISLimits[0]),1+self.ATN(stdP,ISLimits[1]),1+self.ATN(stdP,ISLimits[1])], [0,1+self.ATN(GELimits[5],GELimits[1]),1+self.ATN(GELimits[5],GELimits[1]),0], color="red",linestyle=':', label="Limit box of healthy people (based on  2x Standart Dev (right))")
            plt.scatter([self.ATN(ISPP_First,Media)], [self.ATN(GE_First[0],GELimits[0])],color='blue',marker="x",label="GE(ML) First session left side")
            plt.scatter([self.ATN(ISPP_First,Media)], [self.ATN(GE_First[1],GELimits[1])],color='red',marker="x",label="GE(ML) First session right side")
            
            if(ISPP_Last<0):
                Media  = abs(ISLimits[0])

            else:
                Media = ISLimits[1]
            
            plt.scatter([self.ATN(ISPP_Last,Media)], [self.ATN(GE_Last[0],GELimits[0])],color='blue',marker="o",label="GE(ML) Last session left side")
            plt.scatter([self.ATN(ISPP_Last,Media)], [self.ATN(GE_Last[1],GELimits[1])],color='red',marker="o",label="GE(ML) Last session right side")
            print()
        plt.legend()

    # Vamos fazer agora o grafico da media!

        self.horizontalLayout_18.removeWidget(self.canvasGEM)

        self.figureGEM = plt.figure()
        plt.title("GE(M) vs SI")
        self.canvasGEM = FigureCanvas(self.figureGEM)
        
        self.horizontalLayout_18.addWidget(self.canvasGEM)


        if(pp.SEX.unique()[0] == 0): # female
        
            FemaleLeftMean = pd.read_csv("HFemaleVMeanLeft.csv")
            FemaleRightMean = pd.read_csv("HFemaleVMeanRight.csv")

            GE_First = self.CalculateGE(np.array(PP_VL.iloc[0,1:102]).flatten().tolist(),np.array(PP_VR.iloc[0,1:102]).flatten().tolist(),1,np.array(FemaleRightMean).flatten(),np.array(FemaleLeftMean).flatten(),np.array(self.ReferencialiterariaV),ISPP_First,1,str(pp.iloc[0,8]),'First Session')
            GE_Last = self.CalculateGE(np.array(PP_VL.iloc[PP_VL.shape[0]-1,1:102]).flatten().tolist(),np.array(PP_VR.iloc[PP_VR.shape[0]-1,1:102]).flatten().tolist(),1,np.array(FemaleRightMean).flatten(),np.array(FemaleLeftMean).flatten(),np.array(self.ReferencialiterariaV),ISPP_Last,1,str(pp.iloc[-1,8]),'Last Session')

            plt.xlabel("Symetry index")
            plt.ylabel("GE(ML)")
            plt.xlim([-10,10])
            plt.ylim([0,10])

            if(ISPP_First<0):
                Media = abs(ISLimits[2])

            else:
                Media = ISLimits[3]

            stdP = ISLimits[7] + ISLimits[7]
            stdN = ISLimits[6] + ISLimits[6]

            plt.plot([-1,-1,1,1], [0,1,1,0], color="black",linestyle='--', label="Limit box of healthy people (based on mean) (right & left)")
            plt.plot([-1+self.ATN(stdN,ISLimits[2]),-1+self.ATN(stdN,ISLimits[2]),1+self.ATN(stdP,ISLimits[3]),1+self.ATN(stdP,ISLimits[3])], [0,1+self.ATN(GELimits[6],GELimits[2]),1+self.ATN(GELimits[6],GELimits[2]),0], color="red",linestyle='-.', label="Limit box of healthy people (based on  2x Standart Dev (left))")
            plt.plot([-1+self.ATN(stdN,ISLimits[2]),-1+self.ATN(stdN,ISLimits[2]),1+self.ATN(stdP,ISLimits[3]),1+self.ATN(stdP,ISLimits[3])], [0,1+self.ATN(GELimits[7],GELimits[3]),1+self.ATN(GELimits[7],GELimits[3]),0], color="red",linestyle=':', label="Limit box of healthy people (based on  2x Standart Dev (right))")
            plt.scatter([self.ATN(ISPP_First,Media)], [self.ATN(GE_First[0],GELimits[2])],color='blue', marker="x",label="GE(ML) First session left side")
            plt.scatter([self.ATN(ISPP_First,Media)], [self.ATN(GE_First[1],GELimits[3])],color='red', marker="x", label="GE(ML) First session right side")
            
            if(ISPP_Last<0):
                Media = abs(ISLimits[2])

            else:
                Media = ISLimits[3]
            
            plt.scatter([self.ATN(ISPP_Last,Media)], [self.ATN(GE_Last[0],GELimits[2])],color='blue', marker="o",label="GE(ML) Last session left side")
            plt.scatter([self.ATN(ISPP_Last,Media)], [self.ATN(GE_Last[1],GELimits[3])],color='red', marker="o", label="GE(ML) Last session right side")

        else:
            
            MaleLeftMean = pd.read_csv("HMaleVMeanLeft.csv")
            MaleRightMean = pd.read_csv("HMaleVMeanRight.csv")

            GE_First = self.CalculateGE(np.array(PP_VL.iloc[0,1:102]).flatten().tolist(),np.array(PP_VR.iloc[0,1:102]).flatten().tolist(),0,np.array(MaleRightMean).flatten(),np.array(MaleLeftMean).flatten(),np.array(self.ReferencialiterariaV),ISPP_First,1,str(pp.iloc[0,8]),'First Session')
            GE_Last = self.CalculateGE(np.array(PP_VL.iloc[PP_VL.shape[0]-1,1:102]).flatten().tolist(),np.array(PP_VR.iloc[PP_VR.shape[0]-1,1:102]).flatten().tolist(),0,np.array(MaleRightMean).flatten(),np.array(MaleLeftMean).flatten(),np.array(self.ReferencialiterariaV),ISPP_Last,1,str(pp.iloc[-1,8]),'Last Session')

            plt.xlabel("Symetry index")
            plt.ylabel("GE(ML)")
            plt.xlim([-10,10])
            plt.ylim([0,10])

            if(ISPP_First<0):
                Media = abs(ISLimits[0])

            else:
                Media = ISLimits[1]

            stdP = ISLimits[5] + ISLimits[5]
            stdN = ISLimits[4] + ISLimits[4]

            plt.plot([-1,-1,1,1], [0,1,1,0], color="black",linestyle='--', label="Limit box of healthy people (based on mean) (right & left)")
            plt.plot([-1+self.ATN(stdN,ISLimits[0]),-1+self.ATN(stdN,ISLimits[0]),1+self.ATN(stdP,ISLimits[1]),1+self.ATN(stdP,ISLimits[1])], [0,1+self.ATN(GELimits[4],GELimits[0]),1+self.ATN(GELimits[4],GELimits[0]),0], color="red",linestyle='-.', label="Limit box of healthy people (based on  2x Standart Dev (left))")
            plt.plot([-1+self.ATN(stdN,ISLimits[0]),-1+self.ATN(stdN,ISLimits[0]),1+self.ATN(stdP,ISLimits[1]),1+self.ATN(stdP,ISLimits[1])], [0,1+self.ATN(GELimits[5],GELimits[1]),1+self.ATN(GELimits[5],GELimits[1]),0], color="red",linestyle=':', label="Limit box of healthy people (based on  2x Standart Dev (right))")
            plt.scatter([self.ATN(ISPP_First,Media)], [self.ATN(GE_First[0],GELimits[0])],color='blue',marker="x",label="GE(ML) First session left side")
            plt.scatter([self.ATN(ISPP_First,Media)], [self.ATN(GE_First[1],GELimits[1])],color='red',marker="x",label="GE(ML) First session right side")
            
            if(ISPP_Last<0):
                Media = abs(ISLimits[0])

            else:
                Media = ISLimits[1]
            
            plt.scatter([self.ATN(ISPP_Last,Media)], [self.ATN(GE_Last[0],GELimits[0])],color='blue',marker="o",label="GE(ML) Last session left side")
            plt.scatter([self.ATN(ISPP_Last,Media)], [self.ATN(GE_Last[1],GELimits[1])],color='red',marker="o",label="GE(ML) Last session right side")

        plt.legend()




import Images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GlobalAnalyzis = QtWidgets.QMainWindow()
    ui = Ui_GlobalAnalyzis()
    ui.setupUi(GlobalAnalyzis)
    GlobalAnalyzis.show()
    sys.exit(app.exec_())

