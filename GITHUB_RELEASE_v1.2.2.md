# 🚀 LRU Tracker v1.2.2 - Smart Incremental Updates & Professional Installer

## Major Release Highlights

### ⚡ Smart Incremental Updates (Revolutionary!)
This is the **first release** with our new **incremental update system**!

**What This Means For You:**
- 📥 Download only **0.1-5 MB** instead of **127 MB** for updates
- ⏱️ Updates complete in **10 seconds** instead of **5-10 minutes**
- 💾 Save **99%+ bandwidth** on every update
- 🔄 Automatic file-based patching with verification
- 🛡️ Automatic backup and rollback on failure

**How It Works:**
1. App checks GitHub for changed files
2. Downloads ONLY what's different
3. Verifies files with SHA256 hashes
4. Automatically replaces updated files
5. Restarts app - Done!

**This Update:**
- Files changed: 14
- Download size: **0.10 MB** (103 KB)
- Bandwidth saved: **126.9 MB (99.92%)**
- Time saved: **~5 minutes**

### 🎨 Professional Installer
Beautiful new installer with enhanced features:
- **Modern card-based UI** with scrollable content
- **Platform detection** (Windows/macOS/Linux ready)
- **Disk space indicator** with color coding
- **Auto-update toggle** - Enable/disable update checks
- **Launch after install** - Run app immediately
- **Help button** with troubleshooting guide
- **System requirements** card
- Resizable window (700x650)
- Clean, modern design with icons throughout

### 📥 One-Click Update Downloads
- Updates download directly to your Downloads folder
- No browser navigation needed
- Automatic folder opening with file selected
- Background download (UI stays responsive)
- Smart URL detection
- Progress indicators

## What's New in v1.2.2

### ✨ New Features
1. **Smart Incremental Updates**
   - File-level update system
   - SHA256 hash verification
   - Automatic backup before update
   - Rollback on failure
   - 99%+ bandwidth savings

2. **Professional Installer**
   - Beautiful GUI wizard
   - Platform detection
   - Disk space monitoring
   - Multiple shortcut options
   - Auto-update configuration
   - Launch after install option

3. **Enhanced Update Dialog**
   - Shows bandwidth savings
   - Displays file count
   - Progress indicators
   - Estimated time
   - Smart fallback options

### 🐛 Bug Fixes (from v1.2.1)
- ✅ Fixed PermissionError when running from restricted folders
- ✅ Application works in Program Files and protected locations
- ✅ Intelligent fallback to user-accessible directories
- ✅ Enhanced error handling for file system access

### 📝 Technical Improvements
- File-level incremental updates using SHA256 hashing
- Manifest-based update system (`update_manifest.json`)
- Dual-mode update checker (incremental + traditional fallback)
- Secure HTTPS downloads only
- Automatic version comparison
- Rollback capability with backup system
- Cross-platform installer code (Windows/macOS/Linux)

### ✨ Continued Features (from v1.2.0)
- Professional Excel styling with enhanced colors
- Title rows with timestamps
- Alternating row colors for readability
- Enhanced status indicators (Red/Orange/Green)
- Frozen header panes

## Installation

### New Installation
1. **Download:** `LRU_Tracker_Setup.exe` (141 MB)
2. **Run** the installer
3. Beautiful wizard guides you through:
   - Choose install location
   - Select Desktop/Start Menu shortcuts
   - Enable auto-updates (recommended)
   - Optional: Launch after install
4. **Done!** App is ready to use

### Updating From Previous Version
If you have v1.2.1 or earlier installed:

**Option 1: Smart Update (Recommended)**
1. Open LRU Tracker
2. Click `Help` → `Check for Updates`
3. You'll see: "🚀 Smart Update Available!"
4. Shows: "Download 0.1 MB instead of 127 MB (99.9% savings!)"
5. Click "⚡ Install Update"
6. Wait ~10 seconds
7. Restart when prompted
8. **Done!**

**Option 2: Fresh Install**
1. Download `LRU_Tracker_Setup.exe`
2. Run installer (your data is preserved)
3. Choose same install location
4. Future updates will be incremental!

## Download Options

### Main Release Files
- **LRU_Tracker_Setup.exe** (141 MB)
  - Professional installer with GUI wizard
  - Recommended for new installations
  - Creates shortcuts, adds to Programs & Features
  - Configurable auto-update
  
- **LRU_Tracker.exe** (127 MB) - *(If available)*
  - Standalone executable
  - No installation needed
  - Portable version

### Update Files (For v1.2.1+ Users)
- **update_manifest.json**
  - Used by smart incremental update system
  - Downloaded automatically by the app
  - Don't download manually

## System Requirements

### Minimum Requirements
- **OS:** Windows 10 or later (64-bit)
  - macOS 10.14+ (support coming soon)
  - Linux (support coming soon)
- **Disk Space:** 200 MB free
  - Installation: ~145 MB
  - Updates: Only 0.1-5 MB per update
- **RAM:** 512 MB
- **Internet:** Required for updates

### Recommended
- Windows 11
- 1 GB free disk space
- Broadband internet (though updates are tiny now!)
- Screen resolution: 1920x1080 or higher

## What's Special About This Release

### 🎯 First Smart Update System
This is the **first version** with incremental updates. Once you install v1.2.2:
- ✅ All future updates are 99% smaller
- ✅ Updates complete in seconds
- ✅ No more waiting for large downloads
- ✅ Automatic file replacement
- ✅ Secure with verification

### 📊 Performance Comparison

