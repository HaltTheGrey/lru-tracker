@echo off
REM ===================================================================
REM  LRU Tracker - Smart Update Applier
REM ===================================================================
REM This script runs after the app closes to replace the executable
REM with the newly downloaded version.
REM ===================================================================

echo.
echo ========================================
echo   LRU Tracker Update Applier
echo ========================================
echo.
echo Waiting for application to close...
timeout /t 2 /nobreak >nul

REM Get the directory where this script is located
set "APP_DIR=%~dp0"
cd /d "%APP_DIR%"

REM Check if new exe exists
if not exist "LRU_Tracker.exe.new" (
    echo ERROR: Update file not found!
    echo Expected: %APP_DIR%LRU_Tracker.exe.new
    pause
    exit /b 1
)

REM Backup current exe
echo.
echo Creating backup...
if exist "LRU_Tracker.exe" (
    if exist "LRU_Tracker.exe.backup" del "LRU_Tracker.exe.backup"
    move "LRU_Tracker.exe" "LRU_Tracker.exe.backup" >nul
    if errorlevel 1 (
        echo ERROR: Could not backup current version!
        pause
        exit /b 1
    )
    echo Backup created: LRU_Tracker.exe.backup
)

REM Replace with new version
echo.
echo Installing update...
move "LRU_Tracker.exe.new" "LRU_Tracker.exe" >nul
if errorlevel 1 (
    echo ERROR: Could not install update!
    echo Restoring backup...
    if exist "LRU_Tracker.exe.backup" (
        move "LRU_Tracker.exe.backup" "LRU_Tracker.exe" >nul
    )
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Update Installed Successfully!
echo ========================================
echo.
echo Starting updated application...
timeout /t 1 /nobreak >nul

REM Start the updated application
start "" "%APP_DIR%LRU_Tracker.exe"

REM Clean up backup after successful start
timeout /t 2 /nobreak >nul
if exist "LRU_Tracker.exe.backup" del "LRU_Tracker.exe.backup"

REM Self-destruct this update script
(goto) 2>nul & del "%~f0"
