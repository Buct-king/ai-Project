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
        MainWindow.resize(500, 600)
        MainWindow.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.searchPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchPushButton.setGeometry(QtCore.QRect(260, 510, 93, 36))
        self.searchPushButton.setStyleSheet("QPushButton{background-color: #CCCCCC;}\n"
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
        self.videosHistoryListView.setGeometry(QtCore.QRect(40, 50, 421, 451))
        self.videosHistoryListView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.videosHistoryListView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.videosHistoryListView.setObjectName("videosHistoryListView")
        self.openVedioPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.openVedioPushButton.setGeometry(QtCore.QRect(360, 510, 93, 36))
        self.openVedioPushButton.setStyleSheet("QPushButton{background-color: #CCCCCC;}\n"
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
        self.label.setGeometry(QtCore.QRect(40, 28, 91, 21))
        self.label.setStyleSheet("font: 25 11pt \"Adobe 宋体 Std L\";")
        self.label.setObjectName("label")
        self.deletePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.deletePushButton.setGeometry(QtCore.QRect(437, 25, 20, 20))
        self.deletePushButton.setStyleSheet("QPushButton {\n"
"    background-color:  #F2F2F2;\n"
"border:none;\n"
"color: #CCCCCC;\n"
"border-radius: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ABABAB;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:#848484;\n"
"}\n"
"border:none;")
        self.deletePushButton.setText("")
        self.deletePushButton.setObjectName("deletePushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "视频选择"))
        self.searchPushButton.setText(_translate("MainWindow", "浏览"))
        self.openVedioPushButton.setText(_translate("MainWindow", "打开"))
        self.label.setText(_translate("MainWindow", "历史视频"))
