#!/bin/bash
# Build script for macOS executable

echo "========================================"
echo "Building LRU Tracker for macOS"
echo "========================================"

# Check if PyInstaller is installed
if ! python3 -c "import PyInstaller" 2>/dev/null; then
    echo "Installing PyInstaller..."
    pip3 install pyinstaller
fi

# Navigate to parent directory
cd ..

# Build the executable
echo ""
echo "Creating macOS application bundle..."
pyinstaller --noconfirm --onefile --windowed \
    --name "LRU_Tracker" \
    --icon=NONE \
    --add-data "README.md:." \
    --hidden-import "openpyxl" \
    --hidden-import "pandas" \
    --hidden-import "tkinter" \
    --hidden-import "matplotlib" \
    --osx-bundle-identifier "com.fc.lrutracker" \
    refactored/lru_tracker_refactored.py

# Copy additional files
echo ""
echo "Copying additional files..."
cp README.md dist/
cp QUICK_START.md dist/
cp requirements.txt dist/
cp FC_SCHEDULE_IMPORT_GUIDE.md dist/
cp TEMPLATE_GUIDE.md dist/

# Create installer package
echo ""
echo "Creating installer package..."
mkdir -p "distribution/mac_installer"
cp -R dist/* "distribution/mac_installer/"
cp distribution/INSTALL_MAC.txt "distribution/mac_installer/INSTALL_INSTRUCTIONS.txt"

# Create DMG or zip package
echo ""
echo "Creating zip package..."
cd distribution
zip -r LRU_Tracker_Mac.zip mac_installer/
cd ..

echo ""
echo "========================================"
echo "Build complete!"
echo "========================================"
echo "macOS installer package: distribution/LRU_Tracker_Mac.zip"
echo ""
