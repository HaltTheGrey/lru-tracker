"""Logging configuration for LRU Tracker."""
import logging
import sys
from pathlib import Path
from datetime import datetime
from config import APP_VERSION


def setup_logger(name: str = 'lru_tracker') -> logging.Logger:
    """Setup application logger with file and console handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Prevent duplicate handlers
    if logger.handlers:
        return logger
    
    # Create logs directory if it doesn't exist
    log_dir = Path('logs')
    log_dir.mkdir(exist_ok=True)
    
    # File handler with rotation
    log_file = log_dir / f'lru_tracker_{datetime.now().strftime("%Y%m%d")}.log'
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    
    # Console handler for errors
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.WARNING)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    logger.info(f"LRU Tracker v{APP_VERSION} started")
    
    return logger


def get_logger(name: str = 'lru_tracker') -> logging.Logger:
    """Get existing logger instance."""
    return logging.getLogger(name)
