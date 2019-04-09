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
folder2format_table = {}


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


def action(src_path, operation):  # operation{remove, rename}
    prev_dir = os.path.split(src_path)[0]
    file_name = os.path.split(src_path)[1]
    # string = prev_dir[len(watch_path) + 1:]
    # string_list = string.split('\\') 根目录到文件，每级目录名
    folder = os.path.split(prev_dir)[1]
    file = OperationFile(prev_dir, file_name, folder2format_table[folder][0], table=folder2format_table[folder][1])

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
    watch_path = 'F:\\test'
    table = Table('F:\\table.xlsx')
    table.set_keys(['姓名', '学号'])
    folder2format_table['java'] = ('w1专转本%学号%%姓名%java', table)
    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, watch_path, True)
    observer.start()
    while True:
        time.sleep(1)
        list_action()
    pass

