# 🔧 LRU Tracker v1.2.1 - Critical Permission Error Fix

**Release Date:** February 6, 2026  
**Release Type:** Bug Fix (Patch)  
**Priority:** HIGH - Immediate update recommended

---

## 🚨 Critical Bug Fix

This release fixes a critical bug that prevented users from running the application when installed in write-protected folders (such as Program Files).

### What Was Fixed

**PermissionError: [WinError 5] Access is denied: 'logs'**

Users experienced immediate crashes when trying to launch the application from restricted directories. This has been completely resolved.

---

## ✨ What's New in v1.2.1

### 🐛 Bug Fixes

- **Fixed PermissionError when creating log files** - Application now works from ANY location
- **Added intelligent directory fallback system** - Automatically finds writable locations
- **Improved error handling** - App never crashes due to file system permissions
- **Enhanced logging reliability** - Multiple fallback locations ensure logs are always accessible

### 🔧 Technical Improvements

The logger now tries multiple writable locations in this order:

1. `logs/` in current directory (preferred for portable usage)
2. `%LOCALAPPDATA%\LRU_Tracker\logs\` (Windows user data folder)
3. `~/.lru_tracker/logs/` (Unix-style hidden folder)
4. `%TEMP%\lru_tracker_logs\` (System temporary folder)
5. Console-only logging (if all above fail)

Each location is tested for write permissions before use. The app gracefully degrades and **never crashes** regardless of where it's installed.

---

## 📥 Installation

### New Users

1. Download `LRU_Tracker_Setup.exe` from the Assets below
2. Run the installer
3. Launch the application from the Start Menu or Desktop shortcut
4. Your app will automatically use the best available log location

### Existing Users - UPGRADE

1. Download `LRU_Tracker_Setup.exe` from the Assets below
2. Close any running instances of LRU Tracker
3. Run the new installer (it will upgrade your existing installation)
4. **Your data is automatically preserved** - all stations and history remain intact
5. Launch the upgraded version

**Note:** You can now run the app from Program Files or any restricted folder without issues!

---

## 🎨 Features from v1.2.0 (Still Included)

### Enhanced Excel Export Styling

- **Professional color scheme** with corporate blue headers
- **Title row with timestamp** for better record keeping
- **Alternating row colors** for improved readability
- **Enhanced status indicators:**
  - 🔴 Red: Below minimum threshold
  - 🟠 Orange: At maximum capacity
  - 🟢 Green: Normal operating range
- **Frozen header panes** for easier navigation of large datasets
- **Auto-sized columns** for optimal viewing

### Core Features

- ✅ Track LRU (Least Replenishable Unit) counts across multiple stations
- ✅ Real-time status monitoring with color-coded alerts
- ✅ Global history tracking with timestamps and user attribution
- ✅ Professional Excel exports with formatting
- ✅ CSV template imports for batch station setup
- ✅ FC (Fulfillment Center) schedule management
- ✅ Automatic update notifications
- ✅ Comprehensive error handling and logging

---

## 🔧 System Requirements

- **Operating System:** Windows 10 or later (64-bit)
- **Disk Space:** ~45 MB
- **RAM:** 100 MB minimum
- **Internet:** Optional (for update checks and documentation links)
- **Permissions:** No administrator rights required (runs as standard user)

---

## 📝 Known Issues

None at this time. Please report any issues on the [GitHub Issues](https://github.com/HaltTheGrey/lru-tracker/issues) page.

---

## 🆘 Troubleshooting

### "Where are my logs now?"

Check these locations in order:

1. `logs/` folder next to the executable (if writable)
2. `C:\Users\[YourUsername]\AppData\Local\LRU_Tracker\logs\`
3. Check the console window for a startup message indicating log location

### "I don't see an update notification"

If you're running v1.2.0 or earlier:

1. Click "🔄 Check for Updates" in the app
2. If still no update, check your internet connection
3. Manually download this release if update check fails

### "My data is missing after upgrade"

Your data should be automatically preserved. Check:

1. `lru_data.json` in the application folder
2. `lru_data.json.backup` as a fallback
3. If lost, contact support with your backup file

---

## 📊 Changelog

### v1.2.1 (February 6, 2026) - Current Release

**Fixed:**
- PermissionError when running from write-protected directories
- Application crashes on startup in restricted folders
- Log file creation in Program Files and similar locations

**Added:**
- Intelligent directory fallback system with 4 alternative locations
- Write permission testing before directory usage
- Graceful degradation to console-only logging
- Startup messages indicating log file location

**Technical:**
- Updated `logger.py` with `get_log_directory()` function
- Added type hints for better code safety
- Enhanced error handling throughout logging system
- Improved cross-platform compatibility

### v1.2.0 (Previous Release)

**Added:**
- Professional Excel styling with enhanced colors
- Title rows with timestamps
- Alternating row colors
- Enhanced status indicators
- Frozen header panes

### v1.1.0 and Earlier

See [full changelog](https://github.com/HaltTheGrey/lru-tracker/blob/main/docs/release-notes/README.md) for complete version history.

---

## 🔒 Security

This release includes:

- ✅ HTTPS-only update checks
- ✅ Version format validation
- ✅ JSON structure validation
- ✅ No automatic code execution
- ✅ User-controlled updates
- ✅ Safe file system operations with permission checking

---

## 📚 Documentation

- **User Guide:** [docs/user-guides/](https://github.com/HaltTheGrey/lru-tracker/tree/main/docs/user-guides)
- **Developer Guide:** [docs/developer-guides/](https://github.com/HaltTheGrey/lru-tracker/tree/main/docs/developer-guides)
- **Fix Details:** [PERMISSION_ERROR_FIX_v1.2.1.md](https://github.com/HaltTheGrey/lru-tracker/blob/main/docs/developer-guides/PERMISSION_ERROR_FIX_v1.2.1.md)
- **Quick Guide:** [PERMISSION_FIX_QUICK_GUIDE.md](https://github.com/HaltTheGrey/lru-tracker/blob/main/PERMISSION_FIX_QUICK_GUIDE.md)

---

## 💬 Support

- **Issues:** [GitHub Issues](https://github.com/HaltTheGrey/lru-tracker/issues)
- **Discussions:** [GitHub Discussions](https://github.com/HaltTheGrey/lru-tracker/discussions)
- **Email:** Contact repository owner for urgent issues

---

## 🙏 Acknowledgments

Special thanks to users who reported the permission error and helped test the fix!

---

## ⬇️ Download

**Main Download:**
- `LRU_Tracker_Setup.exe` - Windows Installer (Recommended)

**Alternative Downloads:**
- `LRU_Tracker.exe` - Portable version (no installation required)
- `Source code (zip)` - Full source code archive
- `Source code (tar.gz)` - Full source code archive

**Checksums:** See `checksums.txt` in Assets for SHA-256 verification

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/HaltTheGrey/lru-tracker/blob/main/LICENSE) file for details.

---

**Full Changelog:** https://github.com/HaltTheGrey/lru-tracker/compare/v1.2.0...v1.2.1
