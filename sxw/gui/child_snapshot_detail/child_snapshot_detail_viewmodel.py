import json
import re
import sxw.gui.child_snapshot_detail.child_snapshot_detail  as child_snapshot_detail # 刚刚转为py文件的UI文件名
import cv2
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import scj.code.snapshot as ssnapshot

class ChildSnapshotDetails(QMainWindow, child_snapshot_detail.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.indexNow=None
        self.kind=None
        self.snapshotList=None
        self.idSet=[]
        self.maxSnapshotIndex=None
        self.slot_init()

    def slot_init(self):
        self.cancelPushButton.clicked.connect(lambda: self.cancelPush())
        self.lastPushButton.clicked.connect(lambda: self.lastSnapshotPush())
        self.nextPushButton.clicked.connect(lambda: self.nextSnapshotPush())

    def lastSnapshotPush(self):
        find=self.indexNow-1
        while (find not in self.idSet):
            find-=1
            if find <=0:
                break
        if find <=0:
            QMessageBox.information(self, "警告", "已经是第一张快照")
        else:
            self.updataSnapshotInfo(self.kind,find)
            self.indexNow=find
            print(self.indexNow, self.maxSnapshotIndex)

    def nextSnapshotPush(self):
        find = self.indexNow + 1
        while (find not in self.idSet):
            find += 1
            if find >= self.maxSnapshotIndex:
                break
        if find >= self.maxSnapshotIndex:
            QMessageBox.information(self, "警告", "已经是最后一张快照")
        else:
            self.updataSnapshotInfo(self.kind, find)
            self.indexNow = find
            print(self.indexNow,self.maxSnapshotIndex)

    def cancelPush(self):
        print("in")
        self.close()

    def getSnapshotList(self):
        if self.kind is None:
            return
        self.snapshotList=json.loads(ssnapshot.get_image_list(self.kind))
        image_list=self.snapshotList["image_list"]
        for snapshot in image_list:
            self.idSet.append(snapshot["index"])
        self.maxSnapshotIndex=self.snapshotList["image_index"]


    def updataSnapshotInfo(self,kind,id):
        jsonInfos=ssnapshot.get_image_info(kind,id)
        info=json.loads(jsonInfos)
        self.snapshotNoteShowLabel.setText(info["info"]["image_note"])
        self.snapshotIDShowLabel.setText(str(id))
        self.snapshotVideoTimeShowLabel.setText(info["info"]["video_time"])
        self.snapshotTimeShowLabel.setText(info["info"]["image_time"])
        self.snapshotVideoInfoShowLabel.setText(info["info"]["image_name"])
        image_path=info["info"]["image_path"]
        show=cv2.imread(image_path)

        #
        # size = image.shape
        #
        # im_w = size[1]  # 宽度
        # im_h = size[0]  # 高度
        #
        # show=cv2.resize(show,(551,391))
        show=self.resize_image(show)
        showImage = QImage(show.data, show.shape[1], show.shape[0], show.shape[1]*3, QImage.Format_RGB888)
        self.iamgeLabel.setPixmap(QPixmap.fromImage(showImage))

        print(info)

    def resize_image(self,image):
        size = image.shape
        print(size)
        im_w = size[1]  # 宽度
        im_h = size[0]  # 高度

        W=551
        H=391
        if image.shape[1]>W:
            image=cv2.resize(image,(551,int(551/image.shape[1]*image.shape[0])))
        if image.shape[0]>H:
            image = cv2.resize(image, (int(391 / image.shape[0] * image.shape[1]),391))

        print(image.shape)
        return image