import sys
import os
import shutil
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QListWidget, QApplication

import watchFile
import yaml_rw
from table import Table
from PyQt5 import QtCore, QtWidgets

from main_window import Ui_MainWindow


class MainInteractive(Ui_MainWindow):
    name2table = {}

    def __init__(self):
        super().__init__()
        for excel in yaml_rw.read()['excel']:  # 从配置文件导出excel文件名
            tb_name = os.path.splitext(excel)[0]  # 去后缀名
            self.tb_box.addItem(tb_name)
            if excel != '无':
                self.name2table[tb_name] = Table('excel\\'+excel)
        self.set_format_list_widget()
        self.set_tb_tags_table_widget()
        self.set_event_listeners()

    def set_tb_tags_table_widget(self):
        self.tb_tags_tableWidget.setRowCount(1)
        self.tb_tags_tableWidget.setColumnCount(10)
        self.tb_tags_tableWidget.horizontalHeader().setVisible(False)
        self.tb_tags_tableWidget.verticalHeader().setVisible(False)

    def set_event_listeners(self):
        self.tb_box.currentIndexChanged.connect(self.select_tb_name)
        self.add_tb_btn.clicked.connect(self.get_file)
        self.tb_tags_tableWidget.itemClicked.connect(self.input_tb_tag)
        self.save_btn.clicked.connect(self.save)
        self.clear_btn.clicked.connect(self.clear)
        self.add_format_btn.clicked.connect(self.add_format)

    def update_label_group(self, tb_tags):
        for i in range(len(tb_tags)):
            item = QTableWidgetItem(tb_tags[i])
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tb_tags_tableWidget.setItem(0, i, item)

    def save(self):
        format_name = self.name_lineEdit.text()
        format_ = self.format_lineEdit.text()
        #  todo 弹出提示框
        if format_name == '':
            print('格式名为空')
            return
        if self.format_lineEdit.text() == '':
            print('格式为空')
            return
        if format_name not in watchFile.rename_dict.keys():
            format_index = len(watchFile.format_list)
            table_index = self.tb_box.currentIndex()
            watchFile.format_list.append(format_)
            yaml_rw.write('format', format_)
            watchFile.rename_dict[format_name] = [format_index, table_index]
            yaml_rw.write('rename', {format_name: [format_index, table_index]})
            os.mkdir('watch\\'+format_name)  # 在watch（监控文件）创建与格式名同名的文件夹
            self.clear()
        else:
            print('命名格式名已经存在，请重新更名')

    def clear(self):
        self.name_lineEdit.setText('')
        self.format_lineEdit.setText('')
        self.tb_box.setCurrentIndex(0)

    def input_tb_tag(self, item):
        text = self.format_lineEdit.text()
        self.format_lineEdit.setText(text+'%'+item.text()+'%')

    def select_tb_name(self):
        tb_name = self.tb_box.currentText()
        if tb_name != '无':
            table = self.name2table[tb_name]
            self.update_label_group(table.get_tb_tags())
        else:
            self.tb_tags_tableWidget.clear()

    def get_file(self):
        excel_path, file_type = QFileDialog.getOpenFileName(self, '载入表格', 'C:\\', 'Excel Files (*.xlsx)')
        if not excel_path:
            return
        #  todo 可以获得多种excel后缀名
        excel = os.path.basename(excel_path)  # 带后缀名文件名
        tb_name = os.path.splitext(excel)[0]  # 无后缀名文件名
        if tb_name not in self.name2table.keys():  # 查看是否存在同名文件（包括不同后缀名）
            shutil.copy(excel_path, 'excel')  # 把excel文件保存到excel文件夹
            watchFile.excel_list.append(excel)
            yaml_rw.write('excel', excel)
            self.name2table[tb_name] = Table(excel_path)
            self.tb_box.addItem(tb_name)
            self.tb_box.setCurrentText(tb_name)
            self.select_tb_name()
        else:
            print('表已存在')  # todo 弹出提示框

    def set_format_list_widget(self):
        self.format_list_widget = QListWidget()
        self.format_list_widget.resize(300, 120)
        self.format_list_widget.setWindowTitle('已保存格式')
        self.format_list_widget.itemClicked.connect(self.choice_format)

    def add_format(self):
        self.format_list_widget.addItems(watchFile.format_list)
        self.format_list_widget.show()

    def choice_format(self, item):
        self.format_lineEdit.setText(item.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 建立application对象
    window = MainInteractive()  # 建立窗体对象
    window.show()  # 显示窗体
    sys.exit(app.exec())  # 运行程序
