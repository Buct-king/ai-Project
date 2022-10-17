from PyQt5 import QtCore, QtGui, QtWidgets

class Fault_Detection_Addition_UI():
    def __init__(self):

        self.iconStop = QtGui.QIcon()
        self.iconStop.addPixmap(QtGui.QPixmap("../resource/暂停.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.iconStart = QtGui.QIcon()
        self.iconStart.addPixmap(QtGui.QPixmap("../resource/开始.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    def changeIcon2IconStop(self):
        self.startPushButton.setIcon(self.iconStop)


    def changeIcon2IconStart(self):
        self.startPushButton.setIcon(self.iconStart)
