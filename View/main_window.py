# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\code\python\rename\view\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

from model.table import Table

name2table = {'table': 'C:\\Users\\烂柯\\Desktop\\table.xlsx'}


class Ui_MainWindow(QtWidgets.QMainWindow):

    __tb = None
    __tb_tags = []

    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1216, 930)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rename_frame = QtWidgets.QFrame(self.centralwidget)
        self.rename_frame.setGeometry(QtCore.QRect(20, 10, 841, 481))
        self.rename_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rename_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rename_frame.setObjectName("rename_frame")
        self.format_choice_frame = QtWidgets.QFrame(self.rename_frame)
        self.format_choice_frame.setGeometry(QtCore.QRect(50, 10, 321, 61))
        self.format_choice_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.format_choice_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.format_choice_frame.setObjectName("format_choice_frame")
        self.label_6 = QtWidgets.QLabel(self.format_choice_frame)
        self.label_6.setGeometry(QtCore.QRect(10, 0, 71, 61))
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setObjectName("label_6")
        self.format_choice_box = QtWidgets.QComboBox(self.format_choice_frame)
        self.format_choice_box.setGeometry(QtCore.QRect(90, 10, 211, 41))
        self.format_choice_box.setObjectName("format_choice_box")
        self.file_addRR_frame = QtWidgets.QFrame(self.rename_frame)
        self.file_addRR_frame.setGeometry(QtCore.QRect(10, 80, 811, 391))
        self.file_addRR_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.file_addRR_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.file_addRR_frame.setObjectName("file_addRR_frame")
        self.label = QtWidgets.QLabel(self.file_addRR_frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 72, 15))
        self.label.setObjectName("label")


        self.file_treeView = QtWidgets.QTreeView(self.file_addRR_frame)
        self.file_treeView.setGeometry(QtCore.QRect(0, 20, 801, 301))
        self.file_treeView.setObjectName("file_treeView")
        self.start_btn = QtWidgets.QPushButton(self.file_addRR_frame)
        self.start_btn.setGeometry(QtCore.QRect(350, 330, 121, 51))
        self.start_btn.setObjectName("start_btn")
        self.add_table_btn = QtWidgets.QPushButton(self.file_addRR_frame)
        self.add_table_btn.setGeometry(QtCore.QRect(130, 330, 121, 51))
        self.add_table_btn.setObjectName("add_table_btn")
        self.add_format_btn = QtWidgets.QPushButton(self.file_addRR_frame)
        self.add_format_btn.setGeometry(QtCore.QRect(570, 330, 131, 51))
        self.add_format_btn.setObjectName("add_format_btn")
        self.table_frame = QtWidgets.QFrame(self.rename_frame)
        self.table_frame.setGeometry(QtCore.QRect(450, 10, 291, 61))
        self.table_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.table_frame.setObjectName("table_frame")
        self.label_2 = QtWidgets.QLabel(self.table_frame)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 71, 61))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")

        self.tb_box = QtWidgets.QComboBox(self.table_frame)
        self.tb_box.setGeometry(QtCore.QRect(90, 10, 191, 41))
        self.tb_box.setObjectName("tb_box")
        self.tb_box_layout = QtWidgets.QGridLayout()



        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(30, 490, 831, 311))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.tb_tags_label_group = QtWidgets.QGroupBox(self.frame_4)
        self.tb_tags_label_group.setGeometry(QtCore.QRect(10, 10, 401, 80))
        self.tb_tags_label_group.setObjectName("tb_tags_label_group")
        self.keys_label_group = QtWidgets.QGroupBox(self.frame_4)
        self.keys_label_group.setGeometry(QtCore.QRect(430, 10, 371, 81))
        self.keys_label_group.setObjectName("keys_label_group")
        self.frame_label_group = QtWidgets.QGroupBox(self.frame_4)
        self.frame_label_group.setGeometry(QtCore.QRect(10, 220, 801, 81))
        self.frame_label_group.setObjectName("frame_label_group")
        self.tags_label_group = QtWidgets.QGroupBox(self.frame_4)
        self.tags_label_group.setGeometry(QtCore.QRect(10, 110, 801, 91))
        self.tags_label_group.setObjectName("tags_label_group")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "格式选择:"))
        self.label.setText(_translate("MainWindow", "文件导入"))
        self.start_btn.setText(_translate("MainWindow", "开始"))
        self.add_table_btn.setText(_translate("MainWindow", "添加表格"))
        self.add_format_btn.setText(_translate("MainWindow", "添加格式"))
        self.label_2.setText(_translate("MainWindow", "表格选择:"))
        self.tb_tags_label_group.setTitle(_translate("MainWindow", "表格标签"))
        self.keys_label_group.setTitle(_translate("MainWindow", "主键"))
        self.frame_label_group.setTitle(_translate("MainWindow", "名称格式"))
        self.tags_label_group.setTitle(_translate("MainWindow", "普通标签"))



