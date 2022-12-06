# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'child_snapshot.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import child_sanpshot_addition_ui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(988, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.iamgeLabel = child_sanpshot_addition_ui.MyLabel(self.centralwidget)
        self.iamgeLabel.setGeometry(QtCore.QRect(30, 50, 551, 391))
        self.iamgeLabel.setObjectName("iamgeLabel")
        self.saveSnapshotPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveSnapshotPushButton.setGeometry(QtCore.QRect(700, 420, 93, 28))
        self.saveSnapshotPushButton.setStyleSheet("QPushButton{border-radius:10px;border: 2px groove gray;background-color: rgb(182, 182, 182);}\n"
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
        self.saveSnapshotPushButton.setObjectName("saveSnapshotPushButton")
        self.cancelPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelPushButton.setGeometry(QtCore.QRect(830, 420, 93, 28))
        self.cancelPushButton.setStyleSheet("QPushButton{border-radius:10px;border: 2px groove gray;background-color: rgb(182, 182, 182);}\n"
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
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(670, 230, 72, 25))
        self.label.setStyleSheet("font: 25 11pt \"Adobe 宋体 Std L\";\n"
"background-color: rgb(173, 173, 173);\n"
"border-radius: 4px;   ")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(674, 280, 231, 81))
        self.textEdit.setStyleSheet("border-radius: 4px;  \n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0)")
        self.textEdit.setObjectName("textEdit")
        self.snapshotVideoInfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotVideoInfoLabel.setGeometry(QtCore.QRect(670, 90, 72, 25))
        self.snapshotVideoInfoLabel.setStyleSheet("font: 25 11pt \"Adobe 宋体 Std L\";\n"
"background-color: rgb(173, 173, 173);\n"
"border-radius: 4px;   ")
        self.snapshotVideoInfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.snapshotVideoInfoLabel.setObjectName("snapshotVideoInfoLabel")
        self.snapshotVideoInfoShowLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotVideoInfoShowLabel.setGeometry(QtCore.QRect(674, 125, 231, 21))
        self.snapshotVideoInfoShowLabel.setObjectName("snapshotVideoInfoShowLabel")
        self.snapshotVideoTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotVideoTimeLabel.setGeometry(QtCore.QRect(670, 160, 91, 25))
        self.snapshotVideoTimeLabel.setStyleSheet("font: 25 11pt \"Adobe 宋体 Std L\";\n"
"background-color: rgb(173, 173, 173);\n"
"border-radius: 4px;   ")
        self.snapshotVideoTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.snapshotVideoTimeLabel.setObjectName("snapshotVideoTimeLabel")
        self.snapshotVideoTimeShowLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotVideoTimeShowLabel.setGeometry(QtCore.QRect(674, 200, 251, 21))
        self.snapshotVideoTimeShowLabel.setObjectName("snapshotVideoTimeShowLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 988, 23))
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
        self.iamgeLabel.setText(_translate("MainWindow", "TextLabel"))
        self.saveSnapshotPushButton.setText(_translate("MainWindow", "保存快照"))
        self.cancelPushButton.setText(_translate("MainWindow", "取消"))
        self.label.setText(_translate("MainWindow", "添加备注"))
        self.snapshotVideoInfoLabel.setText(_translate("MainWindow", "视频信息"))
        self.snapshotVideoInfoShowLabel.setText(_translate("MainWindow", "test"))
        self.snapshotVideoTimeLabel.setText(_translate("MainWindow", "视频内时间"))
        self.snapshotVideoTimeShowLabel.setText(_translate("MainWindow", "03：02"))
