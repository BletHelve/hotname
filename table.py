import xlrd

#  各种字符出错加权值
SYMBOL = 1
CHINESE = 2
LOWER = 3
UPPER = 4
NUM = 5


class Table:
    __tb = []
    __tb_tags = []
    __keys = []  # 主键

    def __init__(self, excel_path):  # 用excel进行构造
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

    def get_tb(self):
        return self.__tb

    def get_tb_tags(self):
        return self.__tb_tags

    def get_keys(self):
        return self.__keys

    def set_keys(self, keys):
        keys.sort(cmp=fault_cmp)
        self.__keys = keys


def fault_cmp(key1, key2):  # 比较人类输入出错的可能性
    fault1, fault2 = 0, 0
    for c1 in key1:
        fault1 += what_char(c1)
    for c2 in key2:
        fault2 += what_char(c2)
    return fault1 - fault2


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
