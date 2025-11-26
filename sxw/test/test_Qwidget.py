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

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    button_widget = QWidget()
    layout = QHBoxLayout(button_widget)
    layout.addWidget(QPushButton("Button 1"))
    layout.addWidget(QPushButton("Button 2"))
    layout.addWidget(QPushButton("Button 3"))
    button_widget.show()
    sys.exit(app.exec_())