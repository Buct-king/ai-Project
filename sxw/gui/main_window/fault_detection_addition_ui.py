from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QProgressBar, QPushButton,QMainWindow,QProgressDialog
import os
import scj.code.device as device
import scj.code.snapshot as ssnapshot
import sxw.utils.utils as utils
import sxw.utils.video_utils as vutils
import scj.code.defect_detection as defect_detection
import json
from main import ROOT
import threading
class Fault_Detection_Addition_UI():
    def __init__(self):

        self.iconStop = QtGui.QIcon()
        self.iconStop.addPixmap(QtGui.QPixmap(os.path.join(ROOT, "sxw/resource/暂停.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.iconStart = QtGui.QIcon()
        self.iconStart.addPixmap(QtGui.QPixmap(os.path.join(ROOT, "sxw/resource/暂停.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    def changeIcon2IconStop(self):
        self.startPushButton.setIcon(self.iconStop)


    def changeIcon2IconStart(self):
        self.startPushButton.setIcon(self.iconStart)


class ProgressThread(QtCore.QThread): # 创建线程类
    def __init__(self):
        super(ProgressThread,self).__init__()
        self.progress=QProgressDialog('', '', 0,0)
        self.progress.setFixedSize(400,200)
        self.progress.setWindowTitle('处理中')
        self.progress.setLabelText('当前进度值')
        self.progress.setCancelButtonText('取消')
        self.progress.setRange(0, 0)
        # self.progress.canceled.connect(lambda:print('进度对话框被取消'))
        # self.progress.setAutoClose(True)#value为最大值时自动关闭
    # def run(self):#重写run，为了第二次启动时初始化做准备

        # self.progress.setValue(0)


class WorkThread(QThread):
    #实例化一个信号对象
    trigger = pyqtSignal([str])

    def __int__(self,state_dict,rate):
        super(WorkThread, self).__init__()
        self.state_dict=state_dict
        self.rate=rate

    def run(self):
        #开始进行工作
        print(self.state_dict)
        vutils.translate_frame_rate(self.state_dict["video_info"]["video_path"]+"//"+self.state_dict["video_info"]["video_name"]+".mp4",os.getcwd()+"/temp.mp4",self.rate)
        #
        detectedVideoUrl=defect_detection.video_defect_detection(os.getcwd()+"/temp.mp4")
        #
        #
        # # 工作完毕后发出信号
        self.trigger.emit(detectedVideoUrl)


class RemovalVideoThread(QThread):
    #实例化一个信号对象
    trigger = pyqtSignal([str])

    def __int__(self,video_name):
        super(RemovalVideoThread, self).__init__()
        self.video_name=video_name


    def run(self):

        import scj.code.duplicate_removal as duplicate_removal
        duplicate_removal.video_duplicate_remove_2(self.video_name)
        #
        #
        # # 工作完毕后发出信号
        self.trigger.emit("1")

# 导出线程
class ExportThread(QThread):
    #实例化一个信号对象
    trigger = pyqtSignal([object])

    def __int__(self,state_dict,ids):
        super(WorkThread, self).__init__()
        self.state_dict=state_dict
        self.ids=ids

    def run(self):
        #开始进行工作
        status=ssnapshot.export_snapshot_list(self.state_dict["page_num"],self.ids)

        #
        #
        # # 工作完毕后发出信号
        self.trigger.emit(json.loads(status))





