# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serialsetDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(385, 342)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(200, 290, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 371, 251))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 10, 181, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cbbPortName = QtWidgets.QComboBox(self.layoutWidget)
        self.cbbPortName.setObjectName("cbbPortName")
        self.horizontalLayout.addWidget(self.cbbPortName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.cbbBaudRate = QtWidgets.QComboBox(self.layoutWidget)
        self.cbbBaudRate.setObjectName("cbbBaudRate")
        self.cbbBaudRate.addItem("")
        self.cbbBaudRate.addItem("")
        self.cbbBaudRate.addItem("")
        self.cbbBaudRate.addItem("")
        self.cbbBaudRate.addItem("")
        self.cbbBaudRate.addItem("")
        self.cbbBaudRate.addItem("")
        self.cbbBaudRate.addItem("")
        self.cbbBaudRate.addItem("")
        self.cbbBaudRate.addItem("")
        self.cbbBaudRate.addItem("")
        self.cbbBaudRate.addItem("")
        self.horizontalLayout_2.addWidget(self.cbbBaudRate)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.cbbParity = QtWidgets.QComboBox(self.layoutWidget)
        self.cbbParity.setObjectName("cbbParity")
        self.cbbParity.addItem("")
        self.cbbParity.addItem("")
        self.cbbParity.addItem("")
        self.cbbParity.addItem("")
        self.cbbParity.addItem("")
        self.horizontalLayout_3.addWidget(self.cbbParity)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.cbbDataBit = QtWidgets.QComboBox(self.layoutWidget)
        self.cbbDataBit.setObjectName("cbbDataBit")
        self.cbbDataBit.addItem("")
        self.cbbDataBit.addItem("")
        self.cbbDataBit.addItem("")
        self.cbbDataBit.addItem("")
        self.horizontalLayout_4.addWidget(self.cbbDataBit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.cbbStopBit = QtWidgets.QComboBox(self.layoutWidget)
        self.cbbStopBit.setObjectName("cbbStopBit")
        self.cbbStopBit.addItem("")
        self.cbbStopBit.addItem("")
        self.cbbStopBit.addItem("")
        self.horizontalLayout_5.addWidget(self.cbbStopBit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cbReSend = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.cbReSend.setFont(font)
        self.cbReSend.setObjectName("cbReSend")
        self.horizontalLayout_6.addWidget(self.cbReSend)
        self.sbResendTimePeriod = QtWidgets.QSpinBox(self.layoutWidget)
        self.sbResendTimePeriod.setObjectName("sbResendTimePeriod")
        self.horizontalLayout_6.addWidget(self.sbResendTimePeriod)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.OpenSerialButton = QtWidgets.QPushButton(self.layoutWidget)
        self.OpenSerialButton.setObjectName("OpenSerialButton")
        self.horizontalLayout_7.addWidget(self.OpenSerialButton)
        self.CloseSerialButton = QtWidgets.QPushButton(self.layoutWidget)
        self.CloseSerialButton.setObjectName("CloseSerialButton")
        self.horizontalLayout_7.addWidget(self.CloseSerialButton)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.cbbBaudRate.setCurrentIndex(9)
        self.cbbDataBit.setCurrentIndex(3)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "串口号："))
        self.label_2.setText(_translate("Dialog", "波特率："))
        self.cbbBaudRate.setCurrentText(_translate("Dialog", "115200"))
        self.cbbBaudRate.setItemText(0, _translate("Dialog", "300"))
        self.cbbBaudRate.setItemText(1, _translate("Dialog", "600"))
        self.cbbBaudRate.setItemText(2, _translate("Dialog", "1200"))
        self.cbbBaudRate.setItemText(3, _translate("Dialog", "2400"))
        self.cbbBaudRate.setItemText(4, _translate("Dialog", "4800"))
        self.cbbBaudRate.setItemText(5, _translate("Dialog", "9600"))
        self.cbbBaudRate.setItemText(6, _translate("Dialog", "19200"))
        self.cbbBaudRate.setItemText(7, _translate("Dialog", "38400"))
        self.cbbBaudRate.setItemText(8, _translate("Dialog", "57600"))
        self.cbbBaudRate.setItemText(9, _translate("Dialog", "115200"))
        self.cbbBaudRate.setItemText(10, _translate("Dialog", "128000"))
        self.cbbBaudRate.setItemText(11, _translate("Dialog", "256000"))
        self.label_4.setText(_translate("Dialog", "校验方式："))
        self.cbbParity.setItemText(0, _translate("Dialog", "None"))
        self.cbbParity.setItemText(1, _translate("Dialog", "Even"))
        self.cbbParity.setItemText(2, _translate("Dialog", "Odd"))
        self.cbbParity.setItemText(3, _translate("Dialog", "Mark"))
        self.cbbParity.setItemText(4, _translate("Dialog", "Space"))
        self.label_3.setText(_translate("Dialog", "数据位："))
        self.cbbDataBit.setItemText(0, _translate("Dialog", "5"))
        self.cbbDataBit.setItemText(1, _translate("Dialog", "6"))
        self.cbbDataBit.setItemText(2, _translate("Dialog", "7"))
        self.cbbDataBit.setItemText(3, _translate("Dialog", "8"))
        self.label_5.setText(_translate("Dialog", "停止位："))
        self.cbbStopBit.setItemText(0, _translate("Dialog", "1"))
        self.cbbStopBit.setItemText(1, _translate("Dialog", "1.5"))
        self.cbbStopBit.setItemText(2, _translate("Dialog", "2"))
        self.cbReSend.setText(_translate("Dialog", "Auto"))
        self.OpenSerialButton.setText(_translate("Dialog", "打开串口"))
        self.CloseSerialButton.setText(_translate("Dialog", "关闭串口"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "串口设置"))

