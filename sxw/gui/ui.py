from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import random
import fauilt_detection  # 刚刚转为py文件的UI文件名，我的是untitled
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from child_viewmodel import Child
from PyQt5 import QtCore
class UI(QMainWindow, fauilt_detection.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.ch = Child()

        # 视频播放器
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.videoPlayer)
        self.ch._signal.connect(self.openVideoFile)
        self.timer = QtCore.QTimer()
        self.timer.start(200)

        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setValue(0)
        self.horizontalSlider.setMaximum(1000)
        self.slot_init()

    '''
        绑定控件的回调函数
    '''
    def slot_init(self):
        self.pushButton.clicked.connect(lambda: self.openVideoSelect())
        self.startPushButton.clicked.connect(lambda: self.videoStateChange())
        self.nextPushButton.clicked.connect(lambda: self.fastChange())
        self.lastPushButton.clicked.connect(lambda: self.backoffChange())
        self.timer.timeout.connect(self.timerSync)
        self.horizontalSlider.sliderPressed.connect(lambda :self.sliderPressed())
        self.horizontalSlider.sliderReleased.connect(lambda: self.sliderReleased())
    '''
        打开视频选择窗口
    '''
    def openVideoSelect(self):
        self.ch.show()
        self.ch.setHistoryVideos()

    '''
        接收选择视频子窗口传来的视频地址,对播放做判断
        @:param parameter 视频文件地址（PyQt5.QtCore.QUrl）
        @:return 视频文件地址（PyQt5.QtCore.QUrl）
    '''
    def openVideoFile(self,parameter):

        def isVideoFile(parameter):
            return True

        if isVideoFile("test"):
            self.player.setMedia(QMediaContent(parameter))
            self.player.play()
            self.player.pause()
        else:
            self.openVideoSelect()


    '''
         视频播放暂停回调后函数
    '''
    def videoStateChange(self):
        if self.player.state()==2:
            self.player.play()
        elif self.player.state()==1:
            self.player.pause()

    def fastChange(self):
        print("总长是",self.player.duration())
        self.player.setPosition(self.player.position()+2000)
        print(self.player.position())

    def backoffChange(self):
        self.player.setPosition(self.player.position() - 2000)

    '''
        Timer定时的回调函数，更新slider跟着视频播放进度调整位置
    '''
    def timerSync(self):
        if self.player.duration()==0:
            self.horizontalSlider.setValue(0)
        else:
            rateOfProcess=self.player.position()/self.player.duration()
            self.horizontalSlider.setValue(rateOfProcess*self.horizontalSlider.maximum())

    '''
        Slider的回调函数，调整slider的值，调整视频的位置
    '''
    def sliderPressed(self):
        self.player.pause()
        self.timer.stop()

    def sliderReleased(self):
        self.player.play()
        rateOfProcess=self.horizontalSlider.value()/self.horizontalSlider.maximum()
        self.player.setPosition(self.player.duration()*rateOfProcess)
        self.timer.start()