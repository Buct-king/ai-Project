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
        MainWindow.resize(750, 600)
        MainWindow.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.historyStorageListView = QtWidgets.QListView(self.centralwidget)
        self.historyStorageListView.setGeometry(QtCore.QRect(395, 70, 275, 390))
        self.historyStorageListView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.historyStorageListView.setObjectName("historyStorageListView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(395, 45, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.createNewFilePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.createNewFilePushButton.setGeometry(QtCore.QRect(642, 48, 20, 20))
        self.createNewFilePushButton.setStyleSheet("QPushButton {\n"
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
        self.createNewFilePushButton.setText("")
        self.createNewFilePushButton.setObjectName("createNewFilePushButton")
        self.openHistoryFilePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.openHistoryFilePushButton.setGeometry(QtCore.QRect(610, 490, 93, 36))
        self.openHistoryFilePushButton.setStyleSheet("QPushButton{background-color: #CCCCCC;}\n"
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
        self.openHistoryFilePushButton.setObjectName("openHistoryFilePushButton")
        self.deleteOldFilePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteOldFilePushButton.setGeometry(QtCore.QRect(612, 48, 20, 20))
        self.deleteOldFilePushButton.setStyleSheet("QPushButton {\n"
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
        self.deleteOldFilePushButton.setText("")
        self.deleteOldFilePushButton.setObjectName("deleteOldFilePushButton")
        self.camerasListView = QtWidgets.QListView(self.centralwidget)
        self.camerasListView.setGeometry(QtCore.QRect(60, 70, 275, 390))
        self.camerasListView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.camerasListView.setObjectName("camerasListView")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 45, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "设备选择"))
        self.label.setText(_translate("MainWindow", "存储位置"))
        self.openHistoryFilePushButton.setText(_translate("MainWindow", "打开"))
        self.label_2.setText(_translate("MainWindow", "选择摄像机"))
