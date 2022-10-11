import os
from configparser import ConfigParser
import initialization
from PyQt5.QtCore import QUrl


def video_judge(QUrl_path):
    #  PyQt5.QtCore.QUrl
    path = QUrl_path.toString()
    if os.path.isfile(path) is not True:
        return 1  # 错误码1，文件不存在
    if ".mp4" not in path:
        return 2  # 错误码2，文件类型错误
    return 0  # 文件类型检查无误，可以打开


def history_video():
    config_path = initialization.get_root_path() + "/system.ini"
    conf = ConfigParser()
    conf.read(config_path)
    path = conf.get("path_config", "device_path")
    all_devices = []
    for directory in os.listdir(path):
        all_devices.append(path + directory)
    return all_devices


def new_video():
    pass


if __name__ == '__main__':
    print(video_judge("xxx.mp4"))
    print(history_video())
