# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'child_model_select.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(503, 396)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.modelListLabel = QtWidgets.QLabel(self.centralwidget)
        self.modelListLabel.setGeometry(QtCore.QRect(30, 10, 181, 20))
        self.modelListLabel.setObjectName("modelListLabel")
        self.okModelSelectPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.okModelSelectPushButton.setGeometry(QtCore.QRect(210, 320, 75, 23))
        self.okModelSelectPushButton.setObjectName("okModelSelectPushButton")
        self.modelTableView = QtWidgets.QTableView(self.centralwidget)
        self.modelTableView.setGeometry(QtCore.QRect(30, 40, 441, 271))
        self.modelTableView.setObjectName("modelTableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 503, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.modelListLabel.setText(_translate("MainWindow", "模型列表"))
        self.okModelSelectPushButton.setText(_translate("MainWindow", "确定"))
