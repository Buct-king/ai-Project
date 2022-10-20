import test_openVideo  # 刚刚转为py文件的UI文件名，我的是untitled
from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer


class UI(QMainWindow, test_openVideo.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.widget)
        self.pushButton.clicked.connect(lambda :self.openVideoFile())

    def openVideoFile(self):
        self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))
        self.player.play()