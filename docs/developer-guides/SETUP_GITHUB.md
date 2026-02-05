# 🚀 Setting Up Your GitHub Repository

Step-by-step guide to get your LRU Tracker on GitHub with automatic updates.

## 📝 Step 1: Create the Repository on GitHub

1. **Go to GitHub:** https://github.com/HaltTheGrey
2. **Click "+" in top right** → "New repository"
3. **Fill in details:**
   - Repository name: `lru-tracker`
   - Description: `Professional LRU tracking app for FC stations with min/max pull system`
   - Visibility: **Public** (so users can download) or Private (if internal only)
   - ❌ **DO NOT** check "Initialize with README" (we already have one)
4. **Click "Create repository"**

## 📦 Step 2: Prepare Your Local Repository

Open PowerShell in your project folder and run these commands:

```powershell
# Navigate to your project
cd C:\Users\jessneug\Leetcode\templeteforpartwalks

# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Make your first commit
git commit -m "Initial commit: LRU Tracker v1.0.0"

# Rename branch to main (GitHub's default)
git branch -M main

# Connect to your GitHub repository
git remote add origin https://github.com/HaltTheGrey/lru-tracker.git

# Push to GitHub
git push -u origin main
```

## 🏷️ Step 3: Create Your First Release

1. **Build your installer first:**
   ```powershell
   cd distribution
   .\BUILD_WINDOWS_ONE_CLICK.bat
   ```

2. **Compile with Inno Setup:**
   - Open Inno Setup Compiler
   - Open `distribution\installer_script.iss`
   - Press F9 to compile
   - Installer created at: `distribution\packages\LRU_Tracker_Setup.exe`

3. **Go to GitHub:**
   - Visit: https://github.com/HaltTheGrey/lru-tracker
   - Click "Releases" (right sidebar)
   - Click "Create a new release"

4. **Fill in release details:**
   - **Tag version:** `v1.0.0`
   - **Release title:** `LRU Tracker v1.0.0 - Initial Release`
   - **Description:** Copy from `version.json` release_notes
   - **Attach files:** Upload `LRU_Tracker_Setup.exe`
   - Click "Publish release"

## 🔗 Step 4: Update the App with GitHub URL

Now that your release is live, update the code to point to your GitHub:

1. **Edit `lru_tracker.py`:**
   - Find line 17 (around line 17)
   - Change from:
     ```python
     UPDATE_CHECK_URL = "https://raw.githubusercontent.com/YOUR_USERNAME/lru-tracker/main/version.json"
     ```
   - To:
     ```python
     UPDATE_CHECK_URL = "https://raw.githubusercontent.com/HaltTheGrey/lru-tracker/main/version.json"
     ```

2. **Commit and push the change:**
   ```powershell
   git add lru_tracker.py
   git commit -m "Update: Set correct GitHub URL for auto-updates"
   git push
   ```

## ✅ Step 5: Verify Auto-Updates Work

1. **Run your app:**
   ```powershell
   python lru_tracker.py
   ```

2. **Click "🔄 Check for Updates"**
   - Should say "You're running the latest version (1.0.0)!"
   - This confirms the GitHub connection is working!

## 📊 Step 6: Add Screenshots (Optional)

Make your GitHub page look professional:

1. **Create screenshots folder:**
   ```powershell
   mkdir screenshots
   ```

2. **Take screenshots of your app:**
   - Main interface
   - Trend analysis chart
   - Update notification dialog

3. **Add to GitHub:**
   ```powershell
   git add screenshots/
   git commit -m "Add screenshots for README"
   git push
   ```

## 🎯 Your Repository is Ready!

Your repository URL:
```
https://github.com/HaltTheGrey/lru-tracker
```

Users can now:
- ✅ View your project
- ✅ Download the installer
- ✅ Report issues
- ✅ Get automatic updates

## 🔄 Future Updates Workflow

When you make changes:

1. **Update version in code:**
   ```python
   APP_VERSION = "1.1.0"  # In lru_tracker.py
   ```

2. **Commit changes:**
   ```powershell
   git add .
   git commit -m "Version 1.1.0: Added new features"
   git push
   ```

3. **Build new installer:**
   ```powershell
   cd distribution
   .\BUILD_WINDOWS_ONE_CLICK.bat
   # Then compile with Inno Setup (F9)
   ```

4. **Create new release on GitHub:**
   - Tag: `v1.1.0`
   - Upload new `LRU_Tracker_Setup.exe`

5. **Update `version.json`:**
   ```json
   {
     "version": "1.1.0",
     "download_url": "https://github.com/HaltTheGrey/lru-tracker/releases/download/v1.1.0/LRU_Tracker_Setup.exe",
     "release_notes": "What's new...",
     "size_mb": 45
   }
   ```

6. **Commit version.json:**
   ```powershell
   git add version.json
   git commit -m "Update version.json for v1.1.0"
   git push
   ```

7. **Users get notified automatically!** 🎉

## 🛡️ Optional: Add Repository Badges

Edit `GITHUB_README.md` and add these badges:

```markdown
![GitHub release](https://img.shields.io/github/v/release/HaltTheGrey/lru-tracker)
![GitHub downloads](https://img.shields.io/github/downloads/HaltTheGrey/lru-tracker/total)
![GitHub issues](https://img.shields.io/github/issues/HaltTheGrey/lru-tracker)
```

## 📧 Share With Your Team

Send this link to your FC team:
```
https://github.com/HaltTheGrey/lru-tracker/releases/latest
```

They can download the latest installer directly!

---

## 🎊 You're All Set!

Your professional distribution system is complete:
- ✅ GitHub repository with releases
- ✅ Professional installer
- ✅ Automatic update checking
- ✅ Easy distribution link
- ✅ Version management

**Now go help your FC team track those LRUs! 🚀**
