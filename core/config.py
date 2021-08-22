from core.cycle import end
from utils.logger import logError
import json


path = "./config.json"
configJSON = json.loads(open(path, mode="r").read())


def loadConfig():
    return configJSON


def getConfig(name, childName=None):
    try:
        if childName is None:
            return configJSON[str(name)]
        else:
            return configJSON[str(name)][str(childName)]
    except KeyError:
        logError("Please do not modify or delete \"config.json\"")
        end(1,"KeyError")


class config:
    pass
