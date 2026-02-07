"""
Incremental Update System for LRU Tracker
Instead of downloading the entire 127 MB executable, only download changed files.

This system:
1. Checks GitHub for file manifest (version.json with file hashes)
2. Compares local files against manifest
3. Downloads only files that changed
4. Applies updates incrementally
5. Restarts application

Benefits:
- Saves bandwidth (download only changed files, not entire app)
- Faster updates (seconds instead of minutes)
- More reliable (smaller downloads less likely to fail)
- GitHub API integration (can check commits, releases, etc.)
"""

import hashlib
import json
import urllib.request
import urllib.error
from pathlib import Path
import shutil
import subprocess
import sys
import time
from typing import Dict, List, Optional, Tuple


class IncrementalUpdater:
    """Handles incremental updates by downloading only changed files"""
    
    def __init__(self, current_version: str, github_repo: str = "HaltTheGrey/lru-tracker"):
        self.current_version = current_version
        self.github_repo = github_repo
        self.manifest_url = f"https://raw.githubusercontent.com/{github_repo}/main/update_manifest.json"
        self.base_download_url = f"https://raw.githubusercontent.com/{github_repo}/main/"
        
    def check_for_updates(self) -> Optional[Dict]:
        """
        Check if updates are available
        Returns update info with list of changed files, or None if no updates
        """
        try:
            # Download update manifest from GitHub
            with urllib.request.urlopen(self.manifest_url, timeout=10) as response:
                manifest = json.loads(response.read().decode('utf-8'))
            
            available_version = manifest.get('version')
            
            # Compare versions
            if self._compare_versions(available_version, self.current_version) <= 0:
                return None  # No update available
            
            # Get list of files in the new version
            files_manifest = manifest.get('files', {})
            
            # Compare local files with manifest
            changed_files = self._get_changed_files(files_manifest)
            
            if not changed_files:
                return None  # All files are up to date
            
            # Calculate download size
            total_size = sum(info['size'] for info in changed_files.values())
            
            return {
                'version': available_version,
                'release_date': manifest.get('release_date'),
                'release_notes': manifest.get('release_notes'),
                'changed_files': changed_files,
                'total_download_size': total_size,
                'full_manifest': manifest
            }
            
        except urllib.error.URLError as e:
            print(f"Network error checking for updates: {e}")
            return None
        except Exception as e:
            print(f"Error checking for updates: {e}")
            return None
    
    def _compare_versions(self, v1: str, v2: str) -> int:
        """
        Compare two version strings (e.g., "1.2.2" vs "1.2.1")
        Returns: 1 if v1 > v2, -1 if v1 < v2, 0 if equal
        """
        try:
            parts1 = [int(x) for x in v1.split('.')]
            parts2 = [int(x) for x in v2.split('.')]
            
            for p1, p2 in zip(parts1, parts2):
                if p1 > p2:
                    return 1
                elif p1 < p2:
                    return -1
            
            # If all parts are equal but lengths differ
            if len(parts1) > len(parts2):
                return 1
            elif len(parts1) < len(parts2):
                return -1
            
            return 0
        except:
            return 0
    
    def _get_changed_files(self, files_manifest: Dict) -> Dict:
        """
        Compare local files with manifest to find what changed
        Returns dict of files that need updating
        """
        changed = {}
        app_dir = Path(sys.executable).parent if getattr(sys, 'frozen', False) else Path(__file__).parent.parent
        
        for file_path, file_info in files_manifest.items():
            local_file = app_dir / file_path
            
            # File doesn't exist locally - needs download
            if not local_file.exists():
                changed[file_path] = file_info
                continue
            
            # Compare file hash
            local_hash = self._calculate_file_hash(local_file)
            remote_hash = file_info.get('sha256')
            
            if local_hash != remote_hash:
                changed[file_path] = file_info
        
        return changed
    
    def _calculate_file_hash(self, file_path: Path) -> str:
        """Calculate SHA256 hash of a file"""
        sha256_hash = hashlib.sha256()
        
        try:
            with open(file_path, "rb") as f:
                # Read in chunks to handle large files
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except Exception as e:
            print(f"Error hashing file {file_path}: {e}")
            return ""
    
    def download_updates(self, update_info: Dict, progress_callback=None) -> bool:
        """
        Download and apply incremental updates
        
        For single-file executables, downloads the new .exe and uses a batch script
        to replace it after the app closes.
        
        Args:
            update_info: Dict from check_for_updates()
            progress_callback: Optional function(current, total, filename) for progress
        
        Returns:
            True if successful, False otherwise
        """
        # Check if running as frozen executable (PyInstaller single-file)
        if getattr(sys, 'frozen', False):
            return self._download_exe_update(update_info, progress_callback)
        else:
            # Development mode - update individual files
            return self._download_file_updates(update_info, progress_callback)
    
    def _download_exe_update(self, update_info: Dict, progress_callback=None) -> bool:
        """
        Download new .exe for single-file executable updates
        
        Strategy:
        1. Download new LRU_Tracker.exe to LRU_Tracker.exe.new
        2. Extract/copy updater.bat to app directory
        3. Launch updater.bat and exit
        4. Batch script waits for app to close, replaces .exe, restarts
        """
        try:
            app_dir = Path(sys.executable).parent
            exe_name = Path(sys.executable).name  # Usually "LRU_Tracker.exe"
            
            # Get download URL for the new exe
            exe_url = update_info.get('exe_download_url')
            if not exe_url:
                # Fallback: try to construct from GitHub release
                version = update_info['version']
                exe_url = f"https://github.com/{self.github_repo}/releases/download/v{version}/LRU_Tracker.exe"
            
            if progress_callback:
                progress_callback(0, 100, "Preparing update...")
            
            # Download new exe to temp location
            new_exe_path = app_dir / f"{exe_name}.new"
            
            if progress_callback:
                progress_callback(25, 100, f"Downloading {exe_name}...")
            
            # Download with progress tracking
            self._download_file_with_progress(exe_url, new_exe_path, progress_callback)
            
            if progress_callback:
                progress_callback(90, 100, "Preparing updater...")
            
            # Extract updater.bat from resources or use embedded version
            updater_script = app_dir / "updater.bat"
            self._extract_updater_script(updater_script)
            
            if progress_callback:
                progress_callback(100, 100, "Update ready!")
            
            return True
            
        except Exception as e:
            print(f"Error downloading exe update: {e}")
            # Clean up partial downloads
            if 'new_exe_path' in locals() and new_exe_path.exists():
                new_exe_path.unlink()
            return False
    
    def _download_file_with_progress(self, url: str, destination: Path, progress_callback=None):
        """Download file with progress tracking"""
        import urllib.request
        
        destination.parent.mkdir(parents=True, exist_ok=True)
        
        def reporthook(block_num, block_size, total_size):
            if progress_callback and total_size > 0:
                downloaded = block_num * block_size
                percent = min(int((downloaded / total_size) * 65) + 25, 89)  # 25-89% range
                mb_downloaded = downloaded / (1024 * 1024)
                mb_total = total_size / (1024 * 1024)
                progress_callback(percent, 100, f"Downloading: {mb_downloaded:.1f}/{mb_total:.1f} MB")
        
        urllib.request.urlretrieve(url, destination, reporthook=reporthook)
    
    def _extract_updater_script(self, destination: Path):
        """Extract updater.bat script to app directory"""
        # Updater script content - runs silently, replaces exe, restarts
        updater_content = '''@echo off
REM LRU Tracker - Silent Update Applier
REM Waits for app to close, replaces exe, restarts

REM Wait for application to fully exit
timeout /t 2 /nobreak >nul 2>nul

REM Get the directory where this script is located
set "APP_DIR=%~dp0"
cd /d "%APP_DIR%"

REM Check if new exe exists
if not exist "LRU_Tracker.exe.new" (
    exit /b 1
)

REM Backup current exe
if exist "LRU_Tracker.exe" (
    if exist "LRU_Tracker.exe.backup" del /Q "LRU_Tracker.exe.backup" >nul 2>nul
    move /Y "LRU_Tracker.exe" "LRU_Tracker.exe.backup" >nul 2>nul
)

REM Replace with new version
move /Y "LRU_Tracker.exe.new" "LRU_Tracker.exe" >nul 2>nul
if errorlevel 1 (
    REM Restore backup on failure
    if exist "LRU_Tracker.exe.backup" (
        move /Y "LRU_Tracker.exe.backup" "LRU_Tracker.exe" >nul 2>nul
    )
    exit /b 1
)

REM Wait a moment before restarting
timeout /t 1 /nobreak >nul 2>nul

REM Start the updated application (not waiting for it to exit)
start "" "%APP_DIR%LRU_Tracker.exe"

REM Clean up backup after successful start
timeout /t 2 /nobreak >nul 2>nul
if exist "LRU_Tracker.exe.backup" del /Q "LRU_Tracker.exe.backup" >nul 2>nul

REM Self-destruct
(goto) 2>nul & del /Q "%~f0" >nul 2>nul
'''
        
        destination.write_text(updater_content, encoding='utf-8')
    
    def _download_file_updates(self, update_info: Dict, progress_callback=None) -> bool:
        """
        Download and apply file-by-file updates (for development mode)
        Original implementation for updating individual Python files
        """
        changed_files = update_info['changed_files']
        total_files = len(changed_files)
        
        if total_files == 0:
            return True
        
        # Create backup directory
        app_dir = Path(sys.executable).parent if getattr(sys, 'frozen', False) else Path(__file__).parent.parent
        backup_dir = app_dir / ".update_backup"
        backup_dir.mkdir(exist_ok=True)
        
        downloaded_files = []
        
        try:
            for idx, (file_path, file_info) in enumerate(changed_files.items(), 1):
                if progress_callback:
                    progress_callback(idx, total_files, file_path)
                
                # Download file
                download_url = file_info.get('download_url', self.base_download_url + file_path)
                local_file = app_dir / file_path
                
                # Backup existing file if it exists
                if local_file.exists():
                    backup_file = backup_dir / file_path
                    backup_file.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(local_file, backup_file)
                
                # Download new file
                self._download_file(download_url, local_file)
                downloaded_files.append(file_path)
                
                # Verify hash
                downloaded_hash = self._calculate_file_hash(local_file)
                expected_hash = file_info.get('sha256')
                
                if downloaded_hash != expected_hash:
                    raise ValueError(f"Hash mismatch for {file_path}")
            
            # Update version file
            self._update_local_version(update_info['version'])
            
            # Clean up backup after successful update
            shutil.rmtree(backup_dir, ignore_errors=True)
            
            return True
            
        except Exception as e:
            print(f"Error during update: {e}")
            
            # Rollback - restore from backup
            self._rollback_update(backup_dir, downloaded_files)
            return False
    
    def _download_file(self, url: str, destination: Path):
        """Download a file from URL to destination"""
        destination.parent.mkdir(parents=True, exist_ok=True)
        
        with urllib.request.urlopen(url, timeout=30) as response:
            with open(destination, 'wb') as f:
                f.write(response.read())
    
    def _rollback_update(self, backup_dir: Path, downloaded_files: List[str]):
        """Restore files from backup if update fails"""
        app_dir = Path(sys.executable).parent if getattr(sys, 'frozen', False) else Path(__file__).parent.parent
        
        for file_path in downloaded_files:
            backup_file = backup_dir / file_path
            if backup_file.exists():
                local_file = app_dir / file_path
                shutil.copy2(backup_file, local_file)
        
        print("Update rolled back successfully")
    
    def _update_local_version(self, new_version: str):
        """Update local version file"""
        app_dir = Path(sys.executable).parent if getattr(sys, 'frozen', False) else Path(__file__).parent.parent
        version_file = app_dir / "version.txt"
        
        version_file.write_text(new_version)
    
    def restart_application(self):
        """
        Restart the application to apply updates
        
        For single-file executables, launches the updater batch script
        which waits for the app to close, replaces the .exe, and restarts it.
        """
        if getattr(sys, 'frozen', False):
            # Running as executable - launch updater script
            app_dir = Path(sys.executable).parent
            updater_script = app_dir / "updater.bat"
            
            if updater_script.exists():
                # Launch updater silently in background
                # The batch script will wait for this app to close, then replace the exe
                subprocess.Popen(
                    [str(updater_script)],
                    cwd=str(app_dir),
                    creationflags=subprocess.CREATE_NO_WINDOW | subprocess.DETACHED_PROCESS
                )
                
                # Give the updater time to start
                import time
                time.sleep(0.3)
            else:
                # Fallback: direct restart (may not apply update correctly)
                subprocess.Popen([sys.executable])
            
            # Exit this app so updater can replace the .exe
            sys.exit(0)
        else:
            # Running as script - direct restart
            python = sys.executable
            subprocess.Popen([python] + sys.argv)
            sys.exit(0)


