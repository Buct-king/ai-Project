# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'child_camera_select.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 333)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 181, 20))
        self.label.setObjectName("label")
        self.camerasListView = QtWidgets.QListView(self.centralwidget)
        self.camerasListView.setGeometry(QtCore.QRect(70, 40, 256, 192))
        self.camerasListView.setObjectName("camerasListView")
        self.okCameraSelectPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.okCameraSelectPushButton.setGeometry(QtCore.QRect(160, 250, 75, 23))
        self.okCameraSelectPushButton.setObjectName("okCameraSelectPushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 23))
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
        self.label.setText(_translate("MainWindow", "设备目录"))
        self.okCameraSelectPushButton.setText(_translate("MainWindow", "确定"))
