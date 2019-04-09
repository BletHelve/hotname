import sys

from PyQt5.QtWidgets import QFileDialog, QMenu, QAction, QTableWidgetItem

from model.table import Table
from PyQt5 import QtCore, QtGui, QtWidgets

from view.main_window import Ui_MainWindow


class MainInteractive(Ui_MainWindow):
    name2table = {}
    excel_path = ''
    app = QtWidgets.QApplication(sys.argv)  # 建立application对象

    def __init__(self):
        super().__init__()
        self.tb_box.addItem('无')
        self.set_tb_tags_table_widget()
        self.set_event_listeners()

    def set_tb_tags_table_widget(self):
        self.tb_tags_tableWidget.setRowCount(1)
        self.tb_tags_tableWidget.setColumnCount(10)
        self.tb_tags_tableWidget.horizontalHeader().setVisible(False)
        self.tb_tags_tableWidget.verticalHeader().setVisible(False)

    def update_label_group(self, tb_tags):
        for i in range(len(tb_tags)):
            item = QTableWidgetItem(tb_tags[i])
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tb_tags_tableWidget.setItem(0, i, item)

    def set_event_listeners(self):
        self.tb_box.currentIndexChanged.connect(self.select_tb_name)
        self.add_tb_btn.clicked.connect(self.get_file)
        self.tb_tags_tableWidget.itemClicked.connect(self.input_tb_table)

    def input_tb_table(self, item):
        text = self.format_lineEdit.text()
        self.format_lineEdit.setText(text+'%'+item.text()+'%')

    def select_tb_name(self):
        tb_name = self.tb_box.currentText()
        if tb_name != '空':
            table = self.name2table[tb_name]
            self.update_label_group(table.get_tb_tags())

    def get_file(self):
        excel_path, file_type = QFileDialog.getOpenFileName(self, '载入表格', 'C:\\', 'Excel Files (*.xlsx)')
        tb = Table(excel_path)
        fname = tb.get_name()
        if fname not in self.name2table.keys():
            self.name2table[fname] = tb
            self.tb_box.addItem(fname)
        else:
            print('表已存在')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 建立application对象
    window = MainInteractive()  # 建立窗体对象
    window.show()  # 显示窗体
    sys.exit(app.exec())  # 运行程序
