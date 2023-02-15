from PyQt5.QtMultimedia import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore
import random
import time
import os
import threading
import cv2
import json
import datetime

from sxw.gui.main_window import fault_detection
from sxw.gui.main_window import fault_detection_addition_ui
from sxw.gui.main_window import recognition_training_viewmodel

from sxw.gui.child.child_viewmodel import Child
from sxw.gui.child_camera_select.child_camera_select_viewmodel import ChildCameraSelect
from sxw.gui.child_camera_storage.child_camera_storge_viewmodel import ChildCameraStorage
from sxw.gui.child_snapshot.child_snapshot_viewmodel import ChildSnapshot
from sxw.gui.child_snapshot_detail.child_snapshot_detail_viewmodel import ChildSnapshotDetails
from sxw.gui.child_progress.child_progress_viewmodel import ChildProgress
from sxw.gui.child_model_select.child_model_select_viewmodel import ChildModelSelect
from sxw.gui.child_fps_select.child_fps_select_viewmodle import ChildFpsSelect
from sxw.gui.child_train_result.child_train_result_viewmodel import ChildTrainResult
from sxw.gui.child_covert_video.child_covert_video_viewmodel import ChildCovertVideo

import scj.code.device as device
import scj.code.snapshot as ssnapshot
import sxw.utils.utils as utils
import sxw.utils.video_utils as vutils
import scj.code.defect_detection as defect_detection
import scj.code.model as smodel
import yolo.yolov5_6.yolov5_6.detect_camera as detect_camera


from main import ROOT


