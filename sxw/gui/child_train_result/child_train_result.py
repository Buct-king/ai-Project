# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'child_train_result.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(969, 822)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 10, 101, 31))
        self.label.setStyleSheet("font: 14pt \"Adobe Devanagari\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.resultsPicLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultsPicLabel.setGeometry(QtCore.QRect(40, 50, 890, 350))
        self.resultsPicLabel.setStyleSheet("border-radius: 4px;  \n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0)")
        self.resultsPicLabel.setScaledContents(True)
        self.resultsPicLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultsPicLabel.setObjectName("resultsPicLabel")
        self.confusionMatrixPicLabel = QtWidgets.QLabel(self.centralwidget)
        self.confusionMatrixPicLabel.setGeometry(QtCore.QRect(40, 460, 291, 291))
        self.confusionMatrixPicLabel.setStyleSheet("border-radius: 4px;  \n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0)")
        self.confusionMatrixPicLabel.setScaledContents(True)
        self.confusionMatrixPicLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.confusionMatrixPicLabel.setObjectName("confusionMatrixPicLabel")
        self.labelsPicLabel = QtWidgets.QLabel(self.centralwidget)
        self.labelsPicLabel.setGeometry(QtCore.QRect(340, 460, 291, 291))
        self.labelsPicLabel.setStyleSheet("border-radius: 4px;  \n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0)")
        self.labelsPicLabel.setScaledContents(True)
        self.labelsPicLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.labelsPicLabel.setObjectName("labelsPicLabel")
        self.labelsCorrelogramPicLabel = QtWidgets.QLabel(self.centralwidget)
        self.labelsCorrelogramPicLabel.setGeometry(QtCore.QRect(640, 460, 291, 291))
        self.labelsCorrelogramPicLabel.setStyleSheet("border-radius: 4px;  \n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0)")
        self.labelsCorrelogramPicLabel.setScaledContents(True)
        self.labelsCorrelogramPicLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.labelsCorrelogramPicLabel.setObjectName("labelsCorrelogramPicLabel")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(450, 410, 54, 12))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 760, 101, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(460, 760, 41, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(730, 760, 131, 16))
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 969, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "训练结果"))
        self.resultsPicLabel.setText(_translate("MainWindow", "TextLabel"))
        self.confusionMatrixPicLabel.setText(_translate("MainWindow", "TextLabel"))
        self.labelsPicLabel.setText(_translate("MainWindow", "TextLabel"))
        self.labelsCorrelogramPicLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "results"))
        self.label_7.setText(_translate("MainWindow", "confusion_matrix"))
        self.label_8.setText(_translate("MainWindow", "labels"))
        self.label_9.setText(_translate("MainWindow", "labels_correlogram"))
