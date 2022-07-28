import os.path
from datetime import datetime

YA_LOGIN = "testAcc7654"
YA_PASS = "testPas"
NAME_FILE = "Файл для копирования"

dirname = os.path.dirname(__file__)
FILE_PATH = os.path.join(dirname, "lorem.txt")


def generate_folder_name():
    now = datetime.now()
    global NAME_FOLDER
    NAME_FOLDER = datetime(now.year, now.month, now.day, now.hour, now.minute,now.second)
    return NAME_FOLDER.strftime("%Y.%d.%mT%H-%M-%S")


def prepare_file_to_compare():
    try:
        handle = open(FILE_PATH)
        read_data = handle.read()
        handle.close()
    except IOError:
        print("An IOError has occurred!")
    res_list = read_data.split('\n')
    return list(filter(None, res_list))

print(generate_folder_name())