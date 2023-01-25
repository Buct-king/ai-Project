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

        self.updateModelList()
        # 绑定回调函数
        self.slot_init()

    def slot_init(self):
        """
        绑定回调函数
        :return:
        """
        self.okModelSelectPushButton.clicked.connect(self.okPush)
        self.modelTableView.clicked.connect(self.left_clicked)

    def updateModelList(self):

        # todo: 后端接口
        # 设置数据层次结构，4行4列
        self.modelsDatamodel = QStandardItemModel(5, 5)
        # 设置水平方向四个头标签文本内容
        self.modelsDatamodel.setHorizontalHeaderLabels(['', '编号', '模型名称', '准确率','创建时间'])
        modelsList=json.loads(smodel.get_model_list())
        for index in range(len(modelsList["model_list"])):
            info=modelsList["model_list"][index]
            # checkbox
            item_checked = QStandardItem()
            item_checked.setCheckState(QtCore.Qt.Unchecked)
            item_checked.setCheckable(True)
            self.modelsDatamodel.setItem(index, 0, item_checked)

            itemIndex = QStandardItem(str(info["index"]))
            itemModelName = QStandardItem(info["model_name"])
            itemModelCreateTime=QStandardItem(info["create_time"])
            itemModelAccuracy = QStandardItem(str(random.randint(70,95))+"%")
            self.modelsDatamodel.setItem(index, 1, itemIndex)
            self.modelsDatamodel.setItem(index, 2, itemModelName)
            self.modelsDatamodel.setItem(index, 3, itemModelAccuracy)
            self.modelsDatamodel.setItem(index, 4, itemModelCreateTime)
        self.modelTableView.setModel(self.modelsDatamodel)

    def left_clicked(self):
        rows = []
        for index in self.modelTableView.selectionModel().selection().indexes():
            rows.append(index.row())
        rows = list(set(rows))
        for index in range(self.modelsDatamodel.rowCount()):
            if index in rows:
                item_checked = QStandardItem()
                item_checked.setCheckState(QtCore.Qt.Checked)
                item_checked.setCheckable(True)
                self.modelsDatamodel.setItem(index, 0, item_checked)
            else:
                item_checked = QStandardItem()
                item_checked.setCheckState(QtCore.Qt.Unchecked)
                item_checked.setCheckable(True)
                self.modelsDatamodel.setItem(index, 0, item_checked)

    def okPush(self):
        """
        确认键回调函数
        :return:
        """
        checked=0
        checked_list=[]
        for i in range(self.modelsDatamodel.rowCount()):
            if self.modelsDatamodel.item(i, 0).checkState():
                checked=checked+1
                checked_list.append(int(self.modelsDatamodel.item(i,1).text()))
        if checked==0:
            QMessageBox.critical(self, "错误", "您没有选择模型")
        elif checked>1:
            QMessageBox.critical(self, "错误", "只能选择一个模型")
        else:
            self._signal.emit(checked_list[0])
            QMessageBox.information(self, "模型选择", "您选择的模型编号为:%d" % checked_list[0])
            self.close()

