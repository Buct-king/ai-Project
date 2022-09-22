import sys
import PyQt5
import test_ui  # 刚刚转为py文件的UI文件名，我的是untitled
from PyQt5.QtWidgets import QApplication, QMainWindow
import test_openVideo

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = test_ui.UI()
    window.show()
    sys.exit(app.exec_())