import json

import sxw.gui.child_camera_select.child_camera_select as child_camera_select # 刚刚转为py文件的UI文件名

from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import scj.code.device as device
class ChildCameraSelect(QMainWindow, child_camera_select.Ui_MainWindow):
    # 向父窗口传递打开文件名的信号量
    # cameraName, code
    _signal = QtCore.pyqtSignal([str, int])
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.camerasCount,self.camerasNameList,self.camerasIDList=self.getLocalCameras()
        self.selectedItem = None

        # 绑定回调函数
        self.slot_init()

    def slot_init(self):
        self.okCameraSelectPushButton.clicked.connect(self.cameraSelect)

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
        self.camerasListView.clicked.connect(self.clicked)


    def clicked(self, qModelIndex):
        self.selectedItem = qModelIndex
        # 控制台，你选择的信息
        print('你选择了：' + self.camerasNameList[qModelIndex.row()])

    def cameraSelect(self):
        self._signal.emit(self.camerasNameList[self.selectedItem.row()],self.camerasIDList[self.selectedItem.row()])
        self.close()
