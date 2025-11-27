import logging

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

def print_msg():
    logger.debug("DEBUG")
    logger.log(logging.DEBUG, "DEBUG")
    logger.info("INFO")
    logger.warning("WARNING")
    logger.critical("CRITICAL")
    logger.error("ERROR")
    
print_msg()