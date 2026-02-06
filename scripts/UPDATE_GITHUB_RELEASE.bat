@echo off
REM GitHub Release Update Script for LRU Tracker
REM This script helps prepare and update GitHub releases

echo ========================================
echo   GitHub Release Update Helper
echo   LRU Tracker v1.1.0
echo ========================================
echo.

echo Step 1: Update version.json
echo ----------------------------
echo Current version in version.json: 1.0.0
echo Current version in config.py: 1.1.0
echo.
echo IMPORTANT: Update version.json to match config.py version!
echo.
pause

echo.
echo Step 2: Build the installer
echo ----------------------------
echo Navigate to distribution folder and run:
echo   BUILD_WINDOWS_ONE_CLICK.bat
echo Then compile with Inno Setup (F9)
echo.
pause

echo.
echo Step 3: Create GitHub Release
echo ----------------------------
echo 1. Go to: https://github.com/HaltTheGrey/lru-tracker/releases/new
echo 2. Tag: v1.1.0
echo 3. Title: LRU Tracker v1.1.0
echo 4. Upload: distribution\packages\LRU_Tracker_Setup.exe
echo.
pause

echo.
echo Step 4: Update version.json with release URL
echo ----------------------------
echo After creating the release, update version.json with:
echo   - New version number
echo   - New download URL
echo   - Release notes
echo.
pause

echo.
echo Step 5: Commit and push changes
echo ----------------------------
echo Run these commands:
echo   git add version.json
echo   git commit -m "Update version.json for v1.1.0"
echo   git push origin main
echo.
pause

echo.
echo ========================================
echo   Release Update Complete!
echo ========================================
echo.
echo Next: Share the release link with users!
echo https://github.com/HaltTheGrey/lru-tracker/releases/latest
echo.
pause
