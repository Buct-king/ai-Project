import json
import re
import child_snapshot_detail # 刚刚转为py文件的UI文件名

from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import scj.code.snapshot

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

    def updataSnapshotInfo(self,id):
