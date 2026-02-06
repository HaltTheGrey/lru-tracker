# Quick Local Testing Guide

## Problem
The update checker requires HTTPS for security, so it can't read local files directly.

## Solution: Two Options

### Option 1: Test Mode (Easiest)

1. **Backup original file:**
   ```bash
   cd refactored
   copy update_checker.py update_checker_BACKUP.py
   ```

2. **Replace with test version:**
   ```bash
   copy update_checker_TEST_MODE.py update_checker.py
   ```

3. **Build v1.1.0 app:**
   ```bash
   git checkout main
   cd distribution
   BUILD_WINDOWS_ONE_CLICK.bat
   ```
   Save the .exe as `LRU_Tracker_v1.1.0.exe`

4. **Switch back and restore test mode:**
   ```bash
   git checkout feature/enhanced-excel-export
   cd refactored
   copy update_checker_TEST_MODE.py update_checker.py
   ```

5. **Run v1.1.0 app and click "Check for Updates"**
   - Should detect v1.2.0
   - Should show release notes about Excel improvements

6. **Restore original:**
   ```bash
   copy update_checker_BACKUP.py update_checker.py
   del update_checker_BACKUP.py
   ```

### Option 2: Skip Local Testing (Recommended)

Just merge to main and test with real GitHub:

1. **Merge feature branch:**
   ```bash
   git checkout main
   git merge feature/enhanced-excel-export
   ```

2. **Build v1.2.0:**
   ```bash
   cd distribution
   BUILD_WINDOWS_ONE_CLICK.bat
   ```

3. **Create GitHub release v1.2.0**
   - Upload the installer
   - Copy release notes from GITHUB_RELEASE_v1.2.0.md

4. **Update version.json in main:**
   - Copy content from version_v1.2.0.json to version.json
   - Commit and push

5. **Test with old v1.1.0 build:**
   - Run old executable
   - Click "Check for Updates"
   - Should detect v1.2.0 from GitHub!

## Why Option 2 is Better

- Tests the real update flow
- No file swapping needed
- Tests actual GitHub URLs
- More realistic user experience
- Cleaner process

## Current Status

✅ Feature branch ready  
✅ Version bumped to 1.2.0  
✅ Excel exports enhanced  
✅ Release docs ready  
⏳ Ready to merge and release  

## Quick Merge Commands

```bash
# Make sure everything is committed
git status

# Switch to main
git checkout main

# Merge feature branch
git merge feature/enhanced-excel-export

# Push to GitHub
git push origin main

# Now build and create release!
```
