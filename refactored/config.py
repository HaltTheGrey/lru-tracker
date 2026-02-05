"""Application configuration and constants."""

# Version
APP_VERSION = "1.1.0"
UPDATE_CHECK_URL = "https://raw.githubusercontent.com/HaltTheGrey/lru-tracker/main/version.json"

# File paths
DATA_FILE = "lru_data.json"
BACKUP_SUFFIX = ".backup"
TEMP_SUFFIX = ".tmp"

# Validation limits
MAX_STATION_NAME_LENGTH = 200
MIN_LRU_VALUE = 0
MAX_LRU_VALUE = 999999

# UI Colors
class Colors:
    PRIMARY = '#2c3e50'
    SUCCESS = '#27ae60'
    INFO = '#3498db'
    WARNING = '#e67e22'
    DANGER = '#e74c3c'
    SECONDARY = '#95a5a6'
    
    # Status colors
    UNDER_MIN_BG = '#ffcccc'
    AT_MAX_BG = '#fff4cc'
    NORMAL_BG = '#ccffcc'
    
    # Excel colors
    HEADER_BG = '2C3E50'
    HEADER_SECONDARY = '34495E'
    EXAMPLE_BG = 'ECF0F1'

# UI Dimensions
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 800
RIGHT_PANEL_WIDTH = 380

# Time slots for FC schedule
TIME_SLOTS_1ST = ['6AM', '8AM', '10AM', '12PM', '2PM', '4PM']
TIME_SLOTS_2ND = ['6PM', '8PM', '10PM', '12AM']
ALL_TIME_SLOTS = TIME_SLOTS_1ST + TIME_SLOTS_2ND

# Time slot mappings (hour ranges)
TIME_SLOT_MAP = {
    '6AM': (6, 8),
    '8AM': (8, 10),
    '10AM': (10, 12),
    '12PM': (12, 14),
    '2PM': (14, 18),
    '4PM': (16, 18),
    '6PM': (18, 20),
    '8PM': (20, 22),
    '10PM': (22, 24),
    '12AM': (0, 2)
}

# Date/time formats
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
FILE_TIMESTAMP_FORMAT = "%Y%m%d_%H%M%S"
