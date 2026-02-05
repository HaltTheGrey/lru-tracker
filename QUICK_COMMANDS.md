# 🚀 Quick Command Reference

## First Time Setup

```powershell
# 1. Run the automated setup script
.\SETUP_GIT.bat

# OR do it manually:
git init
git add .
git commit -m "Initial commit: LRU Tracker v1.0.0"
git branch -M main
git remote add origin https://github.com/HaltTheGrey/lru-tracker.git
git push -u origin main
```

## Build Installer

```powershell
# Build executable
cd distribution
.\BUILD_WINDOWS_ONE_CLICK.bat

# Then open Inno Setup Compiler
# Open: distribution\installer_script.iss
# Press: F9 to compile
# Output: distribution\packages\LRU_Tracker_Setup.exe
```

## Future Updates

```powershell
# Make your code changes, then:

# 1. Update version in lru_tracker.py
#    APP_VERSION = "1.1.0"

# 2. Commit changes
git add .
git commit -m "Version 1.1.0: Your update description"
git push

# 3. Build new installer (see above)

# 4. Create release on GitHub:
#    - Go to: https://github.com/HaltTheGrey/lru-tracker/releases
#    - Click "Draft a new release"
#    - Tag: v1.1.0
#    - Upload: LRU_Tracker_Setup.exe

# 5. Update version.json
#    - Change version to "1.1.0"
#    - Update download_url
#    - Update release_notes
git add version.json
git commit -m "Update version.json for v1.1.0"
git push
```

## Common Git Commands

```powershell
# Check status
git status

# See what changed
git diff

# View commit history
git log --oneline

# Undo uncommitted changes
git checkout -- filename.py

# Pull latest from GitHub
git pull

# Push to GitHub
git push
```

## Important URLs

- **Your Repository:** https://github.com/HaltTheGrey/lru-tracker
- **Latest Release:** https://github.com/HaltTheGrey/lru-tracker/releases/latest
- **Create New Release:** https://github.com/HaltTheGrey/lru-tracker/releases/new
- **Version File (raw):** https://raw.githubusercontent.com/HaltTheGrey/lru-tracker/main/version.json

## Files Created for GitHub

- `.gitignore` - Tells Git what NOT to upload
- `LICENSE` - MIT license for your code
- `GITHUB_README.md` - Professional README (copy to README.md)
- `version.json` - Auto-update information
- `SETUP_GITHUB.md` - Detailed setup guide
- `GITHUB_CHECKLIST.md` - Step-by-step checklist
- `SETUP_GIT.bat` - Automated setup script

## Testing Auto-Updates

```powershell
# Run the app
python lru_tracker.py

# Click "🔄 Check for Updates" button
# Should say: "You're running the latest version (1.0.0)!"
```

## Troubleshooting

**Git not found?**
```powershell
# Install Git: https://git-scm.com/downloads
# Restart PowerShell after installing
```

**Can't push to GitHub?**
```powershell
# Make sure repository exists on GitHub.com first!
# Then check remote URL:
git remote -v
# Should show: https://github.com/HaltTheGrey/lru-tracker.git
```

**Update check fails?**
```powershell
# Make sure version.json is uploaded to GitHub
# Check URL in browser:
# https://raw.githubusercontent.com/HaltTheGrey/lru-tracker/main/version.json
```

---

**Quick Start:** Run `.\SETUP_GIT.bat` and follow the checklist in `GITHUB_CHECKLIST.md`!
