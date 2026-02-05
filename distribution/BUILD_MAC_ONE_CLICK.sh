#!/bin/bash

# =============================================================================
# LRU TRACKER - ONE-CLICK BUILD & PACKAGE FOR macOS
# =============================================================================
# This script builds a standalone macOS .app that users can run
# without installing Python. The output is a zip file ready to distribute.
# =============================================================================

echo ""
echo "========================================"
echo "  LRU TRACKER - BUILD FOR macOS"
echo "========================================"
echo ""
echo "This will create a standalone .app file"
echo "No Python installation required to run!"
echo ""
read -p "Press Enter to continue..."

# Install PyInstaller if needed
echo ""
echo "[1/5] Checking PyInstaller..."
if ! python3 -c "import PyInstaller" 2>/dev/null; then
    echo "Installing PyInstaller..."
    pip3 install pyinstaller
    echo "PyInstaller installed!"
else
    echo "PyInstaller already installed."
fi

# Navigate to parent directory
cd ..

# Clean previous builds
echo ""
echo "[2/5] Cleaning previous builds..."
rm -rf dist build *.spec

# Build the application
echo ""
echo "[3/5] Building application (this may take a few minutes)..."
echo ""
python3 -m PyInstaller --noconfirm --onefile --windowed \
    --name "LRU_Tracker" \
    --icon "distribution/lru_icon.png" \
    --hidden-import "openpyxl" \
    --hidden-import "pandas" \
    --hidden-import "tkinter" \
    --hidden-import "matplotlib" \
    --osx-bundle-identifier "com.fc.lrutracker" \
    lru_tracker.py

if [ $? -ne 0 ]; then
    echo ""
    echo "========================================"
    echo "ERROR: Build failed!"
    echo "========================================"
    echo "Check the error messages above."
    echo ""
    exit 1
fi

# Copy only essential files
echo ""
echo "[4/5] Packaging installation guide..."
cp distribution/INSTALL_MAC.txt dist/INSTALL_INSTRUCTIONS.txt

# Create distribution package
echo ""
echo "[5/5] Creating distribution package..."
mkdir -p distribution/packages
cd dist
zip -r ../distribution/packages/LRU_Tracker_Mac.zip . -x "*.DS_Store"
cd ..

echo ""
echo "========================================"
echo "  BUILD SUCCESSFUL!"
echo "========================================"
echo ""
echo "Package created:"
echo "  distribution/packages/LRU_Tracker_Mac.zip"
echo ""
echo "Package contents:"
echo "  - LRU_Tracker.app (standalone application with custom icon)"
echo "  - INSTALL_INSTRUCTIONS.txt (simple setup guide)"
echo ""
echo "File size:"
du -h distribution/packages/LRU_Tracker_Mac.zip | awk '{print $1}'
echo ""
echo "========================================"
echo "  HOW TO DISTRIBUTE"
echo "========================================"
echo ""
echo "1. Share LRU_Tracker_Mac.zip with users"
echo "2. Users extract the zip file"
echo "3. Users move LRU_Tracker.app to Applications"
echo "4. Users right-click > Open (first time only)"
echo "5. No Python installation needed!"
echo ""
echo "NOTE: Users will see a Gatekeeper warning"
echo "      They should right-click the app and"
echo "      select 'Open' to bypass the warning"
echo ""
echo "========================================"
echo ""
echo "Build complete! You can now distribute the zip file."
echo ""
