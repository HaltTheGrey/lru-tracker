"""Update checking functionality."""
import json
import urllib.request
import urllib.error
from typing import Optional, Dict, Any
from validators import validate_version_format, is_newer_version
from config import APP_VERSION, UPDATE_CHECK_URL


class UpdateChecker:
    """Handles application update checking."""
    
    def __init__(self, current_version: str = APP_VERSION, 
                 update_url: str = UPDATE_CHECK_URL):
        self.current_version = current_version
        self.update_url = update_url
    
    def check_for_updates(self) -> Optional[Dict[str, Any]]:
        """
        Check for updates and return update info if available.
        Returns None if no update available or on error.
        """
        # Security check: Validate URL is HTTPS
        if not self.update_url.startswith('https://'):
            raise SecurityError("Update URL must use HTTPS")
        
        try:
            # Download version info with timeout
            with urllib.request.urlopen(self.update_url, timeout=5) as response:
                content = response.read().decode('utf-8')
                update_info = json.loads(content)
            
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
            
        except (urllib.error.URLError, urllib.error.HTTPError) as e:
            raise NetworkError(f"Could not connect to update server: {str(e)}")
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
