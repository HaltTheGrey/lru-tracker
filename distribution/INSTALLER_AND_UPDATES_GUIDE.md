# 📦 GUI INSTALLER & AUTO-UPDATE SYSTEM

Complete guide for creating professional installers and implementing updates.

## 🎨 GUI Installer (Windows)

### What You Get:
- **Professional installer wizard** with custom branding
- **Desktop shortcut option** during installation
- **Start menu entries** automatically created
- **Uninstaller** with data preservation option
- **Custom icon** throughout the installation
- **License agreement** (optional)
- **Choose installation location**

### Requirements:

**Inno Setup** (Free Windows installer creator)
- Download from: https://jrsoftware.org/isinfo.php
- Install Inno Setup 6.x or later

### How to Create the GUI Installer:

#### Step 1: Build Your EXE
```cmd
cd distribution
BUILD_WINDOWS_ONE_CLICK.bat
```

This creates: `dist\LRU_Tracker.exe`

#### Step 2: Install Inno Setup
1. Download Inno Setup from https://jrsoftware.org/isdl.php
2. Install with default options
3. Inno Setup Compiler will be installed

#### Step 3: Compile the Installer
1. Open Inno Setup Compiler
2. File → Open → Select `distribution\installer_script.iss`
3. Build → Compile (or press Ctrl+F9)
4. Wait 10-30 seconds

#### Step 4: Get Your Installer
Find the installer at:
```
distribution\packages\LRU_Tracker_Setup.exe
```

#### Step 5: Distribute!
- Share `LRU_Tracker_Setup.exe` with users
- Much more professional than a zip file!
- Users double-click and follow the wizard

### Installer Features:

**During Installation:**
- ✅ Welcome screen with app name and version
- ✅ Choose installation directory (default: C:\Program Files\LRU Tracker)
- ✅ Optional desktop shortcut
- ✅ Progress bar showing installation
- ✅ Launch app immediately after install (optional)

**After Installation:**
- ✅ App appears in Start Menu
- ✅ Uninstaller added to Windows Programs & Features
- ✅ Desktop shortcut (if selected)
- ✅ Data saved separately (preserved during updates)

**During Uninstall:**
- ✅ Asks if user wants to keep their data
- ✅ Clean removal of program files
- ✅ Data preserved if user chooses

---

## 🔄 Auto-Update System

### How It Works:

1. **Version Check**: App contacts server to check for updates
2. **Comparison**: Compares latest version with current version
3. **Notification**: Shows beautiful dialog if update available
4. **Download**: Opens browser to download new installer
5. **Install**: User runs new installer (preserves data automatically)

### Setup Auto-Updates:

#### Option 1: GitHub Releases (Free & Easy)

1. **Create a GitHub Repository**
   ```
   https://github.com/YOUR_USERNAME/lru-tracker
   ```

2. **Upload version.json to your repo**
   Create `version.json` file:
   ```json
   {
     "version": "1.1.0",
     "download_url": "https://github.com/YOUR_USERNAME/lru-tracker/releases/download/v1.1.0/LRU_Tracker_Setup.exe",
     "release_notes": "✨ New Features:\n- Added feature X\n- Improved feature Y\n\n🐛 Bug Fixes:\n- Fixed issue Z",
     "size_mb": 45,
     "release_date": "2026-02-10T12:00:00"
   }
   ```

3. **Update the app with your GitHub URL**
   In `lru_tracker.py`, change line 17:
   ```python
   UPDATE_CHECK_URL = "https://raw.githubusercontent.com/YOUR_USERNAME/lru-tracker/main/version.json"
   ```

4. **Create a Release on GitHub**
   - Go to your repo → Releases → Create a new release
   - Tag: `v1.0.0`
   - Upload `LRU_Tracker_Setup.exe`
   - Publish release

5. **Update version.json for new releases**
   - Update version number
   - Update download_url to new release
   - Update release_notes
   - Commit to GitHub

#### Option 2: Your Own Server

1. **Upload version.json to your web server**
   ```
   https://yourwebsite.com/lru-tracker/version.json
   ```

2. **Upload installer to your server**
   ```
   https://yourwebsite.com/downloads/LRU_Tracker_Setup.exe
   ```

3. **Update the URL in lru_tracker.py**
   ```python
   UPDATE_CHECK_URL = "https://yourwebsite.com/lru-tracker/version.json"
   ```

### Creating New Versions:

#### When you make updates:

1. **Update version number in lru_tracker.py**
   ```python
   APP_VERSION = "1.1.0"  # Change from 1.0.0
   ```

2. **Build new EXE and installer**
   ```cmd
   cd distribution
   BUILD_WINDOWS_ONE_CLICK.bat
   # Then compile with Inno Setup
   ```

3. **Upload new installer** to GitHub/server

4. **Update version.json**
   ```json
   {
     "version": "1.1.0",
     "download_url": "https://yoursite.com/LRU_Tracker_Setup_v1.1.0.exe",
     "release_notes": "What's new in this version...",
     "size_mb": 45
   }
   ```

5. **Users get notified automatically!**
   - Next time they click "Check for Updates"
   - Or add auto-check on startup

### User Experience:

