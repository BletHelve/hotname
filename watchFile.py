
import time
from watchdog.observers import Observer
from watchdog.events import *
import yaml
from rename import OperationFile
import threading
import warnings
warnings.filterwarnings("ignore")

lock = threading.Lock()


class FileEventHandler(FileSystemEventHandler):

    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        print(event.key)
        if event.is_directory:
            print(event.src_path)
        else:
            self.action(event.src_path, 'rename')

    def on_deleted(self, event):
        if event.is_directory:
            print(event.src_path)
        else:
            self.action(event.src_path, 'remove')

    @staticmethod
    def action(src_path, operation):  # operation{remove, rename}
        prev_dir = os.path.split(src_path)[0]
        file_name = os.path.split(src_path)[1]
        string = prev_dir[len(watch_path) + 1:]
        string_list = string.split('\\')
        if file_name[0] != '~':  # 忽略临时文件
            file = OperationFile(prev_dir, file_name, string_list)
            file.start()
            try:
                file.operation(operation)
            except PermissionError:
                time.sleep(0.0001)
            except KeyError:
                print('不是指定文件')


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


if __name__ == "__main__":
    watch_path = init_path()
    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, watch_path, True)
    observer.start()
    while True:
        time.sleep(1)



