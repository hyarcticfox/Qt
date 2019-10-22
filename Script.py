# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Script.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Script(object):
    def setupUi(self, Script):
        Script.setObjectName("Script")
        Script.resize(598, 604)
        self.pushButtonCopy_1 = QtWidgets.QPushButton(Script)
        self.pushButtonCopy_1.setGeometry(QtCore.QRect(480, 100, 75, 23))
        self.pushButtonCopy_1.setObjectName("pushButtonCopy_1")
        self.layoutWidget = QtWidgets.QWidget(Script)
        self.layoutWidget.setGeometry(QtCore.QRect(320, 40, 141, 401))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEditInstruct1 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEditInstruct1.setObjectName("textEditInstruct1")
        self.verticalLayout_2.addWidget(self.textEditInstruct1)
        self.textEditInstruct2 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEditInstruct2.setObjectName("textEditInstruct2")
        self.verticalLayout_2.addWidget(self.textEditInstruct2)
        self.textEditInstruct3 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEditInstruct3.setObjectName("textEditInstruct3")
        self.verticalLayout_2.addWidget(self.textEditInstruct3)
        self.pushButtonCopy_2 = QtWidgets.QPushButton(Script)
        self.pushButtonCopy_2.setGeometry(QtCore.QRect(480, 220, 75, 23))
        self.pushButtonCopy_2.setObjectName("pushButtonCopy_2")
        self.layoutWidget_2 = QtWidgets.QWidget(Script)
        self.layoutWidget_2.setGeometry(QtCore.QRect(50, 40, 251, 401))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEditScript1 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEditScript1.setObjectName("textEditScript1")
        self.verticalLayout.addWidget(self.textEditScript1)
        self.textEditScript2 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEditScript2.setObjectName("textEditScript2")
        self.verticalLayout.addWidget(self.textEditScript2)
        self.textEditScript3 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEditScript3.setObjectName("textEditScript3")
        self.verticalLayout.addWidget(self.textEditScript3)
        self.pushButtonCopy_3 = QtWidgets.QPushButton(Script)
        self.pushButtonCopy_3.setGeometry(QtCore.QRect(480, 350, 75, 23))
        self.pushButtonCopy_3.setObjectName("pushButtonCopy_3")
        self.textTalent = QtWidgets.QTextBrowser(Script)
        self.textTalent.setGeometry(QtCore.QRect(50, 460, 501, 101))
        self.textTalent.setObjectName("textTalent")

        self.retranslateUi(Script)
        QtCore.QMetaObject.connectSlotsByName(Script)

    def retranslateUi(self, Script):
        _translate = QtCore.QCoreApplication.translate
        Script.setWindowTitle(_translate("Script", "宏"))
        self.pushButtonCopy_1.setText(_translate("Script", "复制"))
        self.pushButtonCopy_2.setText(_translate("Script", "复制"))
        self.pushButtonCopy_3.setText(_translate("Script", "复制"))
