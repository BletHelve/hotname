# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\code\python\rename\view\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(619, 344)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.format_choice_frame = QtWidgets.QFrame(self.centralwidget)
        self.format_choice_frame.setGeometry(QtCore.QRect(10, 180, 591, 61))
        self.format_choice_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.format_choice_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.format_choice_frame.setObjectName("format_choice_frame")
        self.label_6 = QtWidgets.QLabel(self.format_choice_frame)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setObjectName("label_6")
        self.add_format_btn = QtWidgets.QPushButton(self.format_choice_frame)
        self.add_format_btn.setGeometry(QtCore.QRect(540, 10, 41, 41))
        self.add_format_btn.setObjectName("add_format_btn")
        self.format_lineEdit = QtWidgets.QLineEdit(self.format_choice_frame)
        self.format_lineEdit.setGeometry(QtCore.QRect(80, 10, 451, 41))
        self.format_lineEdit.setAcceptDrops(False)
        self.format_lineEdit.setObjectName("format_lineEdit")
        self.table_frame = QtWidgets.QFrame(self.centralwidget)
        self.table_frame.setGeometry(QtCore.QRect(290, 20, 311, 61))
        self.table_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.table_frame.setObjectName("table_frame")
        self.label_2 = QtWidgets.QLabel(self.table_frame)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.tb_box = QtWidgets.QComboBox(self.table_frame)
        self.tb_box.setGeometry(QtCore.QRect(60, 10, 191, 41))
        self.tb_box.setAcceptDrops(True)
        self.tb_box.setObjectName("tb_box")
        self.add_tb_btn = QtWidgets.QPushButton(self.table_frame)
        self.add_tb_btn.setGeometry(QtCore.QRect(260, 10, 41, 41))
        self.add_tb_btn.setObjectName("add_tb_btn")
        self.format_name_frame = QtWidgets.QFrame(self.centralwidget)
        self.format_name_frame.setGeometry(QtCore.QRect(10, 20, 271, 61))
        self.format_name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.format_name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.format_name_frame.setObjectName("format_name_frame")
        self.label = QtWidgets.QLabel(self.format_name_frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 21))
        self.label.setObjectName("label")
        self.name_lineEdit = QtWidgets.QLineEdit(self.format_name_frame)
        self.name_lineEdit.setGeometry(QtCore.QRect(80, 10, 181, 41))
        self.name_lineEdit.setAcceptDrops(False)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.btn_frame = QtWidgets.QFrame(self.centralwidget)
        self.btn_frame.setGeometry(QtCore.QRect(10, 260, 591, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_frame.sizePolicy().hasHeightForWidth())
        self.btn_frame.setSizePolicy(sizePolicy)
        self.btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btn_frame.setObjectName("btn_frame")
        self.save_btn = QtWidgets.QPushButton(self.btn_frame)
        self.save_btn.setGeometry(QtCore.QRect(150, 10, 93, 28))
        self.save_btn.setObjectName("save_btn")
        self.clear_btn = QtWidgets.QPushButton(self.btn_frame)
        self.clear_btn.setGeometry(QtCore.QRect(340, 10, 93, 28))
        self.clear_btn.setObjectName("clear_btn")
        self.tb_tags_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tb_tags_tableWidget.setGeometry(QtCore.QRect(90, 100, 451, 61))
        self.tb_tags_tableWidget.setObjectName("tb_tags_tableWidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 61, 41))
        self.label_3.setObjectName("label_3")
        self.help_btn = QtWidgets.QPushButton(self.centralwidget)
        self.help_btn.setGeometry(QtCore.QRect(550, 110, 41, 41))
        self.help_btn.setObjectName("help_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "格式:"))
        self.add_format_btn.setText(_translate("MainWindow", "+"))
        self.label_2.setText(_translate("MainWindow", "表格"))
        self.add_tb_btn.setText(_translate("MainWindow", "+"))
        self.label.setText(_translate("MainWindow", "格式名"))
        self.save_btn.setText(_translate("MainWindow", "保存"))
        self.clear_btn.setText(_translate("MainWindow", "清空"))
        self.label_3.setText(_translate("MainWindow", "表格列"))
        self.help_btn.setText(_translate("MainWindow", "？"))
