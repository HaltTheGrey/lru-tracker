# 📦 GitHub Release Guide - For Users

This guide explains how to create GitHub releases that users can easily download and install.

## 🎯 What Users Need

Users **DO NOT** need:
- ❌ Source code
- ❌ Build scripts
- ❌ Development files
- ❌ Git repository

Users **ONLY** need:
- ✅ The installer executable (`LRU_Tracker_Setup.exe`)
- ✅ Quick start documentation
- ✅ Installation instructions

## 🚀 Creating a User-Friendly Release

### Option 1: Single Installer File (RECOMMENDED)

**This is the simplest for users!**

1. **Build the installer:**
   ```powershell
   cd distribution
   .\BUILD_WINDOWS_ONE_CLICK.bat
   # Then compile with Inno Setup (F9)
   ```

2. **Create GitHub Release:**
   - Go to: https://github.com/HaltTheGrey/lru-tracker/releases/new
   - Tag: `v1.0.0`
   - Title: `LRU Tracker v1.0.0`
   - Description:
     ```markdown
     ## 🎉 LRU Tracker v1.0.0

     Professional LRU tracking app for FC stations with min/max pull system.

     ### 📦 Installation (Easy - 2 Steps)
     1. Download `LRU_Tracker_Setup.exe` below
     2. Run it and follow the wizard

     ### ✨ Features
     - Min/Max pull system with color indicators
     - Station management
     - LRU tracking with history
     - Excel export & trend analysis
     - Template import/export
     - FC Schedule CSV import
     - Auto-update notifications

     ### 💡 Quick Start
     1. Install and launch the app
     2. Add stations with min/max values
     3. Update LRU counts
     4. Export to Excel when needed

     ### 🔧 Requirements
     - Windows 10 or later
     - ~45 MB disk space

     ### 📖 Documentation
     See [Quick Start Guide](https://github.com/HaltTheGrey/lru-tracker#quick-start) for details.
     ```

3. **Upload files:**
   - Attach: `distribution\packages\LRU_Tracker_Setup.exe`
   
4. **Publish!**

**Users download:** Just one file (`LRU_Tracker_Setup.exe`) - super simple! ✅

---

### Option 2: Package with Documentation

**If you want to include guides:**

1. **Create release package:**
   ```powershell
   cd distribution
   .\CREATE_RELEASE.bat
   ```
   
   This creates: `LRU_Tracker_v1.0.0_Release.zip` with:
   ```
   LRU_Tracker_v1.0.0_Release.zip
   ├── LRU_Tracker_Setup.exe          # The installer
   ├── START_HERE.txt                  # Installation guide
   └── Documentation/
       ├── QUICK_START.md
       ├── FC_SCHEDULE_IMPORT_GUIDE.md
       └── TEMPLATE_FEATURE_GUIDE.md
   ```

2. **Create GitHub Release:**
   - Same as Option 1, but upload the ZIP file instead

3. **Users download:** One ZIP file, extract, run installer ✅

---

## 📤 Release Checklist

Before creating a release:

- [ ] Update `APP_VERSION` in `lru_tracker.py`
- [ ] Build executable with `BUILD_WINDOWS_ONE_CLICK.bat`
- [ ] Compile installer with Inno Setup (F9)
- [ ] Test installer on clean machine
- [ ] Update `version.json` with new version info
- [ ] Commit changes to Git
- [ ] Create GitHub release with installer
- [ ] Test download link
- [ ] Announce to users!

---

## 🔄 Updating version.json for Auto-Updates

After creating the release, update `version.json`:

```json
{
  "version": "1.0.0",
  "download_url": "https://github.com/HaltTheGrey/lru-tracker/releases/download/v1.0.0/LRU_Tracker_Setup.exe",
  "release_notes": "🎉 Initial Release\n\n✨ Features:\n- Min/Max pull system\n- Station management\n- Excel export\n- Trend analysis\n- Auto-updates",
  "size_mb": 45,
  "release_date": "2026-02-05T12:00:00"
}
```

Then commit and push:
```powershell
git add version.json
git commit -m "Update version.json for v1.0.0"
git push
```

---

## 👥 What Users See

### GitHub Releases Page:
```
Releases

v1.0.0 - LRU Tracker v1.0.0
Latest   Feb 5, 2026

📦 Assets
  LRU_Tracker_Setup.exe    (45.2 MB)   [Download]
  
[Release notes displayed here]
```

### User Experience:
1. Click "Download" on `LRU_Tracker_Setup.exe`
2. Run the downloaded file
3. Follow installation wizard
4. Start using the app!

**That's it - no technical knowledge needed!** ✅

---

## 🎯 Best Practices

### ✅ DO:
- Keep releases simple (one installer file is best)
- Write clear, non-technical installation instructions
- Include screenshots in release description
- Test on a clean machine before releasing
- Keep installer filename consistent
- Use semantic versioning (1.0.0, 1.1.0, 2.0.0)

### ❌ DON'T:
- Include source code in release assets (it's automatic anyway)
- Upload build scripts or development files
- Make users unzip multiple files
- Assume users know Git or command line
- Forget to update version.json

---

## 📊 Release Assets Strategy

**For each release, upload ONLY:**

1. **Required:**
   - `LRU_Tracker_Setup.exe` - The installer

2. **Optional:**
   - `LRU_Tracker_v1.0.0_Release.zip` - Installer + docs (if you want)

**GitHub automatically includes:**
- Source code (zip)
- Source code (tar.gz)

**Users can ignore the source code downloads** - they're for developers only!

---

## 🔗 Share with Your Team

**Direct download link format:**
```
https://github.com/HaltTheGrey/lru-tracker/releases/latest/download/LRU_Tracker_Setup.exe
```

This always points to the latest version!

**Or share the releases page:**
```
https://github.com/HaltTheGrey/lru-tracker/releases/latest
```

---

## 📝 Sample Release Notes Template

```markdown
## 🎉 LRU Tracker v1.0.0

### 📦 Installation
1. Download `LRU_Tracker_Setup.exe` below
2. Run and follow the installation wizard
3. That's it!

### ✨ What's New
- Feature 1 description
- Feature 2 description
- Bug fix descriptions

### 🔧 Requirements
- Windows 10 or later
- ~45 MB disk space

### 💡 Quick Start
1. Launch the app
2. Add your FC stations
3. Start tracking LRUs!

### 📖 Documentation
- [Quick Start Guide](link)
- [User Manual](link)
- [Video Tutorial](link) (optional)

### 🐛 Known Issues
- List any known issues (if applicable)

### 🆘 Support
Report issues: [GitHub Issues](https://github.com/HaltTheGrey/lru-tracker/issues)
```

---

## 🎊 Summary

**For the simplest user experience:**

1. Build installer with Inno Setup
2. Create GitHub release
3. Upload ONLY `LRU_Tracker_Setup.exe`
4. Write clear installation steps
5. Share the release link with users

**Users download one file and run it. Done!** 🚀

No Git, no building, no technical knowledge required!
