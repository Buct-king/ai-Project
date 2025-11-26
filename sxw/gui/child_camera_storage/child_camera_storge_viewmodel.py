import json
import re
import sxw.gui.child_camera_storage.child_camera_storge as  child_camera_storge# 刚刚转为py文件的UI文件名
import os
from PyQt5 import QtCore,QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main import ROOT

import scj.code.device as device
class ChildCameraStorage(QMainWindow, child_camera_storge.Ui_MainWindow):
    # 向父窗口传递打开文件名的信号量
    # cameraName, operation_code：0 means open new file, 1 means open old file
    _signal = QtCore.pyqtSignal([str, int,str,int])
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.iconPlus=QtGui.QIcon()
        self.iconPlus.addPixmap(QtGui.QPixmap(os.path.join(ROOT, "sxw/resource/plus.png")), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)
        self.iconMine=QtGui.QIcon()
        self.iconMine.addPixmap(QtGui.QPixmap(os.path.join(ROOT, "sxw/resource/minimize.png")), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)

        self.deleteOldFilePushButton.setIcon(self.iconMine)
        self.createNewFilePushButton.setIcon(self.iconPlus)
        self.selectedItem = None
        self.camerasCount,self.camerasNameList,self.camerasIDList=self.getLocalCameras()
        self.selectedItemCamera = None

        # 绑定回调函数
        self.slot_init()

    def slot_init(self):
        self.createNewFilePushButton.clicked.connect(self.createNewStorage)
        self.openHistoryFilePushButton.clicked.connect(self.openHistoryStorage)
        self.deleteOldFilePushButton.clicked.connect(self.deleteHistorStorage)

    def getHistoryStorages(self):
        historyStorageFiles = json.loads(device.history_camera())
        historyStorageFilesCount = historyStorageFiles["devices_cnt"]
        historyStorageFilenames=list(historyStorageFiles['devices_list'].keys())
        historyStorageFilePath =list(historyStorageFiles['devices_list'].values())
        self.historyStorageFilenames=historyStorageFilenames
        self.historyStorageFilePath=historyStorageFilePath



    def setStorages(self):
        self.getHistoryStorages()
        # 实例化列表模型，添加数据
        slm = QtCore.QStringListModel()
        # 设置模型列表视图，加载数据列表
        slm.setStringList(self.historyStorageFilenames)
        self.historyStorageListView.setModel(slm)
        # 单击触发自定义的槽函数
        self.historyStorageListView.clicked.connect(self.clicked)


    def clicked(self, qModelIndex):
        self.selectedItem = qModelIndex
        # 控制台，你选择的信息
        print('你选择了：' + self.historyStorageFilenames[qModelIndex.row()])

    def createNewStorage(self):
        text, okPressed = QInputDialog.getText(self, "存储文件名","存储文件名:", QLineEdit.Normal, "")
        if okPressed:
            matchStr = re.search(r"\W", text)
            if matchStr == None and (" " not in text):
                print(text)
                self._signal.emit(text, 0,self.camerasNameList[self.selectedItemCamera.row()],self.camerasIDList[self.selectedItemCamera.row()])
                self.close()
            else:
                QMessageBox.critical(self, "错误", "文件命名只能使用数字,字母以及_")
                self.createNewStorage()

    def openHistoryStorage(self):
        self._signal.emit(self.historyStorageFilenames[self.selectedItem.row()],1,self.camerasNameList[self.selectedItemCamera.row()],self.camerasIDList[self.selectedItemCamera.row()])
        self.selectedItem=None
        self.close()

    def deleteHistorStorage(self):
        if self.selectedItem!=None:
            status=json.loads(device.delete_video_or_camera(self.historyStorageFilenames[self.selectedItem.row()],0))
            if status["code"]==1:
                QMessageBox.critical(self, "提示", "文件删除成功")
            else:
                QMessageBox.critical(self, "错误", status["message"])
            self.setStorages()
        else:
            QMessageBox.critical(self, "错误", "请选择要删除的文件")




    def getLocalCameras(self):
        CamerasInfoList = json.loads(device.get_camera_list())
        CamerasCount = CamerasInfoList["camera_num"]
        CamerasNameList = [x["name"] for x in CamerasInfoList["camera_list"]]
        CamerasIDList=[x["id"] for x in CamerasInfoList["camera_list"]]
        return CamerasCount,CamerasNameList,CamerasIDList

    def setCameras(self):
        # 实例化列表模型，添加数据
        slm = QtCore.QStringListModel()
        # 设置模型列表视图，加载数据列表
        slm.setStringList(self.camerasNameList)
        self.camerasListView.setModel(slm)
        # 单击触发自定义的槽函数
        self.camerasListView.clicked.connect(self.clickedCamera)


    def clickedCamera(self, qModelIndex):
        self.selectedItemCamera = qModelIndex
        # 控制台，你选择的信息
        print('你选择了：' + self.camerasNameList[qModelIndex.row()])

    def cameraSelect(self):
        self._signal.emit(self.camerasNameList[self.selectedItemCamera.row()],self.camerasIDList[self.selectedItemCamera.row()])
        self.close()

