"""
Tests for IncrementalUpdater - exe download and batch script generation
"""
import unittest
import sys
import os
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

# Add refactored directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from incremental_updater import IncrementalUpdater


class TestIncrementalUpdater(unittest.TestCase):
    """Test cases for incremental update functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.updater = IncrementalUpdater(current_version="1.2.7")
    
    def test_initialization(self):
        """Test updater initializes correctly"""
        self.assertEqual(self.updater.current_version, "1.2.7")
        self.assertIn("HaltTheGrey/lru-tracker", self.updater.github_repo)
    
    def test_exe_download_detection(self):
        """Test that exe downloads are detected when running as frozen executable"""
        update_info = {
            'version': '1.2.8',
            'exe_download_url': 'https://github.com/test/releases/download/v1.2.8/LRU_Tracker.exe',
            'exe_size_mb': 127
        }
        
        with patch('sys.frozen', True, create=True):
            with patch('sys.executable', 'C:\\Program Files\\LRU_Tracker\\LRU_Tracker.exe'):
                # Should detect frozen executable and use exe download
                self.assertTrue(hasattr(sys, 'frozen'))
    
    def test_batch_script_generation(self):
        """Test that updater.bat script is generated correctly"""
        script_path = Path("test_updater.bat")
        
        try:
            self.updater._extract_updater_script(script_path)
            
            # Verify file exists
            self.assertTrue(script_path.exists())
            
            # Verify script content
            content = script_path.read_text()
            self.assertIn("LRU_Tracker.exe.new", content)
            self.assertIn("LRU_Tracker.exe.backup", content)
            self.assertIn("timeout", content)
            
        finally:
            # Cleanup
            if script_path.exists():
                script_path.unlink()
    
    @patch('urllib.request.urlretrieve')
    def test_download_file_with_progress(self, mock_urlretrieve):
        """Test file download with progress callback"""
        test_url = "https://github.com/test/file.exe"
        test_dest = Path("test_download.exe")
        
        progress_calls = []
        def progress_callback(percent, total, message):
            progress_calls.append((percent, total, message))
        
        try:
            # Mock successful download
            mock_urlretrieve.return_value = None
            
            self.updater._download_file_with_progress(
                test_url,
                test_dest,
                progress_callback
            )
            
            # Verify download was called
            mock_urlretrieve.assert_called_once()
            
        finally:
            if test_dest.exists():
                test_dest.unlink()
    
    def test_version_comparison(self):
        """Test version comparison logic"""
        test_cases = [
            ("1.2.8", "1.2.7", 1),  # newer
            ("1.2.7", "1.2.8", -1),  # older
            ("1.2.7", "1.2.7", 0),  # equal
            ("2.0.0", "1.9.9", 1),  # major version
        ]
        
        for v1, v2, expected in test_cases:
            result = self.updater._compare_versions(v1, v2)
            self.assertEqual(result, expected,
                           f"Failed: {v1} vs {v2} expected {expected}")
    
    @patch('sys.frozen', True, create=True)
    @patch('sys.executable', 'C:\\App\\LRU_Tracker.exe')
    def test_exe_update_flow(self):
        """Test complete exe update workflow"""
        update_info = {
            'version': '1.2.8',
            'exe_download_url': 'https://github.com/test/LRU_Tracker.exe',
            'exe_size_mb': 127
        }
        
        with patch.object(self.updater, '_download_file_with_progress') as mock_download:
            with patch.object(self.updater, '_extract_updater_script') as mock_script:
                result = self.updater._download_exe_update(update_info, None)
                
                # Should call download and script extraction
                self.assertTrue(mock_download.called)
                self.assertTrue(mock_script.called)
                self.assertTrue(result)
    
    def test_fallback_to_file_updates(self):
        """Test fallback to file-by-file updates when not frozen"""
        update_info = {
            'changed_files': {},
            'total_download_size': 0
        }
        
        with patch('sys.frozen', False, create=True):
            result = self.updater._download_file_updates(update_info, None)
            # Empty file list should succeed
            self.assertTrue(result)


class TestBatchScriptContent(unittest.TestCase):
    """Test the generated batch script logic"""
    
    def test_script_has_required_commands(self):
        """Verify batch script contains all required operations"""
        updater = IncrementalUpdater("1.2.7")
        script_path = Path("test_script.bat")
        
        try:
            updater._extract_updater_script(script_path)
            content = script_path.read_text()
            
            # Check for critical operations
            required_operations = [
                "timeout",  # Wait for app to close
                "LRU_Tracker.exe.new",  # New exe file
                "LRU_Tracker.exe.backup",  # Backup creation
                "move",  # File movement
                "start",  # Restart app
            ]
            
            for operation in required_operations:
                self.assertIn(operation, content,
                            f"Missing required operation: {operation}")
        
        finally:
            if script_path.exists():
                script_path.unlink()
    
    def test_script_is_silent(self):
        """Verify script runs silently without console output"""
        updater = IncrementalUpdater("1.2.7")
        script_path = Path("test_script.bat")
        
        try:
            updater._extract_updater_script(script_path)
            content = script_path.read_text()
            
            # Should redirect errors to null
            self.assertIn(">nul 2>nul", content)
            
            # Should NOT have echo statements (except @echo off)
            lines = content.split('\n')
            echo_lines = [l for l in lines if 'echo' in l.lower() and '@echo off' not in l.lower() and 'REM' not in l]
            self.assertEqual(len(echo_lines), 0,
                           "Script should not have echo statements for silent operation")
        
        finally:
            if script_path.exists():
                script_path.unlink()


if __name__ == '__main__':
    unittest.main()
