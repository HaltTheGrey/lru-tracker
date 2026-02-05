"""
Auto-Update System for LRU Tracker
Checks for updates and downloads them automatically
"""

import os
import json
import urllib.request
import urllib.error
import shutil
import tempfile
import subprocess
from pathlib import Path
from datetime import datetime

class AutoUpdater:
    def __init__(self, current_version="1.0.0", update_url=None):
        """
        Initialize the auto-updater
        
        Args:
            current_version: Current version of the application
            update_url: URL to check for updates (GitHub releases, etc.)
        """
        self.current_version = current_version
        self.update_url = update_url or "https://example.com/lru-tracker/version.json"
        self.app_dir = Path(__file__).parent
        
    def check_for_updates(self):
        """Check if a new version is available"""
        try:
            # Download version info
            with urllib.request.urlopen(self.update_url, timeout=5) as response:
                update_info = json.loads(response.read().decode())
            
            latest_version = update_info.get('version', '0.0.0')
            
            # Compare versions
            if self._is_newer_version(latest_version, self.current_version):
                return {
                    'available': True,
                    'version': latest_version,
                    'download_url': update_info.get('download_url'),
                    'release_notes': update_info.get('release_notes', ''),
                    'size': update_info.get('size_mb', 'Unknown')
                }
            
            return {'available': False}
            
        except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError):
            # Update check failed (no internet, server down, etc.)
            return {'available': False, 'error': 'Could not check for updates'}
    
    def _is_newer_version(self, latest, current):
        """Compare version strings (e.g., '1.2.3' vs '1.2.2')"""
        latest_parts = [int(x) for x in latest.split('.')]
        current_parts = [int(x) for x in current.split('.')]
        
        return latest_parts > current_parts
    
    def download_update(self, download_url, progress_callback=None):
        """
        Download the update file
        
        Args:
            download_url: URL to download the update
            progress_callback: Function to call with download progress (0-100)
        
        Returns:
            Path to downloaded file
        """
        try:
            # Create temp directory
            temp_dir = tempfile.mkdtemp()
            update_file = os.path.join(temp_dir, "LRU_Tracker_Update.exe")
            
            # Download with progress
            def report_progress(block_num, block_size, total_size):
                if progress_callback and total_size > 0:
                    progress = min(100, (block_num * block_size * 100) // total_size)
                    progress_callback(progress)
            
            urllib.request.urlretrieve(download_url, update_file, report_progress)
            
            return update_file
            
        except Exception as e:
            return None
    
    def install_update(self, update_file):
        """
        Install the downloaded update
        
        Args:
            update_file: Path to the update installer
        """
        try:
            # Run the installer
            subprocess.Popen([update_file, '/SILENT'])
            
            # Exit current app so installer can replace files
            return True
            
        except Exception as e:
            return False
    
    def create_version_file(self, version, download_url, release_notes="", size_mb=0):
        """
        Create a version.json file for hosting updates
        Use this to create the file you'll upload to your server
        """
        version_info = {
            'version': version,
            'download_url': download_url,
            'release_notes': release_notes,
            'size_mb': size_mb,
            'release_date': datetime.now().isoformat()
        }
        
        with open('version.json', 'w') as f:
            json.dump(version_info, f, indent=2)
        
        print(f"Created version.json for version {version}")
        return version_info


# Example version.json format:
"""
{
  "version": "1.1.0",
  "download_url": "https://example.com/LRU_Tracker_Setup_v1.1.0.exe",
  "release_notes": "- Added new features\n- Fixed bugs\n- Improved performance",
  "size_mb": 45,
  "release_date": "2026-02-05T12:00:00"
}
"""

if __name__ == "__main__":
    # Example usage
    updater = AutoUpdater(current_version="1.0.0")
    
    # Create a version file for hosting
    updater.create_version_file(
        version="1.0.0",
        download_url="https://yourserver.com/downloads/LRU_Tracker_Setup.exe",
        release_notes="Initial release",
        size_mb=45
    )
