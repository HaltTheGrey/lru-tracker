"""
Create a clean release package with only user-essential files.
This script creates a zip file ready for GitHub Releases.
"""

import os
import shutil
import zipfile
from pathlib import Path

# Version number - update this for each release
VERSION = "1.0.0"

# Define what goes in the user release package
USER_ESSENTIALS = {
    # Documentation (root level)
    'docs': [
        'QUICK_START.md',
        'FC_SCHEDULE_IMPORT_GUIDE.md',
        'TEMPLATE_FEATURE_GUIDE.md',
    ],
    
    # The installer (if it exists)
    'installer': [
        'distribution/packages/LRU_Tracker_Setup.exe',
    ],
    
    # Quick start text file
    'instructions': 'USER_INSTALL_INSTRUCTIONS.txt'
}

def create_release_package():
    """Create a clean release package for end users."""
    
    print("=" * 60)
    print("  Creating User Release Package")
    print("=" * 60)
    print()
    
    # Get project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Create temporary release directory
    release_dir = project_root / 'distribution' / 'release_temp'
    if release_dir.exists():
        shutil.rmtree(release_dir)
    release_dir.mkdir(parents=True)
    
    print(f"📁 Working directory: {release_dir}")
    print()
    
    # Copy documentation
    print("📄 Copying documentation...")
    docs_dir = release_dir / 'Documentation'
    docs_dir.mkdir()
    
    for doc in USER_ESSENTIALS['docs']:
        src = project_root / doc
        if src.exists():
            shutil.copy2(src, docs_dir / src.name)
            print(f"  ✓ {src.name}")
        else:
            print(f"  ⚠ Missing: {src.name}")
    
    # Copy installer if it exists
    print()
    print("📦 Looking for installer...")
    installer_copied = False
    for installer_path in USER_ESSENTIALS['installer']:
        src = project_root / installer_path
        if src.exists():
            shutil.copy2(src, release_dir / src.name)
            print(f"  ✓ {src.name}")
            installer_copied = True
        else:
            print(f"  ⚠ Not found: {src.name}")
            print(f"     (Run BUILD_WINDOWS_ONE_CLICK.bat and compile with Inno Setup first)")
    
    # Create installation instructions
    print()
    print("📝 Creating installation instructions...")
    create_install_instructions(release_dir, installer_copied)
    
    # Create the zip file
    print()
    print("🗜️  Creating release ZIP file...")
    zip_path = project_root / 'distribution' / f'LRU_Tracker_v{VERSION}_Release.zip'
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(release_dir):
            for file in files:
                file_path = Path(root) / file
                arcname = file_path.relative_to(release_dir)
                zipf.write(file_path, arcname)
                print(f"  Added: {arcname}")
    
    # Clean up temp directory
    shutil.rmtree(release_dir)
    
    # Show final results
    print()
    print("=" * 60)
    print("✅ RELEASE PACKAGE CREATED!")
    print("=" * 60)
    print()
    print(f"📦 Package: {zip_path.name}")
    print(f"📍 Location: {zip_path}")
    print(f"💾 Size: {zip_path.stat().st_size / (1024*1024):.2f} MB")
    print()
    print("📤 Next Steps:")
    print("1. Go to: https://github.com/HaltTheGrey/lru-tracker/releases/new")
    print(f"2. Tag: v{VERSION}")
    print(f"3. Title: LRU Tracker v{VERSION}")
    print("4. Upload this ZIP file")
    print("5. Publish release!")
    print()
    print("👥 Users will download this single ZIP with everything they need!")
    print()

def create_install_instructions(release_dir, has_installer):
    """Create a simple installation instructions file."""
    
    instructions_path = release_dir / 'START_HERE.txt'
    
    if has_installer:
        content = f"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║          LRU TRACKER v{VERSION} - INSTALLATION GUIDE          ║
║                                                              ║
╔══════════════════════════════════════════════════════════════╗

Thank you for downloading LRU Tracker!

┌──────────────────────────────────────────────────────────────┐
│  QUICK INSTALL (RECOMMENDED)                                 │
└──────────────────────────────────────────────────────────────┘

1. ✅ Double-click "LRU_Tracker_Setup.exe"
2. ✅ Follow the installation wizard
3. ✅ Choose if you want a desktop shortcut
4. ✅ Click Install
5. ✅ Launch the app from Start Menu or desktop!

That's it! The installer handles everything automatically.


┌──────────────────────────────────────────────────────────────┐
│  GETTING STARTED                                             │
└──────────────────────────────────────────────────────────────┘

After installation:

1. 📊 Add Your Stations
   - Click "Add New Station"
   - Enter station name, min, and max LRU counts
   - Click Save

2. 📝 Update LRU Counts
   - Select a station from the list
   - Enter the current LRU count
   - Click "Update LRU Count"
   - Status will update automatically (Green/Yellow/Red)

3. 📁 Export Data
   - Click "Export to Excel" for reports
   - Use "Download Template" for bulk station imports

4. 📈 View Trends
   - Select a station
   - Click "Show Trend Analysis"
   - See historical usage patterns


┌──────────────────────────────────────────────────────────────┐
│  DOCUMENTATION                                               │
└──────────────────────────────────────────────────────────────┘

Check the "Documentation" folder for detailed guides:

📄 QUICK_START.md
   - Complete feature overview
   - Step-by-step tutorials

📄 FC_SCHEDULE_IMPORT_GUIDE.md
   - Import stations from FC Standard Work Spreadsheet

📄 TEMPLATE_FEATURE_GUIDE.md
   - Create and use station templates


┌──────────────────────────────────────────────────────────────┐
│  SYSTEM REQUIREMENTS                                         │
└──────────────────────────────────────────────────────────────┘

✓ Windows 10 or later
✓ ~45 MB disk space
✓ No additional software needed


┌──────────────────────────────────────────────────────────────┐
│  AUTOMATIC UPDATES                                           │
└──────────────────────────────────────────────────────────────┘

The app includes automatic update checking:
- Click "🔄 Check for Updates" button in the app
- Get notified when new versions are available
- Download and install updates with one click
- Your data is automatically preserved!


┌──────────────────────────────────────────────────────────────┐
│  NEED HELP?                                                  │
└──────────────────────────────────────────────────────────────┘

📧 Report issues or request features:
   https://github.com/HaltTheGrey/lru-tracker/issues

📖 View online documentation:
   https://github.com/HaltTheGrey/lru-tracker


┌──────────────────────────────────────────────────────────────┐
│  DATA LOCATION                                               │
└──────────────────────────────────────────────────────────────┘

Your station data is saved automatically to:
C:\\Users\\[YourUsername]\\AppData\\Local\\LRU_Tracker\\lru_data.json

This file is preserved during updates and uninstalls!


════════════════════════════════════════════════════════════════

Made with ❤️ for FC teams
Version {VERSION} | © 2026

════════════════════════════════════════════════════════════════
"""
    else:
        content = f"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║          LRU TRACKER v{VERSION} - INSTALLATION GUIDE          ║
║                                                              ║
╔══════════════════════════════════════════════════════════════╗

⚠️  INSTALLER NOT FOUND

This package doesn't include the installer executable yet.

To get the full installer:
1. Download LRU_Tracker_Setup.exe from the latest release
2. Or build it yourself using the instructions in the repository


════════════════════════════════════════════════════════════════

View the repository for complete installation options:
https://github.com/HaltTheGrey/lru-tracker

════════════════════════════════════════════════════════════════
"""
    
    with open(instructions_path, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    
    print(f"  ✓ START_HERE.txt")

if __name__ == '__main__':
    create_release_package()
