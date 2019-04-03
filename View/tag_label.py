from PyQt5.QtCore import Qt, QMimeData, QDataStream, QIODevice
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QLabel


class TagLabel(QLabel):
    # todo Label拖拽功能

    def __init__(self, parent=None):
        super(self).__init__(parent)
        self.setAcceptDrops(True)  # step1 True

    def dragEnterEvent(self, event):  # step2 dragEnterEvent:accept
        if event.mimeData().hasFormat("application/x-icon-and-text"):
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):  # step3 dragMoveEvent:Copy or Move
        if event.mimeData().hasFormat("application/x-icon-and-text"):
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):  # step4 dropEvent:get data
        if event.mimeData().hasFormat("application/x-icon-and-text"):
            data = event.mimeData().data("application/x-icon-and-text")
            stream = QDataStream(data, QIODevice.ReadOnly)
            text = stream.readQString()
            self.setText(text)
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()


