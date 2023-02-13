import json
import time
import sxw.gui.child_covert_video.child_covert_video as child_covert_video

from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import scj.code.device as device
import sxw.utils.conver_video as cvd
class ChildCovertVideo(QMainWindow, child_covert_video.Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.openFileUrl=None

        # 绑定回调函数
        self.slot_init()

    def slot_init(self):
        """
        绑定回调函数
        :return:
        """
        self.openVideoPushButton.clicked.connect(self.openVideoPush)
        self.covertPushButton.clicked.connect(self.covertPush)


    def openVideoPush(self):
        """
        选择待转换视频回调函数
        :return:
        """
        support_format=["avi","mp4","mpg","mov"]
        openFileUrl = QtCore.QUrl.toString(QFileDialog.getOpenFileUrl()[0])
        if openFileUrl[-3:] not in support_format:
            QMessageBox.critical(self, "错误", "不支持的文件格式")
            return

        self.openFileUrl=openFileUrl

    def covertPush(self):
        """
        转换按钮回调函数
        :return:
        """
        if self.openFileUrl is None:
            QMessageBox.critical(self, "错误", "没有选择视频文件")
            return

        # print(openFileUrl[8:], openFileUrl[8:-4] + "_coverted_" + time.strftime('%Y-%m-%d-%H-%M-%S') + ".mp4")
        cvd.convertVideo(self.openFileUrl[8:],
                         self.openFileUrl[8:-4] + "_coverted_" + time.strftime('%Y-%m-%d-%H-%M-%S') + ".mp4")
        QMessageBox.information(self, "转换", "转换成功，视频保存到：\n" + self.openFileUrl[8:-4] + "_coverted_" + time.strftime(
            '%Y-%m-%d-%H-%M-%S') + ".mp4")




