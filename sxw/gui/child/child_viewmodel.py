import json

import sxw.gui.child.child as child  # 刚刚转为py文件的UI文件名

from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import scj.code.device as device


class Child(QMainWindow, child.Ui_MainWindow):
    # 向父窗口传递打开文件名的信号量
    _signal = QtCore.pyqtSignal([str,QtCore.QUrl,int])

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.slot_init()
        self.historyVideosName, self.historyVideosPath=self.getHistoryVideosInfo()
        self.selectedItem = None

    # 绑定回调函数
    def slot_init(self):
        self.searchPushButton.clicked.connect(lambda: self.searchVideoFile())
        self.openVedioPushButton.clicked.connect(lambda: self.openHistoryVideoFile())

    # 查找视频文件
    def searchVideoFile(self):
        # openFileUrl PyQt5.QtCore.QUrl
        openFileUrl = QFileDialog.getOpenFileUrl()
        print(openFileUrl)
        signal=[openFileUrl[0],1]
        self._signal.emit(None,signal[0],signal[1])
        self.close()

    # 打开历史视频文件
    def openHistoryVideoFile(self):
        if self.selectedItem == None:
            print("您还没有选择视频文件")
            QMessageBox.critical(self, "错误", "您还未选择视频")
        else:
            openFileUrl = QtCore.QUrl(self.historyVideosPath[self.selectedItem.row()])
            openFileName=self.historyVideosName[self.selectedItem.row()]
            print(openFileUrl)
            self._signal.emit(openFileName,openFileUrl,2)
            self.close()


    '''
        填充历史视频列表
    '''

    def setHistoryVideos(self):
        # 实例化列表模型，添加数据
        slm = QtCore.QStringListModel()
        # 设置模型列表视图，加载数据列表
        slm.setStringList(self.historyVideosName)
        self.videosHistoryListView.setModel(slm)
        # 单击触发自定义的槽函数
        self.videosHistoryListView.clicked.connect(self.clicked)

    '''
        视频列表点击回调函数
    '''

    def clicked(self, qModelIndex):
        self.selectedItem = qModelIndex
        print(qModelIndex)
        # 控制台，你选择的信息
        print('你选择了：' + self.historyVideosName[qModelIndex.row()])

    def getHistoryVideosInfo(self):
        historyVideos = json.loads(device.history_video())
        count = historyVideos["devices_cnt"]
        historyVideosName=list(historyVideos["devices_list"].keys())
        historyVideosPath=list(historyVideos["devices_list"].values())
        return historyVideosName, historyVideosPath

    def setHistoryVideosInfo(self):
        self.historyVideosName, self.historyVideosPath = self.getHistoryVideosInfo()