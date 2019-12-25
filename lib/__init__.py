import logging

logger = logging.getLogger('l_system')
stdout_handler = logging.StreamHandler()
stdout_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stdout_handler.setFormatter(stdout_format)
logger.addHandler(stdout_handler)
