# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fault_detection.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(975, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 991, 491))
        self.tabWidget.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.exportPushButton = QtWidgets.QPushButton(self.tab)
        self.exportPushButton.setGeometry(QtCore.QRect(790, 350, 121, 41))
        self.exportPushButton.setStyleSheet("QPushButton{border-radius:10px;border: 2px groove gray;background-color: rgb(182, 182, 182);}\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/11795/.designer/resource/导出icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exportPushButton.setIcon(icon)
        self.exportPushButton.setObjectName("exportPushButton")
        self.deletePushButton = QtWidgets.QPushButton(self.tab)
        self.deletePushButton.setGeometry(QtCore.QRect(590, 350, 81, 41))
        self.deletePushButton.setStyleSheet("QPushButton{border-radius:10px;border: 2px groove gray;background-color: rgb(182, 182, 182);}\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/11795/.designer/resource/删除icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deletePushButton.setIcon(icon1)
        self.deletePushButton.setObjectName("deletePushButton")
        self.detailPushButton = QtWidgets.QPushButton(self.tab)
        self.detailPushButton.setGeometry(QtCore.QRect(690, 350, 81, 41))
        self.detailPushButton.setStyleSheet("QPushButton{border-radius:10px;border: 2px groove gray;background-color: rgb(182, 182, 182);}\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/11795/.designer/resource/感叹号icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.detailPushButton.setIcon(icon2)
        self.detailPushButton.setObjectName("detailPushButton")
        self.snapshotPushButton = QtWidgets.QPushButton(self.tab)
        self.snapshotPushButton.setGeometry(QtCore.QRect(500, 350, 81, 41))
        self.snapshotPushButton.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    border: 2px groove gray;\n"
"    background-color: rgb(238, 0, 0);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(238, 92, 66);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(139, 0, 0);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/11795/.designer/resource/相机icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.snapshotPushButton.setIcon(icon3)
        self.snapshotPushButton.setObjectName("snapshotPushButton")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(550, 20, 71, 31))
        self.label.setStyleSheet("font: 25 11pt \"Adobe 宋体 Std L\";\n"
"")
        self.label.setObjectName("label")
        self.streamSelectTabWidget = QtWidgets.QTabWidget(self.tab)
        self.streamSelectTabWidget.setGeometry(QtCore.QRect(0, 0, 481, 411))
        self.streamSelectTabWidget.setObjectName("streamSelectTabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.videoPlayer = QVideoWidget(self.tab_5)
        self.videoPlayer.setGeometry(QtCore.QRect(0, 0, 511, 291))
        self.videoPlayer.setStyleSheet("background-color: rgb(94, 94, 94);")
        self.videoPlayer.setObjectName("videoPlayer")
        self.horizontalSlider = QtWidgets.QSlider(self.tab_5)
        self.horizontalSlider.setGeometry(QtCore.QRect(110, 320, 271, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.layoutWidget = QtWidgets.QWidget(self.tab_5)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 350, 312, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backOffPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.backOffPushButton.setStyleSheet("border-radius: 10px;  border: 2px groove gray;")
        self.backOffPushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../resource/快退icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backOffPushButton.setIcon(icon4)
        self.backOffPushButton.setObjectName("backOffPushButton")
        self.horizontalLayout.addWidget(self.backOffPushButton)
        self.lastPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.lastPushButton.setStyleSheet("border-radius: 10px;  border: 2px groove gray;")
        self.lastPushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../resource/上一个icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lastPushButton.setIcon(icon5)
        self.lastPushButton.setObjectName("lastPushButton")
        self.horizontalLayout.addWidget(self.lastPushButton)
        self.startPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.startPushButton.setStyleSheet("border-radius: 10px;  border: 2px groove gray;")
        self.startPushButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../../resource/开始.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startPushButton.setIcon(icon6)
        self.startPushButton.setObjectName("startPushButton")
        self.horizontalLayout.addWidget(self.startPushButton)
        self.nextPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.nextPushButton.setStyleSheet("border-radius: 10px;  border: 2px groove gray;")
        self.nextPushButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../../resource/下一个icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextPushButton.setIcon(icon7)
        self.nextPushButton.setObjectName("nextPushButton")
        self.horizontalLayout.addWidget(self.nextPushButton)
        self.fastForwardPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.fastForwardPushButton.setStyleSheet("border-radius: 10px;  border: 2px groove gray;")
        self.fastForwardPushButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../../resource/快进icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fastForwardPushButton.setIcon(icon8)
        self.fastForwardPushButton.setObjectName("fastForwardPushButton")
        self.horizontalLayout.addWidget(self.fastForwardPushButton)
        self.oepnVideoPushButton = QtWidgets.QPushButton(self.tab_5)
        self.oepnVideoPushButton.setGeometry(QtCore.QRect(10, 320, 81, 41))
        self.oepnVideoPushButton.setStyleSheet("QPushButton{border-radius:10px;border: 2px groove gray;background-color: rgb(182, 182, 182);}\n"
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
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("C:/Users/11795/.designer/resource/文件icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.oepnVideoPushButton.setIcon(icon9)
        self.oepnVideoPushButton.setCheckable(True)
        self.oepnVideoPushButton.setAutoExclusive(True)
        self.oepnVideoPushButton.setObjectName("oepnVideoPushButton")
        self.videoTimeLabel = QtWidgets.QLabel(self.tab_5)
        self.videoTimeLabel.setGeometry(QtCore.QRect(160, 300, 171, 21))
        self.videoTimeLabel.setObjectName("videoTimeLabel")
        self.AIDetectPushButton = QtWidgets.QPushButton(self.tab_5)
        self.AIDetectPushButton.setGeometry(QtCore.QRect(420, 300, 51, 41))
        self.AIDetectPushButton.setStyleSheet("QPushButton{border-radius:10px;border: 2px groove gray;background-color: rgb(182, 182, 182);}\n"
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
        self.AIDetectPushButton.setIcon(icon9)
        self.AIDetectPushButton.setObjectName("AIDetectPushButton")
        self.streamSelectTabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.cameraLabel = QtWidgets.QLabel(self.tab_6)
        self.cameraLabel.setGeometry(QtCore.QRect(0, 0, 461, 291))
        self.cameraLabel.setText("")
        self.cameraLabel.setObjectName("cameraLabel")
        self.openCameraPushButton = QtWidgets.QPushButton(self.tab_6)
        self.openCameraPushButton.setGeometry(QtCore.QRect(60, 330, 93, 28))
        self.openCameraPushButton.setStyleSheet("QPushButton{border-radius:10px;border: 2px groove gray;background-color: rgb(182, 182, 182);}\n"
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
        self.openCameraPushButton.setObjectName("openCameraPushButton")
        self.cameraSelectPushButton = QtWidgets.QPushButton(self.tab_6)
        self.cameraSelectPushButton.setGeometry(QtCore.QRect(290, 340, 71, 28))
        self.cameraSelectPushButton.setStyleSheet("QPushButton{border-radius:10px;border: 2px groove gray;background-color: rgb(182, 182, 182);}\n"
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
        self.cameraSelectPushButton.setObjectName("cameraSelectPushButton")
        self.cameraStoragePushButton = QtWidgets.QPushButton(self.tab_6)
        self.cameraStoragePushButton.setGeometry(QtCore.QRect(380, 340, 71, 28))
        self.cameraStoragePushButton.setStyleSheet("QPushButton{border-radius:10px;border: 2px groove gray;background-color: rgb(182, 182, 182);}\n"
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
        self.cameraStoragePushButton.setObjectName("cameraStoragePushButton")
        self.streamSelectTabWidget.addTab(self.tab_6, "")
        self.snapshotTableView = QtWidgets.QTableView(self.tab)
        self.snapshotTableView.setGeometry(QtCore.QRect(550, 50, 361, 261))
        self.snapshotTableView.setObjectName("snapshotTableView")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.importImageLabel = QtWidgets.QLabel(self.tab_2)
        self.importImageLabel.setGeometry(QtCore.QRect(50, 40, 401, 341))
        self.importImageLabel.setObjectName("importImageLabel")
        self.importPicInfosTableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.importPicInfosTableWidget.setGeometry(QtCore.QRect(40, 430, 381, 31))
        self.importPicInfosTableWidget.setObjectName("importPicInfosTableWidget")
        self.importPicInfosTableWidget.setColumnCount(3)
        self.importPicInfosTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.importPicInfosTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.importPicInfosTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.importPicInfosTableWidget.setHorizontalHeaderItem(2, item)
        self.importPicNameLabel = QtWidgets.QLabel(self.tab_2)
        self.importPicNameLabel.setGeometry(QtCore.QRect(50, 400, 81, 21))
        self.importPicNameLabel.setObjectName("importPicNameLabel")
        self.importPicFaultsTableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.importPicFaultsTableWidget.setEnabled(True)
        self.importPicFaultsTableWidget.setGeometry(QtCore.QRect(530, 110, 391, 231))
        self.importPicFaultsTableWidget.setShowGrid(False)
        self.importPicFaultsTableWidget.setObjectName("importPicFaultsTableWidget")
        self.importPicFaultsTableWidget.setColumnCount(3)
        self.importPicFaultsTableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.importPicFaultsTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.importPicFaultsTableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.importPicFaultsTableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.importPicFaultsTableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.importPicFaultsTableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.importPicFaultsTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.importPicFaultsTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.importPicFaultsTableWidget.setHorizontalHeaderItem(2, item)
        self.importPicPushButton = QtWidgets.QPushButton(self.tab_2)
        self.importPicPushButton.setGeometry(QtCore.QRect(860, 50, 81, 41))
        self.importPicPushButton.setStyleSheet("border-radius: 10px;  border: 2px groove gray;")
        self.importPicPushButton.setIcon(icon2)
        self.importPicPushButton.setObjectName("importPicPushButton")
        self.finishTrainingPushButton = QtWidgets.QPushButton(self.tab_2)
        self.finishTrainingPushButton.setGeometry(QtCore.QRect(870, 400, 81, 41))
        self.finishTrainingPushButton.setStyleSheet("border-radius: 10px;  border: 2px groove gray;")
        self.finishTrainingPushButton.setIcon(icon2)
        self.finishTrainingPushButton.setObjectName("finishTrainingPushButton")
        self.importPicFaultDetailPushButton = QtWidgets.QPushButton(self.tab_2)
        self.importPicFaultDetailPushButton.setGeometry(QtCore.QRect(760, 400, 81, 41))
        self.importPicFaultDetailPushButton.setStyleSheet("border-radius: 10px;  border: 2px groove gray;")
        self.importPicFaultDetailPushButton.setIcon(icon2)
        self.importPicFaultDetailPushButton.setObjectName("importPicFaultDetailPushButton")
        self.deleteImportPicFaultPicPushButton = QtWidgets.QPushButton(self.tab_2)
        self.deleteImportPicFaultPicPushButton.setGeometry(QtCore.QRect(660, 400, 81, 41))
        self.deleteImportPicFaultPicPushButton.setStyleSheet("border-radius: 10px;  border: 2px groove gray;")
        self.deleteImportPicFaultPicPushButton.setIcon(icon1)
        self.deleteImportPicFaultPicPushButton.setObjectName("deleteImportPicFaultPicPushButton")
        self.annotationPushButton = QtWidgets.QPushButton(self.tab_2)
        self.annotationPushButton.setGeometry(QtCore.QRect(640, 30, 81, 41))
        self.annotationPushButton.setStyleSheet("border-radius: 10px;  border: 2px groove gray;")
        self.annotationPushButton.setIcon(icon1)
        self.annotationPushButton.setObjectName("annotationPushButton")
        self.tabWidget.addTab(self.tab_2, "")
        self.settingPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingPushButton.setGeometry(QtCore.QRect(880, 10, 41, 28))
        self.settingPushButton.setObjectName("settingPushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 975, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.streamSelectTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exportPushButton.setText(_translate("MainWindow", "导出当前列表"))
        self.deletePushButton.setText(_translate("MainWindow", "删除"))
        self.detailPushButton.setText(_translate("MainWindow", "详情"))
        self.snapshotPushButton.setText(_translate("MainWindow", " 快照"))
        self.label.setText(_translate("MainWindow", "快照记录"))
        self.oepnVideoPushButton.setText(_translate("MainWindow", "打开..."))
        self.videoTimeLabel.setText(_translate("MainWindow", "00：00：00 / 00：00：00"))
        self.AIDetectPushButton.setText(_translate("MainWindow", "AI检测"))
        self.streamSelectTabWidget.setTabText(self.streamSelectTabWidget.indexOf(self.tab_5), _translate("MainWindow", "视频"))
        self.openCameraPushButton.setText(_translate("MainWindow", "打开摄像头"))
        self.cameraSelectPushButton.setText(_translate("MainWindow", "设备选择"))
        self.cameraStoragePushButton.setText(_translate("MainWindow", "存储设置"))
        self.streamSelectTabWidget.setTabText(self.streamSelectTabWidget.indexOf(self.tab_6), _translate("MainWindow", "直播"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "缺陷检测"))
        self.importImageLabel.setText(_translate("MainWindow", "TextLabel"))
        item = self.importPicInfosTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "JPEG"))
        item = self.importPicInfosTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "2930*1640"))
        item = self.importPicInfosTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "1.64MB"))
        self.importPicNameLabel.setText(_translate("MainWindow", "test.jpg"))
        self.importPicFaultsTableWidget.setSortingEnabled(False)
        item = self.importPicFaultsTableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.importPicFaultsTableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.importPicFaultsTableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.importPicFaultsTableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.importPicFaultsTableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.importPicFaultsTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.importPicFaultsTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "文件"))
        item = self.importPicFaultsTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "已训练"))
        self.importPicPushButton.setText(_translate("MainWindow", "导入图片"))
        self.finishTrainingPushButton.setText(_translate("MainWindow", "完成训练"))
        self.importPicFaultDetailPushButton.setText(_translate("MainWindow", "详情"))
        self.deleteImportPicFaultPicPushButton.setText(_translate("MainWindow", "删除"))
        self.annotationPushButton.setText(_translate("MainWindow", "标注"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "识别训练"))
        self.settingPushButton.setText(_translate("MainWindow", "设置"))
from PyQt5.QtMultimediaWidgets import QVideoWidget
