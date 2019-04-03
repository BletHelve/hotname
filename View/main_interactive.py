from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QFont
from PyQt5.QtWidgets import QFileDialog

from model.table import Table
from PyQt5 import QtCore, QtGui, QtWidgets

from view.main_window import Ui_MainWindow


class MainInteractive(Ui_MainWindow):
    __name2table = {}
    __excel_path = ''

    def __init__(self):
        super().__init__()
        self.tb_box.addItem('无')
        self.set_event_listeners()

    def update_label_group(self, col):
        labels = []
        for i in range(col):
            label = QtWidgets.QLabel()
            labels.append(label)
            self.tb_box_layout.addWidget(label, 0, i)
        for i in range(col):
            if i < len(self.__tb_tags):
                labels[i].setText(self.__tb_tags[i])
            else:  # 多出来的部分清空
                labels[i].setText('')
        self.tb_tags_label_group.setLayout(self.tb_box_layout)

    def set_event_listeners(self):
        self.tb_box.currentIndexChanged.connect(self.select_tb_name)
        self.add_table_btn.clicked.connect(self.get_file)

    def select_tb_name(self):
        tb_name = self.tb_box.currentText()
        if tb_name != '空':
            table = self.__name2table[tb_name]
            self.__tb_tags = table.get_tb_tags()
            self.update_label_group(10)  # 在目前界面尺寸，10 能够占满空间

    def get_file(self):
        excel_path, file_type = QFileDialog.getOpenFileName(self, '载入表格', 'C:\\', 'Excel Files (*.xlsx)')
        tb = Table(excel_path)
        fname = tb.get_name()
        if fname not in self.__name2table.keys():
            self.__name2table[fname] = tb
            self.tb_box.addItem(fname)
        else:
            print('表已存在')

