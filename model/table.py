import xlrd
import os
#  各种字符出错加权值
SYMBOL = 1
CHINESE = 2
LOWER = 3
UPPER = 4
NUM = 5


class Table:
    __fname = ''
    __tb = []
    __tb_tags = []
    __keys = []  # 主键
    __key_indexes = []

    def __init__(self, excel_path):  # 用excel进行构造
        file_name = os.path.split(excel_path)[1]
        self.__fname = os.path.splitext(file_name)[0]
        sheet = xlrd.open_workbook(excel_path).sheet_by_index(0)
        row_cnt = sheet.nrows
        for name_cell in sheet.row(0):  # 表格第一行写列名（一定）
            self.__tb_tags.append(name_cell.value)
        for row in range(1, row_cnt):
            stu_row = []
            for col in range(len(self.__tb_tags)):
                cell_type = sheet.cell(row, col).ctype
                val = sheet.cell_value(row, col)
                if cell_type == 2:  # type is number
                    val = str(int(val))
                stu_row.append(val)
            self.__tb.append(stu_row)

    def get_name(self):
        return self.__fname

    def get_tb(self):
        return self.__tb

    def get_tb_tags(self):
        return self.__tb_tags

    def get_keys(self):
        return self.__keys

    def set_keys(self, keys):
        for key in keys:
            self.__key_indexes.append(self.__tb_tags.index(key))
        self.__key_indexes.sort(key=lambda k: fault_weightings(self.__tb[0][k]))
        for i in self.__key_indexes:
            self.__keys.append(self.__tb_tags[i])

    def get_key_indexes(self):
        return self.__key_indexes


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