# GitHub API Integration (Advanced)
class GitHubUpdateChecker:
    """Uses GitHub API to check for updates and get file changes"""
    
    def __init__(self, repo: str = "HaltTheGrey/lru-tracker"):
        self.repo = repo
        self.api_base = f"https://api.github.com/repos/{repo}"
    
    def get_latest_release(self) -> Optional[Dict]:
        """Get latest GitHub release info"""
        try:
            url = f"{self.api_base}/releases/latest"
            
            with urllib.request.urlopen(url, timeout=10) as response:
                release = json.loads(response.read().decode('utf-8'))
            
            return {
                'version': release['tag_name'].lstrip('v'),
                'name': release['name'],
                'body': release['body'],
                'published_at': release['published_at'],
                'assets': [
                    {
                        'name': asset['name'],
                        'size': asset['size'],
                        'download_url': asset['browser_download_url']
                    }
                    for asset in release['assets']
                ]
            }
        except Exception as e:
            print(f"Error getting GitHub release: {e}")
            return None
    
    def get_commits_since_version(self, version: str) -> List[Dict]:
        """Get list of commits since a specific version/tag"""
        try:
            url = f"{self.api_base}/commits?sha=main&since={version}"
            
            with urllib.request.urlopen(url, timeout=10) as response:
                commits = json.loads(response.read().decode('utf-8'))
            
            return [
                {
                    'sha': commit['sha'][:7],
                    'message': commit['commit']['message'],
                    'author': commit['commit']['author']['name'],
                    'date': commit['commit']['author']['date']
                }
                for commit in commits
            ]
        except Exception as e:
            print(f"Error getting commits: {e}")
            return []
    
    def get_changed_files_between_tags(self, old_tag: str, new_tag: str) -> List[str]:
        """Get list of files that changed between two tags"""
        try:
            url = f"{self.api_base}/compare/{old_tag}...{new_tag}"
            
            with urllib.request.urlopen(url, timeout=10) as response:
                comparison = json.loads(response.read().decode('utf-8'))
            
            changed_files = []
            for file in comparison.get('files', []):
                if file['status'] in ['modified', 'added']:
                    changed_files.append(file['filename'])
            
            return changed_files
        except Exception as e:
            print(f"Error comparing tags: {e}")
            return []


# Example usage
if __name__ == "__main__":
    # Test incremental updater
    updater = IncrementalUpdater(current_version="1.2.1")
    
    print("Checking for updates...")
    update_info = updater.check_for_updates()
    
    if update_info:
        print(f"\nUpdate available: v{update_info['version']}")
        print(f"Download size: {update_info['total_download_size'] / 1024 / 1024:.2f} MB")
        print(f"Files to update: {len(update_info['changed_files'])}")
        print("\nChanged files:")
        for file in update_info['changed_files']:
            print(f"  - {file}")
    else:
        print("No updates available")
    
    # Test GitHub API
    print("\n" + "="*50)
    gh = GitHubUpdateChecker()
    
    latest = gh.get_latest_release()
    if latest:
        print(f"\nLatest GitHub Release: v{latest['version']}")
        print(f"Published: {latest['published_at']}")
        print(f"Assets: {len(latest['assets'])}")
