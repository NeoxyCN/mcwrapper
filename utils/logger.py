import time


def log(text, type=0):
    nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if type == 0:
        print("[{}][{}]{}".format(nowTime,"INFO", text))
