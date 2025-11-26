import json
import random
import sxw.gui.child_model_select.child_model_select as child_model_select # 刚刚转为py文件的UI文件名

from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import scj.code.device as device
import scj.code.model as smodel
class ChildModelSelect(QMainWindow, child_model_select.Ui_MainWindow):

    # 选择的模型id信号量
    _signal = QtCore.pyqtSignal([int])

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setFixedSize(self.width(), self.height())
        self.modelTableView.verticalHeader().setVisible(False)  # 设置左边序号不可见
        self.modelTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.modelTableView.setShowGrid(False)
        self.modelTableView.setColumnWidth(0, 100)
        self.modelTableView.setColumnWidth(1, 100)
        self.modelTableView.setColumnWidth(2, 200)

        self.updateModelList()
        # 绑定回调函数
        self.slot_init()

    def slot_init(self):
        """
        绑定回调函数
        :return:
        """
        self.okModelSelectPushButton.clicked.connect(self.okPush)


    def updateModelList(self):

        # todo: 后端接口
        # 设置数据层次结构，4行4列
        self.modelsDatamodel = QStandardItemModel(10, 3)
        self.modelTableView.setColumnWidth(0, 100)
        self.modelTableView.setColumnWidth(1, 100)
        self.modelTableView.setColumnWidth(2, 200)
        # 设置水平方向四个头标签文本内容
        self.modelsDatamodel.setHorizontalHeaderLabels(['编号', '模型名称','创建时间'])
        modelsList=json.loads(smodel.get_model_list())
        for index in range(len(modelsList["model_list"])):
            info=modelsList["model_list"][index]
            itemIndex = QStandardItem(str(info["index"]))
            itemModelName = QStandardItem(info["model_name"])
            itemModelCreateTime=QStandardItem(info["create_time"])
            self.modelsDatamodel.setItem(index, 0, itemIndex)
            self.modelsDatamodel.setItem(index, 1, itemModelName)
            self.modelsDatamodel.setItem(index, 2, itemModelCreateTime)
        self.modelTableView.setModel(self.modelsDatamodel)


    def okPush(self):
        """
        确认键回调函数
        :return:
        """
        rows = []
        for index in self.modelTableView.selectionModel().selection().indexes():
            rows.append(index.row())

        if len(rows)==0:
            QMessageBox.critical(self, "错误", "您没有选择模型")
        elif len(rows)>1:
            QMessageBox.critical(self, "错误", "只能选择一个模型")
        else:
            self._signal.emit(int(self.modelsDatamodel.item(rows[0],0).text()))
            QMessageBox.information(self, "模型选择", "您选择的模型编号为:%d" % int(self.modelsDatamodel.item(rows[0],0).text()))
            self.close()

