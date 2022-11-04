import json
import time

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import child_snapshot

import cv2

import scj.code.snapshot as ssnapshot


class ChildSnapshot(QMainWindow, child_snapshot.Ui_MainWindow):
    # 向父窗口传递打开文件名的信号量
    _signal = pyqtSignal(int)

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.snapshotVideoInfo = None
        self.snapshotVideoTime = None
        self.image = None
        self.snapshotID=None
        self.slot_init()

    # 绑定回调函数
    def slot_init(self):
        self.cancelPushButton.clicked.connect(self.cancelPush)
        self.saveSnapshotPushButton.clicked.connect(self.storeSnapshotPush)

    def setSnapshotInfos(self, frame,stream_kind):
        show = cv2.resize(frame, (480, 320))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        self.image = show
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        self.iamgeLabel.setPixmap(QPixmap.fromImage(showImage))
        self.snapshotVideoInfo="test.ma3"
        self.snapshotVideoTime="43:00"
        self.snapshotID=10
        # todo: 获取 snapshotID
        self.snapshotIDLineEdit.setText(str(self.snapshotID))
        self.snapshotVideoInfoShowLabel.setText(self.snapshotVideoInfo)
        self.snapshotVideoTimeShowLabel.setText(self.snapshotVideoTime)

    def cancelPush(self):
        # self.iamgeLabel.clearRec()
        self._signal.emit(0)
        print("cancelPush")
        self.close()

    def storeSnapshotPush(self):
        poses = self.iamgeLabel.getRectPos()  # 框选位置
        note=str(self.textEdit.toPlainText())

        post_dict = {
            "origin_image": self.image.tolist(),# size(480*320)
            "poses": poses,# [x1，y1，x2，y2]
            "time": time.asctime(),
            "video_time": self.snapshotVideoTime,# (string)
            "note":note, # string
            "type": 0 # 0表示视频，1表示直播
        }

        ssnapshot.new_snapshot(json.dumps(post_dict))
        self._signal.emit(0)
        # todo：保存快照信息
        # self.iamgeLabel.clearRec()
        print(poses)
        self.close()

    def closeEvent(self,event):
        """
        重写关闭窗口方法，清除已经画了的正方形
        """
        poses = self.iamgeLabel.getRectPos()  # 框选位置
        print(poses)
        self.iamgeLabel.clearRec()





