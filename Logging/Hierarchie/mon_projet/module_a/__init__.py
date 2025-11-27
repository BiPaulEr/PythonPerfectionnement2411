import logging, os
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

handler = logging.FileHandler(os.path.join(os.path.dirname(__file__),"messages.log"))
logger.addHandler(handler)
