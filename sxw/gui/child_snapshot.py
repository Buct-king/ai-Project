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
        self.iamgeLabel.setGeometry(QtCore.QRect(30, 50, 480, 320))
        self.iamgeLabel.setObjectName("iamgeLabel")
        self.saveSnapshotPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveSnapshotPushButton.setGeometry(QtCore.QRect(660, 420, 93, 28))
        self.saveSnapshotPushButton.setObjectName("saveSnapshotPushButton")
        self.cancelPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelPushButton.setGeometry(QtCore.QRect(830, 420, 93, 28))
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(670, 270, 72, 15))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(670, 300, 241, 101))
        self.textEdit.setObjectName("textEdit")
        self.snapshotLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotLabel.setGeometry(QtCore.QRect(670, 60, 72, 15))
        self.snapshotLabel.setObjectName("snapshotLabel")
        self.snapshotIDLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.snapshotIDLineEdit.setGeometry(QtCore.QRect(670, 90, 113, 21))
        self.snapshotIDLineEdit.setObjectName("snapshotIDLineEdit")
        self.snapshotVideoInfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotVideoInfoLabel.setGeometry(QtCore.QRect(670, 130, 72, 15))
        self.snapshotVideoInfoLabel.setObjectName("snapshotVideoInfoLabel")
        self.snapshotVideoInfoShowLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotVideoInfoShowLabel.setGeometry(QtCore.QRect(670, 150, 231, 16))
        self.snapshotVideoInfoShowLabel.setObjectName("snapshotVideoInfoShowLabel")
        self.snapshotVideoTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotVideoTimeLabel.setGeometry(QtCore.QRect(670, 170, 72, 15))
        self.snapshotVideoTimeLabel.setObjectName("snapshotVideoTimeLabel")
        self.snapshotVideoTimeShowLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotVideoTimeShowLabel.setGeometry(QtCore.QRect(670, 190, 251, 16))
        self.snapshotVideoTimeShowLabel.setObjectName("snapshotVideoTimeShowLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 988, 26))
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
        self.snapshotLabel.setText(_translate("MainWindow", "快照编号"))
        self.snapshotVideoInfoLabel.setText(_translate("MainWindow", "视频信息"))
        self.snapshotVideoInfoShowLabel.setText(_translate("MainWindow", "xxxxx"))
        self.snapshotVideoTimeLabel.setText(_translate("MainWindow", "视频内时间"))
        self.snapshotVideoTimeShowLabel.setText(_translate("MainWindow", "xxxxx"))
