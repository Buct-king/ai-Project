from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

import fauilt_detection  # 刚刚转为py文件的UI文件名，我的是untitled
from PyQt5.QtWidgets import QMainWindow, QFileDialog


class UI(QMainWindow, fauilt_detection.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.slot_init()

        # 视频播放器
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.videoPlayer)

    # 绑定回调函数
    def slot_init(self):
        pass
        self.oepnVideoPushButton.clicked.connect(lambda: self.openVideoFile())

    '''
        视频播放相关功能
    '''
    # 打卡视频文件
    def openVideoFile(self):
        self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))
        self.player.play()




