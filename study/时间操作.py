import time
import os

def get_time():
    print(time.time())
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    print(current_time)
def get_path():
    path2 = os.path.dirname(os.path.abspath('.')) +'\py.ini'
    print(path2)

get_path()

