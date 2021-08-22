import time


def nowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def logUnknown(text):
    log(text, -1)


def logInfo(text):
    log(text, 0)


def logWarning(text):
    log(text, 1)


def logError(text):
    log(text, 2)


def log(text, type=0):
    if type == -1:
        print("[{}][{}]{}".format(nowTime(), "Unknown", text))
    elif type == 0:
        print("[{}][{}]{}".format(nowTime(), "Info", text))
    elif type == 1:
        print("[{}][{}]{}".format(nowTime(), "Warning", text))
    elif type == 2:
        print("[{}][{}]{}".format(nowTime(), "Error", text))
