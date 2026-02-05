"""Error handling utilities for UI operations."""
from functools import wraps
from tkinter import messagebox
from logger import get_logger

logger = get_logger()


def safe_execute(func):
    """Decorator for safe UI operations with error handling."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred in {func.__name__}:\n{str(e)}")
            return None
    return wrapper


def safe_execute_silent(func):
    """Decorator for operations that should fail silently."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.warning(f"Silent error in {func.__name__}: {e}")
            return None
    return wrapper
