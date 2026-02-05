"""Input validation utilities."""
import re
import os
from typing import Tuple
from config import MAX_STATION_NAME_LENGTH, MIN_LRU_VALUE, MAX_LRU_VALUE


def validate_station_name(name: str) -> bool:
    """Validate station name for security and consistency."""
    if not name or not isinstance(name, str):
        return False
    if not name.strip():
        return False
    if len(name) > MAX_STATION_NAME_LENGTH:
        return False
    # Allow alphanumeric, spaces, hyphens, underscores, and common punctuation
    if not re.match(r'^[\w\s\-.,()#]+$', name):
        return False
    return True


def validate_number(value: str, min_val: int = MIN_LRU_VALUE, 
                   max_val: int = MAX_LRU_VALUE) -> Tuple[bool, int]:
    """Validate numeric input and return (is_valid, number)."""
    try:
        num = int(str(value).strip())
        if min_val <= num <= max_val:
            return True, num
        return False, 0
    except (ValueError, TypeError):
        return False, 0


def sanitize_filename(filename: str) -> str:
    """Sanitize filename to prevent path traversal attacks."""
    if not filename:
        return "export.xlsx"
    # Get just the basename (removes any path components)
    filename = os.path.basename(filename)
    # Remove potentially dangerous characters
    filename = re.sub(r'[^\w\s\-.]', '_', filename)
    # Ensure it has an extension
    if not filename.endswith('.xlsx') and not filename.endswith('.csv'):
        filename += '.xlsx'
    return filename


def validate_version_format(version: str) -> bool:
    """Validate version string format (e.g., 1.0.0)."""
    return bool(re.match(r'^\d+\.\d+\.\d+$', version))


def is_newer_version(latest: str, current: str) -> bool:
    """Compare version strings securely."""
    try:
        if not (validate_version_format(latest) and validate_version_format(current)):
            return False
        latest_parts = [int(x) for x in latest.split('.')]
        current_parts = [int(x) for x in current.split('.')]
        return latest_parts > current_parts
    except (ValueError, AttributeError):
        return False
