# 🔄 How to Update Your LRU Tracker App

Complete guide for releasing updates to your users.

---

## 📋 Quick Update Checklist

When you want to release an update:

- [ ] Make your code changes
- [ ] Update the version number
- [ ] Test thoroughly
- [ ] Build new executable
- [ ] Create GitHub Release
- [ ] Update version.json
- [ ] Users get notified automatically! 🎉

---

## 🚀 Step-by-Step Update Process

### **Step 1: Make Your Code Changes**

Edit `lru_tracker.py` with your improvements:
- Bug fixes
- New features
- Performance improvements
- UI enhancements

### **Step 2: Update the Version Number**

Open `lru_tracker.py` and change line 16:

```python
# Before (current version)
APP_VERSION = "1.0.0"

# After (new version)
APP_VERSION = "1.1.0"  # or 1.0.1 for bug fixes
```

**Version Numbering Guide:**
- `1.0.0 → 1.0.1` - Bug fix (PATCH)
- `1.0.0 → 1.1.0` - New feature (MINOR)
- `1.0.0 → 2.0.0` - Major changes (MAJOR)

### **Step 3: Test Your Changes**

```powershell
# Run the app to test
python lru_tracker.py

# Test all features:
# - Add/edit/delete stations
# - Update LRU counts
# - Export to Excel
# - Import templates
# - Check for updates
```

### **Step 4: Commit to GitHub**

```powershell
# Add all changes
git add .

# Commit with descriptive message
git commit -m "Version 1.1.0: Added new features and bug fixes"

# Push to GitHub
git push
```

### **Step 5: Build New Executable**

#### Option A: With Inno Setup (Installer)

```powershell
# Navigate to distribution folder
cd distribution

# Build the executable
.\BUILD_WINDOWS_ONE_CLICK.bat

# Open Inno Setup Compiler
# File → Open → installer_script.iss
# Press F9 to compile
# Output: packages\LRU_Tracker_Setup.exe
```

#### Option B: ZIP Distribution Only

```powershell
# Navigate to distribution folder
cd distribution

# Build the executable
.\BUILD_WINDOWS_ONE_CLICK.bat

# Output: packages\LRU_Tracker_Windows.zip
```

### **Step 6: Create GitHub Release**

1. **Go to GitHub Releases:**
   ```
   https://github.com/HaltTheGrey/lru-tracker/releases/new
   ```

2. **Fill in release information:**

   **Tag:** `v1.1.0` (match your APP_VERSION)
   
   **Title:** `LRU Tracker v1.1.0 - [Brief Description]`
   
   **Description:**
   ```markdown
   ## 🎉 What's New in v1.1.0
   
   ### ✨ New Features
   - Added feature X
   - Improved feature Y
   - New export option Z
   
   ### 🐛 Bug Fixes
   - Fixed issue with station deletion
   - Resolved Excel export error
   - Corrected trend chart display
   
   ### 🔧 Improvements
   - Faster loading times
   - Better error messages
   - Updated security
   
   ---
   
   ## 📦 Installation
   
   **First-time users:**
   1. Download `LRU_Tracker_Setup.exe` below
   2. Run and follow installation wizard
   
   **Updating from v1.0.0:**
   1. Download `LRU_Tracker_Setup.exe`
   2. Run installer (your data is preserved!)
   3. Or click "Check for Updates" in the app
   
   ---
   
   ## 💾 Download
   
   👉 **LRU_Tracker_Setup.exe** (recommended)
   
   **Requirements:**
   - Windows 10 or later
   - ~45 MB disk space
   
   **Your data is safe!** All station data is automatically preserved during updates.
   ```

3. **Upload files:**
   - Drag and drop `LRU_Tracker_Setup.exe` (or ZIP file)
   - Wait for upload to complete

4. **Click "Publish release"** ✅

### **Step 7: Update version.json for Auto-Updates**

This is CRITICAL for auto-update notifications!

1. **Edit `version.json` in your repository:**

