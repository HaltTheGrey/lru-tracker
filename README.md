# 📦 LRU Tracker for Fulfillment Centers

Professional inventory tracking application for managing LRU (Lowest Replaceable Unit) counts at FC stations using a min/max pull system.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## ✨ Features

- **📊 Min/Max Pull System** - Color-coded status indicators (green/yellow/red)
- **🏭 Station Management** - Easy CRUD operations for FC stations
- **📈 LRU Tracking** - Update counts with automatic history logging
- **📁 Excel Export** - Export to new files or append to existing
- **📉 Trend Analysis** - Built-in charting for usage patterns
- **📋 Template System** - Download/import templates for bulk station setup
- **⚡ FC Schedule Import** - Import from FC Standard Work Spreadsheet
- **🖱️ Click-to-Select** - Quick station selection interface
- **🔄 Auto-Updates** - Automatic update checking and notifications
- **💾 Data Persistence** - All data saved locally in JSON format

## 🚀 Quick Start

### For End Users (Easy Install)

1. **Download the installer:**
   - Go to [Releases](https://github.com/HaltTheGrey/lru-tracker/releases)
   - Download `LRU_Tracker_Setup.exe`

2. **Run the installer:**
   - Double-click `LRU_Tracker_Setup.exe`
   - Follow the installation wizard
   - Choose desktop shortcut (optional)

3. **Launch and use:**
   - Open from Start Menu or desktop shortcut
   - Add your stations
   - Start tracking LRUs!

### For Developers

1. **Clone the repository:**
```bash
git clone https://github.com/HaltTheGrey/lru-tracker.git
cd lru-tracker
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the application:**
```bash
python lru_tracker.py
```

## 📋 Requirements

- Python 3.8 or higher
- Dependencies (see `requirements.txt`):
  - openpyxl 3.1.2
  - pandas 2.2.0
  - Pillow (for icon generation)

## 🏗️ Building from Source

### Windows Executable

1. **Navigate to distribution folder:**
```cmd
cd distribution
```

2. **Run the build script:**
```cmd
BUILD_WINDOWS_ONE_CLICK.bat
```

3. **Create installer (requires Inno Setup):**
   - Download [Inno Setup](https://jrsoftware.org/isdl.php)
   - Open `installer_script.iss` in Inno Setup Compiler
   - Press F9 to compile
   - Find installer in `distribution/packages/`

### Mac Application

```bash
cd distribution
chmod +x BUILD_MAC_ONE_CLICK.sh
./BUILD_MAC_ONE_CLICK.sh
```

## 📖 Documentation

- **[Quick Start Guide](QUICK_START.md)** - Get started in 5 minutes
- **[Template Feature Guide](TEMPLATE_FEATURE_GUIDE.md)** - Using templates
- **[FC Schedule Import Guide](FC_SCHEDULE_IMPORT_GUIDE.md)** - Import from spreadsheets
- **[Installer & Updates Guide](distribution/INSTALLER_AND_UPDATES_GUIDE.md)** - Creating installers and managing updates
- **[Build Instructions](distribution/BUILD_INSTRUCTIONS.md)** - Complete build process

## 🔄 Auto-Updates

The app includes built-in auto-update functionality:
- Click "🔄 Check for Updates" button in the app
- Get notified when new versions are available
- Download updates with one click
- Your data is automatically preserved

## 📊 Screenshots

### Main Interface
![Main Interface](screenshots/main_interface.png)
*Station management with color-coded status indicators*

### Trend Analysis
![Trend Analysis](screenshots/trend_analysis.png)
*Track LRU usage patterns over time*

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Bug Reports & Feature Requests

Found a bug or have a feature request? Please open an issue:
- [Report a Bug](https://github.com/HaltTheGrey/lru-tracker/issues/new?labels=bug)
- [Request a Feature](https://github.com/HaltTheGrey/lru-tracker/issues/new?labels=enhancement)

## 📧 Contact

Project Link: [https://github.com/HaltTheGrey/lru-tracker](https://github.com/HaltTheGrey/lru-tracker)

## 🙏 Acknowledgments

- Built for Amazon Fulfillment Center operations
- Designed to streamline LRU inventory management
- Reduces manual tracking time and errors

---

**Made with ❤️ for FC teams**
