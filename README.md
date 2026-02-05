# 📦 LRU Tracker# 📦 LRU Tracker for Fulfillment Centers



**Warehouse FC Station LRU Tracking Application**Professional inventory tracking application for managing LRU (Lowest Replaceable Unit) counts at FC stations using a min/max pull system.



A professional desktop application for tracking LRUs (Lowest Replaceable Units) at Fulfillment Center stations with min/max pull system integration.![Version](https://img.shields.io/badge/version-1.0.0-blue)

![Python](https://img.shields.io/badge/python-3.8+-green)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)![License](https://img.shields.io/badge/license-MIT-orange)

[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)

[![Platform: Windows](https://img.shields.io/badge/platform-Windows-blue.svg)](https://github.com/HaltTheGrey/lru-tracker/releases)## ✨ Features



---- **📊 Min/Max Pull System** - Color-coded status indicators (green/yellow/red)

- **🏭 Station Management** - Easy CRUD operations for FC stations

## 🚀 Quick Start- **📈 LRU Tracking** - Update counts with automatic history logging

- **📁 Excel Export** - Export to new files or append to existing

### For End Users- **📉 Trend Analysis** - Built-in charting for usage patterns

- **📋 Template System** - Download/import templates for bulk station setup

**Download the latest release:**- **⚡ FC Schedule Import** - Import from FC Standard Work Spreadsheet

👉 [Get LRU Tracker](https://github.com/HaltTheGrey/lru-tracker/releases/latest)- **🖱️ Click-to-Select** - Quick station selection interface

- **🔄 Auto-Updates** - Automatic update checking and notifications

1. Download `LRU_Tracker_Setup.exe`- **💾 Data Persistence** - All data saved locally in JSON format

2. Run the installer

3. Launch from Start Menu## 🚀 Quick Start



📖 **User Documentation:** [`docs/user-guides/`](docs/user-guides/)### For End Users (Easy Install)



### For Developers1. **Download the installer:**

   - Go to [Releases](https://github.com/HaltTheGrey/lru-tracker/releases)

**Clone and run:**   - Download `LRU_Tracker_Setup.exe`

```powershell

git clone https://github.com/HaltTheGrey/lru-tracker.git2. **Run the installer:**

cd lru-tracker   - Double-click `LRU_Tracker_Setup.exe`

python -m venv .venv   - Follow the installation wizard

.venv\Scripts\Activate.ps1   - Choose desktop shortcut (optional)

pip install -r requirements.txt

python lru_tracker.py3. **Launch and use:**

```   - Open from Start Menu or desktop shortcut

   - Add your stations

📖 **Developer Documentation:** [`docs/developer-guides/`](docs/developer-guides/)   - Start tracking LRUs!



---### For Developers



## 📁 Project Structure1. **Clone the repository:**

```bash

```git clone https://github.com/HaltTheGrey/lru-tracker.git

lru-tracker/cd lru-tracker

│```

├── 📄 lru_tracker.py          # Main application (1622 lines)

├── 📄 auto_updater.py         # Auto-update functionality2. **Install dependencies:**

├── 📄 requirements.txt        # Python dependencies```bash

├── 📄 version.json            # Version info for auto-updatespip install -r requirements.txt

├── 📄 LICENSE                 # MIT License```

│

├── 📂 distribution/           # Executable builds & installers3. **Run the application:**

│   ├── BUILD_WINDOWS_ONE_CLICK.bat```bash

│   ├── BUILD_MAC_ONE_CLICK.shpython lru_tracker.py

│   ├── installer_script.iss  # Inno Setup script```

│   └── packages/              # Built executables

│## 📋 Requirements

├── 📂 scripts/                # Utility scripts

│   ├── START_APP.bat          # Quick launcher- Python 3.8 or higher

│   └── SETUP_GIT.bat          # Git configuration- Dependencies (see `requirements.txt`):

│  - openpyxl 3.1.2

├── 📂 docs/                   # All documentation  - pandas 2.2.0

│   ├── 📂 user-guides/        # End-user documentation  - Pillow (for icon generation)

│   │   ├── QUICK_START.md

│   │   ├── HOW_USERS_DOWNLOAD.md## 🏗️ Building from Source

│   │   ├── TEMPLATE_GUIDE.md

│   │   └── FC_SCHEDULE_IMPORT_GUIDE.md### Windows Executable

│   │

│   ├── 📂 developer-guides/   # Developer documentation1. **Navigate to distribution folder:**

│   │   ├── HOW_TO_UPDATE_APP.md```cmd

│   │   ├── RELEASE_GUIDE.mdcd distribution

│   │   ├── SETUP_GITHUB.md```

│   │   └── FIXES_SUMMARY.md

│   │2. **Run the build script:**

│   └── 📂 security/           # Security documentation```cmd

│       ├── SECURITY_ENHANCEMENTS.mdBUILD_WINDOWS_ONE_CLICK.bat

│       ├── SECURITY_WARNING_SOLUTIONS.md```

│       └── SECURITY_WARNING_VISUAL_GUIDE.md

│3. **Create installer (requires Inno Setup):**

├── 📂 .venv/                  # Python virtual environment (gitignored)   - Download [Inno Setup](https://jrsoftware.org/isdl.php)

├── 📂 build/                  # PyInstaller build files (gitignored)   - Open `installer_script.iss` in Inno Setup Compiler

└── 📂 dist/                   # PyInstaller output (gitignored)   - Press F9 to compile

```   - Find installer in `distribution/packages/`



---### Mac Application



## ✨ Features```bash

cd distribution

- ✅ **Min/Max Pull System** - Track current, min, and max LRUs per stationchmod +x BUILD_MAC_ONE_CLICK.sh

- ✅ **Station Management** - Add, edit, delete, and search stations./BUILD_MAC_ONE_CLICK.sh

- ✅ **Excel Export** - Export to Excel with formulas and formatting```

- ✅ **Trend Analysis** - Visual charts showing LRU trends

- ✅ **Template System** - Download/import templates for bulk setup## 📖 Documentation

- ✅ **FC Schedule Import** - Import from FC Standard Work Spreadsheet

- ✅ **Auto-Updates** - Built-in update checker with GitHub integration- **[Quick Start Guide](QUICK_START.md)** - Get started in 5 minutes

- ✅ **Click-to-Select** - Fast station selection with mouse clicks- **[Template Feature Guide](TEMPLATE_FEATURE_GUIDE.md)** - Using templates

- ✅ **Professional UI** - Clean, modern interface with scrollable layout- **[FC Schedule Import Guide](FC_SCHEDULE_IMPORT_GUIDE.md)** - Import from spreadsheets

- ✅ **Data Persistence** - Automatic JSON backup and atomic file writes- **[Installer & Updates Guide](distribution/INSTALLER_AND_UPDATES_GUIDE.md)** - Creating installers and managing updates

- ✅ **Security** - Input validation, HTTPS-only, path traversal prevention- **[Build Instructions](distribution/BUILD_INSTRUCTIONS.md)** - Complete build process



---## 🔄 Auto-Updates



## 🛠️ Tech StackThe app includes built-in auto-update functionality:

- Click "🔄 Check for Updates" button in the app

- **Language:** Python 3.13- Get notified when new versions are available

- **GUI Framework:** tkinter- Download updates with one click

- **Data Processing:** pandas, openpyxl- Your data is automatically preserved

- **Packaging:** PyInstaller, Inno Setup

- **Version Control:** Git, GitHub## 📊 Screenshots

- **Security:** Regex validation, atomic file operations, HTTPS

### Main Interface

---![Main Interface](screenshots/main_interface.png)

*Station management with color-coded status indicators*

## 📖 Documentation Index

### Trend Analysis

### 👥 User Guides![Trend Analysis](screenshots/trend_analysis.png)

- **[Quick Start](docs/user-guides/QUICK_START.md)** - Get started in 5 minutes*Track LRU usage patterns over time*

- **[Download & Install](docs/user-guides/HOW_USERS_DOWNLOAD.md)** - Installation guide

- **[Template System](docs/user-guides/TEMPLATE_GUIDE.md)** - Bulk station setup## 🤝 Contributing

- **[FC Schedule Import](docs/user-guides/FC_SCHEDULE_IMPORT_GUIDE.md)** - Import from spreadsheets

Contributions are welcome! Please feel free to submit a Pull Request.

### 👨‍💻 Developer Guides

- **[Update & Release](docs/developer-guides/HOW_TO_UPDATE_APP.md)** - Complete update process1. Fork the repository

- **[GitHub Release Guide](docs/developer-guides/RELEASE_GUIDE.md)** - Creating releases2. Create your feature branch (`git checkout -b feature/AmazingFeature`)

- **[GitHub Setup](docs/developer-guides/SETUP_GITHUB.md)** - Repository configuration3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)

- **[Fixes Summary](docs/developer-guides/FIXES_SUMMARY.md)** - Recent improvements4. Push to the branch (`git push origin feature/AmazingFeature`)

5. Open a Pull Request

### 🔒 Security Documentation

- **[Security Enhancements](docs/security/SECURITY_ENHANCEMENTS.md)** - Security features & best practices## 📝 License

- **[Windows SmartScreen](docs/security/SECURITY_WARNING_SOLUTIONS.md)** - Handling security warnings

- **[Visual Security Guide](docs/security/SECURITY_WARNING_VISUAL_GUIDE.md)** - Step-by-step screenshotsThis project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



---## 🐛 Bug Reports & Feature Requests



## 🚀 Quick CommandsFound a bug or have a feature request? Please open an issue:

- [Report a Bug](https://github.com/HaltTheGrey/lru-tracker/issues/new?labels=bug)

### Run Application- [Request a Feature](https://github.com/HaltTheGrey/lru-tracker/issues/new?labels=enhancement)

```powershell

# Activate virtual environment## 📧 Contact

.venv\Scripts\Activate.ps1

Project Link: [https://github.com/HaltTheGrey/lru-tracker](https://github.com/HaltTheGrey/lru-tracker)

# Run app

python lru_tracker.py## 🙏 Acknowledgments



# Or use quick launcher- Built for Amazon Fulfillment Center operations

.\scripts\START_APP.bat- Designed to streamline LRU inventory management

```- Reduces manual tracking time and errors



### Build Executable---

```powershell

# Navigate to distribution**Made with ❤️ for FC teams**

cd distribution

# Build Windows installer
.\BUILD_WINDOWS_ONE_CLICK.bat

# Output: packages\LRU_Tracker_Setup.exe
```

### Update Dependencies
```powershell
# Activate venv
.venv\Scripts\Activate.ps1

# Install/update packages
pip install -r requirements.txt

# Check for vulnerabilities
pip-audit
```

---

## 🔄 Version History

- **v1.0.0** (Feb 5, 2026) - Initial release
  - Min/max pull system
  - Station CRUD operations
  - Excel export & trend analysis
  - Template & FC import
  - Auto-update system
  - Security enhancements

---

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details

---

## 🤝 Contributing

This is an internal FC tool. For bug reports or feature requests:
1. Open an [Issue](https://github.com/HaltTheGrey/lru-tracker/issues)
2. Or submit a [Pull Request](https://github.com/HaltTheGrey/lru-tracker/pulls)

---

## 📧 Support

**Questions or issues?**
- 📖 Check the [documentation](docs/)
- 🐛 Report bugs via [GitHub Issues](https://github.com/HaltTheGrey/lru-tracker/issues)
- 💬 Contact the maintainer

---

## 🎯 Roadmap

Future enhancements:
- [ ] Multi-language support
- [ ] Cloud data sync
- [ ] Mobile companion app
- [ ] Advanced analytics dashboard
- [ ] Team collaboration features

---

**Built with ❤️ for FC Operations**
