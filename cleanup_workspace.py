"""
Automated workspace cleanup script for v1.2.8
Removes redundant files and organizes documentation
"""
import os
import shutil
from pathlib import Path

# Get workspace root
WORKSPACE_ROOT = Path(__file__).parent

print("=" * 60)
print("  WORKSPACE CLEANUP - v1.2.8")
print("=" * 60)
print()

# Files to delete from root directory
ROOT_FILES_TO_DELETE = [
    "version_v1.2.0.json",
    "AUTO_UPDATE_FEATURE_v1.2.2.md",
    "CLEANUP_COMPLETE_FEB_6_2026.md",
    "CLEANUP_PLAN.md",
    "EXPORT_IMPROVEMENTS_v1.2.3.md",
    "GITHUB_RELEASE_v1.2.1.md",
    "GITHUB_RELEASE_v1.2.2.md",
    "GITHUB_RELEASE_v1.2.3.md",
    "INCREMENTAL_UPDATE_GUIDE.md",
    "INCREMENTAL_UPDATE_INTEGRATED.md",
    "INSTALLER_IMPROVEMENTS_v1.2.2.md",
    "PERMISSION_FIX_QUICK_GUIDE.md",
    "UPDATE_FIX_v1.2.3.md",
    "USER_NOTIFICATION_v1.2.1.txt",
    "update_manifest_EXAMPLE.json",
]

# Files to delete from distribution/
DIST_FILES_TO_DELETE = [
    "distribution/version.json",
    "distribution/build_windows.bat",
    "distribution/build_mac.sh",
    "distribution/CHANGES_SUMMARY.txt",
    "distribution/INSTALLER_UPDATE_SUMMARY.txt",
    "distribution/START_HERE.txt",
    "distribution/SYSTEM_DIAGRAM.txt",
    "distribution/installer_script.iss",
]

# Files to delete from refactored/
REFACTORED_FILES_TO_DELETE = [
    "refactored/update_checker_TEST_MODE.py",
    "refactored/updater.bat",
]

# Files to move to release notes folders
DOCS_TO_MOVE = {
    "docs/release-notes/v1.2.1/": [
        ("PERMISSION_FIX_QUICK_GUIDE.md", "."),
        ("USER_NOTIFICATION_v1.2.1.txt", "."),
        ("docs/developer-guides/PERMISSION_ERROR_FIX_v1.2.1.md", "docs/developer-guides/"),
    ],
    "docs/release-notes/v1.2.2/": [
        ("AUTO_UPDATE_FEATURE_v1.2.2.md", "."),
        ("INSTALLER_IMPROVEMENTS_v1.2.2.md", "."),
    ],
    "docs/release-notes/v1.2.3/": [
        ("EXPORT_IMPROVEMENTS_v1.2.3.md", "."),
        ("UPDATE_FIX_v1.2.3.md", "."),
    ],
}


def delete_files(file_list, description):
    """Delete a list of files"""
    print(f"🗑️  Deleting {description}...")
    deleted_count = 0
    
    for file_path in file_list:
        full_path = WORKSPACE_ROOT / file_path
        if full_path.exists():
            try:
                full_path.unlink()
                print(f"   ✓ Deleted: {file_path}")
                deleted_count += 1
            except Exception as e:
                print(f"   ✗ Failed to delete {file_path}: {e}")
        else:
            print(f"   - Not found: {file_path}")
    
    print(f"   Deleted {deleted_count}/{len(file_list)} files\n")
    return deleted_count


