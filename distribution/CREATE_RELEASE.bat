@echo off
echo ============================================
echo   LRU Tracker - Create Release Package
echo ============================================
echo.

echo This will create a clean release package
echo with only the files users need.
echo.

echo Step 1: Building executable...
call BUILD_WINDOWS_ONE_CLICK.bat
if errorlevel 1 (
    echo ERROR: Build failed!
    pause
    exit /b 1
)

echo.
echo ============================================
echo.
echo Step 2: Creating release package...
python create_release_package.py

echo.
echo ============================================
echo   IMPORTANT: Compile Installer
echo ============================================
echo.
echo Next, you need to compile the installer:
echo 1. Open Inno Setup Compiler
echo 2. Open: distribution\installer_script.iss
echo 3. Press F9 to compile
echo 4. Then run this script again
echo.

pause
