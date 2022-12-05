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
        self.lastSnapshotPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.lastSnapshotPushButton.setGeometry(QtCore.QRect(50, 450, 93, 28))
        self.lastSnapshotPushButton.setObjectName("lastSnapshotPushButton")
        self.snapshotIDLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotIDLabel.setGeometry(QtCore.QRect(700, 50, 72, 15))
        self.snapshotIDLabel.setObjectName("snapshotIDLabel")
        self.snapshotNoteLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotNoteLabel.setGeometry(QtCore.QRect(700, 210, 72, 15))
        self.snapshotNoteLabel.setObjectName("snapshotNoteLabel")
        self.snapshotVideoInfoShowLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotVideoInfoShowLabel.setGeometry(QtCore.QRect(700, 130, 231, 16))
        self.snapshotVideoInfoShowLabel.setObjectName("snapshotVideoInfoShowLabel")
        self.snapshotVideoTimeShowLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotVideoTimeShowLabel.setGeometry(QtCore.QRect(700, 180, 251, 16))
        self.snapshotVideoTimeShowLabel.setObjectName("snapshotVideoTimeShowLabel")
        self.cancelPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelPushButton.setGeometry(QtCore.QRect(860, 450, 93, 28))
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.snapshotNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotNameLabel.setGeometry(QtCore.QRect(700, 100, 72, 15))
        self.snapshotNameLabel.setObjectName("snapshotNameLabel")
        self.iamgeLabel = QtWidgets.QLabel(self.centralwidget)
        self.iamgeLabel.setGeometry(QtCore.QRect(60, 40, 551, 391))
        self.iamgeLabel.setObjectName("iamgeLabel")
        self.snapshotVideoTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotVideoTimeLabel.setGeometry(QtCore.QRect(700, 160, 72, 15))
        self.snapshotVideoTimeLabel.setObjectName("snapshotVideoTimeLabel")
        self.snapshotIDShowLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotIDShowLabel.setGeometry(QtCore.QRect(700, 70, 231, 16))
        self.snapshotIDShowLabel.setObjectName("snapshotIDShowLabel")
        self.nextSnapshotPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextSnapshotPushButton.setGeometry(QtCore.QRect(420, 450, 93, 28))
        self.nextSnapshotPushButton.setObjectName("nextSnapshotPushButton")
        self.snapshotNoteShowLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotNoteShowLabel.setGeometry(QtCore.QRect(700, 250, 211, 131))
        self.snapshotNoteShowLabel.setObjectName("snapshotNoteShowLabel")
        self.snapshotTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotTimeLabel.setGeometry(QtCore.QRect(690, 380, 111, 16))
        self.snapshotTimeLabel.setObjectName("snapshotTimeLabel")
        self.snapshotTimeShowLabel = QtWidgets.QLabel(self.centralwidget)
        self.snapshotTimeShowLabel.setGeometry(QtCore.QRect(690, 400, 251, 16))
        self.snapshotTimeShowLabel.setObjectName("snapshotTimeShowLabel")
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
        self.lastSnapshotPushButton.setText(_translate("MainWindow", "上一条"))
        self.snapshotIDLabel.setText(_translate("MainWindow", "快照编号"))
        self.snapshotNoteLabel.setText(_translate("MainWindow", "备注"))
        self.snapshotVideoInfoShowLabel.setText(_translate("MainWindow", "xxxxx"))
        self.snapshotVideoTimeShowLabel.setText(_translate("MainWindow", "xxxxx"))
        self.cancelPushButton.setText(_translate("MainWindow", "关闭"))
        self.snapshotNameLabel.setText(_translate("MainWindow", "快照名称"))
        self.iamgeLabel.setText(_translate("MainWindow", "TextLabel"))
        self.snapshotVideoTimeLabel.setText(_translate("MainWindow", "视频内时间"))
        self.snapshotIDShowLabel.setText(_translate("MainWindow", "xxxxx"))
        self.nextSnapshotPushButton.setText(_translate("MainWindow", "下一条"))
        self.snapshotNoteShowLabel.setText(_translate("MainWindow", "TextLabel"))
        self.snapshotTimeLabel.setText(_translate("MainWindow", "快照时间"))
        self.snapshotTimeShowLabel.setText(_translate("MainWindow", "xxxxx"))
