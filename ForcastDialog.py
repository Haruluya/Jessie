import os

from PyQt5 import QtCore
from PyQt5.QtCore import *
from playsound import playsound
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from qtpy import QtWidgets

import ForcastDialogView


class ForcastDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog,self).__init__(parent)
        self.ui = ForcastDialogView.Ui_ForCastDialogView()
        self.ui.setupUi(self)

    @QtCore.pyqtSlot()
    def on_fileLinkButton_clicked(self):
        target = self.ui.fileLinkButton
        self.animation = QPropertyAnimation(self, b'geometry')
        self.animation.setDuration(150)
        self.animation.setTargetObject(target)
        self.animation.setStartValue(QRect(target.x(), target.y(), target.width(), target.height()))
        self.animation.setKeyValueAt(0.5,
                                     QRect(target.x() - 5, target.y() - 5, target.width() + 10, target.height() + 10))
        self.animation.setEndValue(QRect(target.x(), target.y(), target.width(), target.height()))
        self.animation.start()
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取方言语音文件", os.getcwd(),
                                                    "All Files(*);;Text Files(*.wav)")
        self.vedioFileName = fileName
        self.ui.fileNameLabel.setText(fileName.split('/')[-1])
        self.ui.fileNameLabel.showBorder = "true"

    @QtCore.pyqtSlot()
    def on_vedioButton_clicked(self):
        if (self.vedioFileName):
            playsound(self.vedioFileName)




