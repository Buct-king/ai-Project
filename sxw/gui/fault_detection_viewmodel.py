from PyQt5.QtMultimedia import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import random
import fault_detection,fault_detection_addition_ui  # 刚刚转为py文件的UI文件名，我的是untitled
from PyQt5.QtWidgets import *
from child_viewmodel import Child


import cv2

import json
import scj.code.device as device
class Fault_Detection(QMainWindow, fault_detection.Ui_MainWindow,fault_detection_addition_ui.Fault_Detection_Addition_UI):
    def __init__(self):
        QMainWindow.__init__(self)
        fault_detection_addition_ui.Fault_Detection_Addition_UI.__init__(self)
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
        self.videoInfo=None

        # 摄像头
        self.timer_camera = QtCore.QTimer() #初始化定时器
        self.cap = cv2.VideoCapture() #初始化摄像头
        self.CAM_NUM = 0

        # 绑定回调函数
        self.slot_init()

    '''
        绑定控件的回调函数
    '''
    def slot_init(self):
        self.oepnVideoPushButton.clicked.connect(lambda: self.openVideoSelect())
        self.startPushButton.clicked.connect(lambda: self.videoStateChange())
        self.nextPushButton.clicked.connect(lambda: self.fastChange())
        self.lastPushButton.clicked.connect(lambda: self.backoffChange())
        self.timer.timeout.connect(self.timerSync)
        self.horizontalSlider.sliderPressed.connect(lambda :self.sliderPressed())
        self.horizontalSlider.sliderReleased.connect(lambda: self.sliderReleased())
        self.backOffPushButton.clicked.connect(lambda: self.lastVideo())
        self.fastForwardPushButton.clicked.connect(lambda: self.nextVideo())

        #摄像头
        self.timer_camera.timeout.connect(self.show_camera)
        self.openCameraPushButton.clicked.connect(self.slotCameraButton)
    '''
        打开视频选择窗口
    '''
    def openVideoSelect(self):
        self.ch.show()
        self.ch.setHistoryVideosInfo()
        self.ch.setHistoryVideos()

    '''
        接收选择视频子窗口传来的视频地址,对播放做判断
        @:param parameter 视频文件地址,状态码（[]）
    '''
    def openVideoFile(self,videoName,videoUrl,vedioCode):
        # 打开新视频状态码是 1，历史视频状态码是 2
        if vedioCode==1:
            if device.video_judge(videoUrl)==0:
                openInfo=device.open_new_video(videoUrl)
                openInfo=json.loads(openInfo)
                if openInfo["code"]==1:
                    self.player.setMedia(QMediaContent(videoUrl))
                    self.videoInfo=openInfo
                    self.player.play()
                    self.player.pause()
                else:
                    QMessageBox.critical(self, "错误", openInfo["message"])
                    self.openVideoSelect()
            else:
                QMessageBox.critical(self, "错误", "文件格式不正确")
                self.openVideoSelect()
        else:
                openInfo=device.open_old_video(videoName)
                openInfo=json.loads(openInfo)
                print(openInfo)
                if openInfo["code"]==1:
                    videoPath="file:///"+openInfo["video_path"]+"/"+openInfo["video_name"]+".mp4"
                    self.player.setMedia(QMediaContent(QtCore.QUrl(videoPath)))
                    self.videoInfo=openInfo
                    self.player.play()
                    self.player.pause()
                else:
                    QMessageBox.critical(self, "错误",openInfo["message"])
                    self.openVideoSelect()


    '''
         视频播放暂停回调后函数
    '''
    def videoStateChange(self):
        if self.player.state()==2:
            self.player.play()
            self.changeIcon2IconStop()
        elif self.player.state()==1:
            self.player.pause()
            self.changeIcon2IconStart()

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
        self.changeIcon2IconStart()
        self.timer.stop()

    def sliderReleased(self):
        self.player.play()
        self.changeIcon2IconStop()
        rateOfProcess=self.horizontalSlider.value()/self.horizontalSlider.maximum()
        self.player.setPosition(self.player.duration()*rateOfProcess)
        self.timer.start()

    '''
        切换视频
    '''
    def lastVideo(self):
        videoInfo=device.get_pre_video(self.videoInfo["video_name"])
        if videoInfo["code"]==1:
            self.videoInfo=videoInfo
            self.openVideoFile(videoInfo["video_name"],videoInfo["video_path"],2)
        else:
            QMessageBox.critical(self, "错误", videoInfo["message"])

    def nextVideo(self):
        videoInfo=device.get_next_video(self.videoInfo["video_name"])
        if videoInfo["code"]==1:
            self.videoInfo=videoInfo
            self.openVideoFile(videoInfo["video_name"],videoInfo["video_path"],2)
        else:
            QMessageBox.critical(self, "错误", videoInfo["message"])




    '''
        摄像头
    '''
    def show_camera(self):
         flag,self.image = self.cap.read()
         show = cv2.resize(self.image,(480,320))
         show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
         showImage = QImage(show.data, show.shape[1],show.shape[0],QImage.Format_RGB888)
         self.cameraLabel.setPixmap(QPixmap.fromImage(showImage))


     #打开摄像头
    def openCamera(self):
        flag = self.cap.open(self.CAM_NUM)
        if flag == False:
            msg = QMessageBox.Warning(self, u'Warning', u'请检测相机与电脑是否连接正确',
            buttons=QMessageBox.Ok,
            defaultButton=QMessageBox.Ok)
        else:
            self.timer_camera.start(30)

     #打开关闭摄像头控制
    def slotCameraButton(self):
        if self.timer_camera.isActive() == False:
            #打开摄像头并显示图像信息
            self.openCamera()
        else:
            #关闭摄像头并清空显示信息
            self.closeCamera()

    #关闭摄像头
    def closeCamera(self):
         self.timer_camera.stop()
         self.cap.release()
         self.cameraLabel.clear()