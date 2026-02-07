# v1.2.8 - Fixed Incremental Update Detection 🐛

## Critical Bug Fix

This release fixes a critical issue in v1.2.7 where incremental updates were downloading the full installer instead of performing seamless exe-based updates.

## What's Fixed

### 🔧 Incremental Update Detection
- **Fixed:** Update checker now correctly detects exe-based incremental updates from `version.json`
- **Impact:** Users will now get the seamless update experience (no file explorer, automatic restart)
- **File:** `refactored/update_checker.py`

### ✨ User Experience Improvements
- **Silent Background Updates:** No console windows, fully automated
- **Better Messaging:** "Update Ready! The app will close and reopen automatically"
- **Progress Tracking:** Shows download progress in MB
- **Bandwidth Savings:** Downloads 128.7 MB exe instead of 141 MB installer (~12.3 MB savings)

### 🧹 Workspace Cleanup
- Deleted 25 redundant files (old release notes, duplicates, test files)
- Created comprehensive test suite (`test_incremental_updater.py` with 9 tests)
- Organized release notes into versioned folders
- Updated README.md to v1.2.8

## Expected Update Flow

When updating from v1.2.5, v1.2.6, or v1.2.7:

1. Click "🔄 Check for Updates" → Sees "⚡ Smart Update Available (128.7 MB)"
2. Click "⚡ Install Update" → Download progress shown
3. Click "Restart to Apply" → App closes → Silent update → App reopens automatically

**Total time:** ~3 seconds (depending on download speed)  
**Manual steps:** 0  
**User clicks:** 3

## Testing

All 32 tests passing:
- ✅ 9 incremental updater tests
- ✅ 11 model tests
- ✅ 12 validator tests

## Files

- **LRU_Tracker.exe** - Standalone executable (128.7 MB)
  - Windows 11 64-bit
  - Python 3.13.2 + PyInstaller 6.18.0
  - No Python installation required

## Installation

### New Users
1. Download `LRU_Tracker.exe`
2. Double-click to run
3. Click "More info" → "Run anyway" if Windows SmartScreen appears

### Existing Users
Just click "Check for Updates" in the app! The update will download and install automatically.

---

## Technical Details

### Modified Files
1. `refactored/update_checker.py` - Added exe-based incremental update detection
2. `refactored/lru_tracker_refactored.py` - Improved update messaging
3. `refactored/config.py` - Bumped version to 1.2.8
4. `version.json` - Updated with v1.2.8 details

### New Files
1. `refactored/tests/test_incremental_updater.py` - Comprehensive test suite
2. `CLEANUP_COMPLETE_v1.2.8.md` - Workspace cleanup documentation
3. `docs/release-notes/v1.2.8/RELEASE_SUMMARY.md` - Detailed release notes

### Commit
- SHA: 4c19526
- Message: "🐛 v1.2.8 - CRITICAL FIX: Incremental update detection now works from version.json"

---

## Upgrade Path

- v1.2.5 → v1.2.8: ✅ Incremental update (automatic)
- v1.2.6 → v1.2.8: ✅ Incremental update (automatic)
- v1.2.7 → v1.2.8: ✅ Incremental update (automatic, **FIXES BROKEN UPDATE**)
- v1.2.0 → v1.2.8: ⚠️ Manual download recommended
- v1.1.x → v1.2.8: ⚠️ Manual download recommended

---

**Full Changelog:** https://github.com/HaltTheGrey/lru-tracker/compare/v1.2.7...v1.2.8
