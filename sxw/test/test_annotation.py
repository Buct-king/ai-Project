# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_annotation.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QPen,QPixmap,QColor


class MyLabel_inteSeg(QLabel):

    def __init__(self, parent=None):
        super(MyLabel_inteSeg, self).__init__((parent))
        self.flag = False
        self.isShow = True
        self.point_type = 0  # 0-左键前景点,1-右键背景点
        self.clk_pos = None
        self.x = 2
        self.y = 2

    def mousePressEvent(self, event):
        QLabel.mousePressEvent(self, event)
        # self.clear()
        if event.buttons() == QtCore.Qt.LeftButton:
            print("左键按下")
            self.point_type = 0
        elif event.buttons() == QtCore.Qt.RightButton:
            print("右键按下")
            self.point_type = 1
        self.clk_pos = event.globalPos()
        self.x = event.x()
        self.y = event.y()
        if self.isShow == True:
            self.update()

    def paintEvent(self, event):
        # super().paintEvent(event)
        painter = QPainter(self)
        print("paintEvent self.isShow:{}".format(self.isShow))
        if self.isShow == True:
            if self.point_type == 0:
                painter.begin(self)
                painter.setPen(QPen(QColor(255, 0, 0), 7))
                painter.drawPoint(self.x, self.y)
                painter.end()
            elif self.point_type == 1:
                painter.begin(self)
                painter.setPen(QPen(QColor(0, 255, 0), 7))
                painter.drawPoint(self.x, self.y)
                painter.end()

    def mouseReleaseEvent(self, event):
        QLabel.mouseReleaseEvent(self, event)

        # self.isShow = False
    def getPointGlobalPos(self):
        return self.clk_pos


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
        if self.isShow == True:
            painter.drawRect(rect)
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



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = MyLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 70, 531, 361))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setPixmap(QPixmap("G:\Lab_work\\fault_detection_new\\fault_detection\sxw\\test\wushen.jpg"))
