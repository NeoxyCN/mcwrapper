from core import config
from utils.logger import log
def run():
    log(config.getConfig("servername"))