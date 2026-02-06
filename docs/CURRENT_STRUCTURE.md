# 📁 LRU Tracker - Current Project Structure

**Last Updated:** February 6, 2026  
**Current Version:** v1.2.0  
**Architecture:** Modular (Refactored from Monolith)

---

## 🎯 Quick Overview

This project has evolved from a monolithic 1,622-line file to a well-organized modular architecture with 85% test coverage.

**What to use:**
- ✅ **`refactored/`** - Current production code (USE THIS!)
- 📦 **`archive/`** - Original code (reference only)
- 📚 **`docs/`** - All documentation
- 🔨 **`distribution/`** - Build tools

---

## 📂 Complete Directory Structure

```
lru-tracker/
│
├── 📄 README.md                          # Main project documentation
├── 📄 LICENSE                            # MIT License
├── 📄 requirements.txt                   # Python dependencies (pinned versions)
├── 📄 version.json                       # Version info for auto-updates
├── 📄 .gitignore                         # Git exclusions
├── 📄 LRU_Tracker.spec                   # PyInstaller specification
│
├── 📂 refactored/                        # ✨ PRODUCTION CODE (v1.2.0)
│   │
│   ├── 📄 lru_tracker_refactored.py     # Main application entry point
│   ├── 📄 config.py                      # Configuration management
│   ├── 📄 models.py                      # Data models (Station, LRUData)
│   ├── 📄 validators.py                  # Input validation & sanitization
│   ├── 📄 data_manager.py                # Data persistence (JSON)
│   ├── 📄 export_manager.py              # Excel export (v1.2.0 enhanced styling!)
│   ├── 📄 template_manager.py            # Template import/export
│   ├── 📄 fc_schedule_manager.py         # FC schedule CSV integration
│   ├── 📄 update_checker.py              # Auto-update functionality
│   ├── 📄 update_checker_TEST_MODE.py    # Update checker with test mode
│   ├── 📄 logger.py                      # Centralized logging system
│   ├── 📄 error_handler.py               # Error handling decorators
│   ├── 📄 README.md                      # Refactored code documentation
│   │
│   └── 📂 tests/                         # Unit tests (85% coverage)
│       ├── test_validators.py            # Validation tests
│       ├── test_data_manager.py          # Data persistence tests
│       ├── test_export_manager.py        # Export functionality tests
│       ├── test_template_manager.py      # Template tests
│       ├── test_fc_schedule_manager.py   # FC schedule tests
│       ├── test_update_checker.py        # Update checker tests
│       ├── test_update_detection.py      # Update detection tests
│       ├── test_update_server.py         # Update server tests
│       ├── test_models.py                # Model tests
│       ├── test_config.py                # Config tests
│       └── __pycache__/                  # Python cache (gitignored)
│
├── 📂 archive/                           # Original monolith code (REFERENCE ONLY)
│   ├── 📄 lru_tracker.py                 # Original 1,622-line monolithic file
│   ├── 📄 auto_updater.py                # Original auto-updater
│   └── 📄 README.md                      # Archive documentation
│
├── 📂 distribution/                      # Build tools & packaging
│   ├── 📄 BUILD_WINDOWS_ONE_CLICK.bat    # Windows build script
│   ├── 📄 BUILD_MAC_ONE_CLICK.sh         # Mac build script
│   ├── 📄 build_windows.bat              # Detailed Windows build
│   ├── 📄 build_mac.sh                   # Detailed Mac build
│   ├── 📄 installer_script.iss           # Inno Setup installer script
│   ├── 📄 create_icon.py                 # Icon generation script
│   ├── 📄 create_release_package.py      # Release packaging
│   ├── 📄 version.json                   # Distribution version info
│   ├── 🖼️ lru_icon.ico                   # Application icon (ICO)
│   ├── 🖼️ lru_icon.png                   # Application icon (PNG)
│   ├── 📂 packages/                      # Built executables
│   │   ├── LRU_Tracker_Windows.zip       # Windows package
│   │   └── ...                           # Other builds
│   └── 📄 README_DISTRIBUTION.md         # Distribution documentation
│
├── 📂 scripts/                           # Utility scripts
│   ├── 📄 START_APP.bat                  # Quick launcher for Windows
│   ├── 📄 SETUP_GIT.bat                  # Git configuration helper
│   └── 📄 PUSH_TO_GITHUB.bat            # GitHub push automation
│
├── 📂 docs/                              # 📚 All Documentation
│   │
│   ├── 📂 user-guides/                   # End-user documentation
│   │   ├── QUICK_START.md                # Get started in 5 minutes
│   │   ├── HOW_USERS_DOWNLOAD.md         # Download & installation
│   │   ├── TEMPLATE_GUIDE.md             # Template system usage
│   │   ├── TEMPLATE_FEATURE_GUIDE.md     # Advanced template features
│   │   └── FC_SCHEDULE_IMPORT_GUIDE.md   # FC schedule import guide
│   │
│   ├── 📂 developer-guides/              # Developer documentation
│   │   ├── HOW_TO_UPDATE_APP.md          # Update & release process
│   │   ├── RELEASE_GUIDE.md              # GitHub release creation
│   │   ├── SETUP_GITHUB.md               # Repository setup
│   │   ├── GITHUB_CHECKLIST.md           # Release checklist
│   │   ├── FIXES_SUMMARY.md              # Code fixes summary
│   │   ├── FIX_IMPORT_WARNINGS.md        # VS Code import warnings fix
│   │   ├── REFACTORING_GUIDE.md          # Architecture & refactoring
│   │   ├── IMPROVEMENTS.md               # Recent improvements
│   │   ├── WORKSPACE_GUIDE.md            # Workspace organization
│   │   ├── FILE_INDEX.md                 # File reference index
│   │   ├── LOCAL_TESTING_QUICK_GUIDE.md  # Testing guide
│   │   └── TESTING_AUTO_UPDATE_v1.2.0.md # Auto-update testing
│   │
│   ├── 📂 release-notes/                 # Version release notes
│   │   ├── 📂 v1.1.0/                    # Version 1.1.0
│   │   │   ├── GITHUB_RELEASE_v1.1.0.md
│   │   │   └── RELEASE_CHECKLIST_v1.1.0.md
│   │   └── 📂 v1.2.0/                    # Version 1.2.0 (current)
│   │       ├── GITHUB_RELEASE_v1.2.0.md
│   │       ├── FEATURE_BRANCH_SUMMARY_v1.2.0.md
│   │       └── MERGE_COMPLETE_v1.2.0.md
│   │
│   └── 📂 security/                      # Security documentation
│       ├── SECURITY_ENHANCEMENTS.md      # Security features & best practices
│       ├── SECURITY_WARNING_SOLUTIONS.md # Windows SmartScreen solutions
│       └── SECURITY_WARNING_VISUAL_GUIDE.md # Visual security guide
│
├── 📂 logs/                              # Application logs (gitignored)
│   └── lru_tracker.log                   # Runtime logs
│
├── 📂 build/                             # PyInstaller build files (gitignored)
├── 📂 dist/                              # PyInstaller output (gitignored)
├── 📂 .venv/                             # Python virtual environment (gitignored)
├── 📂 .vscode/                           # VS Code settings (gitignored)
├── 📂 .git/                              # Git repository
└── 📂 __pycache__/                       # Python cache (gitignored)
```

