import sys
import PyQt5
from PyQt5 import QtWidgets

import test_openVideo  # 刚刚转为py文件的UI文件名，我的是untitled
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget


class UI(QMainWindow,test_openVideo.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.widget)
        self.pushButton.clicked.connect(lambda :self.openVideoFile())

    def openVideoFile(self):
        self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))
        self.player.play()