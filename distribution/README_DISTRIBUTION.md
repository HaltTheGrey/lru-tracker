# LRU Tracker - Distribution Package

Welcome to the LRU Tracker distribution folder! This folder contains everything needed to create standalone executable installers for Windows and macOS.

## 📦 What's in this folder?

```
distribution/
├── build_windows.bat          # Windows build script
├── build_mac.sh              # macOS build script  
├── INSTALL_WINDOWS.txt       # Windows installation guide
├── INSTALL_MAC.txt           # macOS installation guide
├── BUILD_INSTRUCTIONS.md     # How to build the executables
└── README_DISTRIBUTION.md    # This file
```

## 🚀 Quick Start

### Building for Windows:
1. Open Command Prompt in this folder
2. Run: `build_windows.bat`
3. Share `LRU_Tracker_Windows.zip` with users

### Building for macOS:
1. Open Terminal in this folder
2. Run: `chmod +x build_mac.sh && ./build_mac.sh`
3. Share `LRU_Tracker_Mac.zip` with users

## 📥 For End Users

If you're an end user who received a zip file:

### Windows Users:
1. Extract `LRU_Tracker_Windows.zip`
2. Double-click `LRU_Tracker.exe`
3. See `INSTALL_INSTRUCTIONS.txt` for details

### Mac Users:
1. Extract `LRU_Tracker_Mac.zip`
2. Move `LRU_Tracker.app` to Applications
3. Right-click → Open (first time only)
4. See `INSTALL_INSTRUCTIONS.txt` for details

## ✨ Features

The LRU Tracker application includes:

- **Pull System Tracking** - Min/Max threshold monitoring
- **Color-Coded Status** - Red (under min), Yellow (at/over max), Green (normal)
- **Excel Reports** - Export current status and historical trends
- **FC Schedule Import** - Bulk import from FC Standard Work Spreadsheet
- **FC Schedule Export** - Export with time-slot tracking (6AM-12AM)
- **Trend Analysis** - Visualize LRU patterns with charts
- **Template System** - Download/import station templates
- **Click-to-Update** - Select station from list to quickly update counts
- **Auto-Save** - All data saved automatically

## 🛠️ For Developers

See `BUILD_INSTRUCTIONS.md` for detailed build process.

**Requirements:**
- Python 3.7+
- PyInstaller (installed automatically by build scripts)
- openpyxl, pandas, matplotlib (installed from requirements.txt)

## 📊 How It Works

The build scripts use PyInstaller to:
1. Bundle Python runtime with the application
2. Include all required libraries (tkinter, openpyxl, pandas, matplotlib)
3. Package documentation files
4. Create a standalone executable

**Result:** Users don't need Python installed!

## 🔒 Security Note

The executables are not code-signed. Users may see security warnings:

**Windows:** SmartScreen warning → Click "More info" → "Run anyway"  
**macOS:** Gatekeeper warning → System Preferences → Security → "Open Anyway"

For production use, consider getting a code signing certificate.

## 📏 Package Sizes

- Windows: ~30-50 MB (includes Python 3.13 runtime)
- macOS: ~35-55 MB (includes Python 3.13 runtime)

## 🆕 Version Information

**Current Version:** 1.0.0  
**Build Date:** February 2026  
**Python Version:** 3.13  

**Recent Features:**
- Click-to-select station for quick updates
- FC Schedule format export with time tracking
- Optimized scrollable UI layout

## 📝 License

Internal use for FC operations. All rights reserved.

## 🐛 Bug Reports

For issues with the application:
1. Check the documentation files
2. Verify system requirements
3. Try re-installing from a fresh extract

For build issues:
- See `BUILD_INSTRUCTIONS.md`
- Check PyInstaller documentation

## 🎯 Distribution Strategy

### For Internal FC Use:
1. Build on Windows machine → Get Windows package
2. Build on Mac machine → Get macOS package
3. Upload both to shared drive
4. Users download for their platform

### For GitHub/Cloud Distribution:
1. Create releases for each platform
2. Include installation instructions
3. Tag with version numbers
4. Update changelog

## 📞 Support

Refer to documentation files included in the package:
- `README.md` - Full application guide
- `QUICK_START.md` - Getting started
- `FC_SCHEDULE_IMPORT_GUIDE.md` - FC CSV import help
- `TEMPLATE_GUIDE.md` - Template feature guide

## ✅ Pre-Distribution Checklist

Before sharing with users:

- [ ] Built and tested on target platform
- [ ] All features work without Python installed
- [ ] Documentation files are included
- [ ] Installation instructions are clear
- [ ] File size is reasonable
- [ ] Security warnings are documented

---

**Ready to distribute!** Build the packages and share with your team.

For detailed build instructions, see `BUILD_INSTRUCTIONS.md`
