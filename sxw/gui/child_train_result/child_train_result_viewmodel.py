import json
import re
import sxw.gui.child_train_result.child_train_result as child_train_result # 刚刚转为py文件的UI文件名
import cv2
import os
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ChildTrainResult(QMainWindow, child_train_result.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def setPics(self,save_path):
        self.resultsPicLabel.setPixmap(QPixmap(os.path.join(save_path,"results.png")))
        self.labelsPicLabel.setPixmap(QPixmap(os.path.join(save_path,"labels.jpg")))
        self.confusionMatrixPicLabel.setPixmap(QPixmap(os.path.join(save_path,"confusion_matrix.png")))
        self.labelsCorrelogramPicLabel.setPixmap(QPixmap(os.path.join(save_path,"labels_correlogram.jpg")))