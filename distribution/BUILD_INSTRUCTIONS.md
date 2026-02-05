# LRU Tracker - Build Instructions

This guide explains how to create executable installers for Windows and macOS.

## Overview

The distribution folder contains build scripts that package the LRU Tracker application into standalone executables that don't require Python to be installed.

## Requirements

### For Windows Build:
- Windows 10 or later
- Python 3.7+ installed
- Internet connection (for downloading PyInstaller if needed)

### For macOS Build:
- macOS 10.13 (High Sierra) or later
- Python 3.7+ installed
- Xcode Command Line Tools (install with: `xcode-select --install`)
- Internet connection (for downloading PyInstaller if needed)

## Building on Windows

1. **Open PowerShell or Command Prompt**
   ```
   cd C:\Users\jessneug\Leetcode\templeteforpartwalks\distribution
   ```

2. **Run the build script**
   ```
   build_windows.bat
   ```

3. **What happens:**
   - PyInstaller is installed (if not already present)
   - The Python script is converted to a standalone .exe
   - All dependencies are bundled
   - Documentation files are copied
   - A zip package is created: `LRU_Tracker_Windows.zip`

4. **Output location:**
   ```
   distribution\LRU_Tracker_Windows.zip
   ```

5. **Distribution:**
   - Share `LRU_Tracker_Windows.zip` with Windows users
   - They extract and run `LRU_Tracker.exe` (no Python needed!)

## Building on macOS

1. **Open Terminal**
   ```bash
   cd ~/path/to/templeteforpartwalks/distribution
   ```

2. **Make the script executable**
   ```bash
   chmod +x build_mac.sh
   ```

3. **Run the build script**
   ```bash
   ./build_mac.sh
   ```

4. **What happens:**
   - PyInstaller is installed (if not already present)
   - The Python script is converted to a .app bundle
   - All dependencies are bundled
   - Documentation files are copied
   - A zip package is created: `LRU_Tracker_Mac.zip`

5. **Output location:**
   ```
   distribution/LRU_Tracker_Mac.zip
   ```

6. **Distribution:**
   - Share `LRU_Tracker_Mac.zip` with Mac users
   - They extract and run `LRU_Tracker.app` (no Python needed!)

## Cross-Platform Building

**Important:** You cannot build macOS apps on Windows or Windows apps on macOS.

- To create both packages, you need access to both systems
- Build the Windows version on a Windows machine
- Build the macOS version on a Mac

## Package Contents

### Windows Package (LRU_Tracker_Windows.zip):
```
LRU_Tracker/
├── LRU_Tracker.exe           # Main application
├── README.md
├── QUICK_START.md
├── FC_SCHEDULE_IMPORT_GUIDE.md
├── TEMPLATE_GUIDE.md
├── requirements.txt
└── INSTALL_INSTRUCTIONS.txt  # Installation guide
```

### macOS Package (LRU_Tracker_Mac.zip):
```
LRU_Tracker/
├── LRU_Tracker.app           # Main application bundle
├── README.md
├── QUICK_START.md
├── FC_SCHEDULE_IMPORT_GUIDE.md
├── TEMPLATE_GUIDE.md
├── requirements.txt
└── INSTALL_INSTRUCTIONS.txt  # Installation guide
```

## File Sizes

- Windows executable: ~30-50 MB (includes Python runtime and all libraries)
- macOS application: ~35-55 MB (includes Python runtime and all libraries)

## Troubleshooting Build Issues

### Windows Issues:

**"PyInstaller not found"**
```
pip install pyinstaller
```

**"Module not found" errors**
```
pip install -r ..\requirements.txt
```

**Build fails with permission error**
- Run Command Prompt as Administrator
- Disable antivirus temporarily (it may block PyInstaller)

### macOS Issues:

**"Permission denied"**
```bash
chmod +x build_mac.sh
```

**"PyInstaller not found"**
```bash
pip3 install pyinstaller
```

**"Module not found" errors**
```bash
pip3 install -r ../requirements.txt
```

**"No module named 'tkinter'"**
```bash
# On macOS, you may need to install Python with tkinter support
brew install python-tk@3.13
```

## Testing the Build

### Before Distribution:

1. **Test on a clean machine** (one without Python installed)
2. **Check all features:**
   - Add/Edit/Delete stations
   - Update LRU counts
   - Export to Excel
   - Import templates
   - Import FC schedules
   - View trends (charts)
   - Export FC schedule format

3. **Verify data persistence:**
   - Close and reopen the app
   - Check that data is saved in `lru_data.json`

## Updating the Application

When you make changes to `lru_tracker.py`:

1. Update the version number in the code (if you have one)
2. Re-run the build script
3. Test the new build
4. Distribute the updated package

Users can simply:
1. Download the new version
2. Extract it
3. Their `lru_data.json` file will be preserved (as long as they keep it in the same folder)

## Code Signing (Optional - for Production)

For professional distribution:

### Windows:
- Get a code signing certificate
- Sign the .exe with `signtool`
- This prevents Windows SmartScreen warnings

### macOS:
- Enroll in Apple Developer Program ($99/year)
- Get a Developer ID certificate
- Sign the app with `codesign`
- Notarize with Apple
- This prevents Gatekeeper warnings

**Note:** Code signing is not required for internal/personal use.

## Advanced Options

### Customizing the Icon:

1. Create an icon file:
   - Windows: `icon.ico` (256x256 recommended)
   - macOS: `icon.icns` (1024x1024 recommended)

2. Modify the build script:
   ```
   --icon=path/to/icon.ico
   ```

### Single-File vs Single-Folder:

Current build uses `--onefile` (single executable).

For faster startup, use `--onedir`:
- Removes `--onefile` from build script
- Creates a folder with executable + libraries
- App starts faster but has more files

### Adding More Files:

To include additional files (images, configs, etc.):
```
--add-data "source_path;destination_path"  # Windows
--add-data "source_path:destination_path"  # macOS
```

## Distribution Checklist

Before sharing the packages:

- [ ] Test on Windows (if built)
- [ ] Test on macOS (if built)
- [ ] Verify all features work
- [ ] Check documentation is included
- [ ] Test on machine without Python
- [ ] Verify file size is reasonable
- [ ] Create release notes if needed
- [ ] Upload to distribution platform (if applicable)

## Support

For build issues, check:
1. PyInstaller documentation: https://pyinstaller.org/
2. Python version compatibility
3. All dependencies are installed
4. Antivirus is not blocking the build

---

**Ready to distribute!** After building, share the appropriate zip file with your users based on their operating system.