---

## 🗂️ File Categories

### Production Code (refactored/)
**Purpose:** Current working code - actively maintained  
**Test Coverage:** 85%  
**Lines of Code:** ~2,500  
**Modules:** 10 focused modules

| File | Purpose | Lines | Key Functions |
|------|---------|-------|---------------|
| `lru_tracker_refactored.py` | Main GUI application | ~800 | Application entry, UI management |
| `config.py` | Configuration | ~100 | Settings, paths, constants |
| `models.py` | Data models | ~150 | Station, LRUData classes |
| `validators.py` | Input validation | ~200 | Regex validation, sanitization |
| `data_manager.py` | Data persistence | ~250 | JSON save/load, backups |
| `export_manager.py` | Excel exports | ~400 | Enhanced Excel styling (v1.2.0) |
| `template_manager.py` | Template I/O | ~200 | Import/export templates |
| `fc_schedule_manager.py` | FC integration | ~150 | CSV import from FC schedules |
| `update_checker.py` | Auto-updates | ~200 | GitHub version checking |
| `logger.py` | Logging | ~100 | Centralized logging |
| `error_handler.py` | Error handling | ~150 | Decorators, error messages |

### Archive Code (archive/)
**Purpose:** Historical reference - DO NOT MODIFY  
**Status:** Frozen at v1.0.0  
**Lines of Code:** ~1,622 (monolith)

