import sys
import PyQt5
import ui  # 刚刚转为py文件的UI文件名，我的是untitled
from PyQt5.QtWidgets import QApplication, QMainWindow
import fauilt_detection
from PyQt5 import QtWidgets
class Main(QMainWindow, fauilt_detection.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.slot_init()

    def browse(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', '.')
        fname = open(filename)
        data = fname.read()
        self.textEdit.setText(data)
        fname.close()

    def slot_init(self):
        self.oepnVideoPushButton.clicked.connect(lambda: self.browse())

if __name__ == "__main__":
    app =QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())