| Update Method | Download Size | Time | Bandwidth | User Steps |
|---------------|---------------|------|-----------|------------|
| **Traditional** (v1.2.1 and earlier) | 127 MB | 5-10 min | 127 MB | 8 steps |
| **Incremental** (v1.2.2+) | 0.1-5 MB | 10-30 sec | 0.1-5 MB | 3 steps |
| **Improvement** | **99%+** | **95%+** | **99%+** | **62%** |

### 🌟 Why This Matters
- **Metered connections:** No more blowing through your data cap
- **Slow internet:** Updates finish before your coffee cools
- **Reliability:** Smaller downloads = less chance of failure
- **Convenience:** One click, wait 10 seconds, done
- **Bandwidth:** Server costs reduced, faster downloads

## Known Issues & Limitations

### Current Limitations
- **macOS/Linux:** Installer code is ready but not built yet
  - Windows installer only for now
  - macOS/Linux: Use source code or wait for future release
  
- **First Install:** Still requires 141 MB download
  - Subsequent updates are tiny (0.1-5 MB)
  
- **Unsigned Installer:** May trigger SmartScreen warning
  - Click "More info" → "Run anyway"
  - This is normal for unsigned applications

### Workarounds
- **SmartScreen Warning:**
  1. Click "More info"
  2. Click "Run anyway"
  3. This is safe - code is on GitHub for transparency
  
- **macOS/Linux Users:**
  - Clone repository
  - Run from source with Python 3.13
  - Or wait for platform-specific builds

## Upgrade Path

### From v1.2.1 → v1.2.2
- ✅ **Recommended:** Use in-app smart update
- ✅ Downloads only 0.1 MB
- ✅ Takes 10 seconds
- ✅ Data preserved automatically

### From v1.2.0 or earlier → v1.2.2
- ✅ Use fresh installer (141 MB one-time)
- ✅ Run installer over existing installation
- ✅ Data migrates automatically
- ✅ Future updates are incremental!

### From v1.0.x → v1.2.2
- ⚠️ **Recommended:** Fresh install
- Major improvements since v1.0
- Data compatibility maintained
- Consider exporting data first (optional)

## Documentation

### New Documentation Files
- `INCREMENTAL_UPDATE_GUIDE.md` - How incremental updates work
- `INCREMENTAL_UPDATE_INTEGRATED.md` - Integration details
- `INSTALLER_IMPROVEMENTS_v1.2.2.md` - Installer enhancements
- `tools/generate_update_manifest.py` - Manifest generator tool

### Updated Files
- `README.md` - Installation and usage guide
- `version.json` - Version metadata with incremental update info
- `update_manifest.json` - File hashes and download URLs

## Support & Feedback

### Getting Help
- **Issues:** [GitHub Issues](https://github.com/HaltTheGrey/lru-tracker/issues)
- **Discussions:** [GitHub Discussions](https://github.com/HaltTheGrey/lru-tracker/discussions)
- **Documentation:** Check README.md and guide files

### Reporting Bugs
Please include:
1. Version number (Help → About)
2. Operating System
3. Steps to reproduce
4. Expected vs actual behavior
5. Any error messages

### Feature Requests
We love hearing your ideas! Open an issue with:
1. Description of the feature
2. Use case / why it's useful
3. Suggested implementation (optional)

## Credits & Thanks

### Special Thanks
- To all users who reported the permission error in v1.2.1
- Beta testers who validated the incremental update system
- Community feedback on installer UX

### Technical Stack
- **Language:** Python 3.13
- **UI:** Tkinter
- **Installer:** PyInstaller + Custom Python Installer
- **Updates:** Custom incremental update system
- **Excel:** openpyxl
- **Hosting:** GitHub (code + releases + CDN)

## What's Next

### Planned for v1.2.3
- macOS installer build
- Linux installer build
- Additional installer themes
- Binary patching (even smaller updates)
- Background update downloads

### Long-term Roadmap
- Multi-language support
- Cloud sync for data
- Mobile companion app
- Advanced analytics dashboard
- Team collaboration features

## Changelog Summary

```
v1.2.2 (2026-02-06)
  ✨ NEW: Smart incremental update system (99% bandwidth savings)
  ✨ NEW: Professional installer with modern UI
  ✨ NEW: Auto-update toggle in installer
  ✨ NEW: Launch after install option
  ✨ NEW: Disk space indicator
  ✨ NEW: Platform detection (Windows/macOS/Linux ready)
  🐛 FIX: Permission errors in restricted folders
  🐛 FIX: Program Files installation issues
  📝 IMPROVE: Cross-platform installer code
  📝 IMPROVE: Update dialog with savings display
  📝 IMPROVE: Automatic backup and rollback
  📝 IMPROVE: SHA256 file verification

v1.2.1 (2026-02-05)
  🐛 FIX: Permission fix for file operations
  📝 IMPROVE: Error handling

v1.2.0 (2026-02-04)
  ✨ NEW: Professional Excel styling
  ✨ NEW: Enhanced export features
```

## Download Now

**[⬇️ Download LRU_Tracker_Setup.exe](https://github.com/HaltTheGrey/lru-tracker/releases/download/v1.2.2/LRU_Tracker_Setup.exe)** (141 MB)

**After this one-time download, all future updates are only 0.1-5 MB!** 🚀

---

**Full Changelog:** [CHANGELOG.md](https://github.com/HaltTheGrey/lru-tracker/blob/main/CHANGELOG.md)  
**Source Code:** [GitHub Repository](https://github.com/HaltTheGrey/lru-tracker)  
**Issues:** [Report a Bug](https://github.com/HaltTheGrey/lru-tracker/issues/new)

**Version:** 1.2.2  
**Release Date:** February 6, 2026  
**License:** MIT  
**Platform:** Windows 10+ (macOS/Linux coming soon)
