# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CompareRefPat.ui'
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
from GlobalAnalyzis import Ui_GlobalAnalyzis

import pandas as pd
import numpy as np
import os
from dtw import *
import statistics
import glob

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1621, 750)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(20, 10, 261, 661))
        self.treeWidget.setObjectName("treeWidget")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(20, 680, 261, 31))
        self.widget_4.setObjectName("widget_4")
        self.layoutWidget = QtWidgets.QWidget(self.widget_4)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 261, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setEnabled(True)
        self.tabWidget_2.setGeometry(QtCore.QRect(310, 10, 1301, 711))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget = QtWidgets.QTabWidget(self.tab)
        self.tabWidget.setGeometry(QtCore.QRect(0, 40, 751, 641))
        self.tabWidget.setObjectName("tabWidget")
        self.V = QtWidgets.QWidget()
        self.V.setObjectName("V")
        self.tabWidget.addTab(self.V, "")
        self.ML = QtWidgets.QWidget()
        self.ML.setObjectName("ML")
        self.tabWidget.addTab(self.ML, "")
        self.AP = QtWidgets.QWidget()
        self.AP.setObjectName("AP")
        self.tabWidget.addTab(self.AP, "")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(0, 0, 751, 41))
        self.widget.setObjectName("widget")
        self.layoutWidget1 = QtWidgets.QWidget(self.widget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 0, 731, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setScaledContents(True)
        self.label_8.setWordWrap(False)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/Icon/led_n_pre.png"))
        self.label_10.setScaledContents(False)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout.addWidget(self.label_18)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.widget_3 = QtWidgets.QWidget(self.tab)
        self.widget_3.setGeometry(QtCore.QRect(780, 0, 501, 431))
        self.widget_3.setObjectName("widget_3")
        self.frame_2 = QtWidgets.QFrame(self.widget_3)
        self.frame_2.setGeometry(QtCore.QRect(0, 40, 501, 391))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget2 = QtWidgets.QWidget(self.widget_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 0, 501, 41))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.layoutWidget3 = QtWidgets.QWidget(self.tab)
        self.layoutWidget3.setGeometry(QtCore.QRect(780, 450, 501, 31))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_7.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_7.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_7.addWidget(self.label_17)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.widget_2 = QtWidgets.QWidget(self.tab)
        self.widget_2.setGeometry(QtCore.QRect(780, 480, 501, 191))
        self.widget_2.setObjectName("widget_2")
        self.layoutWidget4 = QtWidgets.QWidget(self.widget_2)
        self.layoutWidget4.setGeometry(QtCore.QRect(0, 0, 501, 41))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_12.setMaximumSize(QtCore.QSize(20, 20))
        self.label_12.setToolTipDuration(2147483647)
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(":/Icon/information.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.widget_2)
        self.treeWidget_2.setGeometry(QtCore.QRect(0, 40, 501, 151))
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.tabWidget_2.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.UpdateListPatients()
        self.ChangesToGUI()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gait Analysis"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Patients"))
        self.pushButton.setText(_translate("MainWindow", "Select"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.V), _translate("MainWindow", "Vertical"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ML), _translate("MainWindow", "Medio-Lateral"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AP), _translate("MainWindow", "Anterior-Posterior"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Icon/led_pre.png\"/></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "M"))
        self.label_11.setText(_translate("MainWindow", "F"))
        self.label.setText(_translate("MainWindow", "Class:"))
        self.label_2.setText(_translate("MainWindow", "-"))
        self.label_5.setText(_translate("MainWindow", "Affected Side: "))
        self.label_18.setText(_translate("MainWindow", "-"))
        self.label_3.setText(_translate("MainWindow", "# of Readmission:"))
        self.label_4.setText(_translate("MainWindow", "00"))
        self.label_6.setText(_translate("MainWindow", "Evolution Of Body Mass Index"))
        self.label_13.setText(_translate("MainWindow", "Age - "))
        self.label_14.setText(_translate("MainWindow", "First Session:"))
        self.label_16.setText(_translate("MainWindow", "Last Session:"))
        self.label_7.setText(_translate("MainWindow", "Distance Values in function of the reference"))
        self.label_12.setToolTip(_translate("MainWindow", "<html><head/><body><p>Here its rpesented the value of the distance based on the dtw for each GRF. Then is presented the mean between the 3 GRF</p></body></html>"))
        self.treeWidget_2.headerItem().setText(0, _translate("MainWindow", "Date"))
        self.treeWidget_2.headerItem().setText(1, _translate("MainWindow", "V (ML)"))
        self.treeWidget_2.headerItem().setText(2, _translate("MainWindow", "V (M)"))
        self.treeWidget_2.headerItem().setText(3, _translate("MainWindow", "ML (ML)"))
        self.treeWidget_2.headerItem().setText(4, _translate("MainWindow", "ML (M)"))
        self.treeWidget_2.headerItem().setText(5, _translate("MainWindow", "AP (ML)"))
        self.treeWidget_2.headerItem().setText(6, _translate("MainWindow", "AP (M)"))
        self.treeWidget_2.headerItem().setText(7, _translate("MainWindow", "Mean DTW (ML)"))
        self.treeWidget_2.headerItem().setText(8, _translate("MainWindow", "Mean DTW (M)"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Gait Graphic Reference"))

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

    def UpdateListPatients(self):
        self.Uploadstuff()

        if(not(os.path.isdir('Patients'))):
            os.mkdir('Patients')

        for patients in self.df.SUBJECT_ID.unique():
            
            root = QtWidgets.QTreeWidgetItem([str(patients)])
            self.treeWidget.addTopLevelItem(root)
            branch = QtWidgets.QTreeWidgetItem(['Left'])
            root.addChild(branch)
            branch = QtWidgets.QTreeWidgetItem(['Right'])
            root.addChild(branch)
            branch = QtWidgets.QTreeWidgetItem(['Global Analyzis'])
            root.addChild(branch)

    def ChangesToGUI(self):
        ## Canvas for graphs
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.V)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        self.figureV = plt.figure()
        plt.title("Vertical GRF")
        self.canvasV = FigureCanvas(self.figureV)
        
        self.horizontalLayout_8.addWidget(self.canvasV)

        #-----------------------------------------------------------------------------------

        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.ML)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")

        self.figureML = plt.figure()
        plt.title("Medio-lateral GRF")
        self.canvasML = FigureCanvas(self.figureML)
        
        self.horizontalLayout_9.addWidget(self.canvasML)

        #-----------------------------------------------------------------------------------

        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.AP)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        self.figureAP = plt.figure()
        plt.title("Anterior-posterior GRF")
        self.canvasAP = FigureCanvas(self.figureAP)
        
        self.horizontalLayout_10.addWidget(self.canvasAP)
        
        #-----------------------------------------------------------------------------------

        ## Canvas for BMI evolution
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        self.figureBMI = plt.figure()
        self.canvasBMI = FigureCanvas(self.figureBMI)
 
        self.horizontalLayout_11.addWidget(self.canvasBMI)

        self.pushButton.clicked.connect(self.BotaoSelect)

    def Change_Labels_And_Leds(self,Idpp):

        pp = self.df[self.df.SUBJECT_ID == int(Idpp)]
        auxpp = self.auxInfo[self.auxInfo.SUBJECT_ID == int(Idpp)]

        if(str(pp.CLASS_LABEL.unique()[0]) == 'H'):
            self.label_2.setText('Hip')
        elif(str(pp.CLASS_LABEL.unique()[0]) == 'A'):
            self.label_2.setText('Ankle')
        elif(str(pp.CLASS_LABEL.unique()[0]) == 'C'):
            self.label_2.setText('Calcaneus')
        elif(str(pp.CLASS_LABEL.unique()[0]) == 'K'):
            self.label_2.setText('Knee')


        if(pp.SEX.unique()[0] == 1):
            self.label_8.setText("<html><head/><body><p><img src=\":/Icon/led_pre.png\"/></p></body></html>")
            self.label_10.setText("<html><head/><body><p><img src=\":/Icon/led_n_pre.png\"/></p></body></html>")
            self.gender = "male"
        else:
            self.label_8.setText("<html><head/><body><p><img src=\":/Icon/led_n_pre.png\"/></p></body></html>")
            self.label_10.setText("<html><head/><body><p><img src=\":/Icon/led_pre.png\"/></p></body></html>")
            self.gender = "female"
        
        self.label_4.setText(str(pp.READMISSION.unique().max()))
        self.label_15.setText(str(pp.AGE.unique().min()))
        self.label_17.setText(str(pp.AGE.unique().max()))

        # Altough we have only one value, this is way is just a cheat to get the value
        if(auxpp.AFFECTED_SIDE.unique().max()==2):
            side = 'both'
        elif(auxpp.AFFECTED_SIDE.unique().max()==1):
            side = 'right'
        else:
            side = 'left'
        
        self.label_18.setText(side)

    def CreateGraphs_S2(self,Idpp,RLFoot):
        pp = self.df[self.df.SUBJECT_ID == int(Idpp)]
        
        path = "Patients/" + str(Idpp)

        self.cores = ['tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan','tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan']

        if(RLFoot == 'Left'):
            if(os.path.isfile(path+'/AP_L_S2_ResultsELMTeste.csv')):

                    a = self.GRF_F_AP_PRO_left.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)
                    b = self.GRF_F_ML_PRO_left.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)
                    c = self.GRF_F_V_PRO_left.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)

                    PP_AP = a.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)
                    PP_ML = b.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)
                    PP_V = c.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)

                    ELMResult_V = pd.read_csv(path+'/V_L_S2_'+'ResultsELMTeste.csv')
                    ELMResult_ML = pd.read_csv(path+'/ML_L_S2_'+'ResultsELMTeste.csv')
                    ELMResult_AP = pd.read_csv(path+'/AP_L_S2_'+'ResultsELMTeste.csv')


                    self.horizontalLayout_8.removeWidget(self.canvasV)
                    self.figureV = plt.figure()
                    self.canvasV = FigureCanvas(self.figureV)
                    plt.title("Vertical GRF")
                    
                    self.horizontalLayout_8.addWidget(self.canvasV)

                    for i in range(0,len(PP_AP)):
                        plt.plot(np.array(PP_V.iloc[i,1:102]).flatten(), color=self.cores[i], linestyle='-', marker ='p', markerfacecolor='white', label=str(PP_AP.iloc[i,109]))
                    
                    plt.plot(self.ReferencialiterariaV.to_numpy().flatten(), color="red",linestyle='-', marker ='h', markerfacecolor='red', label="Vertical literature reference")

                    if(pp.SEX.unique()[0] == 0): # female left
                        plt.plot(pd.read_csv("HFemaleVMeanLeft.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference V")
                    else:
                        plt.plot(pd.read_csv("HMaleVMeanLeft.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference V")

                    plt.plot(ELMResult_V.to_numpy().flatten(), color="orange", linestyle='-', marker ='p', markerfacecolor='orange', label="ELM V")
                
                    plt.legend()
                    self.canvasV.draw()
                    plt.savefig(path + f"/Pathology_{self.gender}_V_GRF_{RLFoot}")

                    self.horizontalLayout_9.removeWidget(self.canvasML)
                    self.figureML = plt.figure()
                    self.canvasML = FigureCanvas(self.figureML)
                    
                    self.horizontalLayout_9.addWidget(self.canvasML)
                    plt.title("Medio-lateral GRF")

                    for i in range(0,len(PP_AP)):
                        plt.plot(np.array(PP_ML.iloc[i,1:102]).flatten(), color=self.cores[i], linestyle='-', marker ='h', markerfacecolor='white', label=str(PP_AP.iloc[i,109]))

                    if(pp.SEX.unique()[0] == 0): # female left
                        plt.plot(pd.read_csv("HFemaleMLMeanLeft.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference ML")
                    else:
                        plt.plot(pd.read_csv("HMaleMLMeanLeft.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference ML")
                    
                    plt.plot(ELMResult_ML.to_numpy().flatten(), color="orange",linestyle='-', marker ='h', markerfacecolor='orange', label="ELM ML")
                    
                    plt.legend()
                    self.canvasML.draw()
                    plt.savefig(path + f"/Pathology_{self.gender}_ML_GRF_{RLFoot}")

                    self.horizontalLayout_10.removeWidget(self.canvasAP)
                    self.figureAP = plt.figure()
                    self.canvasAP = FigureCanvas(self.figureAP)
                    
                    self.horizontalLayout_10.addWidget(self.canvasAP)
                    plt.title("Anterior-posterior GRF")
                    
                    plt.plot(self.ReferencialiterariaAP.to_numpy().flatten(), color="red",linestyle='-', marker ='h', markerfacecolor='red', label="AP literature reference")

                    for i in range(0,len(PP_AP)):
                        plt.plot(np.array(PP_AP.iloc[i,1:102]).flatten(), color=self.cores[i], linestyle='-', marker ='^', markerfacecolor='white', label=str(PP_AP.iloc[i,109]))
                    
                    if(pp.SEX.unique()[0] == 0): # female left
                        plt.plot(pd.read_csv("HFemaleAPMeanLeft.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference AP")
                    else:
                        plt.plot(pd.read_csv("HMaleAPMeanLeft.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference AP")
                    
                    plt.plot(ELMResult_AP.to_numpy().flatten(), color="orange", linestyle='-', marker ='^', markerfacecolor='orange', label="ELM AP")

                    plt.legend()
                    self.canvasAP.draw()
                    plt.savefig(path + f"/Pathology_{self.gender}_AP_GRF_{RLFoot}")

                    if(pp.SEX.unique()[0] == 0): # female left
                        self.DtwDistanceTree(PP_AP,PP_ML,PP_V,ELMResult_ML.to_numpy().flatten(),ELMResult_AP.to_numpy().flatten(),ELMResult_V.to_numpy().flatten(),pd.read_csv("HFemaleVMeanLeft.csv").to_numpy().flatten(),pd.read_csv("HFemaleMLMeanLeft.csv").to_numpy().flatten(),pd.read_csv("HFemaleAPMeanLeft.csv").to_numpy().flatten())
                    else:
                        self.DtwDistanceTree(PP_AP,PP_ML,PP_V,ELMResult_ML.to_numpy().flatten(),ELMResult_AP.to_numpy().flatten(),ELMResult_V.to_numpy().flatten(),pd.read_csv("HMaleVMeanLeft.csv").to_numpy().flatten(),pd.read_csv("HMaleMLMeanLeft.csv").to_numpy().flatten(),pd.read_csv("HMaleAPMeanLeft.csv").to_numpy().flatten())
                    
                    

            else:
                if not os.path.exists(path):
                    os.makedirs(path)

                if(pp.SEX.unique()[0] == 0): # female left

                    a = self.GRF_F_AP_PRO_left.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)
                    b = self.GRF_F_ML_PRO_left.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)
                    c = self.GRF_F_V_PRO_left.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)

                    PP_AP = a.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)
                    PP_AP.SPEED = 2
                    PP_ML = b.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)
                    PP_ML.SPEED = 2
                    PP_V = c.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)
                    PP_V.SPEED = 2
                    
                    Savepath = path+'/V_L_S2_'
                    PP_V.to_csv("ForELM_app.csv",index=False)
                    aux = "matlab -nodesktop -nosplash -r \"LoadELM_app_2(\'Results/ELM/ELM_FL_V.mat\',\'%s\');exit;\""%Savepath
                    os.system(aux)
                    ELMResult_V = pd.read_csv(Savepath + "ResultsELMTeste.csv")

                    Savepath = path+'/AP_L_S2_'
                    PP_AP.to_csv("ForELM_app.csv",index=False)
                    aux = "matlab -nodesktop -nosplash -r \"LoadELM_app_2(\'Results/ELM/ELM_FL_AP.mat\',\'%s\');exit;\""%Savepath
                    os.system(aux)
                    ELMResult_AP = pd.read_csv(Savepath + "ResultsELMTeste.csv")

                    Savepath = path+'/ML_L_S2_'
                    PP_ML.to_csv("ForELM_app.csv",index=False)
                    aux = "matlab -nodesktop -nosplash -r \"LoadELM_app_2(\'Results/ELM/ELM_FL_ML.mat\',\'%s\');exit;\""%Savepath
                    os.system(aux)
                    ELMResult_ML = pd.read_csv(Savepath + "ResultsELMTeste.csv")

                    self.horizontalLayout_8.removeWidget(self.canvasV)
                    self.figureV = plt.figure()
                    self.canvasV = FigureCanvas(self.figureV)
                    plt.title("Vertical GRF")
                    
                    self.horizontalLayout_8.addWidget(self.canvasV)

                    for i in range(0,len(PP_AP)):
                        plt.plot(np.array(PP_V.iloc[i,1:102]).flatten(), color=self.cores[i], linestyle='-', marker ='p', markerfacecolor='white', label=str(PP_AP.iloc[i,109]))
                    
                    plt.plot(self.ReferencialiterariaV.to_numpy().flatten(), color="red",linestyle='-', marker ='h', markerfacecolor='red', label="Vertical literature reference")
                    plt.plot(pd.read_csv("HFemaleVMeanLeft.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference V")
                    plt.plot(ELMResult_V.to_numpy().flatten(), color="orange", linestyle='-', marker ='p', markerfacecolor='orange', label="ELM V")
                    plt.legend()
                    self.canvasV.draw()
                    plt.savefig(path + f"/Pathology_{self.gender}_V_GRF_{RLFoot}")

                    self.horizontalLayout_9.removeWidget(self.canvasML)
                    self.figureML = plt.figure()
                    self.canvasML = FigureCanvas(self.figureML)

                    self.horizontalLayout_9.addWidget(self.canvasML)
                    plt.title("Medio-lateral GRF")

                    for i in range(0,len(PP_AP)):
                        plt.plot(np.array(PP_ML.iloc[i,1:102]).flatten(), color=self.cores[i], linestyle='-', marker ='h', markerfacecolor='white', label=str(PP_AP.iloc[i,109]))
                    
                    plt.plot(pd.read_csv("HFemaleMLMeanLeft.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference ML")
                    plt.plot(ELMResult_ML.to_numpy().flatten(), color="orange",linestyle='-', marker ='h', markerfacecolor='orange', label="ELM ML")
                    plt.legend()
                    self.canvasML.draw()
                    plt.savefig(path + f"/Pathology_{self.gender}_ML_GRF_{RLFoot}")

                    self.horizontalLayout_10.removeWidget(self.canvasAP)
                    self.figureAP = plt.figure()
                    self.canvasAP = FigureCanvas(self.figureAP)
                    
                    self.horizontalLayout_10.addWidget(self.canvasAP)
                    plt.title("Anterior-posterior GRF")


                    for i in range(0,len(PP_AP)):
                        plt.plot(np.array(PP_AP.iloc[i,1:102]).flatten(), color=self.cores[i], linestyle='-', marker ='^', markerfacecolor='white', label=str(PP_AP.iloc[i,109]))
                    
                    plt.plot(self.ReferencialiterariaAP.to_numpy().flatten(), color="red",linestyle='-', marker ='h', markerfacecolor='red', label="AP literature reference")
                    plt.plot(pd.read_csv("HFemaleAPMeanLeft.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference AP")
                    plt.plot(ELMResult_AP.to_numpy().flatten(), color="orange", linestyle='-', marker ='^', markerfacecolor='orange', label="ELM AP")
                    plt.legend()
                    self.canvasAP.draw()
                    plt.savefig(path + f"/Pathology_{self.gender}_AP_GRF_{RLFoot}")


                    self.DtwDistanceTree(PP_AP,PP_ML,PP_V,ELMResult_ML.to_numpy().flatten(),ELMResult_AP.to_numpy().flatten(),ELMResult_V.to_numpy().flatten(),pd.read_csv("HFemaleVMeanLeft.csv").to_numpy().flatten(),pd.read_csv("HFemaleMLMeanLeft.csv").to_numpy().flatten(),pd.read_csv("HFemaleAPMeanLeft.csv").to_numpy().flatten())

                else:

                    a = self.GRF_F_AP_PRO_left.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)
                    b = self.GRF_F_ML_PRO_left.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)
                    c = self.GRF_F_V_PRO_left.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)

                    PP_AP = a.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)
                    PP_AP.SPEED = 2
                    PP_ML = b.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)
                    PP_ML.SPEED = 2
                    PP_V = c.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)
                    PP_V.SPEED = 2
                    
                    Savepath = path+'/AP_L_S2_'
                    PP_AP.to_csv("ForELM_app.csv",index=False)
                    aux = "matlab -nodesktop -nosplash -r \"LoadELM_app_2(\'Results/ELM/ELM_ML_AP.mat\',\'%s\');exit;\""%Savepath
                    os.system(aux)
                    ELMResult_AP = pd.read_csv(Savepath + "ResultsELMTeste.csv")

                    Savepath = path+'/ML_L_S2_'
                    PP_ML.to_csv("ForELM_app.csv",index=False)
                    aux = "matlab -nodesktop -nosplash -r \"LoadELM_app_2(\'Results/ELM/ELM_ML_ML.mat\',\'%s\');exit;\""%Savepath
                    os.system(aux)
                    ELMResult_ML = pd.read_csv(Savepath + "ResultsELMTeste.csv")

                    Savepath = path+'/V_L_S2_'
                    PP_V.to_csv("ForELM_app.csv",index=False)
                    aux = "matlab -nodesktop -nosplash -r \"LoadELM_app_2(\'Results/ELM/ELM_ML_V.mat\',\'%s\');exit;\""%Savepath
                    os.system(aux)
                    ELMResult_V = pd.read_csv(Savepath + "ResultsELMTeste.csv")

                    self.horizontalLayout_8.removeWidget(self.canvasV)
                    self.figureV = plt.figure()
                    self.canvasV = FigureCanvas(self.figureV)
                    plt.title("Vertical GRF")
                    
                    self.horizontalLayout_8.addWidget(self.canvasV)

                    for i in range(0,len(PP_AP)):
                        plt.plot(np.array(PP_V.iloc[i,1:102]).flatten(), color=self.cores[i], linestyle='-', marker ='p', markerfacecolor='white', label=str(PP_AP.iloc[i,109]))
                    
                    plt.plot(self.ReferencialiterariaV.to_numpy().flatten(), color="red",linestyle='-', marker ='h', markerfacecolor='red', label="Vertical literature reference")
                    plt.plot(pd.read_csv("HMaleVMeanLeft.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference V")
                    plt.plot(ELMResult_V.to_numpy().flatten(), color="orange", linestyle='-', marker ='p', markerfacecolor='orange', label="ELM V")
                    plt.legend()
                    self.canvasV.draw()
                    plt.savefig(path + f"/Pathology_{self.gender}_V_GRF_{RLFoot}")

                    self.horizontalLayout_9.removeWidget(self.canvasML)
                    self.figureML = plt.figure()
                    self.canvasML = FigureCanvas(self.figureML)
                    
                    self.horizontalLayout_9.addWidget(self.canvasML)
                    plt.title("Medio-lateral GRF")

                    for i in range(0,len(PP_AP)):
                        plt.plot(np.array(PP_ML.iloc[i,1:102]).flatten(), color=self.cores[i], linestyle='-', marker ='h', markerfacecolor='white', label=str(PP_AP.iloc[i,109]))
                    
                    plt.plot(pd.read_csv("HMaleMLMeanLeft.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference ML")
                    plt.plot(ELMResult_ML.to_numpy().flatten(), color="orange",linestyle='-', marker ='h', markerfacecolor='orange', label="ELM ML")
                    plt.legend()
                    self.canvasML.draw()
                    plt.savefig(path + f"/Pathology_{self.gender}_ML_GRF_{RLFoot}")

                    self.horizontalLayout_10.removeWidget(self.canvasAP)
                    self.figureAP = plt.figure()
                    self.canvasAP = FigureCanvas(self.figureAP)
                    
                    self.horizontalLayout_10.addWidget(self.canvasAP)
                    plt.title("Anterior-posterior GRF")


                    for i in range(0,len(PP_AP)):
                        plt.plot(np.array(PP_AP.iloc[i,1:102]).flatten(), color=self.cores[i], linestyle='-', marker ='^', markerfacecolor='white', label=str(PP_AP.iloc[i,109]))
                    
                    plt.plot(self.ReferencialiterariaAP.to_numpy().flatten(), color="red",linestyle='-', marker ='h', markerfacecolor='red', label="AP literature reference")
                    plt.plot(pd.read_csv("HMaleAPMeanLeft.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference AP")
                    plt.plot(ELMResult_AP.to_numpy().flatten(), color="orange", linestyle='-', marker ='^', markerfacecolor='orange', label="ELM AP")
                    plt.legend()
                    self.canvasAP.draw()
                    plt.savefig(path + f"/Pathology_{self.gender}_AP_GRF_{RLFoot}")


                    self.DtwDistanceTree(PP_AP,PP_ML,PP_V,ELMResult_ML.to_numpy().flatten(),ELMResult_AP.to_numpy().flatten(),ELMResult_V.to_numpy().flatten(),pd.read_csv("HMaleVMeanLeft.csv").to_numpy().flatten(),pd.read_csv("HMaleMLMeanLeft.csv").to_numpy().flatten(),pd.read_csv("HMaleAPMeanLeft.csv").to_numpy().flatten())
        else:
            if(os.path.isfile(path+'/AP_R_S2_ResultsELMTeste.csv')): # Is AP but could test with V or ML its a choice

                a = self.GRF_F_AP_PRO_right.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)
                b = self.GRF_F_ML_PRO_right.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)
                c = self.GRF_F_V_PRO_right.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)

                PP_AP = a.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)
                PP_ML = b.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)
                PP_V = c.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)
                
                ELMResult_V = pd.read_csv(path+'/V_R_S2_'+'ResultsELMTeste.csv')
                ELMResult_ML = pd.read_csv(path+'/ML_R_S2_'+'ResultsELMTeste.csv')
                ELMResult_AP = pd.read_csv(path+'/AP_R_S2_'+'ResultsELMTeste.csv')

                self.horizontalLayout_8.removeWidget(self.canvasV)
                self.figureV = plt.figure()
                self.canvasV = FigureCanvas(self.figureV)
                plt.title("Vertical GRF")
                
                self.horizontalLayout_8.addWidget(self.canvasV)

                for i in range(0,len(PP_AP)):
                    plt.plot(np.array(PP_V.iloc[i,1:102]).flatten(), color=self.cores[i], linestyle='-', marker ='p', markerfacecolor='white', label=str(PP_AP.iloc[i,109]))
                
                plt.plot(self.ReferencialiterariaV.to_numpy().flatten(), color="red",linestyle='-', marker ='h', markerfacecolor='red', label="Vertical literature reference")

                if(pp.SEX.unique()[0] == 0): # female right
                    plt.plot(pd.read_csv("HFemaleVMeanRight.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference V")
                else:
                    plt.plot(pd.read_csv("HMaleVMeanRight.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference V")

                plt.plot(ELMResult_V.to_numpy().flatten(), color="orange", linestyle='-', marker ='p', markerfacecolor='orange', label="ELM V")

                plt.legend()
                self.canvasV.draw()
                plt.savefig(path + f"/Pathology_{self.gender}_V_GRF_{RLFoot}")

                self.horizontalLayout_9.removeWidget(self.canvasML)
                self.figureML = plt.figure()
                self.canvasML = FigureCanvas(self.figureML)
                
                self.horizontalLayout_9.addWidget(self.canvasML)
                plt.title("Medio-lateral GRF")

                for i in range(0,len(PP_AP)):
                    plt.plot(np.array(PP_ML.iloc[i,1:102]).flatten(), color=self.cores[i], linestyle='-', marker ='h', markerfacecolor='white', label=str(PP_AP.iloc[i,109]))
                
                if(pp.SEX.unique()[0] == 0): # female right
                    plt.plot(pd.read_csv("HFemaleMLMeanRight.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference ML")
                else:
                    plt.plot(pd.read_csv("HMaleMLMeanRight.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference ML")
                    
                plt.plot(ELMResult_ML.to_numpy().flatten(), color="orange",linestyle='-', marker ='h', markerfacecolor='orange', label="ELM ML")

                plt.legend()
                self.canvasML.draw()
                plt.savefig(path + f"/Pathology_{self.gender}_ML_GRF_{RLFoot}")

                self.horizontalLayout_10.removeWidget(self.canvasAP)
                self.figureAP = plt.figure()
                self.canvasAP = FigureCanvas(self.figureAP)
                
                self.horizontalLayout_10.addWidget(self.canvasAP)
                plt.title("Anterior-posterior GRF")


                for i in range(0,len(PP_AP)):
                    plt.plot(np.array(PP_AP.iloc[i,1:102]).flatten(), color=self.cores[i], linestyle='-', marker ='^', markerfacecolor='white', label=str(PP_AP.iloc[i,109]))
                
                plt.plot(self.ReferencialiterariaAP.to_numpy().flatten(), color="red",linestyle='-', marker ='h', markerfacecolor='red', label="AP literature reference")

                if(pp.SEX.unique()[0] == 0): # female right
                    plt.plot(pd.read_csv("HFemaleAPMeanRight.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference AP")
                else:
                    plt.plot(pd.read_csv("HMaleAPMeanRight.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference AP")
                    
                plt.plot(ELMResult_AP.to_numpy().flatten(), color="orange", linestyle='-', marker ='^', markerfacecolor='orange', label="ELM AP")

                plt.legend()
                self.canvasAP.draw()
                plt.savefig(path + f"/Pathology_{self.gender}_AP_GRF_{RLFoot}")

                if(pp.SEX.unique()[0] == 0): # female right
                    self.DtwDistanceTree(PP_AP,PP_ML,PP_V,ELMResult_ML.to_numpy().flatten(),ELMResult_AP.to_numpy().flatten(),ELMResult_V.to_numpy().flatten(),pd.read_csv("HFemaleVMeanRight.csv").to_numpy().flatten(),pd.read_csv("HFemaleMLMeanRight.csv").to_numpy().flatten(),pd.read_csv("HFemaleAPMeanRight.csv").to_numpy().flatten())
                else:
                    self.DtwDistanceTree(PP_AP,PP_ML,PP_V,ELMResult_ML.to_numpy().flatten(),ELMResult_AP.to_numpy().flatten(),ELMResult_V.to_numpy().flatten(),pd.read_csv("HMaleVMeanRight.csv").to_numpy().flatten(),pd.read_csv("HMaleMLMeanRight.csv").to_numpy().flatten(),pd.read_csv("HMaleAPMeanRight.csv").to_numpy().flatten())

            else:
                
                if not os.path.exists(path):
                    os.makedirs(path)

                if(pp.SEX.unique()[0] == 0): # female right

                    a = self.GRF_F_AP_PRO_right.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)
                    b = self.GRF_F_ML_PRO_right.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)
                    c = self.GRF_F_V_PRO_right.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)

                    PP_AP = a.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)
                    PP_AP.SPEED = 2
                    PP_ML = b.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)
                    PP_ML.SPEED = 2
                    PP_V = c.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)
                    PP_V.SPEED = 2
                    
                    Savepath = path+'/AP_R_S2_'
                    PP_AP.to_csv("ForELM_app.csv",index=False)
                    aux = "matlab -nodesktop -nosplash -r \"LoadELM_app_2(\'Results/ELM/ELM_FR_AP.mat\',\'%s\');exit;\""%Savepath
                    os.system(aux)
                    ELMResult_AP = pd.read_csv(Savepath + "ResultsELMTeste.csv")

                    Savepath = path+'/ML_R_S2_'
                    PP_ML.to_csv("ForELM_app.csv",index=False)
                    aux = "matlab -nodesktop -nosplash -r \"LoadELM_app_2(\'Results/ELM/ELM_FR_ML.mat\',\'%s\');exit;\""%Savepath
                    os.system(aux)
                    ELMResult_ML = pd.read_csv(Savepath + "ResultsELMTeste.csv")

                    Savepath = path+'/V_R_S2_'
                    PP_V.to_csv("ForELM_app.csv",index=False)
                    aux = "matlab -nodesktop -nosplash -r \"LoadELM_app_2(\'Results/ELM/ELM_FR_V.mat\',\'%s\');exit;\""%Savepath
                    os.system(aux)
                    ELMResult_V = pd.read_csv(Savepath + "ResultsELMTeste.csv")

                    self.horizontalLayout_8.removeWidget(self.canvasV)
                    self.figureV = plt.figure()
                    self.canvasV = FigureCanvas(self.figureV)
                    plt.title("Vertical GRF")
                    
                    self.horizontalLayout_8.addWidget(self.canvasV)

                    for i in range(0,len(PP_AP)):
                        plt.plot(np.array(PP_V.iloc[i,1:102]).flatten(), color=self.cores[i], linestyle='-', marker ='p', markerfacecolor='white', label=str(PP_AP.iloc[i,109]))

                    plt.plot(self.ReferencialiterariaV.to_numpy().flatten(), color="red",linestyle='-', marker ='h', markerfacecolor='red', label="Vertical literature reference")
                    plt.plot(pd.read_csv("HFemaleVMeanRight.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference V")
                    plt.plot(ELMResult_V.to_numpy().flatten(), color="orange", linestyle='-', marker ='p', markerfacecolor='orange', label="ELM V")
                    plt.legend()
                    self.canvasV.draw()
                    plt.savefig(path + f"/Pathology_{self.gender}_V_GRF_{RLFoot}")

                    self.horizontalLayout_9.removeWidget(self.canvasML)
                    self.figureML = plt.figure()
                    self.canvasML = FigureCanvas(self.figureML)
                    
                    self.horizontalLayout_9.addWidget(self.canvasML)
                    plt.title("Medio-lateral GRF")

                    for i in range(0,len(PP_AP)):
                        plt.plot(np.array(PP_ML.iloc[i,1:102]).flatten(), color=self.cores[i], linestyle='-', marker ='h', markerfacecolor='white', label=str(PP_AP.iloc[i,109]))
                    
                    plt.plot(pd.read_csv("HFemaleMLMeanRight.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference ML")
                    plt.plot(ELMResult_ML.to_numpy().flatten(), color="orange",linestyle='-', marker ='h', markerfacecolor='orange', label="ELM ML")
                    plt.legend()
                    self.canvasML.draw()
                    plt.savefig(path + f"/Pathology_{self.gender}_ML_GRF_{RLFoot}")

                    self.horizontalLayout_10.removeWidget(self.canvasAP)
                    self.figureAP = plt.figure()
                    self.canvasAP = FigureCanvas(self.figureAP)
                    
                    self.horizontalLayout_10.addWidget(self.canvasAP)
                    plt.title("Anterior-posterior GRF")


                    for i in range(0,len(PP_AP)):
                        plt.plot(np.array(PP_AP.iloc[i,1:102]).flatten(), color=self.cores[i], linestyle='-', marker ='^', markerfacecolor='white', label=str(PP_AP.iloc[i,109]))
                    
                    plt.plot(self.ReferencialiterariaAP.to_numpy().flatten(), color="red",linestyle='-', marker ='h', markerfacecolor='red', label="AP literature reference")
                    plt.plot(pd.read_csv("HFemaleAPMeanRight.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference AP")
                    plt.plot(ELMResult_AP.to_numpy().flatten(), color="orange", linestyle='-', marker ='^', markerfacecolor='orange', label="ELM AP")
                    plt.legend()
                    self.canvasAP.draw()
                    plt.savefig(path + f"/Pathology_{self.gender}_AP_GRF_{RLFoot}")

                    self.DtwDistanceTree(PP_AP,PP_ML,PP_V,ELMResult_ML.to_numpy().flatten(),ELMResult_AP.to_numpy().flatten(),ELMResult_V.to_numpy().flatten(),pd.read_csv("HFemaleVMeanRight.csv").to_numpy().flatten(),pd.read_csv("HFemaleMLMeanRight.csv").to_numpy().flatten(),pd.read_csv("HFemaleAPMeanRight.csv").to_numpy().flatten())

                else:

                    a = self.GRF_F_AP_PRO_right.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)
                    b = self.GRF_F_ML_PRO_right.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)
                    c = self.GRF_F_V_PRO_right.groupby(['SESSION_ID']).mean().drop(['TRIAL_ID'],axis=1)

                    PP_AP = a.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)
                    PP_AP.SPEED = 2
                    PP_ML = b.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)
                    PP_ML.SPEED = 2
                    PP_V = c.merge(pp, how='inner', on='SESSION_ID').drop(['SUBJECT_ID_x'],axis=1)
                    PP_V.SPEED = 2
                    
                    Savepath = path+'/AP_R_S2_'
                    PP_AP.to_csv("ForELM_app.csv",index=False)
                    aux = "matlab -nodesktop -nosplash -r \"LoadELM_app_2(\'Results/ELM/ELM_MR_AP.mat\',\'%s\');exit;\""%Savepath
                    os.system(aux)
                    ELMResult_AP = pd.read_csv(Savepath + "ResultsELMTeste.csv")

                    Savepath = path+'/ML_R_S2_'
                    PP_ML.to_csv("ForELM_app.csv",index=False)
                    aux = "matlab -nodesktop -nosplash -r \"LoadELM_app_2(\'Results/ELM/ELM_MR_ML.mat\',\'%s\');exit;\""%Savepath
                    os.system(aux)
                    ELMResult_ML = pd.read_csv(Savepath + "ResultsELMTeste.csv")

                    Savepath = path+'/V_R_S2_'
                    PP_V.to_csv("ForELM_app.csv",index=False)
                    aux = "matlab -nodesktop -nosplash -r \"LoadELM_app_2(\'Results/ELM/ELM_MR_V.mat\',\'%s\');exit;\""%Savepath
                    os.system(aux)
                    ELMResult_V = pd.read_csv(Savepath + "ResultsELMTeste.csv")

                    self.horizontalLayout_8.removeWidget(self.canvasV)
                    self.figureV = plt.figure()
                    self.canvasV = FigureCanvas(self.figureV)
                    plt.title("Vertical GRF")
                    
                    self.horizontalLayout_8.addWidget(self.canvasV)

                    for i in range(0,len(PP_AP)):
                        plt.plot(np.array(PP_V.iloc[i,1:102]).flatten(), color=self.cores[i], linestyle='-', marker ='p', markerfacecolor='white', label=str(PP_AP.iloc[i,109]))

                    plt.plot(self.ReferencialiterariaV.to_numpy().flatten(), color="red",linestyle='-', marker ='h', markerfacecolor='red', label="Vertical literature reference")
                    plt.plot(pd.read_csv("HMaleVMeanRight.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference V")
                    plt.plot(ELMResult_V.to_numpy().flatten(), color="orange", linestyle='-', marker ='p', markerfacecolor='orange', label="ELM V")
                    plt.legend()
                    self.canvasV.draw()
                    plt.savefig(path + f"/Pathology_{self.gender}_V_GRF_{RLFoot}")

                    self.horizontalLayout_9.removeWidget(self.canvasML)
                    self.figureML = plt.figure()
                    self.canvasML = FigureCanvas(self.figureML)
                    
                    self.horizontalLayout_9.addWidget(self.canvasML)
                    plt.title("Medio-lateral GRF")

                    for i in range(0,len(PP_AP)):
                        plt.plot(np.array(PP_ML.iloc[i,1:102]).flatten(), color=self.cores[i], linestyle='-', marker ='h', markerfacecolor='white', label=str(PP_AP.iloc[i,109]))
                    
                    plt.plot(pd.read_csv("HMaleMLMeanRight.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference ML")
                    plt.plot(ELMResult_ML.to_numpy().flatten(), color="orange",linestyle='-', marker ='h', markerfacecolor='orange', label="ELM ML")
                    plt.legend()
                    self.canvasML.draw()
                    plt.savefig(path + f"/Pathology_{self.gender}_ML_GRF_{RLFoot}")

                    self.horizontalLayout_10.removeWidget(self.canvasAP)
                    self.figureAP = plt.figure()
                    self.canvasAP = FigureCanvas(self.figureAP)
                    
                    self.horizontalLayout_10.addWidget(self.canvasAP)
                    plt.title("Anterior-posterior GRF")


                    for i in range(0,len(PP_AP)):
                        plt.plot(np.array(PP_AP.iloc[i,1:102]).flatten(), color=self.cores[i], linestyle='-', marker ='^', markerfacecolor='white', label=str(PP_AP.iloc[i,109]))
                    
                    plt.plot(self.ReferencialiterariaAP.to_numpy().flatten(), color="red",linestyle='-', marker ='h', markerfacecolor='red', label="AP literature reference")
                    plt.plot(pd.read_csv("HMaleAPMeanRight.csv").to_numpy().flatten(), color="blue", linestyle='-', marker ='p', markerfacecolor='blue', label="Mean Reference AP")
                    plt.plot(ELMResult_AP.to_numpy().flatten(), color="orange", linestyle='-', marker ='^', markerfacecolor='orange', label="ELM AP")
                    plt.legend()
                    self.canvasAP.draw()
                    plt.savefig(path + f"/Pathology_{self.gender}_AP_GRF_{RLFoot}")

                    self.DtwDistanceTree(PP_AP,PP_ML,PP_V,ELMResult_ML.to_numpy().flatten(),ELMResult_AP.to_numpy().flatten(),ELMResult_V.to_numpy().flatten(),pd.read_csv("HMaleVMeanRight.csv").to_numpy().flatten(),pd.read_csv("HMaleMLMeanRight.csv").to_numpy().flatten(),pd.read_csv("HMaleAPMeanRight.csv").to_numpy().flatten())

    def BMIGraph(self,Idpp,RLFoot):
        pp = self.df[self.df.SUBJECT_ID == int(Idpp)]
        
        path = "Patients/" + str(Idpp)

        cores = ['tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan','tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:pink','tab:gray','tab:olive','tab:cyan']
        
        self.horizontalLayout_11.removeWidget(self.canvasBMI)
        self.figureBMI = plt.figure()
        self.canvasBMI = FigureCanvas(self.figureBMI)
 
        self.horizontalLayout_11.addWidget(self.canvasBMI)

        lista = np.array(pp.iloc[:,8]).flatten().tolist()

        plt.plot(range(1,len(lista)+1),np.array(pp.iloc[:,9]).flatten().tolist(), color=cores[0], linestyle='-', marker ='^', markerfacecolor='white', label=lista)

        for i, v in enumerate(lista):
            if(i%2 == 0):
                plt.annotate(str(v), xy=(i+1,pp.iloc[i,9]), xytext=(-25,7), textcoords='offset points')
            else:
                plt.annotate(str(v), xy=(i+1,pp.iloc[i,9]), xytext=(-25,-17), textcoords='offset points')
        
        plt.ylim(15,50) # After study in implementacao the max and min are 15.8 and 48.2, so i choose this values

        self.canvasBMI.draw()

    def DtwDistanceTree(self,PP_AP,PP_ML,PP_V,ELM_ML,ELM_AP,ELM_V, M_V, M_ML, M_AP):
        self.treeWidget_2.clear()
        DistAP =[]
        DistV =[]
        DistML =[]

        for i in range(0,len(PP_AP)):
            DistAP.append(dtw(np.array(PP_AP.iloc[i,1:102]).flatten().tolist(), ELM_AP.tolist()).distance)
            DistV.append(dtw(np.array(PP_V.iloc[i,1:102]).flatten().tolist(), ELM_V.tolist()).distance)
            DistML.append(dtw(np.array(PP_ML.iloc[i,1:102]).flatten().tolist(), ELM_ML.tolist()).distance)

        maximoAP = max(DistAP)
        minimoAP = min(DistAP)
        maximoV = max(DistV)
        minimoV = min(DistV)
        maximoML = max(DistML)
        minimoML = min(DistML)

        for i in range(0,len(PP_AP)):
            
            DistAP[i] = (DistAP[i]- minimoAP)/(maximoAP-minimoAP)
            DistV[i] = (DistV[i]- minimoV)/(maximoV-minimoV)
            DistML[i] = (DistML[i]- minimoML)/(maximoML-minimoML)

        #str((round(DistV[i],2) + round(DistML[i],2) + round(DistAP[i],2)))

        DistAP_M =[]
        DistV_M =[]
        DistML_M =[]

        for i in range(0,len(PP_AP)):
            DistAP_M.append(dtw(np.array(PP_AP.iloc[i,1:102]).flatten().tolist(), M_AP.tolist()).distance)
            DistV_M.append(dtw(np.array(PP_V.iloc[i,1:102]).flatten().tolist(), M_V.tolist()).distance)
            DistML_M.append(dtw(np.array(PP_ML.iloc[i,1:102]).flatten().tolist(), M_ML.tolist()).distance)

        maximoAP_M = max(DistAP_M)
        minimoAP_M = min(DistAP_M)
        maximoV_M = max(DistV_M)
        minimoV_M = min(DistV_M)
        maximoML_M = max(DistML_M)
        minimoML_M = min(DistML_M)

        for i in range(0,len(PP_AP)):
            
            DistAP_M[i] = (DistAP_M[i]- minimoAP_M)/(maximoAP_M-minimoAP_M)
            DistV_M[i] = (DistV_M[i]- minimoV_M)/(maximoV_M-minimoV_M)
            DistML_M[i] = (DistML_M[i]- minimoML_M)/(maximoML_M-minimoML_M)


        for i in range(0,len(PP_AP)):
            root = QtWidgets.QTreeWidgetItem([str(str(PP_AP.iloc[i,109])), str(round(DistV[i],2)), str(round(DistV_M[i],2)), str(round(DistML[i],2)), str(round(DistML_M[i],2)), str(round(DistAP[i],2)), str(round(DistAP_M[i],2)), str(round(statistics.mean([DistV[i],DistML[i],DistAP[i]]),2)),str(round(statistics.mean([DistV_M[i],DistML_M[i],DistAP_M[i]]),2))])
            self.treeWidget_2.addTopLevelItem(root)

    def BotaoSelect(self):
        
        try:
            x = self.treeWidget.selectedItems()[0]
            print("Eu sou 0: ",x.parent().text(0))
            print(x.text(0))

            self.Change_Labels_And_Leds(x.parent().text(0))

            if(x.text(0) == 'Global Analyzis'):
                #print((len(glob.glob(f"Patients/{x.parent().text(0)}/*_R_S2_ResultsELMTeste.csv")) == 0) & (len(glob.glob(f"Patients/{x.parent().text(0)}/*_L_S2_ResultsELMTeste.csv")) == 0))
                if((len(glob.glob(f"Patients/{x.parent().text(0)}/*_R_S2_ResultsELMTeste.csv")) == 0) | (len(glob.glob(f"Patients/{x.parent().text(0)}/*_L_S2_ResultsELMTeste.csv")) == 0)):
                    dialog = QtWidgets.QDialog()
                    dialog.ui = Form2()
                    dialog.ui.setupUi(dialog)
                    dialog.exec_()
                    dialog.show()
                else:
                    self.globalAnalyzis = QtWidgets.QMainWindow()
                    self.globalAnalyzis.ui = Ui_GlobalAnalyzis()
                    self.globalAnalyzis.ui.setupUi(self.globalAnalyzis,x.parent().text(0))
                    self.globalAnalyzis.show()
            else:

                QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

                self.CreateGraphs_S2(x.parent().text(0),x.text(0))
                self.BMIGraph(x.parent().text(0),x.text(0))
                QtWidgets.QApplication.restoreOverrideCursor()
        
        
        except:
            dialog = QtWidgets.QDialog()
            dialog.ui = Form()
            dialog.ui.setupUi(dialog)
            dialog.exec_()
            dialog.show()


import Images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

