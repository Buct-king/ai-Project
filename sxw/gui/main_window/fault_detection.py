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
        MainWindow.resize(1920, 1046)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(16, 5, 1910, 1071))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabBar::tab{height:38}\n"
"QTabBar::tab{width:160}\n"
"\n"
"\n"
"\n"
"QTabBar::tab:selected {\n"
"background-color: #F2F2F2;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"background-color: #D7D9DF;\n"
"}\n"
"\n"
"QTabWidget {\n"
"border-top-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QWidget#tab,#tab_2{\n"
"background-color: #F2F2F2;\n"
"}")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(25, 25))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.selectAllPushButton = QtWidgets.QPushButton(self.tab)
        self.selectAllPushButton.setGeometry(QtCore.QRect(1470, 920, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectAllPushButton.setFont(font)
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
        icon.addPixmap(QtGui.QPixmap("C:/Users/11795/resource/chooses.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.selectAllPushButton.setIcon(icon)
        self.selectAllPushButton.setObjectName("selectAllPushButton")
        self.streamSelectTabWidget = QtWidgets.QTabWidget(self.tab)
        self.streamSelectTabWidget.setGeometry(QtCore.QRect(0, 0, 1451, 951))
        self.streamSelectTabWidget.setStyleSheet(" QWidget#tab_6,#tab_5{\n"
"    background-color: #F2F2F2;\n"
"}")
        self.streamSelectTabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.streamSelectTabWidget.setIconSize(QtCore.QSize(22, 22))
        self.streamSelectTabWidget.setObjectName("streamSelectTabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.videoPlayer = QVideoWidget(self.tab_5)
        self.videoPlayer.setGeometry(QtCore.QRect(0, 15, 1440, 810))
        self.videoPlayer.setStyleSheet("background-color: rgb(94, 94, 94);")
        self.videoPlayer.setObjectName("videoPlayer")
        self.horizontalSlider = QtWidgets.QSlider(self.tab_5)
        self.horizontalSlider.setGeometry(QtCore.QRect(130, 885, 1181, 20))
        self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal{ \n"
"height: 10px; \n"
"left: 0px; \n"
"right: 0px; \n"
"border:0px; \n"
"border-radius:6px; \n"
"background:#808080;\n"
"} \n"
"\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: #FFFFFF;\n"
"width: 14px;\n"
"height: 14px;\n"
"margin: -3px 0;\n"
"border-radius: 7px;\n"
"}\n"
"QSlider::sub-page:horizontal{\n"
"background:rgba(80,166,234,1);\n"
"}\n"
"")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.oepnVideoPushButton = QtWidgets.QPushButton(self.tab_5)
        self.oepnVideoPushButton.setGeometry(QtCore.QRect(34, 844, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.oepnVideoPushButton.setFont(font)
        self.oepnVideoPushButton.setStyleSheet("QPushButton {\n"
"    background-color:  #666666;\n"
"border:none;\n"
"color: #CCCCCC;\n"
"border-radius: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #525252;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:#525252;\n"
"}\n"
"border:none;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/11795/resource/open_file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.oepnVideoPushButton.setIcon(icon1)
        self.oepnVideoPushButton.setCheckable(True)
        self.oepnVideoPushButton.setAutoExclusive(True)
        self.oepnVideoPushButton.setObjectName("oepnVideoPushButton")
        self.videoTimeLabel = QtWidgets.QLabel(self.tab_5)
        self.videoTimeLabel.setGeometry(QtCore.QRect(40, 880, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.videoTimeLabel.setFont(font)
        self.videoTimeLabel.setStyleSheet("color: #CCCCCC;")
        self.videoTimeLabel.setObjectName("videoTimeLabel")
        self.label_3 = QtWidgets.QLabel(self.tab_5)
        self.label_3.setGeometry(QtCore.QRect(0, 825, 1440, 101))
        self.label_3.setStyleSheet("background-color: #666666;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.videoTimeLabel_2 = QtWidgets.QLabel(self.tab_5)
        self.videoTimeLabel_2.setGeometry(QtCore.QRect(1330, 880, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.videoTimeLabel_2.setFont(font)
        self.videoTimeLabel_2.setStyleSheet("color: #CCCCCC;")
        self.videoTimeLabel_2.setObjectName("videoTimeLabel_2")
        self.AIDetectPushButton = QtWidgets.QPushButton(self.tab_5)
        self.AIDetectPushButton.setGeometry(QtCore.QRect(1105, 844, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AIDetectPushButton.setFont(font)
        self.AIDetectPushButton.setStyleSheet("QPushButton {\n"
"    background-color:  #999999;\n"
"border:none;\n"
"color: #000000;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#2E75B6;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:#1F4E79;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/11795/resource/smart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AIDetectPushButton.setIcon(icon2)
        self.AIDetectPushButton.setIconSize(QtCore.QSize(15, 15))
        self.AIDetectPushButton.setObjectName("AIDetectPushButton")
        self.snapshotPushButton = QtWidgets.QPushButton(self.tab_5)
        self.snapshotPushButton.setGeometry(QtCore.QRect(1305, 844, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.snapshotPushButton.setFont(font)
        self.snapshotPushButton.setStyleSheet("QPushButton {\n"
"    background-color:  #999999;\n"
"border:none;\n"
"color: #000000;\n"
"border-radius: 8px;\n"
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
        icon3.addPixmap(QtGui.QPixmap("C:/Users/11795/resource/redspot1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.snapshotPushButton.setIcon(icon3)
        self.snapshotPushButton.setIconSize(QtCore.QSize(11, 11))
        self.snapshotPushButton.setObjectName("snapshotPushButton")
        self.startPushButton = QtWidgets.QPushButton(self.tab_5)
        self.startPushButton.setGeometry(QtCore.QRect(700, 840, 40, 40))
        self.startPushButton.setStyleSheet("QPushButton {\n"
"    background-color:  #666666;\n"
"border:none;\n"
"color: #CCCCCC;\n"
"border-radius: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #525252;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:#525252;\n"
"}\n"
"border:none;")
        self.startPushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("C:/Users/11795/resource/暂停.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startPushButton.setIcon(icon4)
        self.startPushButton.setIconSize(QtCore.QSize(22, 22))
        self.startPushButton.setObjectName("startPushButton")
        self.lastPushButton = QtWidgets.QPushButton(self.tab_5)
        self.lastPushButton.setGeometry(QtCore.QRect(650, 840, 40, 40))
        self.lastPushButton.setStyleSheet("QPushButton {\n"
"    background-color:  #666666;\n"
"border:none;\n"
"color: #CCCCCC;\n"
"border-radius: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #525252;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:#525252;\n"
"}\n"
"border:none;")
        self.lastPushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Users/11795/resource/后退.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lastPushButton.setIcon(icon5)
        self.lastPushButton.setIconSize(QtCore.QSize(22, 22))
        self.lastPushButton.setObjectName("lastPushButton")
        self.backOffPushButton = QtWidgets.QPushButton(self.tab_5)
        self.backOffPushButton.setGeometry(QtCore.QRect(600, 840, 40, 40))
        self.backOffPushButton.setStyleSheet("QPushButton {\n"
"    background-color:  #666666;\n"
"border:none;\n"
"color: #CCCCCC;\n"
"border-radius: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #525252;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:#525252;\n"
"}\n"
"border:none;")
        self.backOffPushButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("C:/Users/11795/resource/逐帧后退.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backOffPushButton.setIcon(icon6)
        self.backOffPushButton.setIconSize(QtCore.QSize(22, 22))
        self.backOffPushButton.setObjectName("backOffPushButton")
        self.nextPushButton = QtWidgets.QPushButton(self.tab_5)
        self.nextPushButton.setGeometry(QtCore.QRect(750, 840, 40, 40))
        self.nextPushButton.setStyleSheet("QPushButton {\n"
"    background-color:  #666666;\n"
"border:none;\n"
"color: #CCCCCC;\n"
"border-radius: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #525252;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:#525252;\n"
"}\n"
"border:none;")
        self.nextPushButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("C:/Users/11795/resource/前进.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextPushButton.setIcon(icon7)
        self.nextPushButton.setIconSize(QtCore.QSize(22, 22))
        self.nextPushButton.setObjectName("nextPushButton")
        self.fastForwardPushButton = QtWidgets.QPushButton(self.tab_5)
        self.fastForwardPushButton.setGeometry(QtCore.QRect(800, 840, 40, 40))
        self.fastForwardPushButton.setStyleSheet("QPushButton {\n"
"    background-color:  #666666;\n"
"border:none;\n"
"color: #CCCCCC;\n"
"border-radius: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #525252;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:#525252;\n"
"}\n"
"border:none;")
        self.fastForwardPushButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("C:/Users/11795/resource/逐帧前进.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fastForwardPushButton.setIcon(icon8)
        self.fastForwardPushButton.setIconSize(QtCore.QSize(22, 22))
        self.fastForwardPushButton.setObjectName("fastForwardPushButton")
        self.removeRepeatVideoPushButton = QtWidgets.QPushButton(self.tab_5)
        self.removeRepeatVideoPushButton.setGeometry(QtCore.QRect(1200, 844, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.removeRepeatVideoPushButton.setFont(font)
        self.removeRepeatVideoPushButton.setStyleSheet("QPushButton {\n"
"    background-color:  #999999;\n"
"border:none;\n"
"color: #000000;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#2E75B6;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:#1F4E79;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.removeRepeatVideoPushButton.setIcon(icon2)
        self.removeRepeatVideoPushButton.setIconSize(QtCore.QSize(15, 15))
        self.removeRepeatVideoPushButton.setObjectName("removeRepeatVideoPushButton")
        self.label_3.raise_()
        self.videoPlayer.raise_()
        self.horizontalSlider.raise_()
        self.videoTimeLabel.raise_()
        self.oepnVideoPushButton.raise_()
        self.videoTimeLabel_2.raise_()
        self.AIDetectPushButton.raise_()
        self.snapshotPushButton.raise_()
        self.startPushButton.raise_()
        self.lastPushButton.raise_()
        self.backOffPushButton.raise_()
        self.nextPushButton.raise_()
        self.fastForwardPushButton.raise_()
        self.removeRepeatVideoPushButton.raise_()
        self.streamSelectTabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.cameraLabel = QtWidgets.QLabel(self.tab_6)
        self.cameraLabel.setGeometry(QtCore.QRect(0, 15, 1440, 810))
        self.cameraLabel.setStyleSheet("\n"
"background-color: rgb(94, 94, 94);")
        self.cameraLabel.setText("")
        self.cameraLabel.setObjectName("cameraLabel")
        self.openCameraPushButton = QtWidgets.QPushButton(self.tab_6)
        self.openCameraPushButton.setGeometry(QtCore.QRect(700, 840, 40, 40))
        self.openCameraPushButton.setStyleSheet("QPushButton {\n"
"    background-color:  #666666;\n"
"border:none;\n"
"color: #CCCCCC;\n"
"border-radius: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #525252;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:#525252;\n"
"}\n"
"border:none;")
        self.openCameraPushButton.setText("")
        self.openCameraPushButton.setObjectName("openCameraPushButton")
        self.cameraStoragePushButton = QtWidgets.QPushButton(self.tab_6)
        self.cameraStoragePushButton.setGeometry(QtCore.QRect(34, 844, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(8)
        self.cameraStoragePushButton.setFont(font)
        self.cameraStoragePushButton.setStyleSheet("QPushButton {\n"
"    background-color:  #666666;\n"
"border:none;\n"
"color: #CCCCCC;\n"
"border-radius: 1px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #525252;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:#525252;\n"
"}\n"
"border:none;")
        self.cameraStoragePushButton.setObjectName("cameraStoragePushButton")
        self.label_6 = QtWidgets.QLabel(self.tab_6)
        self.label_6.setGeometry(QtCore.QRect(0, 825, 1440, 101))
        self.label_6.setStyleSheet("background-color: #666666;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.snapshotPushButton_2 = QtWidgets.QPushButton(self.tab_6)
        self.snapshotPushButton_2.setGeometry(QtCore.QRect(1305, 844, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.snapshotPushButton_2.setFont(font)
        self.snapshotPushButton_2.setStyleSheet("QPushButton {\n"
"    background-color:  #999999;\n"
"border:none;\n"
"color: #000000;\n"
"border-radius: 8px;\n"
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
        self.snapshotPushButton_2.setIcon(icon3)
        self.snapshotPushButton_2.setIconSize(QtCore.QSize(11, 11))
        self.snapshotPushButton_2.setObjectName("snapshotPushButton_2")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.tab_6)
        self.horizontalSlider_2.setEnabled(False)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(130, 885, 1181, 20))
        self.horizontalSlider_2.setStyleSheet("QSlider::groove:horizontal{ \n"
"height: 10px; \n"
"left: 0px; \n"
"right: 0px; \n"
"border:0px; \n"
"border-radius:6px; \n"
"background:#808080;\n"
"} \n"
"\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: #FFFFFF;\n"
"width: 14px;\n"
"height: 14px;\n"
"margin: -3px 0;\n"
"border-radius: 7px;\n"
"}\n"
"QSlider::sub-page:horizontal{\n"
"background:rgba(80,166,234,1);\n"
"}\n"
"")
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.capTimeLabel = QtWidgets.QLabel(self.tab_6)
        self.capTimeLabel.setGeometry(QtCore.QRect(40, 880, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.capTimeLabel.setFont(font)
        self.capTimeLabel.setStyleSheet("color: #CCCCCC;")
        self.capTimeLabel.setObjectName("capTimeLabel")
        self.capTimeLabel_2 = QtWidgets.QLabel(self.tab_6)
        self.capTimeLabel_2.setGeometry(QtCore.QRect(1330, 880, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.capTimeLabel_2.setFont(font)
        self.capTimeLabel_2.setStyleSheet("color: #CCCCCC;")
        self.capTimeLabel_2.setObjectName("capTimeLabel_2")
        self.removeRepeatPushButton = QtWidgets.QPushButton(self.tab_6)
        self.removeRepeatPushButton.setGeometry(QtCore.QRect(1200, 844, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.removeRepeatPushButton.setFont(font)
        self.removeRepeatPushButton.setStyleSheet("QPushButton {\n"
"    background-color:  #999999;\n"
"border:none;\n"
"color: #000000;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#2E75B6;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:#1F4E79;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.removeRepeatPushButton.setIcon(icon2)
        self.removeRepeatPushButton.setIconSize(QtCore.QSize(15, 15))
        self.removeRepeatPushButton.setObjectName("removeRepeatPushButton")
        self.startDetectPushButton = QtWidgets.QPushButton(self.tab_6)
        self.startDetectPushButton.setGeometry(QtCore.QRect(1095, 844, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.startDetectPushButton.setFont(font)
        self.startDetectPushButton.setStyleSheet("QPushButton {\n"
"    background-color:  #999999;\n"
"border:none;\n"
"color: #000000;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#2E75B6;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:#1F4E79;\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}")
        self.startDetectPushButton.setIcon(icon2)
        self.startDetectPushButton.setIconSize(QtCore.QSize(15, 15))
        self.startDetectPushButton.setObjectName("startDetectPushButton")
        self.label_6.raise_()
        self.cameraLabel.raise_()
        self.openCameraPushButton.raise_()
        self.cameraStoragePushButton.raise_()
        self.snapshotPushButton_2.raise_()
        self.horizontalSlider_2.raise_()
        self.capTimeLabel.raise_()
        self.capTimeLabel_2.raise_()
        self.removeRepeatPushButton.raise_()
        self.startDetectPushButton.raise_()
        self.streamSelectTabWidget.addTab(self.tab_6, "")
        self.snapshotTableView = QtWidgets.QTableView(self.tab)
        self.snapshotTableView.setGeometry(QtCore.QRect(1450, 15, 441, 896))
        self.snapshotTableView.setObjectName("snapshotTableView")
        self.exportPushButton = QtWidgets.QPushButton(self.tab)
        self.exportPushButton.setGeometry(QtCore.QRect(1730, 920, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exportPushButton.setFont(font)
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
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("C:/Users/11795/.designer/resource/导出icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exportPushButton.setIcon(icon9)
        self.exportPushButton.setObjectName("exportPushButton")
        self.deletePushButton = QtWidgets.QPushButton(self.tab)
        self.deletePushButton.setGeometry(QtCore.QRect(1600, 920, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deletePushButton.setFont(font)
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
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("C:/Users/11795/.designer/resource/删除icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deletePushButton.setIcon(icon10)
        self.deletePushButton.setObjectName("deletePushButton")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 960, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.annotationPushButton = QtWidgets.QPushButton(self.tab_2)
        self.annotationPushButton.setGeometry(QtCore.QRect(1750, 10, 81, 31))
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
        self.annotationPushButton.setIcon(icon10)
        self.annotationPushButton.setObjectName("annotationPushButton")
        self.deleteModelPushButton = QtWidgets.QPushButton(self.tab_2)
        self.deleteModelPushButton.setGeometry(QtCore.QRect(525, 25, 20, 20))
        self.deleteModelPushButton.setStyleSheet("QPushButton {\n"
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
        self.deleteModelPushButton.setText("")
        self.deleteModelPushButton.setIcon(icon10)
        self.deleteModelPushButton.setObjectName("deleteModelPushButton")
        self.importDatasetPushButton = QtWidgets.QPushButton(self.tab_2)
        self.importDatasetPushButton.setGeometry(QtCore.QRect(1620, 10, 111, 31))
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
        self.importDatasetPushButton.setIcon(icon10)
        self.importDatasetPushButton.setObjectName("importDatasetPushButton")
        self.modelsListLabel = QtWidgets.QLabel(self.tab_2)
        self.modelsListLabel.setGeometry(QtCore.QRect(90, 25, 71, 21))
        self.modelsListLabel.setStyleSheet("font: 25 11pt \"Adobe 宋体 Std L\";\n"
"")
        self.modelsListLabel.setObjectName("modelsListLabel")
        self.trainingPushButton = QtWidgets.QPushButton(self.tab_2)
        self.trainingPushButton.setGeometry(QtCore.QRect(1750, 930, 81, 41))
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
        self.trainingPushButton.setIcon(icon10)
        self.trainingPushButton.setObjectName("trainingPushButton")
        self.modelsTableView = QtWidgets.QTableView(self.tab_2)
        self.modelsTableView.setGeometry(QtCore.QRect(80, 50, 471, 871))
        self.modelsTableView.setStyleSheet("border-radius: 4px;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0)")
        self.modelsTableView.setObjectName("modelsTableView")
        self.datasetTableView = QtWidgets.QTableView(self.tab_2)
        self.datasetTableView.setGeometry(QtCore.QRect(560, 50, 1270, 871))
        self.datasetTableView.setStyleSheet("border-radius: 4px;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0)")
        self.datasetTableView.setObjectName("datasetTableView")
        self.datasetLabel = QtWidgets.QLabel(self.tab_2)
        self.datasetLabel.setGeometry(QtCore.QRect(550, 25, 71, 21))
        self.datasetLabel.setStyleSheet("font: 25 11pt \"Adobe 宋体 Std L\";\n"
"")
        self.datasetLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.datasetLabel.setObjectName("datasetLabel")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(94, 948, 641, 28))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.parametersSetLabel = QtWidgets.QLabel(self.layoutWidget)
        self.parametersSetLabel.setObjectName("parametersSetLabel")
        self.horizontalLayout.addWidget(self.parametersSetLabel)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.epochsLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.epochsLineEdit.setObjectName("epochsLineEdit")
        self.horizontalLayout.addWidget(self.epochsLineEdit)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.batchSizeLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.batchSizeLineEdit.setObjectName("batchSizeLineEdit")
        self.horizontalLayout.addWidget(self.batchSizeLineEdit)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.workersLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.workersLineEdit.setObjectName("workersLineEdit")
        self.horizontalLayout.addWidget(self.workersLineEdit)
        self.tabWidget.addTab(self.tab_2, "")
        self.label_background_top = QtWidgets.QLabel(self.centralwidget)
        self.label_background_top.setGeometry(QtCore.QRect(0, 0, 1920, 43))
        self.label_background_top.setStyleSheet("background-color: #DFE1E5;")
        self.label_background_top.setText("")
        self.label_background_top.setObjectName("label_background_top")
        self.label_background_botton = QtWidgets.QLabel(self.centralwidget)
        self.label_background_botton.setGeometry(QtCore.QRect(0, 43, 1920, 1037))
        self.label_background_botton.setStyleSheet("background-color: #F2F2F2;")
        self.label_background_botton.setText("")
        self.label_background_botton.setObjectName("label_background_botton")
        self.pushButton_model_settings = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_model_settings.setGeometry(QtCore.QRect(1750, 0, 70, 43))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_model_settings.setFont(font)
        self.pushButton_model_settings.setStyleSheet("QPushButton { border: none; }\n"
"QPushButton:hover { background-color: #828282; }\n"
"QPushButton:pressed { background-color: #696969; }")
        self.pushButton_model_settings.setObjectName("pushButton_model_settings")
        self.pushButton_minimize = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minimize.setGeometry(QtCore.QRect(1820, 0, 50, 43))
        self.pushButton_minimize.setStyleSheet("QPushButton { border: none; }\n"
"QPushButton:hover { background-color: #828282; }\n"
"QPushButton:pressed { background-color: #696969; }")
        self.pushButton_minimize.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("C:/Users/11795/resource/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_minimize.setIcon(icon11)
        self.pushButton_minimize.setObjectName("pushButton_minimize")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(1870, 0, 50, 43))
        self.pushButton_close.setStyleSheet("QPushButton { border: none; }\n"
"QPushButton:hover { background-color: #828282; }\n"
"QPushButton:pressed { background-color: red; }")
        self.pushButton_close.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("C:/Users/11795/resource/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_close.setIcon(icon12)
        self.pushButton_close.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_FPS_settings = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_FPS_settings.setGeometry(QtCore.QRect(1670, 0, 70, 43))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_FPS_settings.setFont(font)
        self.pushButton_FPS_settings.setStyleSheet("QPushButton { border: none; }\n"
"QPushButton:hover { background-color: #828282; }\n"
"QPushButton:pressed { background-color: #696969; }")
        self.pushButton_FPS_settings.setObjectName("pushButton_FPS_settings")
        self.label_background_botton.raise_()
        self.label_background_top.raise_()
        self.tabWidget.raise_()
        self.pushButton_model_settings.raise_()
        self.pushButton_close.raise_()
        self.pushButton_minimize.raise_()
        self.pushButton_FPS_settings.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
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

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.streamSelectTabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectAllPushButton.setText(_translate("MainWindow", "全选"))
        self.oepnVideoPushButton.setText(_translate("MainWindow", "打开文件"))
        self.videoTimeLabel.setText(_translate("MainWindow", "00：00：00 "))
        self.videoTimeLabel_2.setText(_translate("MainWindow", "00：00：00 "))
        self.AIDetectPushButton.setText(_translate("MainWindow", "AI检测"))
        self.snapshotPushButton.setText(_translate("MainWindow", " 手动快照[S]"))
        self.removeRepeatVideoPushButton.setText(_translate("MainWindow", "快照去重"))
        self.streamSelectTabWidget.setTabText(self.streamSelectTabWidget.indexOf(self.tab_5), _translate("MainWindow", "视频"))
        self.cameraStoragePushButton.setText(_translate("MainWindow", "存储设置"))
        self.snapshotPushButton_2.setText(_translate("MainWindow", " 手动快照[S]"))
        self.capTimeLabel.setText(_translate("MainWindow", "00：00：00 "))
        self.capTimeLabel_2.setText(_translate("MainWindow", "--：--：-- "))
        self.removeRepeatPushButton.setText(_translate("MainWindow", "快照去重"))
        self.startDetectPushButton.setText(_translate("MainWindow", "开启检测"))
        self.streamSelectTabWidget.setTabText(self.streamSelectTabWidget.indexOf(self.tab_6), _translate("MainWindow", "直播"))
        self.exportPushButton.setText(_translate("MainWindow", "导出当前列表"))
        self.deletePushButton.setText(_translate("MainWindow", "删除"))
        self.label.setText(_translate("MainWindow", "混凝土缺陷检测程序v1.0 "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "缺陷检测"))
        self.annotationPushButton.setText(_translate("MainWindow", "标注"))
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
        self.pushButton_model_settings.setText(_translate("MainWindow", "模型设置"))
        self.pushButton_FPS_settings.setText(_translate("MainWindow", "帧率设置"))
        self.actionselect_model.setText(_translate("MainWindow", "模型设置"))
        self.actionselect_fps.setText(_translate("MainWindow", "检测频率设置"))
        self.actionSetModel.setText(_translate("MainWindow", "模型设置"))
        self.actionDetectFps.setText(_translate("MainWindow", "检测频率设置"))
        self.actionCovertVideo.setText(_translate("MainWindow", "视频格式转换"))
from PyQt5.QtMultimediaWidgets import QVideoWidget
