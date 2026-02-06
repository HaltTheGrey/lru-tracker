# GitHub Release Checklist - v1.1.0

## Pre-Release Checklist

- [x] Update APP_VERSION in config.py to "1.1.0" ✅
- [x] Update version.json to v1.1.0 ✅
- [ ] Build executable with BUILD_WINDOWS_ONE_CLICK.bat
- [ ] Compile installer with Inno Setup (F9)
- [ ] Test installer on clean machine
- [ ] Commit version.json changes to Git

## GitHub Release Steps

### 1. Create New Release
Go to: https://github.com/HaltTheGrey/lru-tracker/releases/new

### 2. Fill in Release Details
- **Tag:** `v1.1.0`
- **Target:** `main` branch
- **Title:** `LRU Tracker v1.1.0`
- **Description:** Copy from `GITHUB_RELEASE_v1.1.0.md`

### 3. Upload Assets
- [ ] Upload: `distribution\packages\LRU_Tracker_Setup.exe`

### 4. Publish Release
- [ ] Click "Publish release"
- [ ] Verify download link works

## Post-Release Steps

### 5. Update version.json Download URL
The download URL should be:
```
https://github.com/HaltTheGrey/lru-tracker/releases/download/v1.1.0/LRU_Tracker_Setup.exe
```

This is already set in the updated version.json file.

### 6. Commit and Push
```bash
git add version.json
git commit -m "Update version.json for v1.1.0 release"
git push origin main
```

### 7. Test Auto-Update
- [ ] Open old version of app
- [ ] Check for updates
- [ ] Verify update notification appears
- [ ] Verify download link works

## Share the Release

**Direct Download Link:**
```
https://github.com/HaltTheGrey/lru-tracker/releases/latest/download/LRU_Tracker_Setup.exe
```

**Latest Release Page:**
```
https://github.com/HaltTheGrey/lru-tracker/releases/latest
```

## Quick Commands

```bash
# Check current status
git status

# Add and commit version.json
git add version.json
git commit -m "Update version.json for v1.1.0 release"

# Push to GitHub
git push origin main

# Create and push tag (optional, GitHub can do this)
git tag v1.1.0
git push origin v1.1.0
```

## Notes

- The installer file should be ~45 MB
- Users only need to download LRU_Tracker_Setup.exe
- Source code is automatically included by GitHub
- Auto-update will check version.json in main branch
