# 🔧 Alternative Ways to Get Inno Setup (When Website is Blocked)

## Option 1: Download from Alternative Sources

### Microsoft Winget (Windows Package Manager)
If you have Windows 10/11, you can install via command line:

```powershell
winget install JRSoftware.InnoSetup
```

### Chocolatey (Windows Package Manager)
If you have Chocolatey installed:

```powershell
choco install innosetup
```

### Direct Download Mirrors
- **GitHub**: https://github.com/jrsoftware/issrc/releases
- **SourceForge**: https://sourceforge.net/projects/innounp/files/
- **FossHub**: https://www.fosshub.com/Inno-Setup.html

---

## Option 2: Skip Inno Setup - Use ZIP Distribution Instead

You can distribute your app **without** creating an installer! Just use a ZIP file.

### Quick Method - Already Built!

The `BUILD_WINDOWS_ONE_CLICK.bat` script already creates a ZIP package for you:

**Location:** `distribution\packages\LRU_Tracker_Windows.zip`

**What's inside:**
- `LRU_Tracker.exe` (your app)
- `INSTALL_INSTRUCTIONS.txt` (setup guide)

**User experience:**
1. Download the ZIP
2. Extract it
3. Double-click `LRU_Tracker.exe`
4. Done! ✅

### Share this ZIP file directly on GitHub Releases!

---

## Option 3: Create a Portable Package (No Installation Required)

Make a professional portable app without an installer.

**I can create a script that:**
- Packages the .exe with documentation
- Creates a nice folder structure
- No installation needed - just extract and run
- Works exactly like big portable apps (like Notepad++, 7-Zip portable, etc.)

**User downloads:** One ZIP file
**User extracts:** To any folder they want
**User runs:** The .exe directly

This is actually **preferred by many users** because:
- ✅ No admin rights needed
- ✅ Can run from USB drive
- ✅ No registry entries
- ✅ Easy to uninstall (just delete folder)

Would you like me to create this portable package system?

---

## Option 4: Ask IT/Network Admin

If you're on a corporate network (Amazon FC), the website might be blocked by IT.

**You can:**
1. Contact IT help desk
2. Explain you need Inno Setup for software development
3. They can whitelist the site or install it for you
4. Reference: https://jrsoftware.org (official open-source tool)

---

## 🎯 My Recommendation: Use the ZIP Distribution!

**Why:**
- ✅ You already have it! (BUILD_WINDOWS_ONE_CLICK.bat creates it)
- ✅ No extra software needed
- ✅ Works great for internal FC distribution
- ✅ Users can easily extract and run
- ✅ No security warnings from Windows SmartScreen
- ✅ Can be shared via email, shared drive, or GitHub

**How to use it:**

1. **Find your ZIP:**
   ```
   distribution\packages\LRU_Tracker_Windows.zip
   ```

2. **Upload to GitHub Release:**
   - Go to: https://github.com/HaltTheGrey/lru-tracker/releases/new
   - Upload the ZIP file
   - Users download, extract, and run!

3. **Or share internally:**
   - Put on shared drive
   - Email to team
   - Post on internal wiki/portal

---

## 📦 What Would You Prefer?

**A)** Try alternative download methods for Inno Setup (Winget, Chocolatey, GitHub)

**B)** Use the existing ZIP distribution (easiest, already done!)

**C)** Create an enhanced portable package with better documentation

**D)** Ask IT to help you access the Inno Setup website

Let me know and I'll help you proceed! 🚀
