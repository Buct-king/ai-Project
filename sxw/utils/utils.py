"""
    工具文件
"""
from PyQt5 import QtCore

def ms_to_hours(millis):
    """
    毫秒转化为格式化时间
    :param millis: 毫秒
    :return: 格式化时间
    """
    seconds, milliseconds = divmod(millis, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return ("%02d:%02d:%02d" % (hours, minutes, seconds))

def url_to_QUrl(url):
    qUrl="file:///" +url
    return QtCore.QUrl(qUrl)
