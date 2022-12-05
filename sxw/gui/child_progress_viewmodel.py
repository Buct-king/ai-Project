import json
import time

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import child_progress

import cv2



class ChildProgress(QMainWindow, child_progress.Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.progressBar.setRange(0,0)


    def setLabel(self,minute):
        string="正在检测：预计需要%d分钟"%(minute)
        self.label.setText("正在检测：预计需要%d分钟")


