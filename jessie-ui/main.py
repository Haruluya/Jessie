import sys
import os
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from qtpy import QtGui

import DialectsClassificationView
from ForcastDialog import ForcastDialog
from QssHelper import QssHelper


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = DialectsClassificationView.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

    @QtCore.pyqtSlot()
    def on_SixClasButton_clicked(self):
        target = self.ui.SixClasButton
        self.animation = QPropertyAnimation(self, b'geometry')
        self.animation.setDuration(150)
        self.animation.setTargetObject(target)
        self.animation.setStartValue(QRect(target.x(), target.y(), target.width(), target.height()))
        self.animation.setKeyValueAt(0.5,
                                     QRect(target.x() - 5, target.y() - 5, target.width() + 10, target.height() + 10))
        self.animation.setEndValue(QRect(target.x(), target.y(), target.width(), target.height()))
        self.animation.start()
        self.ForcastDialog = ForcastDialog(type='SixClas')
        self.ForcastDialog.setStyleSheet(forcastDialogQssStyle)
        self.ForcastDialog.show()
        self.ForcastDialog.move(1200,200)

    @QtCore.pyqtSlot()
    def on_JDClasButton_clicked(self):
        target = self.ui.JDClasButton
        self.animation = QPropertyAnimation(self, b'geometry')
        self.animation.setDuration(150)
        self.animation.setTargetObject(target)
        self.animation.setStartValue(QRect(target.x(), target.y(), target.width(), target.height()))
        self.animation.setKeyValueAt(0.5,
                                     QRect(target.x() - 5, target.y() - 5, target.width() + 10, target.height() + 10))
        self.animation.setEndValue(QRect(target.x(), target.y(), target.width(), target.height()))
        self.animation.start()
        self.ForcastDialog = ForcastDialog(type='JDClas')
        self.ForcastDialog.setStyleSheet(forcastDialogQssStyle)
        self.ForcastDialog.show()
        self.ForcastDialog.move(1200,200)


    @QtCore.pyqtSlot()
    def on_DocumentLink_clicked(self):
        # self.browser = QWebEngineView()
        # self.browser.load("")
        # self.setCentralWidget(self.browser)
        target = self.ui.DocumentLink
        self.animation = QPropertyAnimation(self, b'geometry')
        self.animation.setDuration(150)
        self.animation.setTargetObject(target)
        self.animation.setStartValue(QRect(target.x(), target.y(), target.width(), target.height()))
        self.animation.setKeyValueAt(0.5,
                                     QRect(target.x() - 5, target.y() - 5, target.width() + 10, target.height() + 10))
        self.animation.setEndValue(QRect(target.x(), target.y(), target.width(), target.height()))
        self.animation.start()

    @QtCore.pyqtSlot()
    def on_AboutAuthLink_clicked(self):
    #     self.browser = QWebEngineView()
    #     self.browser.load("")
    #     self.setCentralWidget(self.browser)
        target = self.ui.AboutAuthLink
        self.animation = QPropertyAnimation(self, b'geometry')
        self.animation.setDuration(150)
        self.animation.setTargetObject(target)
        self.animation.setStartValue(QRect(target.x(), target.y(), target.width(), target.height()))
        self.animation.setKeyValueAt(0.5,
                                     QRect(target.x() - 5, target.y() - 5, target.width() + 10, target.height() + 10))
        self.animation.setEndValue(QRect(target.x(), target.y(), target.width(), target.height()))
        self.animation.start()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 设置qss样式。
    styleFile = './style.qss'
    qssStyle = QssHelper.readQss(styleFile)
    forcastDialogQssStyleFile = './forcastDialogStyle.qss'
    forcastDialogQssStyle = QssHelper.readQss(forcastDialogQssStyleFile)

    QtGui.QFontDatabase.addApplicationFont("./font.ttf")

    # 初始化窗口。
    mainWindow = MainWindow()
    mainWindow.setStyleSheet(qssStyle)
    mainWindow.show()
    sys.exit(app.exec_())
