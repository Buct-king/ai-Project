# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'child.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(494, 344)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.searchPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchPushButton.setGeometry(QtCore.QRect(60, 230, 93, 41))
        self.searchPushButton.setStyleSheet("QPushButton{border-radius:10px;border: 2px groove gray;background-color: rgb(182, 182, 182);}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(193, 205, 205);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(131, 139, 139);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.searchPushButton.setObjectName("searchPushButton")
        self.videosHistoryListView = QtWidgets.QListView(self.centralwidget)
        self.videosHistoryListView.setGeometry(QtCore.QRect(10, 50, 256, 161))
        self.videosHistoryListView.setObjectName("videosHistoryListView")
        self.openVedioPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.openVedioPushButton.setGeometry(QtCore.QRect(340, 230, 93, 41))
        self.openVedioPushButton.setStyleSheet("QPushButton{border-radius:10px;border: 2px groove gray;background-color: rgb(182, 182, 182);}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(193, 205, 205);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(131, 139, 139);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.openVedioPushButton.setObjectName("openVedioPushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 14, 72, 21))
        self.label.setStyleSheet("font: 25 11pt \"Adobe 宋体 Std L\";")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 494, 23))
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
        self.searchPushButton.setText(_translate("MainWindow", "浏览"))
        self.openVedioPushButton.setText(_translate("MainWindow", "打开"))
        self.label.setText(_translate("MainWindow", "历史视频"))
