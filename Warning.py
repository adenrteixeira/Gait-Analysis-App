# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Warning.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(404, 180)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 371, 151))
        self.widget.setObjectName("widget")
        self.buttonBox_3 = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox_3.setGeometry(QtCore.QRect(250, 110, 101, 31))
        self.buttonBox_3.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_3.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_3.setObjectName("buttonBox_3")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(280, 20, 61, 51))
        self.label_6.setText("")
        self.label_6.setTextFormat(QtCore.Qt.PlainText)
        self.label_6.setPixmap(QtGui.QPixmap(":/Icon/WarningSign.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 81, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(20, 50, 211, 61))
        self.label_5.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        self.buttonBox_3.clicked['QAbstractButton*'].connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Warning:"))
        self.label_5.setText(_translate("Dialog", "The values that you selected are not in the range available"))
import Images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
