import logging, time, os
from logging.handlers import TimedRotatingFileHandler
logger = logging.getLogger()

logger.setLevel(logging.DEBUG)
path_log_file = os.path.join(os.path.dirname(__file__), "time.log")
rot_handler = TimedRotatingFileHandler(path_log_file, backupCount=3, when="M", interval=1)
rot_handler.setFormatter(logging.Formatter("%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s", datefmt="%d/%Y %I/%M %p"))
logger.addHandler(rot_handler)

def print_msg():
    time.sleep(0.2)
    logger.debug("Message From DEBUG")
    logger.log(logging.DEBUG, "DEBUG")
    logger.info("Message From  INFO")
    logger.warning("Message From  WARNING")
    logger.error("Message From  ERROR")
    logger.critical("Message From  CRITICAL")
for i in range(0, 100000):
    print_msg()