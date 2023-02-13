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
        MainWindow.resize(1680, 951)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1680, 950))
        self.tabWidget.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.selectAllPushButton = QtWidgets.QPushButton(self.tab)
        self.selectAllPushButton.setGeometry(QtCore.QRect(1570, 10, 51, 21))
        self.selectAllPushButton.setStyleSheet("QPushButton{border-radius:10px;border: 2px groove gray;background-color: rgb(182, 182, 182);}\n"
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
        icon.addPixmap(QtGui.QPixmap("C:/Users/11795/.designer/resource/感叹号icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectAllPushButton.setIcon(icon)
        self.selectAllPushButton.setObjectName("selectAllPushButton")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(1130, 10, 71, 31))
        self.label.setStyleSheet("font: 25 11pt \"Adobe 宋体 Std L\";\n"
"")
        self.label.setObjectName("label")
        self.streamSelectTabWidget = QtWidgets.QTabWidget(self.tab)
        self.streamSelectTabWidget.setGeometry(QtCore.QRect(0, 0, 1101, 861))
        self.streamSelectTabWidget.setObjectName("streamSelectTabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.videoPlayer = QVideoWidget(self.tab_5)
        self.videoPlayer.setGeometry(QtCore.QRect(100, 40, 900, 600))
        self.videoPlayer.setStyleSheet("background-color: rgb(94, 94, 94);")
        self.videoPlayer.setObjectName("videoPlayer")
        self.horizontalSlider = QtWidgets.QSlider(self.tab_5)
        self.horizontalSlider.setGeometry(QtCore.QRect(50, 710, 1001, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.layoutWidget = QtWidgets.QWidget(self.tab_5)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 750, 761, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backOffPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.backOffPushButton.setStyleSheet("border-radius: 10px;  border: 2px groove gray;")
        self.backOffPushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../resource/快退icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backOffPushButton.setIcon(icon1)
        self.backOffPushButton.setObjectName("backOffPushButton")
        self.horizontalLayout.addWidget(self.backOffPushButton)
        self.lastPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.lastPushButton.setStyleSheet("border-radius: 10px;  border: 2px groove gray;")
        self.lastPushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../resource/上一个icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lastPushButton.setIcon(icon2)
        self.lastPushButton.setObjectName("lastPushButton")
        self.horizontalLayout.addWidget(self.lastPushButton)
        self.startPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.startPushButton.setStyleSheet("border-radius: 10px;  border: 2px groove gray;")
        self.startPushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../resource/开始.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startPushButton.setIcon(icon3)
        self.startPushButton.setObjectName("startPushButton")
        self.horizontalLayout.addWidget(self.startPushButton)
        self.nextPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.nextPushButton.setStyleSheet("border-radius: 10px;  border: 2px groove gray;")
        self.nextPushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../resource/下一个icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextPushButton.setIcon(icon4)
        self.nextPushButton.setObjectName("nextPushButton")
        self.horizontalLayout.addWidget(self.nextPushButton)
        self.fastForwardPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.fastForwardPushButton.setStyleSheet("border-radius: 10px;  border: 2px groove gray;")
        self.fastForwardPushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../resource/跨进icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fastForwardPushButton.setIcon(icon5)
        self.fastForwardPushButton.setObjectName("fastForwardPushButton")
        self.horizontalLayout.addWidget(self.fastForwardPushButton)
        self.oepnVideoPushButton = QtWidgets.QPushButton(self.tab_5)
        self.oepnVideoPushButton.setGeometry(QtCore.QRect(10, 770, 81, 41))
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:/Users/11795/.designer/resource/文件icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.oepnVideoPushButton.setIcon(icon6)
        self.oepnVideoPushButton.setCheckable(True)
        self.oepnVideoPushButton.setAutoExclusive(True)
        self.oepnVideoPushButton.setObjectName("oepnVideoPushButton")
        self.videoTimeLabel = QtWidgets.QLabel(self.tab_5)
        self.videoTimeLabel.setGeometry(QtCore.QRect(470, 670, 171, 21))
        self.videoTimeLabel.setObjectName("videoTimeLabel")
        self.AIDetectPushButton = QtWidgets.QPushButton(self.tab_5)
        self.AIDetectPushButton.setGeometry(QtCore.QRect(1030, 760, 51, 41))
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
        self.AIDetectPushButton.setIcon(icon6)
        self.AIDetectPushButton.setObjectName("AIDetectPushButton")
        self.streamSelectTabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.cameraLabel = QtWidgets.QLabel(self.tab_6)
        self.cameraLabel.setGeometry(QtCore.QRect(90, 20, 900, 600))
        self.cameraLabel.setStyleSheet("border-radius: 4px;  \n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0)")
        self.cameraLabel.setText("")
        self.cameraLabel.setObjectName("cameraLabel")
        self.openCameraPushButton = QtWidgets.QPushButton(self.tab_6)
        self.openCameraPushButton.setGeometry(QtCore.QRect(20, 690, 93, 28))
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
        self.cameraSelectPushButton.setGeometry(QtCore.QRect(210, 690, 71, 28))
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
        self.cameraStoragePushButton.setGeometry(QtCore.QRect(310, 690, 71, 28))
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
        self.snapshotTableView.setGeometry(QtCore.QRect(1130, 40, 491, 741))
        self.snapshotTableView.setObjectName("snapshotTableView")
        self.exportPushButton = QtWidgets.QPushButton(self.tab)
        self.exportPushButton.setGeometry(QtCore.QRect(1490, 800, 121, 41))
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
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("C:/Users/11795/.designer/resource/导出icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exportPushButton.setIcon(icon7)
        self.exportPushButton.setObjectName("exportPushButton")
        self.snapshotPushButton = QtWidgets.QPushButton(self.tab)
        self.snapshotPushButton.setGeometry(QtCore.QRect(1130, 800, 81, 41))
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
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("C:/Users/11795/.designer/resource/相机icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.snapshotPushButton.setIcon(icon8)
        self.snapshotPushButton.setObjectName("snapshotPushButton")
        self.deletePushButton = QtWidgets.QPushButton(self.tab)
        self.deletePushButton.setGeometry(QtCore.QRect(1230, 800, 81, 41))
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
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("C:/Users/11795/.designer/resource/删除icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deletePushButton.setIcon(icon9)
        self.deletePushButton.setObjectName("deletePushButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.annotationPushButton = QtWidgets.QPushButton(self.tab_2)
        self.annotationPushButton.setGeometry(QtCore.QRect(1500, 10, 81, 31))
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
        self.annotationPushButton.setIcon(icon9)
        self.annotationPushButton.setObjectName("annotationPushButton")
        self.deleteModelPushButton = QtWidgets.QPushButton(self.tab_2)
        self.deleteModelPushButton.setGeometry(QtCore.QRect(450, 10, 81, 31))
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
        self.deleteModelPushButton.setIcon(icon9)
        self.deleteModelPushButton.setObjectName("deleteModelPushButton")
        self.importDatasetPushButton = QtWidgets.QPushButton(self.tab_2)
        self.importDatasetPushButton.setGeometry(QtCore.QRect(980, 10, 81, 31))
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
        self.importDatasetPushButton.setIcon(icon9)
        self.importDatasetPushButton.setObjectName("importDatasetPushButton")
        self.modelsListLabel = QtWidgets.QLabel(self.tab_2)
        self.modelsListLabel.setGeometry(QtCore.QRect(90, 20, 71, 31))
        self.modelsListLabel.setStyleSheet("font: 25 11pt \"Adobe 宋体 Std L\";\n"
"")
        self.modelsListLabel.setObjectName("modelsListLabel")
        self.trainingPushButton = QtWidgets.QPushButton(self.tab_2)
        self.trainingPushButton.setGeometry(QtCore.QRect(1480, 820, 81, 41))
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
        self.trainingPushButton.setIcon(icon9)
        self.trainingPushButton.setObjectName("trainingPushButton")
        self.modelsTableView = QtWidgets.QTableView(self.tab_2)
        self.modelsTableView.setGeometry(QtCore.QRect(90, 50, 451, 761))
        self.modelsTableView.setStyleSheet("border-radius: 4px;  \n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0)")
        self.modelsTableView.setObjectName("modelsTableView")
        self.datasetTableView = QtWidgets.QTableView(self.tab_2)
        self.datasetTableView.setGeometry(QtCore.QRect(560, 50, 1031, 761))
        self.datasetTableView.setStyleSheet("border-radius: 4px;  \n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0)")
        self.datasetTableView.setObjectName("datasetTableView")
        self.datasetLabel = QtWidgets.QLabel(self.tab_2)
        self.datasetLabel.setGeometry(QtCore.QRect(550, 20, 71, 21))
        self.datasetLabel.setStyleSheet("font: 25 11pt \"Adobe 宋体 Std L\";\n"
"")
        self.datasetLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.datasetLabel.setObjectName("datasetLabel")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(130, 830, 641, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.parametersSetLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.parametersSetLabel.setObjectName("parametersSetLabel")
        self.horizontalLayout_2.addWidget(self.parametersSetLabel)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.epochsLineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.epochsLineEdit.setObjectName("epochsLineEdit")
        self.horizontalLayout_2.addWidget(self.epochsLineEdit)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.batchSizeLineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.batchSizeLineEdit.setObjectName("batchSizeLineEdit")
        self.horizontalLayout_2.addWidget(self.batchSizeLineEdit)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.workersLineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.workersLineEdit.setObjectName("workersLineEdit")
        self.horizontalLayout_2.addWidget(self.workersLineEdit)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1680, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionselect_model = QtWidgets.QAction(MainWindow)
        self.actionselect_model.setObjectName("actionselect_model")
        self.actionselect_fps = QtWidgets.QAction(MainWindow)
        self.actionselect_fps.setObjectName("actionselect_fps")
        self.actionSetModel = QtWidgets.QAction(MainWindow)
        self.actionSetModel.setObjectName("actionSetModel")
        self.actionDetectFps = QtWidgets.QAction(MainWindow)
        self.actionDetectFps.setObjectName("actionDetectFps")
        self.actionCovertVideo = QtWidgets.QAction(MainWindow)
        self.actionCovertVideo.setObjectName("actionCovertVideo")
        self.menu.addAction(self.actionSetModel)
        self.menu.addAction(self.actionDetectFps)
        self.menu.addAction(self.actionCovertVideo)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.streamSelectTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectAllPushButton.setText(_translate("MainWindow", "全选"))
        self.label.setText(_translate("MainWindow", "快照记录"))
        self.oepnVideoPushButton.setText(_translate("MainWindow", "打开..."))
        self.videoTimeLabel.setText(_translate("MainWindow", "00：00：00 / 00：00：00"))
        self.AIDetectPushButton.setText(_translate("MainWindow", "AI检测"))
        self.streamSelectTabWidget.setTabText(self.streamSelectTabWidget.indexOf(self.tab_5), _translate("MainWindow", "视频"))
        self.openCameraPushButton.setText(_translate("MainWindow", "打开摄像头"))
        self.cameraSelectPushButton.setText(_translate("MainWindow", "设备选择"))
        self.cameraStoragePushButton.setText(_translate("MainWindow", "存储设置"))
        self.streamSelectTabWidget.setTabText(self.streamSelectTabWidget.indexOf(self.tab_6), _translate("MainWindow", "直播"))
        self.exportPushButton.setText(_translate("MainWindow", "导出当前列表"))
        self.snapshotPushButton.setText(_translate("MainWindow", "快照"))
        self.deletePushButton.setText(_translate("MainWindow", "删除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "缺陷检测"))
        self.annotationPushButton.setText(_translate("MainWindow", "标注"))
        self.deleteModelPushButton.setText(_translate("MainWindow", "删除模型"))
        self.importDatasetPushButton.setText(_translate("MainWindow", "导入数据集"))
        self.modelsListLabel.setText(_translate("MainWindow", "模型列表"))
        self.trainingPushButton.setText(_translate("MainWindow", "训练"))
        self.datasetLabel.setText(_translate("MainWindow", "数据集"))
        self.parametersSetLabel.setText(_translate("MainWindow", "参数设置"))
        self.label_2.setText(_translate("MainWindow", "epochs:"))
        self.epochsLineEdit.setText(_translate("MainWindow", "1"))
        self.label_4.setText(_translate("MainWindow", "batch_size:"))
        self.batchSizeLineEdit.setText(_translate("MainWindow", "2"))
        self.label_5.setText(_translate("MainWindow", "workers:"))
        self.workersLineEdit.setText(_translate("MainWindow", "8"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "识别训练"))
        self.menu.setTitle(_translate("MainWindow", "设置"))
        self.actionselect_model.setText(_translate("MainWindow", "模型设置"))
        self.actionselect_fps.setText(_translate("MainWindow", "检测频率设置"))
        self.actionSetModel.setText(_translate("MainWindow", "模型设置"))
        self.actionDetectFps.setText(_translate("MainWindow", "检测频率设置"))
        self.actionCovertVideo.setText(_translate("MainWindow", "视频格式转换"))
from PyQt5.QtMultimediaWidgets import QVideoWidget
