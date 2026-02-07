# LRU Tracker for Fulfillment Centers

Inventory tracking application for managing LRU (Lowest Replaceable Unit) counts at FC stations using a min/max pull system.

**Version: 1.2.8** | Python 3.8+ | License: MIT

[![GitHub Release](https://img.shields.io/badge/release-v1.2.8-blue)](https://github.com/HaltTheGrey/lru-tracker/releases/tag/v1.2.8)
[![Python](https://img.shields.io/badge/python-3.8+-green)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)
[![Test Coverage](https://img.shields.io/badge/coverage-85%25-brightgreen)](refactored/tests/)

## Features

### v1.2.8 - Seamless Auto-Updates ✨
- **Fixed Incremental Updates** - Now correctly detects exe-based updates from version.json
- **Silent Background Updates** - No console windows, fully automated process
- **Smart Update Detection** - Downloads 127 MB exe instead of 141 MB installer (10% savings)
- **Automated Restart** - App closes, updates, and reopens automatically

### Previous Features
- **Professional Excel Exports** (v1.2.0) - Enhanced styling, colors, formatting
- **Incremental Updates** (v1.2.2) - Bandwidth-saving update system
- **Permission Handling** (v1.2.1) - Works in restricted folders

### Core Features
- **Min/Max Pull System** - Color-coded status indicators
- **Station Management** - Full CRUD operations
- **LRU Tracking** - Automatic history logging
- **Excel Export** - New files or append to existing
- **Trend Analysis** - Built-in charting
- **Template System** - Bulk station setup
- **FC Schedule Import** - Standard Work Spreadsheet integration
- **Auto-Updates** - Seamless version checking with GitHub integration
- **Data Persistence** - JSON format with backups

## Quick Start

### For End Users

1. Install Python 3.8+ (if not already installed)
2. Clone or download this repository
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   cd refactored
   python lru_tracker_refactored.py
   ```

### For Developers

```bash
# Clone repository
git clone https://github.com/HaltTheGrey/lru-tracker.git
cd lru-tracker

# Install dependencies
pip install -r requirements.txt

# Run application
cd refactored
python lru_tracker_refactored.py

# Run tests
pytest tests/ -v
```

## Project Structure

```
lru-tracker/
│
├── 📄 README.md                    # Project overview
├── 📄 LICENSE                      # MIT License  
├── 📄 requirements.txt             # Python dependencies
├── 📄 version.json                 # Version info for auto-updates
│
├── 📂 refactored/                  # ✨ PRODUCTION CODE (use this!)
│   ├── lru_tracker_refactored.py  # Main application
│   ├── config.py                  # Configuration management
│   ├── models.py                  # Data models
│   ├── validators.py              # Input validation
│   ├── data_manager.py            # Data persistence
│   ├── export_manager.py          # Excel export (v1.2.0 enhanced!)
│   ├── template_manager.py        # Template import/export
│   ├── fc_schedule_manager.py     # FC schedule integration
│   ├── update_checker.py          # Auto-update functionality
│   ├── logger.py                  # Logging system
│   ├── error_handler.py           # Error handling
│   ├── README.md                  # Refactored code docs
│   └── tests/                     # Unit tests (85% coverage)
│       ├── test_validators.py
│       ├── test_data_manager.py
│       ├── test_export_manager.py
│       ├── test_update_detection.py
│       └── ...
│
├── 📂 archive/                     # Original monolith code (reference only)
│   ├── lru_tracker.py             # Original 1,622-line file
│   ├── auto_updater.py            # Original updater
│   └── README.md                  # Archive documentation
│
├── 📂 distribution/                # Build tools & installers
│   ├── BUILD_WINDOWS_ONE_CLICK.bat
│   ├── BUILD_MAC_ONE_CLICK.sh
│   ├── installer_script.iss       # Inno Setup script
│   ├── create_icon.py             # Icon generation
│   └── packages/                  # Built executables
│
├── 📂 scripts/                     # Utility scripts
│   ├── START_APP.bat
│   └── SETUP_GIT.bat
│
├── 📂 docs/                        # 📚 All documentation
│   ├── 📂 user-guides/            # End-user documentation
│   │   ├── QUICK_START.md
│   │   ├── HOW_USERS_DOWNLOAD.md
│   │   ├── TEMPLATE_GUIDE.md
│   │   └── FC_SCHEDULE_IMPORT_GUIDE.md
│   │
│   ├── 📂 developer-guides/       # Developer documentation
│   │   ├── HOW_TO_UPDATE_APP.md
│   │   ├── RELEASE_GUIDE.md
│   │   ├── SETUP_GITHUB.md
│   │   ├── REFACTORING_GUIDE.md
│   │   ├── IMPROVEMENTS.md
│   │   └── ...
│   │
│   ├── 📂 release-notes/          # Version release notes
│   │   ├── v1.1.0/
│   │   └── v1.2.0/
│   │
│   └── 📂 security/               # Security documentation
│       ├── SECURITY_ENHANCEMENTS.md
│       └── ...
│
└── 📂 logs/                        # Application logs (gitignored)
```

## Documentation

### User Guides
- [Quick Start Guide](docs/user-guides/QUICK_START.md) - Get started in 5 minutes
- [Template Guide](docs/user-guides/TEMPLATE_GUIDE.md) - Bulk station setup
- [FC Schedule Import](docs/user-guides/FC_SCHEDULE_IMPORT_GUIDE.md) - Import from spreadsheets

### Developer Guides
- [Refactoring Guide](docs/developer-guides/REFACTORING_GUIDE.md) - Architecture overview
- [Improvements Summary](docs/developer-guides/IMPROVEMENTS.md) - Recent enhancements
- [Testing Guide](docs/developer-guides/LOCAL_TESTING_QUICK_GUIDE.md) - How to run tests
- [Update Guide](docs/developer-guides/HOW_TO_UPDATE_APP.md) - Release process

### Release Notes
- [v1.2.0 - Enhanced Excel Exports](docs/release-notes/v1.2.0/) - Latest release
- [v1.1.0 - Refactored Architecture](docs/release-notes/v1.1.0/) - Major refactor

### Security
- [Security Enhancements](docs/security/SECURITY_ENHANCEMENTS.md) - Security features

## Testing

```bash
cd refactored
pytest tests/ -v
pytest tests/ --cov=. --cov-report=html
```

Test Coverage: 85%

## Security Features

- Input validation with regex patterns
- Path traversal prevention
- HTTPS-only update checks
- Atomic file writes with backups
- Sanitized error messages
- Comprehensive logging

## Code Quality

| Metric | Value |
|--------|-------|
| Total Modules | 10 |
| Test Coverage | 85% |
| Lines of Code | ~2,500 |
| Test Cases | 35+ |

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Support

- Check the [documentation](docs/)
- Report bugs via [GitHub Issues](https://github.com/HaltTheGrey/lru-tracker/issues)
- Contact the maintainer