**When update is available:**
```
┌─────────────────────────────────────┐
│   🎉 Update Available!              │
├─────────────────────────────────────┤
│ Current Version: 1.0.0              │
│ Latest Version: 1.1.0               │
│                                      │
│ What's New:                         │
│ ┌─────────────────────────────────┐│
│ │ ✨ New Features:                ││
│ │ - Added feature X               ││
│ │ - Improved feature Y            ││
│ │                                  ││
│ │ 🐛 Bug Fixes:                   ││
│ │ - Fixed issue Z                 ││
│ └─────────────────────────────────┘│
│                                      │
│ Download Size: ~45 MB               │
│                                      │
│  [📥 Download Update]  [Later]      │
└─────────────────────────────────────┘
```

**When up to date:**
```
You're running the latest version (1.0.0)!
```

---

## 🔄 Update Workflow Example:

### Scenario: You fixed a bug

**Step 1:** Make changes to `lru_tracker.py`

**Step 2:** Update version number
```python
APP_VERSION = "1.0.1"  # Bug fix release
```

**Step 3:** Build new installer
```cmd
distribution\BUILD_WINDOWS_ONE_CLICK.bat
# Then compile with Inno Setup
```

**Step 4:** Upload to GitHub/server
- Upload `LRU_Tracker_Setup.exe` to GitHub releases or your server

**Step 5:** Update version.json
```json
{
  "version": "1.0.1",
  "download_url": "https://github.com/you/lru-tracker/releases/download/v1.0.1/LRU_Tracker_Setup.exe",
  "release_notes": "🐛 Bug fix: Fixed station count update issue",
  "size_mb": 45
}
```

**Step 6:** Users get notified!
- They click "Check for Updates"
- See your bug fix notification
- Download and install
- **Their data is preserved automatically!**

---

## 📊 Version Numbering:

Use **Semantic Versioning**: `MAJOR.MINOR.PATCH`

- `1.0.0` → `1.0.1` = Bug fix (PATCH)
- `1.0.1` → `1.1.0` = New feature (MINOR)
- `1.1.0` → `2.0.0` = Major changes (MAJOR)

Examples:
- `1.0.0` - Initial release
- `1.0.1` - Bug fix
- `1.1.0` - Added new export feature
- `1.2.0` - Added multiple station types
- `2.0.0` - Complete UI redesign

---

## 🎯 Best Practices:

### For Updates:
1. **Always test** new version before distributing
2. **Write clear release notes** - users appreciate knowing what changed
3. **Keep file size reasonable** - compress if needed
4. **Backup data** is handled automatically by installer
5. **Version consistently** - don't skip numbers

### For Installers:
1. **Code sign your installer** (optional, costs money) - removes security warnings
2. **Test on clean PC** before distributing
3. **Keep installer name consistent** - helps with auto-downloads
4. **Include version in filename** (optional) - `LRU_Tracker_Setup_v1.1.0.exe`

---

## 🛠️ Advanced: Auto-Check on Startup

Add this to check for updates when app starts (optional):

In `lru_tracker.py`, add to `__init__` method:
```python
def __init__(self, root):
    # ... existing code ...
    
    # Check for updates in background (don't block startup)
    def auto_check():
        import time
        time.sleep(2)  # Wait 2 seconds after startup
        try:
            import urllib.request
            with urllib.request.urlopen(UPDATE_CHECK_URL, timeout=3) as response:
                update_info = json.loads(response.read().decode())
                if self._is_newer_version(update_info.get('version'), APP_VERSION):
                    # Show small notification, don't interrupt
                    self.root.after(0, lambda: messagebox.showinfo(
                        "Update Available", 
                        f"Version {update_info.get('version')} is available!\n\n"
                        "Click 'Check for Updates' button for details."
                    ))
        except:
            pass  # Silently fail if offline
    
    threading.Thread(target=auto_check, daemon=True).start()
```

---

## 📁 Files Summary:

### Created Files:
- `distribution/installer_script.iss` - Inno Setup script
- `auto_updater.py` - Update system (integrated into main app)
- `INSTALLER_AND_UPDATES_GUIDE.md` - This file

### Modified Files:
- `lru_tracker.py` - Added update checking

### Generated Files (after build):
- `distribution/packages/LRU_Tracker_Setup.exe` - GUI installer
- `version.json` - Update information file

---

## ✅ Quick Checklist:

**For First Release:**
- [ ] Install Inno Setup
- [ ] Build exe with BUILD_WINDOWS_ONE_CLICK.bat
- [ ] Compile installer with Inno Setup
- [ ] Create GitHub repo (or web hosting)
- [ ] Upload installer
- [ ] Create version.json
- [ ] Update UPDATE_CHECK_URL in code
- [ ] Distribute!

**For Updates:**
- [ ] Make code changes
- [ ] Update APP_VERSION number
- [ ] Build new exe and installer
- [ ] Upload to GitHub/server
- [ ] Update version.json
- [ ] Announce to users

---

## 🎊 You're Done!

You now have:
✅ Professional GUI installer
✅ Automatic update checking
✅ Beautiful update notifications
✅ Data preservation during updates
✅ Easy distribution workflow

Users can simply:
1. Download and run installer
2. Get notified of updates automatically
3. Update with one click
4. Never lose their data!

**Much better than sending zip files!** 🚀
