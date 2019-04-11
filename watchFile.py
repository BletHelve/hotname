import time
from watchdog.observers import Observer
from watchdog.events import *
import yaml_rw
import threading
import warnings

import operate
from operate import OperationFile
from table import Table

warnings.filterwarnings("ignore")

lock = threading.Lock()

operate_list = []  # 放入元组（文件路径，操作名)
fail_list = []
tb_name_list = []
excel_list = []
format_list = []
rename_dict = {}  # 格式名：[格式(index), Table(index)]


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
    folder = os.path.split(prev_dir)[1]  # 文件名==格式名
    file = OperationFile(prev_dir, file_name,
                         format_list[rename_dict[folder][0]],
                         table=Table('excel\\'+excel_list[rename_dict[folder][1]]))
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


def data_update():
    config = yaml_rw.read()
    global excel_list, format_list, rename_dict
    excel_list = config['excel']
    format_list = config['format']
    rename_dict = config['rename']


if __name__ == "__main__":
    watch_path = 'watch'
    data_update()
    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, watch_path, True)
    observer.start()
    while True:
        time.sleep(1)
        list_action()
    pass

