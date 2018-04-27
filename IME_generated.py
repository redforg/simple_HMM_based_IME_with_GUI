# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IME.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(854, 629)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.InputBox = QtWidgets.QLineEdit(self.centralwidget)
        self.InputBox.setGeometry(QtCore.QRect(140, 320, 611, 51))
        self.InputBox.setObjectName("InputBox")
        self.Result = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Result.setGeometry(QtCore.QRect(130, 10, 1491, 261))
        self.Result.setObjectName("Result")
        self.candidate = QtWidgets.QLineEdit(self.centralwidget)
        self.candidate.setGeometry(QtCore.QRect(0, 450, 1631, 101))
        self.candidate.setObjectName("candidate")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 70, 141, 91))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 320, 131, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 410, 108, 24))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 854, 30))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiontrain = QtWidgets.QAction(MainWindow)
        self.actiontrain.setObjectName("actiontrain")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.actionload = QtWidgets.QAction(MainWindow)
        self.actionload.setObjectName("actionload")
        self.menu.addAction(self.actiontrain)
        self.menu.addAction(self.actionload)
        self.menu.addAction(self.actionabout)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.InputBox.returnPressed.connect(MainWindow.mysetfocus)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "银河系航洋输入法 by ZYH"))
        self.InputBox.setText(_translate("MainWindow", "在此输入拼音"))
        self.label.setText(_translate("MainWindow", "已输入："))
        self.label_2.setText(_translate("MainWindow", "在此输入："))
        self.label_3.setText(_translate("MainWindow", "候选词："))
        self.menu.setTitle(_translate("MainWindow", "设置"))
        self.actiontrain.setText(_translate("MainWindow", "训练"))
        self.actionabout.setText(_translate("MainWindow", "关于"))
        self.actionload.setText(_translate("MainWindow", "载入"))

