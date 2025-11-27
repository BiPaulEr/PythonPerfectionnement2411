import logging


class AdresseMailFilter(logging.Filter):
    def filter(self, record):
        msg = record.getMessage()
        return not "@" in msg

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.addFilter(AdresseMailFilter())
logger.addHandler(console_handler)

def print_msg():
    logger.debug("Message From DEBUG adresseemail@mail.com")
    logger.log(logging.DEBUG, "DEBUG")
    logger.info("Message From  INFO")
    logger.warning("Message From  WARNING")
    logger.error("Message From  ERROR")
    logger.critical("Message From  CRITICAL")
    
print_msg()