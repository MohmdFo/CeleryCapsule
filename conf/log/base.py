import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    # Log file settings
    LOG_FILENAME = "application.log"
    MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
    BACKUP_COUNT = 3  # Keep 3 backup copies

    # Create a logger
    logger = logging.getLogger('application')
    logger.setLevel(logging.DEBUG)  # Set to whatever level of logging you want

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create a rotating file handler
    handler = RotatingFileHandler(LOG_FILENAME, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)

    # Set the formatter for this handler
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
