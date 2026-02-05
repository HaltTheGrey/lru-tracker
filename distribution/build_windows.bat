@echo off
REM Build script for Windows executable
echo ========================================
echo Building LRU Tracker for Windows
echo ========================================

REM Check if PyInstaller is installed
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo Installing PyInstaller...
    pip install pyinstaller
)

REM Navigate to parent directory
cd ..

REM Build the executable
echo.
echo Creating Windows executable...
python -m PyInstaller --noconfirm --onefile --windowed ^
    --name "LRU_Tracker" ^
    --icon "distribution\lru_icon.ico" ^
    --hidden-import "openpyxl" ^
    --hidden-import "pandas" ^
    --hidden-import "tkinter" ^
    --hidden-import "matplotlib" ^
    lru_tracker.py

REM Copy only essential files to dist folder
echo.
echo Copying installation guide...
copy distribution\INSTALL_WINDOWS.txt dist\INSTALL_INSTRUCTIONS.txt

REM Create installer package
echo.
echo Creating installer package...
if not exist "distribution\windows_installer" mkdir "distribution\windows_installer"
xcopy /E /I /Y dist "distribution\windows_installer\LRU_Tracker"
copy distribution\INSTALL_WINDOWS.txt distribution\windows_installer\INSTALL_INSTRUCTIONS.txt

REM Create zip package
echo.
echo Creating zip package...
powershell Compress-Archive -Path "distribution\windows_installer\*" -DestinationPath "distribution\LRU_Tracker_Windows.zip" -Force

echo.
echo ========================================
echo Build complete!
echo ========================================
echo Windows installer package: distribution\LRU_Tracker_Windows.zip
echo.
pause
