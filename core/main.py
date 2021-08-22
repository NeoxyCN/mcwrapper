from core import config
from utils.logger import logInfo


def run(args):
    if len(args) == 2 and args[1] == "init":
        # TODO: Init
        init(args)
    logInfo(config.getConfig("\033servername\033"))

def init(args):
    pass