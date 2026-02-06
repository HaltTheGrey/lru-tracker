"""
TEMPORARY FILE FOR LOCAL TESTING ONLY
Replace update_checker.py with this file to test locally, then restore original.
"""
import json
from typing import Optional, Dict, Any
from validators import validate_version_format, is_newer_version
from config import APP_VERSION

class UpdateChecker:
    """Handles application update checking - TEST MODE."""
    
    def __init__(self, current_version: str = APP_VERSION, update_url: str = None):
        self.current_version = current_version
        # For local testing, use the v1.2.0 version file
        self.update_url = update_url
    
    def check_for_updates(self) -> Optional[Dict[str, Any]]:
        """
        Check for updates - LOCAL TEST MODE.
        Reads from version_v1.2.0.json file.
        """
        try:
            # Read local version file for testing
            import os
            test_file = os.path.join(os.path.dirname(__file__), '..', 'version_v1.2.0.json')
            
            with open(test_file, 'r') as f:
                update_info = json.load(f)
            
            # Validate data structure
            if not isinstance(update_info, dict):
                raise ValueError("Invalid update data format")
            
            required_fields = ['version', 'download_url']
            missing_fields = [f for f in required_fields if f not in update_info]
            if missing_fields:
                raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
            
            latest_version = update_info.get('version', '0.0.0')
            
            # Validate version format
            if not validate_version_format(latest_version):
                raise ValueError("Invalid version format")
            
            # Compare versions
            if is_newer_version(latest_version, self.current_version):
                return update_info
            
            return None
            
        except FileNotFoundError:
            raise NetworkError("Test version file not found")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid update data received: {str(e)}")


class UpdateError(Exception):
    """Base exception for update-related errors."""
    pass


class NetworkError(UpdateError):
    """Raised when network connection fails."""
    pass


class SecurityError(UpdateError):
    """Raised when security validation fails."""
    pass
