# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'child_covert_viedo.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(448, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 121, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.openVideoPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.openVideoPushButton.setGeometry(QtCore.QRect(160, 100, 75, 23))
        self.openVideoPushButton.setObjectName("openVideoPushButton")
        self.covertPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.covertPushButton.setGeometry(QtCore.QRect(150, 310, 101, 23))
        self.covertPushButton.setObjectName("covertPushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 448, 23))
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
        self.label.setText(_translate("MainWindow", "转换视频格式"))
        self.openVideoPushButton.setText(_translate("MainWindow", "打开"))
        self.covertPushButton.setText(_translate("MainWindow", "转换"))
