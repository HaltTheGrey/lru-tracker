"""GitHub Sync Manager for collaborative LRU tracking across multiple computers.

Allows multiple users to share the same data file via GitHub repository.
Use case: Computer A does morning walk, Computer B continues afternoon walk.
"""
import json
import base64
import urllib.request
import urllib.error
from typing import Dict, Optional, Tuple
from datetime import datetime
from pathlib import Path
from logger import get_logger

logger = get_logger(__name__)


class GitHubSyncManager:
    """Manages syncing LRU data with GitHub repository."""
    
    def __init__(self, 
                 repo_owner: str,
                 repo_name: str,
                 data_file_path: str = "shared_data/lru_data.json",
                 branch: str = "main"):
        """
        Initialize GitHub sync manager.
        
        Args:
            repo_owner: GitHub username/organization (e.g., "HaltTheGrey")
            repo_name: Repository name (e.g., "lru-shared-data")
            data_file_path: Path to data file in repo (e.g., "shared_data/lru_data.json")
            branch: Branch name (default "main")
        """
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.data_file_path = data_file_path
        self.branch = branch
        
        # GitHub API endpoints
        self.api_base = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
        self.file_url = f"{self.api_base}/contents/{data_file_path}"
        
        # Authentication token (optional but recommended for private repos)
        self.token: Optional[str] = None
        
        # Track last sync info
        self.last_sha: Optional[str] = None
        self.last_sync_time: Optional[datetime] = None
    
    def set_token(self, token: str) -> None:
        """Set GitHub personal access token for authentication."""
        self.token = token
        logger.info("GitHub token configured")
    
    def check_remote_changes(self) -> Tuple[bool, Optional[Dict]]:
        """
        Check if remote file has been updated since last sync.
        
        Returns:
            Tuple of (has_changes, remote_info)
            has_changes: True if remote is different from last known state
            remote_info: Dict with file metadata if available
        """
        try:
            # Get file metadata from GitHub
            request = urllib.request.Request(self.file_url)
            request.add_header('Accept', 'application/vnd.github.v3+json')
            if self.token:
                request.add_header('Authorization', f'token {self.token}')
            
            with urllib.request.urlopen(request, timeout=10) as response:
                remote_info = json.loads(response.read().decode())
                
                remote_sha = remote_info.get('sha')
                
                # If we have no last_sha, this is first sync - consider it changed
                if self.last_sha is None:
                    logger.info("No previous sync - remote file exists")
                    return True, remote_info
                
                # Check if SHA changed (file was modified)
                has_changes = (remote_sha != self.last_sha)
                
                if has_changes:
                    logger.info(f"Remote file changed (SHA: {remote_sha[:8]}...)")
                else:
                    logger.debug("Remote file unchanged")
                
                return has_changes, remote_info
                
        except urllib.error.HTTPError as e:
            if e.code == 404:
                logger.warning("Remote file not found (first push needed)")
                return False, None
            else:
                logger.error(f"HTTP error checking remote: {e.code} - {e.reason}")
                raise Exception(f"Failed to check remote: {e.code} {e.reason}")
        except Exception as e:
            logger.error(f"Error checking remote changes: {e}")
            raise
    
    def pull_from_github(self) -> Optional[Dict]:
        """
        Download data file from GitHub.
        
        Returns:
            Dict with stations and history data, or None if file doesn't exist
        """
        try:
            logger.info(f"Pulling from GitHub: {self.repo_owner}/{self.repo_name}/{self.data_file_path}")
            
            # Get file from GitHub
            request = urllib.request.Request(self.file_url)
            request.add_header('Accept', 'application/vnd.github.v3+json')
            if self.token:
                request.add_header('Authorization', f'token {self.token}')
            
            with urllib.request.urlopen(request, timeout=10) as response:
                file_info = json.loads(response.read().decode())
                
                # Decode base64 content
                content_base64 = file_info['content']
                content_bytes = base64.b64decode(content_base64)
                content_text = content_bytes.decode('utf-8')
                
                # Parse JSON data
                data = json.loads(content_text)
                
                # Update tracking
                self.last_sha = file_info['sha']
                self.last_sync_time = datetime.now()
                
                sha_display = self.last_sha[:8] + "..." if self.last_sha else "unknown"
                logger.info(f"✅ Pulled successfully (SHA: {sha_display})")
                logger.info(f"Stations: {len(data.get('stations', {}))}, History: {len(data.get('history', []))}")
                
                return data
                
        except urllib.error.HTTPError as e:
            if e.code == 404:
                logger.warning("Remote file not found - needs initial push")
                return None
            else:
                logger.error(f"HTTP error pulling from GitHub: {e.code} - {e.reason}")
                raise Exception(f"Pull failed: {e.code} {e.reason}")
        except Exception as e:
            logger.error(f"Error pulling from GitHub: {e}")
            raise
    
    def push_to_github(self, data: Dict, commit_message: Optional[str] = None) -> bool:
        """
        Upload data file to GitHub.
        
        Args:
            data: Dict with stations and history data
            commit_message: Optional custom commit message
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Default commit message with timestamp and computer name
            if commit_message is None:
                import platform
                computer = platform.node()
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                commit_message = f"Updated by {computer} at {timestamp}"
            
            logger.info(f"Pushing to GitHub: {self.repo_owner}/{self.repo_name}/{self.data_file_path}")
            
            # Convert data to JSON
            content_text = json.dumps(data, indent=2)
            content_bytes = content_text.encode('utf-8')
            content_base64 = base64.b64encode(content_bytes).decode('utf-8')
            
            # Check if file exists (need SHA for updates)
            try:
                request = urllib.request.Request(self.file_url)
                request.add_header('Accept', 'application/vnd.github.v3+json')
                if self.token:
                    request.add_header('Authorization', f'token {self.token}')
                
                with urllib.request.urlopen(request, timeout=10) as response:
                    existing_file = json.loads(response.read().decode())
                    file_sha = existing_file['sha']
                    logger.debug(f"File exists, SHA: {file_sha[:8]}...")
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    file_sha = None  # File doesn't exist yet
                    logger.debug("File doesn't exist, will create new")
                else:
                    raise
            
            # Prepare request body
            body = {
                "message": commit_message,
                "content": content_base64,
                "branch": self.branch
            }
            
            if file_sha:
                body["sha"] = file_sha  # Required for updates
            
            # Push to GitHub
            request = urllib.request.Request(
                self.file_url,
                data=json.dumps(body).encode('utf-8'),
                method='PUT'
            )
            request.add_header('Accept', 'application/vnd.github.v3+json')
            request.add_header('Content-Type', 'application/json')
            if self.token:
                request.add_header('Authorization', f'token {self.token}')
            
            with urllib.request.urlopen(request, timeout=15) as response:
                result = json.loads(response.read().decode())
                
                # Update tracking
                self.last_sha = result['content']['sha']
                self.last_sync_time = datetime.now()
                
                sha_display = self.last_sha[:8] + "..." if self.last_sha else "unknown"
                logger.info(f"✅ Pushed successfully (SHA: {sha_display})")
                return True
                
        except urllib.error.HTTPError as e:
            error_body = e.read().decode() if e.fp else "No details"
            logger.error(f"HTTP error pushing to GitHub: {e.code} - {e.reason}")
            logger.error(f"Error details: {error_body}")
            raise Exception(f"Push failed: {e.code} {e.reason}\n{error_body}")
        except Exception as e:
            logger.error(f"Error pushing to GitHub: {e}")
            raise
    
    def get_sync_status(self) -> Dict:
        """Get current sync status information."""
        return {
            "repo": f"{self.repo_owner}/{self.repo_name}",
            "file_path": self.data_file_path,
            "branch": self.branch,
            "last_sha": self.last_sha[:8] + "..." if self.last_sha else "Never synced",
            "last_sync": self.last_sync_time.strftime("%Y-%m-%d %H:%M:%S") if self.last_sync_time else "Never",
            "has_token": bool(self.token)
        }
    
    def test_connection(self) -> Tuple[bool, str]:
        """
        Test GitHub connection and permissions.
        
        Returns:
            Tuple of (success, message)
        """
        try:
            # Try to access repository
            request = urllib.request.Request(self.api_base)
            request.add_header('Accept', 'application/vnd.github.v3+json')
            if self.token:
                request.add_header('Authorization', f'token {self.token}')
            
            with urllib.request.urlopen(request, timeout=10) as response:
                repo_info = json.loads(response.read().decode())
                repo_name = repo_info.get('name', 'Unknown')
                is_private = repo_info.get('private', False)
                
                message = f"✅ Connected to '{repo_name}' ({'Private' if is_private else 'Public'})"
                logger.info(message)
                return True, message
                
        except urllib.error.HTTPError as e:
            if e.code == 404:
                message = f"❌ Repository not found: {self.repo_owner}/{self.repo_name}"
            elif e.code == 401:
                message = "❌ Authentication failed - check your token"
            else:
                message = f"❌ HTTP Error {e.code}: {e.reason}"
            
            logger.error(message)
            return False, message
            
        except Exception as e:
            message = f"❌ Connection error: {str(e)}"
            logger.error(message)
            return False, message
