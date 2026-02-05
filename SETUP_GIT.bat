@echo off
echo ============================================
echo   LRU Tracker - GitHub Setup Script
echo ============================================
echo.

echo Step 1: Initializing Git repository...
git init
echo.

echo Step 2: Adding all files...
git add .
echo.

echo Step 3: Creating initial commit...
git commit -m "Initial commit: LRU Tracker v1.0.0 with auto-updates"
echo.

echo Step 4: Renaming branch to main...
git branch -M main
echo.

echo Step 5: Connecting to GitHub repository...
git remote add origin https://github.com/HaltTheGrey/lru-tracker.git
echo.

echo Step 6: Pushing to GitHub...
git push -u origin main
echo.

echo ============================================
echo   Setup Complete!
echo ============================================
echo.
echo Next steps:
echo 1. Go to: https://github.com/HaltTheGrey/lru-tracker
echo 2. Click "Releases" - Create a new release
echo 3. Tag: v1.0.0
echo 4. Upload your LRU_Tracker_Setup.exe
echo 5. Upload version.json
echo.
echo See SETUP_GITHUB.md for detailed instructions!
echo.
pause
