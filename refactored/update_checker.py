"""Update checking functionality with incremental update support."""
import json
import urllib.request
import urllib.error
from typing import Optional, Dict, Any, Tuple
from validators import validate_version_format, is_newer_version
from config import APP_VERSION, UPDATE_CHECK_URL


class UpdateChecker:
    """Handles application update checking with incremental update support."""
    
    def __init__(self, current_version: str = APP_VERSION, 
                 update_url: str = UPDATE_CHECK_URL):
        self.current_version = current_version
        self.update_url = update_url
        # Check for incremental update manifest
        self.manifest_url = UPDATE_CHECK_URL.replace('version.json', 'update_manifest.json')
        self.supports_incremental = False
    
    def check_for_updates(self) -> Optional[Dict[str, Any]]:
        """
        Check for updates and return update info if available.
        
        First tries incremental update manifest, falls back to version.json.
        Returns None if no update available or on error.
        """
        # Try incremental update first
        incremental_info = self._check_incremental_updates()
        if incremental_info:
            return incremental_info
        
        # Fall back to traditional update
        return self._check_traditional_updates()
    
    def _check_incremental_updates(self) -> Optional[Dict[str, Any]]:
        """
        Check for incremental updates using update_manifest.json.
        Returns update info with file-level details if available.
        """
        # Security check: Validate URL is HTTPS
        if not self.manifest_url.startswith('https://'):
            return None
        
        try:
            # Download manifest with timeout
            with urllib.request.urlopen(self.manifest_url, timeout=5) as response:
                content = response.read().decode('utf-8')
                manifest = json.loads(content)
            
            # Validate data structure
            if not isinstance(manifest, dict):
                return None
            
            latest_version = manifest.get('version', '0.0.0')
            
            # Validate version format
            if not validate_version_format(latest_version):
                return None
            
            # Compare versions
            if is_newer_version(latest_version, self.current_version):
                self.supports_incremental = True
                
                # Calculate changed files and sizes
                files = manifest.get('files', {})
                total_size = sum(f.get('size', 0) for f in files.values())
                
                return {
                    'version': latest_version,
                    'release_date': manifest.get('release_date'),
                    'release_notes': manifest.get('release_notes'),
                    'download_url': manifest.get('changelog_url', ''),
                    'update_type': 'incremental',
                    'files': files,
                    'file_count': len(files),
                    'total_size': total_size,
                    'manifest': manifest,
                    'savings_info': manifest.get('incremental_update_info', {})
                }
            
            return None
            
        except Exception as e:
            # If incremental manifest fails, we'll fall back to traditional
            print(f"Incremental update check failed: {e}")
            return None
    
    def _check_traditional_updates(self) -> Optional[Dict[str, Any]]:
        """
        Check for traditional updates using version.json.
        Returns update info for full installer download.
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
                # Add update type marker
                update_info['update_type'] = 'traditional'
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
