# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'child_camera_storge.ui'
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
        self.historyStorageListView = QtWidgets.QListView(self.centralwidget)
        self.historyStorageListView.setGeometry(QtCore.QRect(70, 110, 256, 192))
        self.historyStorageListView.setObjectName("historyStorageListView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 80, 54, 12))
        self.label.setObjectName("label")
        self.createNewFilePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.createNewFilePushButton.setGeometry(QtCore.QRect(80, 320, 75, 23))
        self.createNewFilePushButton.setObjectName("createNewFilePushButton")
        self.openHistoryFilePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.openHistoryFilePushButton.setGeometry(QtCore.QRect(280, 320, 75, 23))
        self.openHistoryFilePushButton.setObjectName("openHistoryFilePushButton")
        self.deleteOldFilePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteOldFilePushButton.setGeometry(QtCore.QRect(190, 320, 75, 23))
        self.deleteOldFilePushButton.setObjectName("deleteOldFilePushButton")
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
        self.label.setText(_translate("MainWindow", "历史文件"))
        self.createNewFilePushButton.setText(_translate("MainWindow", "创新新文件"))
        self.openHistoryFilePushButton.setText(_translate("MainWindow", "打开"))
        self.deleteOldFilePushButton.setText(_translate("MainWindow", "删除文件"))
