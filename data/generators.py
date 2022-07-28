from datetime import datetime


def generate_folder_name():
    now = datetime.now()
    global NAME_FOLDER
    NAME_FOLDER = datetime(now.year, now.month, now.day, now.hour, now.minute,now.second)
    return NAME_FOLDER.strftime("%Y.%d.%mT%H-%M-%S")
