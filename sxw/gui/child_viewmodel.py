from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

import child  # 刚刚转为py文件的UI文件名
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from PyQt5 import QtCore


class Child(QMainWindow, child.Ui_MainWindow):

    # 向父窗口传递打开文件名的信号量
    _signal = QtCore.pyqtSignal(QtCore.QUrl)
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.slot_init()
        self.historyVideos=['file:///C:/Users/11795/Videos/航拍海水翻着白浪席卷沙滩_爱给网_aigei_com.mp4',
                            'file:///C:/Users/11795/Videos/航拍海水翻着白浪席卷沙滩_爱给网_aigei_com.mp4',
                            'file:///C:/Users/11795/Videos/航拍海水翻着白浪席卷沙滩_爱给网_aigei_com.mp4',
                            'file:///C:/Users/11795/Videos/航拍海水翻着白浪席卷沙滩_爱给网_aigei_com.mp4']
        self.selectedItem=None
    # 绑定回调函数
    def slot_init(self):
        self.searchPushButton.clicked.connect(lambda: self.searchVideoFile())
        self.openVedioPushButton.clicked.connect(lambda: self.openHistoryVideoFile() )

    # 查找视频文件
    def searchVideoFile(self):
        # openFileUrl PyQt5.QtCore.QUrl
        openFileUrl=QFileDialog.getOpenFileUrl()
        self._signal.emit(openFileUrl[0])
        self.close()

    # 打开历史视频文件
    def openHistoryVideoFile(self):
        if self.selectedItem==None:
            print("您还咩有选择视频文件")
        else:
            openFileUrl=QtCore.QUrl(self.historyVideos[self.selectedItem.row()])
            print(openFileUrl)
            self._signal.emit(openFileUrl)
            self.close()


    '''
        填充历史视频列表
    '''
    def setHistoryVideos(self):
        # 实例化列表模型，添加数据
        slm = QtCore.QStringListModel()
        # 设置模型列表视图，加载数据列表
        slm.setStringList(self.historyVideos)
        self.videosHistoryListView.setModel(slm)
        # 单击触发自定义的槽函数
        self.videosHistoryListView.clicked.connect(self.clicked)

    '''
        视频列表点击回调函数
    '''
    def clicked(self, qModelIndex):
        self.selectedItem=qModelIndex
        print(qModelIndex)
        # 控制台，你选择的信息
        print('你选择了：'+self.historyVideos[qModelIndex.row()])