```json
{
  "version": "1.1.0",
  "download_url": "https://github.com/HaltTheGrey/lru-tracker/releases/download/v1.1.0/LRU_Tracker_Setup.exe",
  "release_notes": "🎉 What's New in v1.1.0\n\n✨ New Features:\n- Added feature X\n- Improved feature Y\n\n🐛 Bug Fixes:\n- Fixed issue Z",
  "size_mb": 45,
  "release_date": "2026-02-05T12:00:00",
  "minimum_version": "1.0.0"
}
```

**Important fields:**
- `version`: Must match your `APP_VERSION`
- `download_url`: Direct link to the installer in your release
- `release_notes`: What's new (users see this)
- `size_mb`: Approximate file size

2. **Commit and push version.json:**

```powershell
git add version.json
git commit -m "Update version.json for v1.1.0 release"
git push
```

### **Step 8: Notify Users! 🎉**

**Users with v1.0.0 will automatically get notified when they:**
- Click "🔄 Check for Updates" button
- (Optional) Add auto-check on startup

**They'll see:**
```
┌─────────────────────────────────────┐
│   🎉 Update Available!              │
├─────────────────────────────────────┤
│ Current Version: 1.0.0              │
│ Latest Version: 1.1.0               │
│                                      │
│ What's New:                         │
│ ✨ New Features:                    │
│ - Added feature X                   │
│ - Improved feature Y                │
│                                      │
│  [📥 Download Update]  [Later]      │
└─────────────────────────────────────┘
```

---

## 🎯 Complete Example: Releasing v1.1.0

Let's say you fixed a bug and added a new feature:

### **1. Update the code:**

```python
# lru_tracker.py - line 16
APP_VERSION = "1.1.0"  # Changed from "1.0.0"

# ... your bug fixes and new features ...
```

### **2. Commit changes:**

```powershell
git add .
git commit -m "Version 1.1.0: Fixed Excel export bug, added bulk delete feature"
git push
```

### **3. Build executable:**

```powershell
cd distribution
.\BUILD_WINDOWS_ONE_CLICK.bat
# Then compile with Inno Setup (F9)
```

### **4. Create GitHub Release:**

- Tag: `v1.1.0`
- Upload: `LRU_Tracker_Setup.exe`
- Write release notes (see template above)
- Publish!

### **5. Update version.json:**

```json
{
  "version": "1.1.0",
  "download_url": "https://github.com/HaltTheGrey/lru-tracker/releases/download/v1.1.0/LRU_Tracker_Setup.exe",
  "release_notes": "🎉 What's New\n\n✨ New: Bulk delete stations\n🐛 Fixed: Excel export crash",
  "size_mb": 45,
  "release_date": "2026-02-06T10:00:00"
}
```

```powershell
git add version.json
git commit -m "Update version.json for v1.1.0"
git push
```

### **6. Done! 🎉**

Users click "Check for Updates" → See your new version → Download → Install!

---

## 🔄 Update Frequency Best Practices

### **When to Release Updates:**

**Patch Updates (1.0.0 → 1.0.1):**
- Critical bug fixes
- Security patches
- Release ASAP

**Minor Updates (1.0.0 → 1.1.0):**
- New features
- Enhancements
- Release monthly or when ready

**Major Updates (1.0.0 → 2.0.0):**
- Breaking changes
- Complete redesigns
- Release yearly or as needed

### **Update Schedule Example:**

- **v1.0.0** - Initial release (February 5, 2026)
- **v1.0.1** - Bug fix (February 10, 2026) - Fixed critical Excel bug
- **v1.1.0** - New features (March 1, 2026) - Added bulk operations
- **v1.2.0** - More features (April 1, 2026) - Added reporting
- **v2.0.0** - Major update (June 1, 2026) - Complete UI redesign

---

## 📧 Announcing Updates to Users

### **Email Template:**

