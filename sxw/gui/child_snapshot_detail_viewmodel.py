import json
import re
import child_snapshot_detail # 刚刚转为py文件的UI文件名
import cv2
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import scj.code.snapshot as ssnapshot

class ChildSnapshotDetails(QMainWindow, child_snapshot_detail.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)


    def slot_init(self):
        self.cancelPushButton.clicked.connect(lambda: self.cancelPush())

    def nextSnapshotPush(self):
        pass

    def lastSnapshotPush(self):
        pass
    def cancelPush(self):
        self.close()

    def updataSnapshotInfo(self,kind,id):
        jsonInfos=ssnapshot.get_image_info(kind,id)
        info=json.loads(jsonInfos)
        self.snapshotNoteShowLabel.setText(info["info"]["image_note"])
        self.snapshotIDShowLabel.setText(str(id))
        self.snapshotVideoTimeShowLabel.setText(info["info"]["video_time"])
        self.snapshotTimeShowLabel.setText(info["info"]["image_time"])
        self.snapshotNameLabel.setText(info["info"]["image_name"])
        image_path=info["info"]["image_path"]
        show=cv2.imread(image_path)
        show=cv2.resize(show,(551,391))
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        self.iamgeLabel.setPixmap(QPixmap.fromImage(showImage))

        print(info)