def move_and_organize_docs():
    """Move documentation to organized folders"""
    print("📁 Organizing documentation...")
    moved_count = 0
    
    for target_folder, files in DOCS_TO_MOVE.items():
        target_path = WORKSPACE_ROOT / target_folder
        
        # Create target folder if it doesn't exist
        target_path.mkdir(parents=True, exist_ok=True)
        print(f"\n   📂 {target_folder}")
        
        for source_file, source_location in files:
            if source_location == ".":
                source_path = WORKSPACE_ROOT / source_file
            else:
                source_path = WORKSPACE_ROOT / source_location / source_file
            
            dest_path = target_path / Path(source_file).name
            
            if source_path.exists():
                try:
                    shutil.move(str(source_path), str(dest_path))
                    print(f"      ✓ Moved: {source_file}")
                    moved_count += 1
                except Exception as e:
                    print(f"      ✗ Failed to move {source_file}: {e}")
            else:
                print(f"      - Not found: {source_file}")
    
    print(f"\n   Moved {moved_count} files\n")
    return moved_count


def create_release_notes_folder():
    """Create folder for v1.2.8 release notes"""
    print("📝 Creating v1.2.8 release notes folder...")
    
    folder_path = WORKSPACE_ROOT / "docs/release-notes/v1.2.8"
    folder_path.mkdir(parents=True, exist_ok=True)
    
    # Create placeholder README
    readme_content = """# v1.2.8 Release Notes

**Release Date:** February 7, 2026

## Critical Fix: Incremental Update Detection

Fixed issue where incremental updates weren't being detected from version.json,
causing users to download full installer instead of just the exe.

### Files in this folder:
- (Add release-specific documentation here)
"""
    
    readme_path = folder_path / "README.md"
    readme_path.write_text(readme_content)
    
    print(f"   ✓ Created: {folder_path}")
    print(f"   ✓ Created: {readme_path}\n")


def generate_summary():
    """Generate cleanup summary"""
    print("=" * 60)
    print("  CLEANUP SUMMARY")
    print("=" * 60)
    
    # Count remaining files in root
    root_md_files = list(WORKSPACE_ROOT.glob("*.md"))
    root_json_files = list(WORKSPACE_ROOT.glob("*.json"))
    
    print(f"\n📊 Current State:")
    print(f"   Root .md files:   {len(root_md_files)}")
    print(f"   Root .json files: {len(root_json_files)}")
    
    # List remaining root markdown files
    if root_md_files:
        print(f"\n📄 Remaining root .md files:")
        for f in sorted(root_md_files):
            print(f"   - {f.name}")
    
    # Check release notes organization
    release_notes_path = WORKSPACE_ROOT / "docs/release-notes"
    if release_notes_path.exists():
        version_folders = [d for d in release_notes_path.iterdir() if d.is_dir()]
        print(f"\n📂 Release notes folders: {len(version_folders)}")
        for folder in sorted(version_folders):
            file_count = len(list(folder.glob("*.md")))
            print(f"   - {folder.name}: {file_count} files")


def main():
    """Execute cleanup"""
    total_deleted = 0
    total_moved = 0
    
    # Phase 1: Delete redundant files
    print("\n🧹 Phase 1: Deleting redundant files\n")
    total_deleted += delete_files(ROOT_FILES_TO_DELETE, "root directory files")
    total_deleted += delete_files(DIST_FILES_TO_DELETE, "distribution files")
    total_deleted += delete_files(REFACTORED_FILES_TO_DELETE, "refactored test files")
    
    # Phase 2: Organize documentation
    print("\n📚 Phase 2: Organizing documentation\n")
    total_moved = move_and_organize_docs()
    
    # Phase 3: Create v1.2.8 release notes
    print("\n📦 Phase 3: Setting up v1.2.8 release notes\n")
    create_release_notes_folder()
    
    # Summary
    generate_summary()
    
    print(f"\n✅ Cleanup complete!")
    print(f"   - Deleted: {total_deleted} files")
    print(f"   - Moved: {total_moved} files")
    print(f"\n💡 Next steps:")
    print(f"   1. Review changes with: git status")
    print(f"   2. Run tests: python -m pytest refactored/tests/")
    print(f"   3. Update README.md version to v1.2.8")
    print(f"   4. Commit cleanup: git add . && git commit -m '🧹 Workspace cleanup for v1.2.8'")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Cleanup cancelled by user")
    except Exception as e:
        print(f"\n\n❌ Error during cleanup: {e}")
        import traceback
        traceback.print_exc()
