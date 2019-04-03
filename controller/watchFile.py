import sys
import time
from watchdog.observers import Observer
from watchdog.events import *
import yaml
import threading
import warnings
from PyQt5 import QtWidgets, uic,QtCore,QtGui


from model import operate
from model.operate import OperationFile
from model.table import Table
from view.main_interactive import *
from view.main_window import *

warnings.filterwarnings("ignore")

lock = threading.Lock()

operate_list = []  # 放入元组（文件路径，操作名)
fail_list = []
folder2table = {}
folder2tb_tag_index = {}




class FileEventHandler(FileSystemEventHandler):

    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        print(event.key)
        if event.is_directory:
            print(event.src_path)
        else:
            if not is_tempfile(event.src_path):
                operate_list.append((event.src_path, 'rename'))

    def on_deleted(self, event):
        print(event.key)
        if event.is_directory:
            print(event.src_path)
        else:
            if not is_tempfile(event.src_path):
                operate_list.append((event.src_path, 'remove'))


def add_path():
    while True:
        path = input('请输入文件地址：')
        if os.path.isdir(path):
            break
        else:
            print('输入的地址不存在，请重新输入')
    config = open('config.yaml', 'w', encoding='utf-8')
    content = {'watch_path': path}
    yaml.dump(content, config)
    config.close()
    return path


def init_path():
    config = open('config.yaml', 'r', encoding='utf-8')
    res = yaml.load(config)
    config.close()
    path = res['watch_path']
    if path == 'without':
        return add_path()
    return path


def action(src_path, operation):  # operation{remove, rename}
    prev_dir = os.path.split(src_path)[0]
    file_name = os.path.split(src_path)[1]
    # string = prev_dir[len(watch_path) + 1:]
    # string_list = string.split('\\') 根目录到文件，每级目录名
    folder = os.path.dirname(src_path)
    file = OperationFile(prev_dir, file_name, tags, table=folder2table[folder],
                         tb_tag_index=folder2tb_tag_index[folder])
    file.start()
    try:
        state = file.operation(operation)
    except KeyError:
        print('不是指定文件')
        return operate.FAIL
    return state


def is_tempfile(src_path):
    return os.path.split(src_path)[1][0] == '~'


def list_action():
    if len(operate_list) > 0:
        for i in range(len(operate_list)):
            state = action(operate_list[i][0], operate_list[i][1])
            if state != operate.SUCCESS:
                fail_list.append(operate_list[i])
        operate_list.clear()


if __name__ == "__main__":

    # watch_path = init_path()
    # folder_path = input('请输入更名文件夹')  # 手动在监控文件夹创建

    # folder2table[folder_path] = table
    # keys = input('请输入主键，以空格分格').split(' ')
    # table.set_keys(keys)
    # tags = input('请输入标签，以空格分格').split(' ')

    # tb_tag_index = []
    # for t in range(len(tags)):
    #      if tags[t] in table.get_tb_tags():
    #          tb_tag_index.append(t)
    # folder2tb_tag_index[folder_path] = tb_tag_index

    app = QtWidgets.QApplication(sys.argv)  # 建立application对象
    window = MainInteractive()  # 建立窗体对象


    # self.add_table_btn.clicked.connect()
    # self.add_format_btn.clicked.connect()
    window.show()  # 显示窗体

    sys.exit(app.exec())  # 运行程序

    # event_handler = FileEventHandler()
    # observer = Observer()
    # observer.schedule(event_handler, watch_path, True)
    # observer.start()
    # while True:
    #     time.sleep(1)
    #     list_action()


