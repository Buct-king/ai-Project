import sys
import fault_detection_viewmodel  # 刚刚转为py文件的UI文件名，我的是untitled
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = fault_detection_viewmodel.Fault_Detection()
    window.show()
    sys.exit(app.exec_())