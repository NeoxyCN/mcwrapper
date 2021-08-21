import json
from utils.logger import log

configJSON = json.loads(open("./config.json", mode="r").read())


def loadConfig():
    return configJSON


def getConfig(name, childname):
    if childname in dir():
        return configJSON[str(name)]
    else:
        return configJSON[str(name)][str(childname)]
