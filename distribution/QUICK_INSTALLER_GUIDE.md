# Quick Start: Creating Your First Installer

## 🎯 Goal
Create a professional Windows installer with a GUI wizard (like other apps).

## ⚡ 5-Minute Setup:

### Step 1: Download Inno Setup (2 minutes)
1. Go to: https://jrsoftware.org/isdl.php
2. Download "Inno Setup 6.x" (latest version)
3. Run installer and click "Next" through everything
4. Inno Setup Compiler is now installed!

### Step 2: Build Your EXE (1 minute)
```cmd
cd distribution
BUILD_WINDOWS_ONE_CLICK.bat
```
Wait for it to finish.

### Step 3: Create Installer (2 minutes)
1. Open "Inno Setup Compiler" (Windows Start Menu)
2. File → Open
3. Browse to: `distribution\installer_script.iss`
4. Click "Build" → "Compile" (or press F9)
5. Wait 30 seconds

### Step 4: Done! 🎉
Your installer is at:
```
distribution\packages\LRU_Tracker_Setup.exe
```

Share this file with users instead of the zip!

## 📦 What Users See:

1. Double-click `LRU_Tracker_Setup.exe`
2. See professional welcome screen
3. Choose installation location
4. Choose if they want desktop shortcut
5. Click Install
6. Launch app immediately
7. Done!

Much cleaner than extracting zip files!

## 🔄 For Updates Later:

When you make changes to the app:

1. **Change version number** in `lru_tracker.py`:
   ```python
   APP_VERSION = "1.1.0"  # Update this
   ```

2. **Build new installer** (same steps as above)

3. **Upload to GitHub or your server**

4. **Update version.json**:
   ```json
   {
     "version": "1.1.0",
     "download_url": "https://yourlink.com/LRU_Tracker_Setup.exe",
     "release_notes": "What you changed...",
     "size_mb": 45
   }
   ```

5. **Users click "Check for Updates" button in the app**
   - They see what's new
   - Download automatically opens
   - Install new version
   - **Data is preserved automatically!**

## 🎯 Key Benefits:

### With Installer:
✅ Professional presentation
✅ Automatic shortcuts
✅ Easy uninstall
✅ Data preserved during updates
✅ No confusion about where files go

### With Auto-Update:
✅ Users know when updates are available
✅ One-click download
✅ No manual file copying
✅ Never lose data
✅ Everyone stays up-to-date

## 📚 More Details:

See `INSTALLER_AND_UPDATES_GUIDE.md` for:
- GitHub setup for free hosting
- Custom branding
- Advanced options
- Troubleshooting

## ❓ Questions:

**Q: Do I need to buy anything?**
A: No! Inno Setup is completely free.

**Q: Can I change the installer appearance?**
A: Yes! Edit `installer_script.iss` - it's well commented.

**Q: What if I don't have GitHub?**
A: You can use any file hosting (Dropbox, Google Drive, your website, etc.)

**Q: Will users lose their data when updating?**
A: No! The installer preserves `lru_data.json` automatically.

**Q: Can I distribute without an installer?**
A: Yes, but installers are much more professional and user-friendly.

---

**Ready to create your first installer?** Just follow the 5-minute setup above! 🚀
