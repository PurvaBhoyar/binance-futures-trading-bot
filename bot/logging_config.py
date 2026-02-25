import logging
import os
from logging.handlers import RotatingFileHandler

# Get absolute path to the root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(BASE_DIR, "trading.log")

def setup_logging():
    # Force reset any existing loggers (like Streamlit's internal one)
    root = logging.getLogger()
    if root.handlers:
        for handler in root.handlers:
            root.removeHandler(handler)

    # Professional formatting
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    # Create handler that writes to file
    file_handler = RotatingFileHandler(LOG_FILE, mode='a', maxBytes=1024*1024, backupCount=5)
    file_handler.setFormatter(formatter)
    
    # Create the logger
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    
    # This prevents the log from being "swallowed" by other libraries
    logger.propagate = False
    
    return logger

logger = setup_logging()