@echo off
REM =============================================================================
REM LRU TRACKER - ONE-CLICK BUILD & PACKAGE
REM =============================================================================
REM This script builds a standalone Windows executable that users can run
REM without installing Python. The output is a zip file ready to distribute.
REM =============================================================================

echo.
echo ========================================
echo   LRU TRACKER - BUILD FOR WINDOWS
echo ========================================
echo.
echo This will create a standalone .exe file
echo No Python installation required to run!
echo.
pause

REM Install PyInstaller if needed
echo.
echo [1/5] Checking PyInstaller...
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo Installing PyInstaller...
    pip install pyinstaller
    echo PyInstaller installed!
) else (
    echo PyInstaller already installed.
)

REM Navigate to parent directory
cd ..

REM Clean previous builds
echo.
echo [2/5] Cleaning previous builds...
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"
if exist "*.spec" del /q "*.spec"

REM Build the executable
echo.
echo [3/5] Building executable (this may take a few minutes)...
echo.
python -m PyInstaller --noconfirm --onefile --windowed ^
    --name "LRU_Tracker" ^
    --icon "distribution\lru_icon.ico" ^
    --hidden-import "openpyxl" ^
    --hidden-import "pandas" ^
    --hidden-import "tkinter" ^
    --hidden-import "matplotlib" ^
    lru_tracker.py

if errorlevel 1 (
    echo.
    echo ========================================
    echo ERROR: Build failed!
    echo ========================================
    echo Check the error messages above.
    echo.
    pause
    exit /b 1
)

REM Copy only essential files
echo.
echo [4/5] Packaging installation guide...
copy distribution\INSTALL_WINDOWS.txt dist\INSTALL_INSTRUCTIONS.txt >nul

REM Create distribution package
echo.
echo [5/5] Creating distribution package...
if not exist "distribution\packages" mkdir "distribution\packages"

REM Create the zip file
powershell -Command "Compress-Archive -Path 'dist\*' -DestinationPath 'distribution\packages\LRU_Tracker_Windows.zip' -Force"

echo.
echo ========================================
echo   BUILD SUCCESSFUL!
echo ========================================
echo.
echo Package created:
echo   distribution\packages\LRU_Tracker_Windows.zip
echo.
echo Package contents:
echo   - LRU_Tracker.exe (standalone executable with custom icon)
echo   - INSTALL_INSTRUCTIONS.txt (simple setup guide)
echo.
echo File size: 
powershell -Command "(Get-Item 'distribution\packages\LRU_Tracker_Windows.zip').Length / 1MB | ForEach-Object {'{0:N2} MB' -f $_}"
echo.
echo ========================================
echo   HOW TO DISTRIBUTE
echo ========================================
echo.
echo 1. Share LRU_Tracker_Windows.zip with users
echo 2. Users extract the zip file
echo 3. Users double-click LRU_Tracker.exe
echo 4. No Python installation needed!
echo.
echo NOTE: Users may see a Windows SmartScreen warning
echo       They should click "More info" then "Run anyway"
echo.
echo ========================================

REM Open the folder
echo Opening distribution folder...
explorer distribution\packages

echo.
echo Build complete! You can now distribute the zip file.
echo.
pause