| File | Purpose | Status |
|------|---------|--------|
| `lru_tracker.py` | Original monolithic app | Archived |
| `auto_updater.py` | Original updater | Archived |

### Documentation (docs/)
**Purpose:** All project documentation  
**Total Files:** 25+ markdown files  
**Categories:** User guides, Developer guides, Release notes, Security

### Build Tools (distribution/)
**Purpose:** Create installable packages  
**Platforms:** Windows, macOS  
**Installer:** Inno Setup (Windows)

---

## 🔍 File Types by Extension

### Python Files (.py)
- **Production:** 11 files in `refactored/`
- **Tests:** 10+ files in `refactored/tests/`
- **Archive:** 2 files in `archive/`
- **Build Tools:** 2 files in `distribution/`

### Documentation (.md)
- **Root:** 1 file (README.md)
- **User Guides:** 5 files
- **Developer Guides:** 12 files
- **Release Notes:** 5 files
- **Security:** 3 files

### Configuration Files
- `requirements.txt` - Python dependencies
- `version.json` - Version info
- `.gitignore` - Git exclusions
- `LRU_Tracker.spec` - PyInstaller spec

### Build Files
- `BUILD_WINDOWS_ONE_CLICK.bat` - Windows build
- `BUILD_MAC_ONE_CLICK.sh` - Mac build
- `installer_script.iss` - Inno Setup
- `create_icon.py` - Icon generation

---

## 📊 Code Metrics

### Production Code (refactored/)
| Metric | Value |
|--------|-------|
| Total Modules | 10 |
| Total Lines | ~2,500 |
| Test Files | 10+ |
| Test Cases | 35+ |
| Test Coverage | 85% |
| Code-to-Test Ratio | 1:1.2 |

### Documentation
| Category | Files |
|----------|-------|
| User Guides | 5 |
| Developer Guides | 12 |
| Release Notes | 5 |
| Security Docs | 3 |
| **Total** | **25+** |

---

## 🎯 What to Use When

### "I want to run the app"
```bash
cd refactored
python lru_tracker_refactored.py
```

### "I want to build an executable"
```bash
cd distribution
# Windows
.\BUILD_WINDOWS_ONE_CLICK.bat

# Mac
./BUILD_MAC_ONE_CLICK.sh
```

### "I want to run tests"
```bash
cd refactored
pytest tests/ -v
```

### "I want to see test coverage"
```bash
cd refactored
pytest tests/ --cov=. --cov-report=html
```

### "I want to understand the architecture"
Read: `docs/developer-guides/REFACTORING_GUIDE.md`

### "I want to release a new version"
Read: `docs/developer-guides/HOW_TO_UPDATE_APP.md`

### "I want to see what changed in v1.2.0"
Read: `docs/release-notes/v1.2.0/`

---

## 🚫 What NOT to Use

### ❌ archive/
- **Don't edit** - Historical reference only
- **Don't run** - Use `refactored/` instead
- **Don't delete** - Kept for comparison

### ❌ build/ and dist/
- **Auto-generated** - Created by PyInstaller
- **Gitignored** - Not tracked in version control
- **Rebuild anytime** - Safe to delete

