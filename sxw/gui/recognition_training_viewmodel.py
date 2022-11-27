from PyQt5.QtMultimedia import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

import fault_detection


class RecognitionTraining(QMainWindow, fault_detection.Ui_MainWindow, ):
    def __init__(self):
        QMainWindow.__init__(self)

        self.slot_init()

    def slot_init(self):
        self.importPicPushButton.clicked.connect(self.importImagePush)

    def importImagePush(self):
        """
        插入图片按钮回调函数，点击之后，状态成功，则正常显示成功，失败则显示插入失败
        """
        # todo: 判断文件是否合法
        openFileUrl = QFileDialog.getOpenFileUrl()
        print(openFileUrl)
