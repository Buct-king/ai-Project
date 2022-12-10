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
        icon8.addPixmap(QtGui.QPixmap("../../resource/跨进icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.annotationPushButton = QtWidgets.QPushButton(self.tab_2)
        self.annotationPushButton.setGeometry(QtCore.QRect(860, 10, 81, 31))
        self.annotationPushButton.setStyleSheet("QPushButton{border-radius:10px;border: 2px groove gray;background-color: rgb(182, 182, 182);}\n"
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
        self.annotationPushButton.setIcon(icon1)
        self.annotationPushButton.setObjectName("annotationPushButton")
        self.deleteModelPushButton = QtWidgets.QPushButton(self.tab_2)
        self.deleteModelPushButton.setGeometry(QtCore.QRect(230, 10, 81, 31))
        self.deleteModelPushButton.setStyleSheet("QPushButton{border-radius:10px;border: 2px groove gray;background-color: rgb(182, 182, 182);}\n"
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
        self.deleteModelPushButton.setIcon(icon1)
        self.deleteModelPushButton.setObjectName("deleteModelPushButton")
        self.importDatasetPushButton = QtWidgets.QPushButton(self.tab_2)
        self.importDatasetPushButton.setGeometry(QtCore.QRect(420, 10, 81, 31))
        self.importDatasetPushButton.setStyleSheet("QPushButton{border-radius:10px;border: 2px groove gray;background-color: rgb(182, 182, 182);}\n"
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
        self.importDatasetPushButton.setIcon(icon1)
        self.importDatasetPushButton.setObjectName("importDatasetPushButton")
        self.modelsListLabel = QtWidgets.QLabel(self.tab_2)
        self.modelsListLabel.setGeometry(QtCore.QRect(30, 20, 71, 31))
        self.modelsListLabel.setStyleSheet("font: 25 11pt \"Adobe 宋体 Std L\";\n"
"")
        self.modelsListLabel.setObjectName("modelsListLabel")
        self.trainingPushButton = QtWidgets.QPushButton(self.tab_2)
        self.trainingPushButton.setGeometry(QtCore.QRect(850, 410, 81, 41))
        self.trainingPushButton.setStyleSheet("QPushButton{border-radius:10px;border: 2px groove gray;background-color: rgb(182, 182, 182);}\n"
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
        self.trainingPushButton.setIcon(icon1)
        self.trainingPushButton.setObjectName("trainingPushButton")
        self.modelsTableView = QtWidgets.QTableView(self.tab_2)
        self.modelsTableView.setGeometry(QtCore.QRect(20, 50, 291, 351))
        self.modelsTableView.setStyleSheet("border-radius: 4px;  \n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0)")
        self.modelsTableView.setObjectName("modelsTableView")
        self.datasetTableView = QtWidgets.QTableView(self.tab_2)
        self.datasetTableView.setGeometry(QtCore.QRect(330, 50, 621, 351))
        self.datasetTableView.setStyleSheet("border-radius: 4px;  \n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0)")
        self.datasetTableView.setObjectName("datasetTableView")
        self.datasetLabel = QtWidgets.QLabel(self.tab_2)
        self.datasetLabel.setGeometry(QtCore.QRect(330, 20, 71, 21))
        self.datasetLabel.setStyleSheet("font: 25 11pt \"Adobe 宋体 Std L\";\n"
"")
        self.datasetLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.datasetLabel.setObjectName("datasetLabel")
        self.importAnnotationPushButton = QtWidgets.QPushButton(self.tab_2)
        self.importAnnotationPushButton.setGeometry(QtCore.QRect(20, 420, 91, 31))
        self.importAnnotationPushButton.setStyleSheet("QPushButton{border-radius:10px;border: 2px groove gray;background-color: rgb(182, 182, 182);}\n"
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
        self.importAnnotationPushButton.setIcon(icon1)
        self.importAnnotationPushButton.setObjectName("importAnnotationPushButton")
        self.annotationLabel = QtWidgets.QLabel(self.tab_2)
        self.annotationLabel.setGeometry(QtCore.QRect(330, 420, 121, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.annotationLabel.sizePolicy().hasHeightForWidth())
        self.annotationLabel.setSizePolicy(sizePolicy)
        self.annotationLabel.setStyleSheet("font: 25 11pt \"Adobe 宋体 Std L\";\n"
"background-color: rgb(173, 173, 173);\n"
"border-radius: 8px;   ")
        self.annotationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.annotationLabel.setObjectName("annotationLabel")
        self.annotationShowLabel = QtWidgets.QLabel(self.tab_2)
        self.annotationShowLabel.setGeometry(QtCore.QRect(460, 420, 261, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.annotationShowLabel.sizePolicy().hasHeightForWidth())
        self.annotationShowLabel.setSizePolicy(sizePolicy)
        self.annotationShowLabel.setStyleSheet("")
        self.annotationShowLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.annotationShowLabel.setObjectName("annotationShowLabel")
        self.tabWidget.addTab(self.tab_2, "")
        self.settingPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingPushButton.setGeometry(QtCore.QRect(880, 5, 41, 28))
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
        self.annotationPushButton.setText(_translate("MainWindow", "标注"))
        self.deleteModelPushButton.setText(_translate("MainWindow", "删除模型"))
        self.importDatasetPushButton.setText(_translate("MainWindow", "导入数据集"))
        self.modelsListLabel.setText(_translate("MainWindow", "模型列表"))
        self.trainingPushButton.setText(_translate("MainWindow", "训练"))
        self.datasetLabel.setText(_translate("MainWindow", "数据集"))
        self.importAnnotationPushButton.setText(_translate("MainWindow", "导入标注信息"))
        self.annotationLabel.setText(_translate("MainWindow", "标注信息路径:"))
        self.annotationShowLabel.setText(_translate("MainWindow", "未导入！"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "识别训练"))
        self.settingPushButton.setText(_translate("MainWindow", "设置"))
from PyQt5.QtMultimediaWidgets import QVideoWidget
