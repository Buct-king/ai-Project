# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'child_snapshot_detail.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(984, 539)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.snapshotIDLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotIDLabel.setGeometry(QtCore.QRect(669, 46, 71, 25))
        self.snapshotIDLabel.setStyleSheet("font: 25 11pt \"Adobe 宋体 Std L\";\n"
"background-color: rgb(173, 173, 173);\n"
"border-radius: 4px;   ")
        self.snapshotIDLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.snapshotIDLabel.setObjectName("snapshotIDLabel")
        self.snapshotNoteLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotNoteLabel.setGeometry(QtCore.QRect(669, 240, 51, 25))
        self.snapshotNoteLabel.setStyleSheet("font: 25 11pt \"Adobe 宋体 Std L\";\n"
"background-color: rgb(173, 173, 173);\n"
"border-radius: 4px;   ")
        self.snapshotNoteLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.snapshotNoteLabel.setObjectName("snapshotNoteLabel")
        self.snapshotVideoInfoShowLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotVideoInfoShowLabel.setGeometry(QtCore.QRect(674, 144, 231, 21))
        self.snapshotVideoInfoShowLabel.setObjectName("snapshotVideoInfoShowLabel")
        self.snapshotVideoTimeShowLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotVideoTimeShowLabel.setGeometry(QtCore.QRect(674, 210, 251, 21))
        self.snapshotVideoTimeShowLabel.setObjectName("snapshotVideoTimeShowLabel")
        self.cancelPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelPushButton.setGeometry(QtCore.QRect(882, 447, 71, 31))
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
        self.snapshotNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotNameLabel.setGeometry(QtCore.QRect(669, 110, 71, 25))
        self.snapshotNameLabel.setStyleSheet("font: 25 11pt \"Adobe 宋体 Std L\";\n"
"background-color: rgb(173, 173, 173);\n"
"border-radius: 4px;   ")
        self.snapshotNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.snapshotNameLabel.setObjectName("snapshotNameLabel")
        self.iamgeLabel = QtWidgets.QLabel(self.centralwidget)
        self.iamgeLabel.setGeometry(QtCore.QRect(30, 30, 551, 391))
        self.iamgeLabel.setStyleSheet("border-radius: 4px;  \n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0)")
        self.iamgeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.iamgeLabel.setObjectName("iamgeLabel")
        self.snapshotVideoTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotVideoTimeLabel.setGeometry(QtCore.QRect(669, 176, 91, 25))
        self.snapshotVideoTimeLabel.setStyleSheet("font: 25 11pt \"Adobe 宋体 Std L\";\n"
"background-color: rgb(173, 173, 173);\n"
"border-radius: 4px;   ")
        self.snapshotVideoTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.snapshotVideoTimeLabel.setObjectName("snapshotVideoTimeLabel")
        self.snapshotIDShowLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotIDShowLabel.setGeometry(QtCore.QRect(674, 80, 101, 21))
        self.snapshotIDShowLabel.setStyleSheet("\n"
"border-radius: 4px;   \n"
"font: 25 11pt \"Adobe 宋体 Std L\";")
        self.snapshotIDShowLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.snapshotIDShowLabel.setObjectName("snapshotIDShowLabel")
        self.snapshotNoteShowLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotNoteShowLabel.setGeometry(QtCore.QRect(674, 283, 211, 91))
        self.snapshotNoteShowLabel.setStyleSheet("border-radius: 4px;  \n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0)")
        self.snapshotNoteShowLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.snapshotNoteShowLabel.setWordWrap(True)
        self.snapshotNoteShowLabel.setObjectName("snapshotNoteShowLabel")
        self.snapshotTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotTimeLabel.setGeometry(QtCore.QRect(669, 390, 71, 25))
        self.snapshotTimeLabel.setStyleSheet("font: 25 11pt \"Adobe 宋体 Std L\";\n"
"background-color: rgb(173, 173, 173);\n"
"border-radius: 4px;   ")
        self.snapshotTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.snapshotTimeLabel.setObjectName("snapshotTimeLabel")
        self.snapshotTimeShowLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotTimeShowLabel.setGeometry(QtCore.QRect(674, 423, 251, 21))
        self.snapshotTimeShowLabel.setObjectName("snapshotTimeShowLabel")
        self.lastPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.lastPushButton.setGeometry(QtCore.QRect(110, 440, 71, 31))
        self.lastPushButton.setStyleSheet("QPushButton{border-radius:10px;border: 2px groove gray;background-color: rgb(182, 182, 182);}\n"
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
        self.lastPushButton.setObjectName("lastPushButton")
        self.nextPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextPushButton.setGeometry(QtCore.QRect(400, 440, 71, 31))
        self.nextPushButton.setStyleSheet("QPushButton{border-radius:10px;border: 2px groove gray;background-color: rgb(182, 182, 182);}\n"
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
        self.nextPushButton.setObjectName("nextPushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 984, 23))
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
        self.snapshotIDLabel.setText(_translate("MainWindow", "快照编号"))
        self.snapshotNoteLabel.setText(_translate("MainWindow", "备注"))
        self.snapshotVideoInfoShowLabel.setText(_translate("MainWindow", "test"))
        self.snapshotVideoTimeShowLabel.setText(_translate("MainWindow", "03：22"))
        self.cancelPushButton.setText(_translate("MainWindow", "关闭"))
        self.snapshotNameLabel.setText(_translate("MainWindow", "快照名称"))
        self.iamgeLabel.setText(_translate("MainWindow", "TextLabel"))
        self.snapshotVideoTimeLabel.setText(_translate("MainWindow", "视频内时间"))
        self.snapshotIDShowLabel.setText(_translate("MainWindow", "1"))
        self.snapshotNoteShowLabel.setText(_translate("MainWindow", "TextLabeldsfsfsfsfsfsfsdfsdfsfsfweeweqwfwfwe"))
        self.snapshotTimeLabel.setText(_translate("MainWindow", "快照时间"))
        self.snapshotTimeShowLabel.setText(_translate("MainWindow", "2022-1-20"))
        self.lastPushButton.setText(_translate("MainWindow", "上一张"))
        self.nextPushButton.setText(_translate("MainWindow", "下一张"))
