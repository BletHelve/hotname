# This Python file uses the following encoding: utf-8

from threading import Thread
from win32com import client as wc
import docx
import pythoncom
import os
import sys

from model.table import Table

LACK = -1
FAIL = 0
SUCCESS = 1
REPEAT = 2

# 打包之后当前路径
if getattr(sys, 'frozen', None):
    basedir = sys._MEIPASS
else:
    basedir = os.path.dirname(__file__)
#


class OperationFile(Thread):
    table = None  # (Table类型)
    __file_list = []
    __prev_dir, __filename = '', ''
    __state = 0
    rename_format = ''

    def __init__(self, prev_dir, filename, rename_format, table=None):
        Thread.__init__(self)
        self.__filename = filename
        self.__prev_dir = prev_dir
        self.rename_format = rename_format
        if table:
            self.table = table

    def get_file_list(self):
        return self.__file_list

    def operation(self, operation):
        return {'remove': self.remove,
                'rename': self.rename,
                'alt': self.alt
                }[operation]()

    def remove(self):
        filename = os.path.splitext(self.__filename)[0]  # 去后缀名
        if filename in self.__file_list:
            self.__file_list.remove(filename)
            return SUCCESS
        else:
            return FAIL

    def rename(self):
        print(self.__prev_dir + '\\' + self.__filename, end=' ==> ')
        print(self.name_match())
        if self.__state == SUCCESS:
            print('文件重命名成功')
        else:
            print('文件重命名失败:')
            if self.__state == LACK:
                print('文件提供的信息，不足以进行重命名')
            elif self.__state == REPEAT:
                print('将要修改的名称与此文件夹中其他文件名重复')
        return self.__state

    def alt(self):  # 直接根据文件内容进行重命名
        i = self.match_file(self.__prev_dir + '\\' + self.__filename)
        if i != -1:
            print(self.__os_rename(self.__filename, self.table.get_tb()[i]))
            return SUCCESS
        else:
            print('没有改变关键信息，不需要重命名')
            return FAIL

    def name_match(self):
        i = self.match_str(self.__filename)  # 文件名与个人信息表匹配
        if i == -1:  # 没有在文件名中找到姓名和学号，进入word里直接查询
            i = self.match_file(self.__prev_dir + '\\' + self.__filename)
        if i != -1:
            return self.__os_rename(self.__filename, self.table.get_tb()[i])
        else:
            self.__state = LACK

    def __os_rename(self, filename, line):  # line：一行所有信息
        new_name = self.rename_format  # 新名称
        tb_tags = self.table.get_tb_tags()
        for i in range(len(tb_tags)):
            new_name = new_name.replace('%' + tb_tags[i] + '%', line[i])
        if new_name not in self.__file_list:  # 文件名没有重复
            self.__file_list.append(new_name)
            extension = os.path.splitext(filename)[1]  # 文件后缀名
            os.renames(self.__prev_dir + '\\' + filename,
                       self.__prev_dir + '\\' + new_name + extension)
            self.__state = SUCCESS
        else:
            self.__state = REPEAT
        return new_name

    def match_file(self, file_path):  # 找到文件中的姓名，学号
        extension = os.path.splitext(file_path)[1]  # 获取后缀名
        return {'.doc': self.__match_doc,  # 返回表格的行数
                '.docx': self.__match_docx,
                }[extension](file_path)

    def __match_doc(self, doc_path):
        # todo 这个是io操作，在这里实现切换
        pythoncom.CoInitialize()
        word = wc.Dispatch('Word.Application')
        doc = word.Documents.Open(doc_path)  # 目标路径下的文件
        reg_dir = basedir+'\\reg\\' + os.path.basename(doc_path) + 'x'
        doc.SaveAs(reg_dir, 16)  # 转化成docx，放在reg文件下
        i = self.__match_docx(reg_dir)
        doc.Close()
        word.Quit()
        os.remove(reg_dir)
        return i

    def __match_docx(self, dox_path):
        document = docx.Document(dox_path)
        for paragraph in document.paragraphs:
            line = str(paragraph.text).strip(' ')  # 去掉空格
            i = self.match_str(line)
            if i != -1:
                return i

    def match_str(self, string):  # 名称匹配
        for i in range(len(self.table.get_tb())):
            for j in self.table.get_key_indexes():
                if self.table.get_tb()[i][j] in string:
                    return i
        return -1
