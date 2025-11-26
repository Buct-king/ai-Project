import json

import sxw.gui.child_fps_select.chiild_fps_select as child_fps_select

from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import scj.code.device as device
class ChildFpsSelect(QMainWindow, child_fps_select.Ui_MainWindow):

    # 选择的模型id信号量
    _signal = QtCore.pyqtSignal([int])

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setFixedSize(self.width(), self.height())

        # 绑定回调函数
        self.slot_init()

    def slot_init(self):
        """
        绑定回调函数
        :return:
        """
        self.pushButton.clicked.connect(self.okPush)


    def okPush(self):
        """
        确认键回调函数
        :return:
        """
        text=self.lineEdit.text()
        if text.isdigit():
            self._signal.emit(int(text))
            QMessageBox.information(self, "检测帧率设置", "您设置的帧率为:%d" % int(text))
            self.presentDetectFpsLabel.setText("当前检测帧率：%dfps"%(int(text)))
            self.close()
        else:
            QMessageBox.critical(self, "错误", "请输入正确的数字")


