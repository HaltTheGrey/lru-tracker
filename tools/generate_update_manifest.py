"""
Update Manifest Generator
Creates update_manifest.json with file hashes for incremental updates
"""

import hashlib
import json
from pathlib import Path
from typing import Dict, List
import os


class ManifestGenerator:
    """Generates update manifests for incremental updates"""
    
    def __init__(self, version: str, base_dir: Path = None):
        self.version = version
        self.base_dir = base_dir or Path(__file__).parent.parent
        self.github_repo = "HaltTheGrey/lru-tracker"
        
    def generate_manifest(self, 
                         files_to_track: List[str] = None,
                         output_file: str = "update_manifest.json") -> Dict:
        """
        Generate update manifest with file hashes
        
        Args:
            files_to_track: List of file paths to include (relative to base_dir)
                           If None, auto-detects Python files
            output_file: Where to save the manifest
        
        Returns:
            The generated manifest dict
        """
        
        if files_to_track is None:
            # Auto-detect important files
            files_to_track = self._auto_detect_files()
        
        files_manifest = {}
        total_size = 0
        
        for file_path in files_to_track:
            full_path = self.base_dir / file_path
            
            if not full_path.exists():
                print(f"Warning: {file_path} not found, skipping...")
                continue
            
            # Calculate file hash
            file_hash = self._calculate_file_hash(full_path)
            file_size = full_path.stat().st_size
            total_size += file_size
            
            # Determine download URL
            download_url = f"https://raw.githubusercontent.com/{self.github_repo}/main/{file_path.replace(chr(92), '/')}"
            
            files_manifest[file_path] = {
                "size": file_size,
                "sha256": file_hash,
                "download_url": download_url,
                "description": self._get_file_description(file_path)
            }
        
        # Build full manifest
        manifest = {
            "version": self.version,
            "release_date": self._get_current_timestamp(),
            "release_notes": "See GitHub release for details",
            "files": files_manifest,
            "update_strategy": "incremental",
            "minimum_version": "1.2.0",
            "changelog_url": f"https://github.com/{self.github_repo}/releases/tag/v{self.version}",
            "incremental_update_info": {
                "total_files_changed": len(files_manifest),
                "total_download_size": total_size,
                "comparison": {
                    "full_download": 133169152,  # ~127 MB
                    "incremental_download": total_size,
                    "savings_mb": round((133169152 - total_size) / 1024 / 1024, 2),
                    "savings_percent": round((1 - total_size / 133169152) * 100, 2)
                }
            }
        }
        
        # Save to file
        output_path = self.base_dir / output_file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Manifest generated: {output_path}")
        print(f"   Version: {self.version}")
        print(f"   Files tracked: {len(files_manifest)}")
        print(f"   Total size: {total_size / 1024 / 1024:.2f} MB")
        print(f"   Savings vs full download: {manifest['incremental_update_info']['comparison']['savings_mb']} MB ({manifest['incremental_update_info']['comparison']['savings_percent']}%)")
        
        return manifest
    
    def _auto_detect_files(self) -> List[str]:
        """Auto-detect files to track (Python source files)"""
        files = []
        
        # Track all Python files in refactored directory
        refactored_dir = self.base_dir / "refactored"
        if refactored_dir.exists():
            for py_file in refactored_dir.glob("*.py"):
                rel_path = py_file.relative_to(self.base_dir)
                files.append(str(rel_path))
        
        # Track version.json
        if (self.base_dir / "version.json").exists():
            files.append("version.json")
        
        return files
    
    def _calculate_file_hash(self, file_path: Path) -> str:
        """Calculate SHA256 hash of a file"""
        sha256_hash = hashlib.sha256()
        
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        
        return sha256_hash.hexdigest()
    
    def _get_file_description(self, file_path: str) -> str:
        """Get human-readable description of file"""
        descriptions = {
            "refactored/lru_tracker_refactored.py": "Main application file",
            "refactored/config.py": "Configuration settings",
            "refactored/update_checker.py": "Update checking logic",
            "refactored/ui.py": "User interface components",
            "refactored/data_handler.py": "Data management",
            "refactored/excel_handler.py": "Excel export functionality",
            "refactored/validators.py": "Input validation",
            "version.json": "Version metadata"
        }
        
        return descriptions.get(file_path, Path(file_path).name)
    
    def _get_current_timestamp(self) -> str:
        """Get current timestamp in ISO format"""
        from datetime import datetime
        return datetime.now().isoformat()
    
    def compare_with_previous_version(self, old_manifest_path: str) -> Dict:
        """
        Compare current files with previous version manifest
        Returns dict showing what changed
        """
        try:
            with open(old_manifest_path, 'r') as f:
                old_manifest = json.load(f)
        except FileNotFoundError:
            print(f"Previous manifest not found: {old_manifest_path}")
            return {}
        
        current_files = self._auto_detect_files()
        old_files = old_manifest.get('files', {})
        
        changes = {
            'added': [],
            'modified': [],
            'removed': [],
            'unchanged': []
        }
        
        # Check each current file
        for file_path in current_files:
            full_path = self.base_dir / file_path
            
            if not full_path.exists():
                continue
            
            current_hash = self._calculate_file_hash(full_path)
            
            if file_path not in old_files:
                changes['added'].append(file_path)
            elif old_files[file_path]['sha256'] != current_hash:
                changes['modified'].append(file_path)
            else:
                changes['unchanged'].append(file_path)
        
        # Check for removed files
        for old_file in old_files:
            if old_file not in current_files:
                changes['removed'].append(old_file)
        
        # Print summary
        print("\n📊 Changes from previous version:")
        print(f"   ✅ Added: {len(changes['added'])}")
        for f in changes['added']:
            print(f"      + {f}")
        
        print(f"   📝 Modified: {len(changes['modified'])}")
        for f in changes['modified']:
            print(f"      ~ {f}")
        
        print(f"   ❌ Removed: {len(changes['removed'])}")
        for f in changes['removed']:
            print(f"      - {f}")
        
        print(f"   ⚪ Unchanged: {len(changes['unchanged'])}")
        
        return changes


def main():
    """Generate manifest for current version"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate update manifest')
    parser.add_argument('--version', required=True, help='Version number (e.g., 1.2.2)')
    parser.add_argument('--compare', help='Path to previous manifest for comparison')
    parser.add_argument('--output', default='update_manifest.json', help='Output filename')
    
    args = parser.parse_args()
    
    generator = ManifestGenerator(version=args.version)
    
    # Compare with previous version if specified
    if args.compare:
        generator.compare_with_previous_version(args.compare)
    
    # Generate new manifest
    manifest = generator.generate_manifest(output_file=args.output)
    
    print("\n📋 Next steps:")
    print("   1. Review the generated manifest")
    print("   2. Commit update_manifest.json to GitHub")
    print("   3. Users will download only changed files (~99% smaller)")
    print("   4. Update process will be much faster!")


if __name__ == "__main__":
    # Quick test
    generator = ManifestGenerator(version="1.2.2")
    manifest = generator.generate_manifest()
    
    print("\n" + "="*60)
    print("Sample manifest generated!")
    print("="*60)