```
Subject: LRU Tracker v1.1.0 Update Available

Hi team,

A new version of LRU Tracker is available!

🎉 What's New in v1.1.0:
✨ New bulk delete feature
✨ Improved Excel export speed
🐛 Fixed station sorting issue
🔒 Enhanced security

📥 How to Update:

Option 1 (Automatic):
1. Open LRU Tracker
2. Click "🔄 Check for Updates"
3. Click "Download Update"
4. Run the installer

Option 2 (Manual):
1. Download from: https://github.com/HaltTheGrey/lru-tracker/releases/latest
2. Run LRU_Tracker_Setup.exe
3. Your data is preserved automatically!

Questions? Let me know!
```

---

## 🛡️ Data Preservation During Updates

**Good news:** User data is automatically preserved!

**How it works:**

1. **Data is stored separately:**
   ```
   C:\Users\[Username]\AppData\Local\LRU_Tracker\lru_data.json
   ```

2. **Installer doesn't touch data:**
   - Only replaces the .exe file
   - Leaves `lru_data.json` untouched

3. **Users keep all their:**
   - ✅ Stations
   - ✅ LRU counts
   - ✅ History
   - ✅ Settings

**Backup reminder for users:**
```
Before updating, your data is automatically safe!
But for extra safety, you can backup:
C:\Users\[YourName]\AppData\Local\LRU_Tracker\lru_data.json
```

---

## 🧪 Testing Updates Before Release

### **Test Checklist:**

Before publishing an update, test:

- [ ] Install fresh on clean machine
- [ ] Upgrade from previous version
- [ ] All features work correctly
- [ ] Data is preserved
- [ ] No crashes or errors
- [ ] Update notification works
- [ ] Download link is correct
- [ ] Installer runs without errors

### **Test on Different Environments:**

- [ ] Windows 10
- [ ] Windows 11
- [ ] Clean install (no previous version)
- [ ] Upgrade install (from v1.0.0)

---

## 📊 Tracking Update Adoption

### **See who downloaded:**

Check GitHub Release downloads:
```
https://github.com/HaltTheGrey/lru-tracker/releases
```

You'll see download count for each release!

### **Monitor issues:**

Check GitHub Issues for bug reports:
```
https://github.com/HaltTheGrey/lru-tracker/issues
```

---

## 🆘 Troubleshooting Updates

### **Problem: Users don't see update notification**

**Solution:**
1. Check `version.json` is uploaded to GitHub
2. Verify URL: `https://raw.githubusercontent.com/HaltTheGrey/lru-tracker/main/version.json`
3. Check version number matches release
4. Wait a few minutes for GitHub to update

### **Problem: Download link doesn't work**

**Solution:**
1. Check release is published (not draft)
2. Verify download URL in `version.json`
3. Format: `https://github.com/HaltTheGrey/lru-tracker/releases/download/v1.1.0/LRU_Tracker_Setup.exe`

### **Problem: Users report data lost**

**Solution:**
1. Data is at: `C:\Users\[Name]\AppData\Local\LRU_Tracker\lru_data.json`
2. Check if file exists
3. Look for backup: `lru_data.json.backup`
4. Restore from backup if needed

---

## ✅ Summary: Quick Update Steps

1. **Edit code** → Make changes
2. **Update version** → Change `APP_VERSION = "1.1.0"`
3. **Test** → Run `python lru_tracker.py`
4. **Commit** → `git commit -m "Version 1.1.0: ..."`
5. **Build** → `cd distribution; .\BUILD_WINDOWS_ONE_CLICK.bat`
6. **Compile** → Inno Setup → F9
7. **Release** → GitHub → Create release → Upload installer
8. **Update version.json** → Edit → Commit → Push
9. **Announce** → Email team
10. **Monitor** → Check downloads and issues

**Users get notified automatically!** 🎉

---

## 📚 Related Documentation

- **SETUP_GITHUB.md** - How to set up GitHub releases
- **HOW_USERS_DOWNLOAD.md** - User download experience
- **INSTALLER_AND_UPDATES_GUIDE.md** - Complete installer guide
- **SECURITY_ENHANCEMENTS.md** - Security best practices

---

**Ready to release your first update?** Follow the steps above! 🚀
