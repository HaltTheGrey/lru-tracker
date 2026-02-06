@echo off
REM ========================================
REM  LRU TRACKER - BUILD PYTHON INSTALLER
REM ========================================
REM
REM This script builds a standalone installer using PyInstaller
REM Bundles: setup_installer.py + LRU_Tracker.exe
REM No external dependencies required (uses Python + tkinter)
REM
echo.
echo ========================================
echo   BUILDING LRU TRACKER INSTALLER
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo.
    echo Please install Python 3.x and add it to PATH
    echo.
    pause
    exit /b 1
)

REM Check if the main executable exists
if not exist "dist\LRU_Tracker.exe" (
    echo ERROR: LRU_Tracker.exe not found in dist folder!
    echo.
    echo Please build the main application first:
    echo   1. Run BUILD_REFACTORED.bat
    echo   2. Then run this script again
    echo.
    pause
    exit /b 1
)

REM Check if installer script exists
if not exist "installer\setup_installer.py" (
    echo ERROR: setup_installer.py not found!
    echo.
    echo Missing installer script in installer folder.
    echo.
    pause
    exit /b 1
)

echo [1/5] Checking Python environment...
python --version
echo.

echo [2/5] Installing/checking PyInstaller...
pip install --quiet --upgrade pyinstaller
if errorlevel 1 (
    echo WARNING: Could not update PyInstaller, using existing version
)
echo.

echo [3/5] Installing/checking pywin32 (for shortcuts)...
pip install --quiet pywin32
if errorlevel 1 (
    echo WARNING: Could not install pywin32, will use PowerShell fallback
)
echo.

echo [4/5] Creating output directory...
if not exist "dist\installer" mkdir "dist\installer"
echo.

echo [5/5] Building standalone installer with PyInstaller...
echo This will take 2-3 minutes...
echo.

REM Copy main exe to installer folder for bundling
echo   - Copying LRU_Tracker.exe to installer folder...
copy "dist\LRU_Tracker.exe" "installer\LRU_Tracker.exe" >nul
if errorlevel 1 (
    echo ERROR: Failed to copy LRU_Tracker.exe
    pause
    exit /b 1
)

REM Build the installer executable
echo   - Running PyInstaller...
echo.
python -m PyInstaller --noconfirm ^
    --onefile ^
    --windowed ^
    --name "LRU_Tracker_Setup" ^
    --icon "distribution\lru_icon.ico" ^
    --add-data "installer\LRU_Tracker.exe;." ^
    --add-data "installer\uninstall.py;." ^
    --hidden-import "win32com.client" ^
    --hidden-import "win32com.shell" ^
    --hidden-import "winreg" ^
    "installer\setup_installer.py"

if errorlevel 1 (
    echo.
    echo ========================================
    echo   BUILD FAILED!
    echo ========================================
    echo.
    echo Check the error messages above.
    echo Common issues:
    echo   - Missing PyInstaller: pip install pyinstaller
    echo   - Path issues: Use absolute paths
    echo   - Icon missing: Check refactored\icons\app.ico exists
    echo.
    pause
    exit /b 1
)

REM Move installer to distribution folder
echo.
echo   - Moving installer to dist\installer...
move /Y "dist\LRU_Tracker_Setup.exe" "dist\installer\LRU_Tracker_Setup.exe" >nul

REM Clean up temporary files
echo   - Cleaning up...
del "installer\LRU_Tracker.exe" >nul 2>&1
rmdir /s /q "build" >nul 2>&1
del "LRU_Tracker_Setup.spec" >nul 2>&1

echo.
echo ========================================
echo   BUILD SUCCESSFUL!
echo ========================================
echo.
echo Installer created:
echo   dist\installer\LRU_Tracker_Setup.exe
echo.
echo Installer features:
echo   - Professional GUI wizard
echo   - Progress bar with status updates
echo   - Custom install location
echo   - Desktop shortcut (optional)
echo   - Start Menu shortcut (optional)
echo   - Adds to Programs and Features
echo   - Includes uninstaller
echo   - No admin rights required (installs to user folder by default)
echo.

REM Get file size
for %%A in ("dist\installer\LRU_Tracker_Setup.exe") do (
    set size=%%~zA
    set /a size_mb=%%~zA/1024/1024
)
echo File size: ~%size_mb% MB
echo.

echo ========================================
echo   HOW TO USE
echo ========================================
echo.
echo 1. Upload to GitHub release:
echo    dist\installer\LRU_Tracker_Setup.exe
echo.
echo 2. Update version.json download_url to:
echo    https://github.com/HaltTheGrey/lru-tracker/releases/download/v1.2.2/LRU_Tracker_Setup.exe
echo.
echo 3. Users download and run LRU_Tracker_Setup.exe
echo.
echo 4. Installer wizard guides them through:
echo    - Choose install location (default: Program Files\LRU Tracker)
echo    - Select shortcut options
echo    - Automatic installation with progress bar
echo    - Creates shortcuts and registry entries
echo.
echo 5. App can be uninstalled from:
echo    - Windows Settings ^> Apps ^> LRU Tracker
echo    - Or run the uninstall.exe in install folder
echo.
echo ========================================
echo   TESTING INSTALLER
echo ========================================
echo.
echo Before distributing, test the installer:
echo   1. Run: dist\installer\LRU_Tracker_Setup.exe
echo   2. Complete installation wizard
echo   3. Verify shortcuts were created
echo   4. Check Programs and Features for entry
echo   5. Run the installed app to ensure it works
echo   6. Test uninstaller
echo.
echo ========================================
echo Opening installer folder...
echo ========================================
echo.

explorer "dist\installer"

echo.
echo Build complete!
echo.
pause
