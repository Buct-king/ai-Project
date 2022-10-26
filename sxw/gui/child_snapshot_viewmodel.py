
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import child_snapshot

import cv2

class ChildSnapshot(QMainWindow, child_snapshot.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.slot_init()

    # 绑定回调函数
    def slot_init(self):
      self.cancelPushButton.clicked.connect(self.cancelPush)


    def setSnapshotInfos(self,frame):
        snapshotVideoInfo="2022-混凝土检测.mp3"
        snapshotVideoTime="12:00/25:00"

        show = cv2.resize(frame, (480, 320))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        self.iamgeLabel.setPixmap(QPixmap.fromImage(showImage))
        self.snapshotVideoInfoShowLabel.setText(snapshotVideoInfo)
        self.snapshotVideoTimeShowLabel.setText(snapshotVideoTime)


    def cancelPush(self):
        self.iamgeLabel.clearRec()
        self.close()