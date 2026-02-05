# 📋 GitHub Setup Checklist

Follow these steps in order to get your LRU Tracker on GitHub.

## ✅ Pre-Setup (Do These First)

- [ ] **Install Git** (if not already installed)
  - Download from: https://git-scm.com/downloads
  - Install with default options
  - Restart PowerShell after installation

- [ ] **Install Inno Setup** (for creating installer)
  - Download from: https://jrsoftware.org/isdl.php
  - Install with default options

## 📦 Phase 1: Build Your Installer

- [ ] **Build the executable:**
  ```powershell
  cd distribution
  .\BUILD_WINDOWS_ONE_CLICK.bat
  ```
  ✅ Creates: `dist\LRU_Tracker.exe`

- [ ] **Compile the installer:**
  1. Open Inno Setup Compiler
  2. File → Open → `distribution\installer_script.iss`
  3. Press F9 to compile
  ✅ Creates: `distribution\packages\LRU_Tracker_Setup.exe`

- [ ] **Test the installer locally**
  - Run `LRU_Tracker_Setup.exe`
  - Make sure it installs correctly
  - Launch the app and test features

## 🌐 Phase 2: Create GitHub Repository

- [ ] **Create repository on GitHub:**
  1. Go to: https://github.com/HaltTheGrey
  2. Click "+" → "New repository"
  3. Name: `lru-tracker`
  4. Description: `Professional LRU tracking app for FC stations`
  5. Public or Private (your choice)
  6. **DO NOT** check "Initialize with README"
  7. Click "Create repository"

## 📤 Phase 3: Push to GitHub

- [ ] **Run the setup script:**
  ```powershell
  .\SETUP_GIT.bat
  ```
  This will:
  - Initialize Git
  - Add all files
  - Create initial commit
  - Connect to GitHub
  - Push to GitHub

  **Alternative (Manual):**
  ```powershell
  git init
  git add .
  git commit -m "Initial commit: LRU Tracker v1.0.0"
  git branch -M main
  git remote add origin https://github.com/HaltTheGrey/lru-tracker.git
  git push -u origin main
  ```

- [ ] **Verify on GitHub:**
  - Visit: https://github.com/HaltTheGrey/lru-tracker
  - You should see all your files!

## 🏷️ Phase 4: Create First Release

- [ ] **Create release on GitHub:**
  1. Go to: https://github.com/HaltTheGrey/lru-tracker
  2. Click "Releases" (right sidebar)
  3. Click "Create a new release"

- [ ] **Fill in release details:**
  - **Tag:** `v1.0.0`
  - **Title:** `LRU Tracker v1.0.0 - Initial Release`
  - **Description:** 
    ```
    🎉 Initial Release
    
    ✨ Features:
    - Min/Max pull system with color indicators
    - Station management
    - LRU tracking with history
    - Excel export capabilities
    - Trend analysis charts
    - Template import/export
    - FC Schedule import
    - Auto-update system
    
    📦 Installation:
    Download LRU_Tracker_Setup.exe and run!
    ```

- [ ] **Upload files:**
  - Attach: `distribution\packages\LRU_Tracker_Setup.exe`
  - Click "Publish release"

- [ ] **Upload version.json to main branch:**
  1. Go to repository main page
  2. Click "Add file" → "Upload files"
  3. Upload `version.json`
  4. Commit message: "Add version.json for auto-updates"
  5. Click "Commit changes"

## 🧪 Phase 5: Test Auto-Updates

- [ ] **Test update checking:**
  1. Run your app: `python lru_tracker.py`
  2. Click "🔄 Check for Updates"
  3. Should say: "You're running the latest version (1.0.0)!"
  
  ✅ If this works, auto-updates are configured correctly!

## 📋 Phase 6: Update README

- [ ] **Replace README.md with GitHub version:**
  ```powershell
  copy GITHUB_README.md README.md
  git add README.md
  git commit -m "Update README for GitHub"
  git push
  ```

## 🎊 Phase 7: Share With Team

- [ ] **Get your download link:**
  ```
  https://github.com/HaltTheGrey/lru-tracker/releases/latest
  ```

- [ ] **Share with FC team:**
  - Send the link via email/Slack
  - They can download directly from GitHub
  - No need to email large files!

## 📝 Optional: Add Screenshots

- [ ] **Take screenshots:**
  - Main interface
  - Trend analysis
  - Update dialog

- [ ] **Upload to GitHub:**
  ```powershell
  mkdir screenshots
  # Copy your screenshots to this folder
  git add screenshots/
  git commit -m "Add screenshots"
  git push
  ```

## 🔄 Future Updates Workflow

When you make changes:

- [ ] **Update version number:**
  - Edit `APP_VERSION = "1.1.0"` in `lru_tracker.py`

- [ ] **Commit changes:**
  ```powershell
  git add .
  git commit -m "Version 1.1.0: Description of changes"
  git push
  ```

- [ ] **Build new installer:**
  ```powershell
  cd distribution
  .\BUILD_WINDOWS_ONE_CLICK.bat
  # Then Inno Setup (F9)
  ```

- [ ] **Create new release:**
  - Tag: `v1.1.0`
  - Upload new installer

- [ ] **Update version.json:**
  - Change version to "1.1.0"
  - Update download_url to v1.1.0
  - Update release_notes
  - Commit and push

- [ ] **Users get notified automatically!**

---

## 🆘 Troubleshooting

### "git: command not found"
→ Install Git from https://git-scm.com/downloads

### "Permission denied (publickey)"
→ You need to authenticate with GitHub:
1. Use GitHub Desktop (easier)
2. Or set up SSH keys (advanced)

### "Installer won't compile"
→ Make sure Inno Setup is installed

### "Update check says 404 error"
→ Make sure version.json is uploaded to GitHub main branch

### "Can't push to GitHub"
→ Make sure you created the repository first on GitHub.com

---

**Your repository URL:** https://github.com/HaltTheGrey/lru-tracker

**Need help?** See `SETUP_GITHUB.md` for detailed instructions!
