"""Logging configuration for LRU Tracker."""
import logging
import sys
import os
from pathlib import Path
from datetime import datetime
from typing import Optional
from config import APP_VERSION


def get_log_directory() -> Optional[Path]:
    """Get writable log directory, falling back to user's temp/appdata if needed."""
    # Try multiple locations in order of preference
    possible_dirs = [
        Path('logs'),  # Current directory (preferred)
        Path.home() / 'AppData' / 'Local' / 'LRU_Tracker' / 'logs',  # Windows user appdata
        Path.home() / '.lru_tracker' / 'logs',  # Unix-style hidden folder
        Path(os.environ.get('TEMP', '.')) / 'lru_tracker_logs',  # System temp folder
    ]
    
    for log_dir in possible_dirs:
        try:
            log_dir.mkdir(parents=True, exist_ok=True)
            # Test write permission
            test_file = log_dir / '.write_test'
            test_file.touch()
            test_file.unlink()
            return log_dir
        except (PermissionError, OSError):
            continue
    
    # If all fails, return None (will use console-only logging)
    return None


def setup_logger(name: str = 'lru_tracker') -> logging.Logger:
    """Setup application logger with file and console handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Prevent duplicate handlers
    if logger.handlers:
        return logger
    
    # Try to get a writable log directory
    log_dir = get_log_directory()
    
    # File handler with rotation (if we have write access)
    file_handler: Optional[logging.FileHandler] = None
    if log_dir:
        try:
            log_file = log_dir / f'lru_tracker_{datetime.now().strftime("%Y%m%d")}.log'
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setLevel(logging.INFO)
        except (PermissionError, OSError) as e:
            # Can't create file handler, will use console only
            print(f"Warning: Cannot create log file at {log_dir}: {e}")
            file_handler = None
    
    # Console handler for errors
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.WARNING)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Add formatter and handlers
    if file_handler:
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # Log startup message
    if log_dir:
        logger.info(f"LRU Tracker v{APP_VERSION} started - Logs at: {log_dir}")
    else:
        logger.warning(f"LRU Tracker v{APP_VERSION} started - Console logging only (no write access)")
    
    return logger


def get_logger(name: str = 'lru_tracker') -> logging.Logger:
    """Get existing logger instance."""
    return logging.getLogger(name)
