
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QPen,QPixmap,QColor

class MyLabel(QLabel):
    def __init__(self, parent=None):
        super(MyLabel, self).__init__((parent))
        self.x0 = 0
        self.y0 = 0
        self.x1 = 0
        self.y1 = 0
        self.pos0 = None
        self.pos1 = None
        self.flag = False
        self.isShow = True

    def paintEvent(self, event):
        super().paintEvent(event)
        rect = QRect(self.x0, self.y0, abs(self.x1 - self.x0), abs(self.y1 - self.y0))
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        painter.begin(self)
        if self.isShow == True:
            painter.drawRect(rect)
        painter.end()
        # qp.begin(self)
        # qp.end()

    def mousePressEvent(self, event):
        QLabel.mousePressEvent(self, event)
        self.flag = True
        self.pos0 = event.globalPos()
        self.x0 = event.x()
        self.y0 = event.y()

    def mouseMoveEvent(self, event):
        QLabel.mouseMoveEvent(self, event)
        if self.flag:
            self.pos1 = event.globalPos()
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()

    def mouseReleaseEvent(self, event):
        QLabel.mouseReleaseEvent(self, event)
        self.flag = False
        self.isShow = True

    def getRectGlobalPos(self):
        # 返回绝对坐标
        poses = [(self.pos0.x(), self.pos0.y())]
        poses.append((self.pos1.x(), self.pos1.y()))
        return poses

    def clearRec(self):
        self.isShow=False
        self.x0=0
        self.y0=0
        self.x1=0
        self.y1=0