### ❌ __pycache__/
- **Python cache** - Auto-generated
- **Gitignored** - Not tracked
- **Safe to delete** - Python recreates it

---

## 🔄 Version History

### v1.2.0 (Current) - February 5, 2026
**Enhanced Excel Exports**
- Professional Excel styling with enhanced colors
- Title rows with timestamps
- Alternating row colors
- Better status indicators (Red/Orange/Green)
- Frozen header panes
- Improved readability

### v1.1.0 - Previous
**Refactored Architecture**
- Split monolith into 10 modules
- Added 85% test coverage
- Implemented logging system
- Added template import/export
- FC schedule integration
- Comprehensive error handling

### v1.0.0 - Initial
**Monolithic Version**
- Single 1,622-line file
- Basic functionality
- No tests
- Limited error handling

---

## 📋 Maintenance

### Monthly Tasks
- [ ] Review and update dependencies
- [ ] Run security audit (`pip-audit`)
- [ ] Check for unused files
- [ ] Update documentation if structure changes
- [ ] Review and close old issues

### Before Each Release
- [ ] Run full test suite
- [ ] Update version numbers
- [ ] Update CHANGELOG
- [ ] Build and test executables
- [ ] Create GitHub release
- [ ] Update version.json

---

## 🔗 Key Files Reference

### Must Read First
1. `README.md` - Project overview
2. `docs/developer-guides/REFACTORING_GUIDE.md` - Architecture
3. `docs/user-guides/QUICK_START.md` - How to use

### For Development
1. `refactored/README.md` - Refactored code docs
2. `docs/developer-guides/LOCAL_TESTING_QUICK_GUIDE.md` - Testing
3. `docs/developer-guides/HOW_TO_UPDATE_APP.md` - Releases

### For Building
1. `distribution/BUILD_INSTRUCTIONS.md` - Build process
2. `distribution/README_DISTRIBUTION.md` - Distribution docs

---

## 🎓 Understanding the Structure

### Why refactored/ and archive/?
- **archive/** = Original monolithic code (v1.0.0)
- **refactored/** = New modular code (v1.1.0+)
- Kept archive for reference and rollback capability

### Why so many docs/ subfolders?
- **user-guides/** = End users who run the app
- **developer-guides/** = Developers who maintain code
- **release-notes/** = Version-specific changes
- **security/** = Security features and warnings

### Why tests/ inside refactored/?
- Tests live with the code they test
- Makes it clear what's tested vs what's not
- Easier to run: `cd refactored && pytest tests/`

---

## 📌 Quick Navigation

### User Documentation
- 📖 Quick Start → `docs/user-guides/QUICK_START.md`
- 📥 Download → `docs/user-guides/HOW_USERS_DOWNLOAD.md`
- 📋 Templates → `docs/user-guides/TEMPLATE_GUIDE.md`
- 📊 FC Import → `docs/user-guides/FC_SCHEDULE_IMPORT_GUIDE.md`

### Developer Documentation
- 🏗️ Architecture → `docs/developer-guides/REFACTORING_GUIDE.md`
- 📦 Build → `distribution/BUILD_INSTRUCTIONS.md`
- 🧪 Testing → `docs/developer-guides/LOCAL_TESTING_QUICK_GUIDE.md`
- 🚀 Release → `docs/developer-guides/HOW_TO_UPDATE_APP.md`

### Release Information
- 📰 Latest (v1.2.0) → `docs/release-notes/v1.2.0/`
- 📰 Previous (v1.1.0) → `docs/release-notes/v1.1.0/`

---

## ✅ Structure Benefits

1. **Clear Separation** - Production vs Archive vs Docs
2. **Easy Navigation** - Logical folder hierarchy
3. **Self-Documenting** - Folder names explain purpose
4. **Scalable** - Room to grow without clutter
5. **Professional** - Industry-standard organization
6. **Testable** - Tests organized with code
7. **Maintainable** - Easy to find and update files

---

**Last Structure Update:** February 6, 2026  
**Maintained By:** Project maintainers  
**Status:** ✅ Clean and organized
