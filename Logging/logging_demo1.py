import logging

logger = logging.getLogger()
logger.disabled = False

logger.setLevel(logging.ERROR)

console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

def print_msg():
    logger.debug("Message From DEBUG")
    logger.log(logging.DEBUG, "DEBUG")
    logger.info("Message From  INFO")
    logger.warning("Message From  WARNING")
    logger.error("Message From  ERROR")
    logger.critical("Message From  CRITICAL")
    
print_msg()