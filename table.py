import xlrd
import os
#  各种字符出错加权值
SYMBOL = 1
CHINESE = 2
LOWER = 3
UPPER = 4
NUM = 5


class Table:
    # tb_name = ''
    # tb = []
    # tb_tags = []
    # keys = []  # 主键
    # key_indexes = []

    def __init__(self, excel_path, keys=None):  # 用excel进行构造
        self.tb_tags = []
        self.tb = []
        self.keys = []
        self.key_indexes = []
        file_name = os.path.split(excel_path)[1]  # 带后缀名的文件名
        self.tb_name = os.path.splitext(file_name)[0]  # 无后缀名的文件名
        sheet = xlrd.open_workbook(excel_path).sheet_by_index(0)
        row_cnt = sheet.nrows
        for name_cell in sheet.row(0):  # 表格第一行写列名（一定）
            self.tb_tags.append(name_cell.value)
        for row in range(1, row_cnt):
            stu_row = []
            for col in range(len(self.tb_tags)):
                cell_type = sheet.cell(row, col).ctype
                val = sheet.cell_value(row, col)
                if cell_type == 2:  # type is number
                    val = str(int(val))
                stu_row.append(val)
            self.tb.append(stu_row)
        if not keys:
            self.set_keys(self.tb_tags)

    def get_name(self):
        return self.tb_name

    def get_tb(self):
        return self.tb

    def get_tb_tags(self):
        return self.tb_tags

    def get_keys(self):
        return self.keys

    def set_keys(self, keys):
        for key in keys:
            self.key_indexes.append(self.tb_tags.index(key))
        self.key_indexes.sort(key=lambda k: fault_weightings(self.tb[0][k]))
        for i in self.key_indexes:
            self.keys.append(self.tb_tags[i])

    def get_key_indexes(self):
        return self.key_indexes


def fault_weightings(string):  # 获取输出错误的
    weighting = 0
    for c in string:
        weighting += what_char(c)
    return weighting


def what_char(char):
    if u'\u4e00' <= char <= u'\u9fff':
        return CHINESE
    elif char.isdigit():
        return NUM
    elif char.islower():
        return LOWER
    elif char.isupper():
        return UPPER
    else:
        return SYMBOL
