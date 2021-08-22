from core import config
from utils.logger import logError, logInfo

def end(status=0, reason=None):
    # TODO:More details
    if status == 0:
        pass
    elif status == 1:
        logError("Encountered error(s):{}".format(reason))
    logInfo("mcwrapper is stopping, and Minecraft server will also be stopped.")
    exit(status)