class Fault_Detection(QMainWindow, fault_detection.Ui_MainWindow,
                      fault_detection_addition_ui.Fault_Detection_Addition_UI):
    def __init__(self):
        QMainWindow.__init__(self)
        fault_detection_addition_ui.Fault_Detection_Addition_UI.__init__(self)
        self.setupUi(self)

        self.state_dict = {
            "page_num": None,
            "video_info": None,
            "video_state": None,
            "cap_num": None,
            "cap_storage_name": None,
            "cap_activate": None
        }

        self.parameters = {
            "model_id": 0,
            "detect_fps": 10,
            "dataset_path": None
        }

        # init 菜单
        self.childModelSelect = ChildModelSelect()
        self.childModelSelect.setWindowModality(QtCore.Qt.ApplicationModal)
        self.childModelSelect._signal.connect(self.updateModelId)
        self.childFpsSelect = ChildFpsSelect()
        self.childFpsSelect.setWindowModality(QtCore.Qt.ApplicationModal)
        self.childFpsSelect._signal.connect(self.updateDetectFps)
        self.childCovertVideo=ChildCovertVideo()
        self.initMenuAction()

        # streamTabWidget
        self.initStreamSelectTabWidget()

        # iniIcons
        self.iniIcon()

        # 视频播放器
        self.ch = Child()
        self.ch.setWindowModality(QtCore.Qt.ApplicationModal)
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.videoPlayer)
        self.ch._signal.connect(self.openVideoFile)
        self.timer = QtCore.QTimer()
        self.timer.start(200)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setValue(0)
        self.horizontalSlider.setMaximum(1000)
        self.videoInfo = None  # 记录当前打开视频的视频名、路径等信息
        self.cvPlayer = cv2.VideoCapture()
        self.VIDEO_NAME = None  # 记录当前打开视频的视频名
        self.timer_AIDetect = QtCore.QTimer()  # 初始化定时器
        self.childDetectProgress = ChildProgress()  # 视频检测进度条

        # 摄像头
        self.chCameraSelect = ChildCameraSelect()
        self.chCameraSelect.setWindowModality(QtCore.Qt.ApplicationModal)
        self.chCameraSelect._signal.connect(self.openCamera)
        self.chCameraStorage = ChildCameraStorage()
        self.chCameraStorage.setWindowModality(QtCore.Qt.ApplicationModal)
        self.chCameraStorage._signal.connect(self.openStorage)
        self.timer_camera = QtCore.QTimer()  # 初始化定时器
        self.cap = cv2.VideoCapture()  # 初始化摄像头
        self.CAM_NUM = None
        self.CAM_STORAGE = None  # 选择存储文件信号量
        self.CAM_STORAGE_NAME = None  # 视频存储文件名
        self.detectModel = None  # 识别模型

        # 快照
        self.SNAPSHOT = 0  # 0表示没有资源，1表示视频，2表示直播
        self.chSnapshot = ChildSnapshot()
        self.chCameraStorage._signal.connect(self.updateSnapshotsList)

        # 快照列表
        self.setSanpshotTableView()
        self.childSnapshotDetails = ChildSnapshotDetails()
        self.childSnapshotDetails.setWindowModality(QtCore.Qt.ApplicationModal)

        self.childExportProgress = ChildProgress()  # 视频导出进度条

        # 识别训练
        self.childTrainResult = ChildTrainResult()
        self.childTrainResult.setWindowModality(QtCore.Qt.ApplicationModal)
        # 绑定回调函数
        self.slot_init_fault_detetion()
        self.slot_init_recognition_training()

    '''
        绑定控件的回调函数
    '''

    def slot_init_fault_detetion(self):
        """
            缺陷检测页面回调函数绑定
        """

        # 菜单栏回调函数绑定

        # self.localfile_action.triggered.connect(self.openLocalFile)

        # streamSelectTabWidget
        self.streamSelectTabWidget.currentChanged.connect(self.streamSelectTabWidgetPush)

        # tabWidget窗口变化绑定回调函数
        self.tabWidget.currentChanged.connect(self.tabWidgetCurrentChanged)

        # 视频
        self.oepnVideoPushButton.clicked.connect(lambda: self.openVideoSelect())
        self.startPushButton.clicked.connect(lambda: self.videoStateChange())
        self.nextPushButton.clicked.connect(lambda: self.fastChange())
        self.lastPushButton.clicked.connect(lambda: self.backoffChange())
        self.timer.timeout.connect(self.timerSync)
        self.horizontalSlider.sliderPressed.connect(lambda: self.sliderPressed())
        self.horizontalSlider.sliderReleased.connect(lambda: self.sliderReleased())
        self.backOffPushButton.clicked.connect(lambda: self.backoffMiniChange())
        self.fastForwardPushButton.clicked.connect(lambda: self.fastMiniChange())
        self.AIDetectPushButton.clicked.connect(lambda: self.AIDetectPush())

        # 摄像头
        self.timer_camera.timeout.connect(self.show_camera)
        self.openCameraPushButton.clicked.connect(self.slotCameraButton)
        self.cameraSelectPushButton.clicked.connect(self.openCameraSelect)
        self.cameraStoragePushButton.clicked.connect(self.openCameraStorage)

        # 快照
        self.snapshotPushButton.clicked.connect(self.snapshotPush)
        self.exportPushButton.clicked.connect(self.exportSnapshotPush)
        self.deletePushButton.clicked.connect(self.deleteSnapShotPush)
        # self.detailPushButton.clicked.connect(self.printline)

        self.snapshotTableView.clicked.connect(self.printline)
        self.selectAllPushButton.clicked.connect(self.selectAllPush)

        # 识别训练
        self.modelsTableView.clicked.connect(self.left_clicked)

    """
        初始化相关
    """

    def iniIcon(self):
        """
        Icon初始化
        :return:
        """
        self.iconStop = QtGui.QIcon()
        self.iconStop.addPixmap(QtGui.QPixmap(os.path.join(ROOT, "sxw/resource/暂停.png")), QtGui.QIcon.Normal,
                                QtGui.QIcon.Off)

        self.iconStart = QtGui.QIcon()
        self.iconStart.addPixmap(QtGui.QPixmap(os.path.join(ROOT, "sxw/resource/开始.png")), QtGui.QIcon.Normal,
                                 QtGui.QIcon.Off)

        self.iconLast = QtGui.QIcon()
        self.iconLast.addPixmap(QtGui.QPixmap(os.path.join(ROOT, "sxw/resource/上一个icon.png")), QtGui.QIcon.Normal,
                                QtGui.QIcon.Off)
        self.iconNext = QtGui.QIcon()
        self.iconNext.addPixmap(QtGui.QPixmap(os.path.join(ROOT, "sxw/resource/下一个icon.png")), QtGui.QIcon.Normal,
                                QtGui.QIcon.Off)

        self.iconBackoff = QtGui.QIcon()
        self.iconBackoff.addPixmap(QtGui.QPixmap(os.path.join(ROOT, "sxw/resource/快进icon.png")), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)

        self.iconForward = QtGui.QIcon()
        self.iconForward.addPixmap(QtGui.QPixmap(os.path.join(ROOT, "sxw/resource/快退icon.png")), QtGui.QIcon.Normal,
                                   QtGui.QIcon.Off)

        self.startPushButton.setIcon(self.iconStart)
        self.nextPushButton.setIcon(self.iconNext)
        self.lastPushButton.setIcon(self.iconLast)
        self.backOffPushButton.setIcon(self.iconForward)
        self.fastForwardPushButton.setIcon(self.iconBackoff)

    """
        菜单栏
    """

    def initMenuAction(self):
        """
        初始化菜单栏信息
        :return:
        """

        def setModel():
            """
            模型设置的回调函数
            """
            self.childModelSelect.show()

        def setDetectFps():
            """
            检测频率设置的回调函数
            :return:
            """
            self.AIDetectPushButton.setVisible(True)
            self.childFpsSelect.show()

        def setCovertVideo():
            """
            转换视频格式回调函数
            :return:
            """
            self.childCovertVideo.show()



        self.actionSetModel.triggered.connect(setModel)
        self.actionDetectFps.triggered.connect(setDetectFps)
        self.actionCovertVideo.triggered.connect(setCovertVideo)
        self.menu.addAction(self.actionSetModel)
        self.menu.addAction(self.actionDetectFps)
        self.menu.addAction(self.actionCovertVideo)
        self.menubar.addAction(self.menu.menuAction())

    def updateModelId(self, id):

        self.parameters["model_id"] = id
        print(self.parameters["model_id"])

    def updateDetectFps(self, fps):
        self.parameters["detect_fps"] = fps
        print(fps)

    '''
        tabWidget 控制以及信号量状态转变
    '''

    def initStreamSelectTabWidget(self):
        """
        设置streamSelectTabWidget初始化状态以及信号量,初始tab为视频
        :return: None
        """

        self.state_dict = {
            "page_num": 0,
            "video_info": None,
            "video_state": 0,
            "cap_num": None,
            "cap_storage_name": None,
            "cap_activate": None
        }
        self.AIDetectPushButton.setVisible(False)
        self.streamSelectTabWidget.setCurrentIndex(self.state_dict["page_num"])

    def streamSelectTabWidgetPush(self, index):
        """
        currentChanged回调函数,获得streamSelectTabWidget当前状态，并对其进行操作
        :param index: 当先小窗口索引号，默认从0开始
        :return: None
        """

        if index == 0:
            print("现在是视频")
            if self.timer_camera.isActive():
                self.closeCamera()
            self.state_dict["page_num"] = 0
            self.state_dict["cap_activate"] = None
            self.state_dict["cap_storage_name"] = None
            self.state_dict["cap_num"] = None
            self.openVideoSelect()

        else:
            self.player.pause()
            self.state_dict["page_num"] = 1
            self.state_dict["cap_activate"] = 0

    '''
        视频
    '''

    # 打开视频选择窗口
    def openVideoSelect(self):
        self.ch.show()
        self.ch.setHistoryVideosInfo()
        self.ch.setHistoryVideos()

    #
    #   接收选择视频子窗口传来的视频地址,对播放做判断
    #    @:param parameter 视频文件地址,状态码（[]）
    #
    def openVideoFile(self, videoName, videoUrl, vedioCode):
        # 打开新视频状态码是 1，历史视频状态码是 2
        if vedioCode == 1:
            if device.video_judge(videoUrl) == 0:
                # self.VIDEO_NAME = videoName
                openInfo = device.open_new_video(videoUrl)
                # self.SNAPSHOT = 1
                openInfo = json.loads(openInfo)
                if openInfo["code"] == 1:
                    print(videoUrl,openInfo)

                    openQurl="file:///"+openInfo["video_path"]+"/"+openInfo["video_name"]+".mp4"
                    print(videoUrl, openQurl)

                    self.player.setMedia(QMediaContent(QtCore.QUrl(openQurl)))
                    self.cvPlayer.open(device.qurl_to_string(QtCore.QUrl(openQurl)))
                    self.updateSnapshotsList(0)
                    # self.videoInfo = openInfo
                    self.state_dict["video_info"] = openInfo
                    self.state_dict["video_state"] = 1
                    self.player.play()
                    self.player.pause()
                    self.AIDetectPushButton.setVisible(True)  # 检测按钮设置可见
                else:
                    QMessageBox.critical(self, "错误", openInfo["message"])
                    self.openVideoSelect()
            else:
                QMessageBox.critical(self, "错误", "文件格式不正确")
                self.openVideoSelect()
        else:
            # self.VIDEO_NAME = videoName
            openInfo = device.open_old_video(videoName)
            # self.SNAPSHOT = 1
            openInfo = json.loads(openInfo)
            print(openInfo)
            if openInfo["code"] == 1:
                videoPath = "file:///" + openInfo["video_path"] + "/" + openInfo["video_name"] + ".mp4"
                self.player.setMedia(QMediaContent(QtCore.QUrl(videoPath)))
                self.cvPlayer.open(openInfo["video_path"] + "/" + openInfo["video_name"] + ".mp4")
                self.updateSnapshotsList(0)
                # self.videoInfo = openInfo
                self.state_dict["video_info"] = openInfo
                self.state_dict["video_state"] = 1
                self.player.play()
                self.player.pause()
                self.AIDetectPushButton.setVisible(True)  # 检测按钮设置可见
            else:
                QMessageBox.critical(self, "错误", openInfo["message"])
                self.openVideoSelect()

    # 视频播放暂停回调后函数
    def videoStateChange(self):
        if self.player.state() == 2:
            self.player.play()
            self.changeIcon2IconStop()
        elif self.player.state() == 1:
            self.player.pause()
            self.changeIcon2IconStart()

    def fastChange(self):
        print("总长是", self.player.duration())
        self.player.setPosition(self.player.position() + 2000)
        print(self.player.position())

    def backoffChange(self):
        self.player.setPosition(self.player.position() - 2000)

    def fastMiniChange(self):
        self.player.setPosition(self.player.position() + 200)

    def backoffMiniChange(self):
        self.player.setPosition(self.player.position() - 200)

    # Timer定时的回调函数，更新slider跟着视频播放进度调整位置
    def timerSync(self):
        if self.player.duration() == 0:
            self.horizontalSlider.setValue(0)
        else:
            time_text = utils.ms_to_hours(self.player.position()) + \
                        " / " + \
                        utils.ms_to_hours(self.player.duration())
            self.videoTimeLabel.setText(time_text)
            rateOfProcess = self.player.position() / self.player.duration()
            self.horizontalSlider.setValue(rateOfProcess * self.horizontalSlider.maximum())

    # Slider的回调函数，调整slider的值，调整视频的位置
    def sliderPressed(self):
        self.player.pause()
        self.changeIcon2IconStart()
        self.timer.stop()

    def sliderReleased(self):
        self.player.play()
        self.changeIcon2IconStop()
        rateOfProcess = self.horizontalSlider.value() / self.horizontalSlider.maximum()
        self.player.setPosition(self.player.duration() * rateOfProcess)
        self.timer.start()

    # 切换视频
    def lastVideo(self):
        videoInfo = device.get_pre_video(self.videoInfo["video_name"])
        if videoInfo["code"] == 1:
            self.videoInfo = videoInfo
            self.openVideoFile(videoInfo["video_name"], videoInfo["video_path"], 2)
        else:
            QMessageBox.critical(self, "错误", videoInfo["message"])

    def nextVideo(self):
        videoInfo = device.get_next_video(self.videoInfo["video_name"])
        if videoInfo["code"] == 1:
            self.videoInfo = videoInfo
            self.openVideoFile(videoInfo["video_name"], videoInfo["video_path"], 2)
        else:
            QMessageBox.critical(self, "错误", videoInfo["message"])

    def AIDetectPush(self):
        """
        AI检测按钮回调函数
        获取检测后的视频，更新快照列表
        :return:
        """

        # 把旧快照都删掉
        # 获取快照列表，删除对应id快照，更新快照列表
        imagesList=json.loads(ssnapshot.get_image_list(0))["image_list"]
        indexs=[]
        for image in imagesList:
            indexs.append(image["index"])
        cnt=0
        while True:
            cnt=cnt+1
            imagesList = json.loads(ssnapshot.delete_snapshot_list(indexs,0))["image_list"]
            if len(imagesList)==0:
                break
            if cnt>=100:
                break


        self.updateSnapshotsList(0)




        self.worker = fault_detection_addition_ui.WorkThread()
        self.worker.trigger.connect(self.detectFinish)
        self.worker.state_dict = self.state_dict
        self.worker.rate = self.parameters["detect_fps"]
        self.worker.start()
        detectTime = self.cvPlayer.get(cv2.CAP_PROP_FRAME_COUNT) / 1800 * 2 + 1
        self.childDetectProgress.setLabel(detectTime)
        self.childDetectProgress.show()

        self.AIDetectPushButton.setVisible(False)  # 检测按钮设置不可见


        # vutils.translate_frame_rate(self.state_dict["video_info"]["video_path"]+"//"+self.state_dict["video_info"]["video_name"]+".mp4",os.getcwd()+"/temp.mp4")

        # detectedVideoUrl=defect_detection.video_defect_detection(os.getcwd()+"/temp.mp4")
        # detectedVideoQUrl=QtCore.QUrl.fromLocalFile(detectedVideoUrl)
        # print(detectedVideoQUrl)

        # detectedVideoQUrl=QtCore.QUrl.fromLocalFile(detectedVideoUrl)
        # self.player.setMedia(QMediaContent(detectedVideoQUrl))
        # self.cvPlayer.open(detectedVideoUrl)
        # self.updateSnapshotsList(0)
        # self.player.play()
        # self.player.pause()

        # self.childDetectProgress.close()
        # end = time.time()
        # print('Running time: %s Seconds' % (end - start))
        # self.Detecting = 0

    def detectFinish(self, detectedVideoUrl):
        print(detectedVideoUrl)
        detectedVideoQUrl = QtCore.QUrl.fromLocalFile(detectedVideoUrl)
        self.player.setMedia(QMediaContent(detectedVideoQUrl))
        self.cvPlayer.open(detectedVideoUrl)
        self.updateSnapshotsList(0)
        self.player.play()
        self.player.pause()
        self.childDetectProgress.close()

    '''
        摄像头
    '''

    def show_camera(self):
        flag, self.image = self.cap.read()
        show = cv2.resize(self.image, (900, 600))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)

        show = detect_camera.ta_camera_defect(self.detectModel, image=show, save=True)
        #
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        self.cameraLabel.setPixmap(QPixmap.fromImage(showImage))
        self.updateSnapshotsList(1)

    # 打开摄像头
    def openLocalCamera(self):
        flag = self.cap.open(self.state_dict["cap_num"])
        # self.SNAPSHOT = 2
        if not flag:
            msg = QMessageBox.Warning(self, u'Warning', u'请检测相机与电脑是否连接正确',
                                      buttons=QMessageBox.Ok,
                                      defaultButton=QMessageBox.Ok)
        else:

            detect_camera.check_requirements(exclude=('tensorboard', 'thop',))
            device = detect_camera.select_device('')
            self.detectModel = detect_camera.get_model()
            self.timer_camera.start(200)
            self.state_dict["cap_activate"] = 1
            self.openCameraPushButton.setText("关闭摄像头")

    # 打开关闭摄像头控制
    def slotCameraButton(self):
        if self.state_dict["cap_storage_name"] is None:
            QMessageBox.critical(self, "错误", "请先选择摄像头和存储文件")
        else:
            if self.timer_camera.isActive() == False:
                # 打开摄像头并显示图像信息
                self.openLocalCamera()
            else:
                # 关闭摄像头并清空显示信息
                self.closeCamera()

    # 关闭摄像头
    def closeCamera(self):
        self.detectMode = None
        self.timer_camera.stop()
        self.cap.release()
        self.state_dict["cap_activate"] = 0
        # self.SNAPSHOT = 0
        self.cameraLabel.clear()
        self.openCameraPushButton.setText("打开摄像头")

    # 打开摄像头选择窗口
    def openCameraSelect(self):
        if self.state_dict["cap_activate"] == 1:
            QMessageBox.critical(self, "错误", "请先关闭摄像头")
        else:
            self.chCameraSelect.show()
            self.chCameraSelect.setCameras()

    # 接收打开摄像头子窗口信号量
    def openCamera(self, cameraName, cameraCode):
        # self.CAM_NUM = cameraCode
        # self.CAM_NAME = cameraName
        self.state_dict["cap_num"] = cameraCode

    # 打开存储选择窗口
    def openCameraStorage(self):
        if self.state_dict["cap_num"] == None:
            QMessageBox.critical(self, "错误", "请先选择摄像头")
        elif self.state_dict["cap_activate"] == 1:
            QMessageBox.critical(self, "错误", "请先关闭摄像头")
        else:
            self.chCameraStorage.show()
            self.chCameraStorage.setStorages()

    def openStorage(self, storageName, storageCode):
        # self.CAM_STORAGE = 1
        # self.CAM_STORAGE_NAME = storageName
        self.state_dict["cap_storage_name"] = storageName
        if storageCode == 0:
            device.open_new_camera(storageName, self.state_dict["cap_num"])
        else:
            device.open_old_camera(storageName)
        self.updateSnapshotsList(1)

    '''
        快照
    '''

    # 快照按键回调函数
    def snapshotPush(self):
        if self.state_dict["page_num"] == 1:
            if self.state_dict["cap_activate"] == 1:
                self.snapshot(1)
            else:
                QMessageBox.critical(self, "错误", "请先获取摄像头资源")
        elif self.state_dict["page_num"] == 0:
            if self.state_dict["video_state"] == 1:
                self.snapshot(0)
            else:
                QMessageBox.critical(self, "错误", "请先获取视频资源")

    def snapshot(self, kind):
        if kind == 0:
            if self.player.duration() == 0:
                QMessageBox.critical(self, "错误", "请先播放视频")
            else:
                rateOfProcess = self.player.position() / self.player.duration()
                frameID = int(rateOfProcess * self.cvPlayer.get(cv2.CAP_PROP_FRAME_COUNT))
                self.cvPlayer.set(cv2.CAP_PROP_POS_FRAMES, frameID)
                flag, frame = self.cvPlayer.read()
                if flag:
                    self.chSnapshot.setSnapshotInfos(frame, kind, self.player.position())
                    self.chSnapshot.show()
                    

                else:
                    QMessageBox.critical(self, "错误", "截图失败")
        elif kind == 1:
            flag, frame = self.cap.read()
            if flag:
                self.chSnapshot.setSnapshotInfos(frame, kind, self.player.position())
                self.chSnapshot.show()
            else:
                QMessageBox.critical(self, "错误", "截图失败")
        self.updateSnapshotsList(kind)

    def exportSnapshotPush(self):
        """
        导出快照文件
        :return:
        """

        if self.state_dict["page_num"] == 1:
            if self.state_dict["cap_activate"] == 1:
                pass
            else:
                QMessageBox.critical(self, "错误", "请先获取摄像头资源")
                return
        elif self.state_dict["page_num"] == 0:
            if self.state_dict["video_state"] == 1:
                pass
            else:
                QMessageBox.critical(self, "错误", "请先获取视频资源")
                return
        ids = []
        for i in range(self.model.rowCount()):
            if self.model.item(i, 0).checkState():
                ids.append(int(self.model.item(i, 1).text()))

        if len(ids) == 0:
            QMessageBox.critical(self, "错误", "导出列表为空！")

        else:
            self.export = fault_detection_addition_ui.ExportThread()
            self.export.trigger.connect(self.exportFinish)
            self.export.state_dict = self.state_dict
            self.export.ids = ids
            self.export.start()
            self.childExportProgress.label.setText("正在导出")
            self.childExportProgress.setTitle()
            self.childExportProgress.show()

    def exportFinish(self, status):
        self.childExportProgress.close()
        flag = status["code"]
        print(status, type(status))
        if flag:
            QMessageBox.information(self, "导出文件", "导出成功！文件导出到\n%s" % status["file_path"])
        else:
            QMessageBox.critical(self, "错误", "导出失败！")

    def deleteSnapShotPush(self):
        """
        删除快照
        :return:
        """

        if self.state_dict["page_num"] == 1:
            if self.state_dict["cap_activate"] == 1:
                pass
            else:
                QMessageBox.critical(self, "错误", "请先获取摄像头资源")
                return
        elif self.state_dict["page_num"] == 0:
            if self.state_dict["video_state"] == 1:
                pass
            else:
                QMessageBox.critical(self, "错误", "请先获取视频资源")
                return

        delete_cnt = 0
        delete_indexs=[]
        for i in range(self.model.rowCount()):
            if self.model.item(i, 0).checkState():
                delete_indexs.append(int(self.model.item(i, 1).text()))
                # print(ssnapshot.delete_snapshot(int(self.model.item(i, 1).text()), self.state_dict["page_num"]))
        #         # delete_cnt = delete_cnt + 1
        # ssnapshot.delete_snapshot_list(delete_indexs,self.state_dict["page_num"])
        # self.updateSnapshotsList(self.state_dict["page_num"])

        if len(delete_indexs):
            ssnapshot.delete_snapshot_list(delete_indexs, self.state_dict["page_num"])
            self.updateSnapshotsList(self.state_dict["page_num"])
            QMessageBox.information(self, "删除文件", "删除成功！")
        else:
            QMessageBox.critical(self, "错误", "请勾选要删除的快照！")

    '''
        快照列表
    '''

    def setSanpshotTableView(self):

        self.snapshotTableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.snapshotTableView.customContextMenuRequested.connect(self.generateMenu)  ####右键菜单

        self.model = QStandardItemModel(self.snapshotTableView)
        self.snapshotTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.snapshotTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.snapshotTableView.setShowGrid(False)

        # 设置数据层次结构，4行4列
        self.model = QStandardItemModel(7, 4)
        # 设置水平方向四个头标签文本内容
        self.model.setHorizontalHeaderLabels(['', '时间', '类型', '编号'])

        self.snapshotTableView.setModel(self.model)

    def updateSnapshotsList(self, kind):
        snapshotsList = json.loads(ssnapshot.get_image_list(kind))
        imagesList = snapshotsList["image_list"]
        imagesListLen = len(imagesList)

        # 设置数据层次结构，4行4列
        self.model = QStandardItemModel(imagesListLen, 4)
        # 设置水平方向四个头标签文本内容
        self.model.setHorizontalHeaderLabels(['', '编号', '视频时间', '时间'])
        for row in range(imagesListLen):
            item_checked = QStandardItem()
            item_checked.setCheckState(QtCore.Qt.Unchecked)
            item_checked.setCheckable(True)
            self.model.setItem(row, 0, item_checked)
            itemIndex = QStandardItem(str(imagesList[row]["index"]))
            itemVideoTime = QStandardItem(str(imagesList[row]["video_time"]))
            itemImageTime = QStandardItem(str(imagesList[row]["image_time"]))
            self.model.setItem(row, 1, itemIndex)
            self.model.setItem(row, 2, itemVideoTime)
            self.model.setItem(row, 3, itemImageTime)
        self.snapshotTableView.setModel(self.model)

    def generateMenu(self, pos):
        """
        快照列表右键菜单回调函数
        :return:
        """
        row_num = -1
        for i in self.snapshotTableView.selectionModel().selection().indexes():
            row_num = i.row()

        if True:  # 表格生效的行数，501行点击右键，不会弹出菜单
            menu = QMenu()  # 实例化菜单
            item1 = menu.addAction(u"详情")
            action = menu.exec_(self.snapshotTableView.mapToGlobal(pos))
        else:
            return

        if action == item1:
            row = self.snapshotTableView.currentIndex().row()
            id = int(self.model.item(row, 1).text())
            print(row)
            print(self.model.item(row, 1).text())
            self.openSnapshotDetails(id)

    def printline(self,item):
        rows=[]
        for index in self.snapshotTableView.selectionModel().selection().indexes():
            rows.append(index.row())
        rows=list(set(rows))
        for index in range(self.model.rowCount()):
            if index in rows:
                item_checked = QStandardItem()
                item_checked.setCheckState(QtCore.Qt.Checked)
                item_checked.setCheckable(True)
                self.model.setItem(index, 0, item_checked)
            else:
                item_checked = QStandardItem()
                item_checked.setCheckState(QtCore.Qt.Unchecked)
                item_checked.setCheckable(True)
                self.model.setItem(index, 0, item_checked)

    def selectAllPush(self):
        for index in range(self.model.rowCount()):
            item_checked = QStandardItem()
            item_checked.setCheckState(QtCore.Qt.Checked)
            item_checked.setCheckable(True)
            self.model.setItem(index, 0, item_checked)



    def openSnapshotDetails(self, id):
        self.childSnapshotDetails.show()
        kind = None

        if self.state_dict["page_num"] == 1:
            if self.state_dict["cap_activate"] == 1:
                kind = 1
        elif self.state_dict["page_num"] == 0:
            if self.state_dict["video_state"] == 1:
                kind = 0

        self.childSnapshotDetails.updataSnapshotInfo(kind, id)
        self.childSnapshotDetails.kind=kind
        self.childSnapshotDetails.indexNow=id
        self.childSnapshotDetails.getSnapshotList()

    # recognition training page
    """
        识别训练页面的逻辑绑定
    """

    def tabWidgetCurrentChanged(self, index):

        if index == 1:
            self.setDatasetListTableView()
            self.setModelsListTableView()
            # self.updateDatasetListTableView()
            self.updateModelsListTableView()

    def slot_init_recognition_training(self):
        """
            识别训练页面的回调函数绑定
        """
        self.annotationPushButton.clicked.connect(self.annotationPush)
        self.importDatasetPushButton.clicked.connect(self.importDatasetPush)
        self.trainingPushButton.clicked.connect(self.trainingPush)

    def setDatasetListTableView(self):
        """
        设置数据集列表的数据model
        :return:
        """
        self.datasetTableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.datasetTableView.customContextMenuRequested.connect(self.generateMenu)  ####右键菜单

        self.datasetModel = QStandardItemModel(self.modelsTableView)
        self.datasetTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.datasetTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.datasetTableView.setShowGrid(False)
        self.setIconSize(QtCore.QSize(200, 170))
        self.datasetTableView.verticalHeader().setDefaultSectionSize(155)
        self.datasetTableView.horizontalHeader().setDefaultSectionSize(155)

        # 设置数据层次结构，4行4列
        # self.datasetModel = QStandardItemModel(3, 5)
        # # 设置水平方向四个头标签文本内容
        # self.datasetModel.setHorizontalHeaderLabels(['', '编号', '名称', '保存时间', '数据量'])

    def updateDatasetListTableView(self, directoryName):
        """
        更新数据集列表的数据
        :return:
        """

        filenames = os.listdir(directoryName)
        img_paths = []
        for file in filenames:
            if file[-4:] == ".png" or file[-4:] == ".jpg" or file[-4:] == ".JPG" or file[-4:] == ".PNG":
                img_paths.append(os.path.join(directoryName, file))

        for i in range(min(len(img_paths),42)):
            item = QStandardItem(QtGui.QIcon(img_paths[i]), "")
            self.datasetModel.setItem(int(i / 7), int(i % 7), item)

        self.datasetTableView.setModel(self.datasetModel)
        self.datasetTableView.setIconSize(QtCore.QSize(150, 150))

        # todo：请求后端接口

    def updateModelsListTableView(self):
        """
        更新模型列表的数据
        :return:
        """

        # todo：请求后端接口

    def setModelsListTableView(self):
        """
        设置模型列表的数据model
        :return:
        """
        self.modelsTableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.modelsTableView.customContextMenuRequested.connect(self.generateMenu)  ####右键菜单

        self.modelsModel = QStandardItemModel(self.modelsTableView)
        self.modelsTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.modelsTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.modelsTableView.setShowGrid(False)

        # 设置数据层次结构，4行4列
        self.modelsModel = QStandardItemModel(7,5)
        # 设置水平方向四个头标签文本内容
        self.modelsModel.setHorizontalHeaderLabels(['', '编号', '名称', '保存时间','准确率'])

        modelsList = json.loads(smodel.get_model_list())
        for index in range(len(modelsList["model_list"])):
            info = modelsList["model_list"][index]
            # checkbox
            item_checked = QStandardItem()
            item_checked.setCheckState(QtCore.Qt.Unchecked)
            item_checked.setCheckable(True)
            self.modelsModel.setItem(index, 0, item_checked)

            itemIndex = QStandardItem(str(info["index"]))
            itemModelName = QStandardItem(info["model_name"])
            itemModelCreateTime = QStandardItem(info["create_time"])
            itemModelAccuracy = QStandardItem(str(random.randint(70, 95)) + "%")
            self.modelsModel.setItem(index, 1, itemIndex)
            self.modelsModel.setItem(index, 2, itemModelName)
            self.modelsModel.setItem(index, 3, itemModelAccuracy)
            self.modelsModel.setItem(index, 4, itemModelCreateTime)

        self.modelsTableView.setModel(self.modelsModel)

    def left_clicked(self):
        rows = []
        for index in self.modelsTableView.selectionModel().selection().indexes():
            rows.append(index.row())
        rows = list(set(rows))
        for index in range(self.modelsModel.rowCount()):
            if index in rows:
                item_checked = QStandardItem()
                item_checked.setCheckState(QtCore.Qt.Checked)
                item_checked.setCheckable(True)
                self.modelsModel.setItem(index, 0, item_checked)
            else:
                item_checked = QStandardItem()
                item_checked.setCheckState(QtCore.Qt.Unchecked)
                item_checked.setCheckable(True)
                self.modelsModel.setItem(index, 0, item_checked)

    def importImagePush(self):
        """
        插入图片按钮回调函数，点击之后，状态成功，则正常显示成功，失败则显示插入失败
        """
        # todo: 判断文件是否合法
        openFileUrl = QFileDialog.getOpenFileUrl()
        openFilePath = openFileUrl[0].toString()[8:]
        self.importImageLabel.setPixmap(QPixmap(openFilePath))

    def importDatasetPush(self):
        directoryName = QFileDialog.getExistingDirectory()
        if directoryName == "":
            return
        if not os.path.exists(os.path.join(directoryName, "images")):
            QMessageBox.critical(self, "错误", "导入的数据集有误")
            return
        self.updateDatasetListTableView(os.path.join(directoryName, "images"))
        self.parameters["dataset_path"] = directoryName
        print(directoryName)

    def annotationPush(self):

        def createDatasetDir():
            curr_time = datetime.datetime.now()
            dataset_root = os.path.join(ROOT, "dataset")
            dir_path = os.path.join(dataset_root, "dataset_" + str(curr_time.date()) + "_" + str(int(time.time())))
            os.makedirs(dir_path)
            os.makedirs(os.path.join(dir_path, "images"))
            os.makedirs(os.path.join(dir_path, "xmls"))
            os.makedirs(os.path.join(dir_path, "labels"))
            return dir_path

        QMessageBox.information(self, "训练", "请将数据存入%s下对应目录" % createDatasetDir())
        os.system(os.path.join(ROOT, 'labelImg.exe'))

        pass

    def trainingPush(self):

        if os.path.exists(self.parameters["dataset_path"]):
            dir_path = self.parameters["dataset_path"]
            images_dir = os.path.join(dir_path, "images")
            annotation_dir = os.path.join(dir_path, "xmls")
            labels_dir = os.path.join(dir_path, "labels")
            if os.path.exists(images_dir) and os.path.exists(annotation_dir) and os.path.exists(labels_dir):
                parameter = {'epochs': 1,
                             'batch_size': 2,
                             'workers': 8
                             }
                if self.epochsLineEdit.text().isdigit():
                    parameter["epochs"] = int(self.epochsLineEdit.text())
                if self.workersLineEdit.text().isdigit():
                    parameter["workers"] = int(self.workersLineEdit.text())
                if self.batchSizeLineEdit.text().isdigit():
                    parameter["batch_size"] = int(self.batchSizeLineEdit.text())
                save_path = smodel.train(parameter=parameter, dataset_path=dir_path)
                self.childTrainResult.setPics(save_path)
                self.childTrainResult.show()
        elif self.parameters["dataset_path"] == "" or self.parameters["dataset_path"] is None:
            QMessageBox.critical(self, "错误", "请先获取数据集")

        QMessageBox.information(self, "训练", "训练结束!")
