# Testing Auto-Update Feature - v1.2.0

This guide explains how to test the auto-update feature with the new v1.2.0 Excel export improvements.

## 🎯 What We're Testing

1. **Feature Branch**: Enhanced Excel exports with better styling
2. **Auto-Update**: How existing v1.1.0 users will be notified of v1.2.0
3. **Update Flow**: Complete update experience from user perspective

## 📋 Testing Steps

### Step 1: Build v1.1.0 (Current Version)
```bash
# Make sure you're on main branch with v1.1.0
git checkout main
cd distribution
BUILD_WINDOWS_ONE_CLICK.bat
```

This creates your "current" version that users have installed.

### Step 2: Build v1.2.0 (New Version)
```bash
# Switch to feature branch
git checkout feature/enhanced-excel-export
cd distribution
BUILD_WINDOWS_ONE_CLICK.bat
```

This creates the new version with enhanced Excel exports.

### Step 3: Test the Excel Export Improvements

Run the v1.2.0 build and test:
1. Add some stations
2. Export to Excel
3. Check the new features:
   - ✅ Title row with timestamp
   - ✅ Enhanced color scheme (Red/Orange/Green)
   - ✅ Alternating row colors
   - ✅ Borders on all cells
   - ✅ Frozen header panes
   - ✅ Better column widths
   - ✅ Professional appearance

### Step 4: Test Auto-Update Notification

**Option A: Test Locally (Recommended)**

1. Run v1.1.0 executable
2. Temporarily modify `update_checker.py` to point to local version.json:
   ```python
   # In update_checker.py, change URL to local file for testing
   UPDATE_CHECK_URL = "file:///c:/path/to/version_v1.2.0.json"
   ```
3. Click "Check for Updates" in the app
4. Verify update dialog shows v1.2.0 with release notes

**Option B: Test with GitHub (After Release)**

1. Merge feature branch to main
2. Update version.json in main branch to v1.2.0
3. Create GitHub release v1.2.0
4. Run v1.1.0 executable
5. Click "Check for Updates"
6. Verify it detects v1.2.0

## 🔄 Complete Update Workflow

### For Developers (You)

1. **Develop Feature**
   ```bash
   git checkout -b feature/enhanced-excel-export
   # Make changes
   git add .
   git commit -m "Enhanced Excel export styling"
   ```

2. **Update Version**
   - Update `config.py`: APP_VERSION = "1.2.0"
   - Create release notes

3. **Build & Test**
   ```bash
   cd distribution
   BUILD_WINDOWS_ONE_CLICK.bat
   # Test the new features
   ```

4. **Merge to Main**
   ```bash
   git checkout main
   git merge feature/enhanced-excel-export
   git push origin main
   ```

5. **Create GitHub Release**
   - Go to: https://github.com/HaltTheGrey/lru-tracker/releases/new
   - Tag: v1.2.0
   - Upload: LRU_Tracker_Setup.exe
   - Copy release notes from version_v1.2.0.json

6. **Update version.json**
   ```bash
   # Replace version.json with version_v1.2.0.json content
   git add version.json
   git commit -m "Update version.json for v1.2.0"
   git push origin main
   ```

### For Users (Automatic)

1. **User opens v1.1.0 app**
2. **App checks for updates** (automatic or manual)
3. **Update notification appears** with:
   - Current version: 1.1.0
   - New version: 1.2.0
   - Release notes
   - Download button
4. **User clicks "Download Update"**
5. **Browser opens to GitHub release**
6. **User downloads and installs v1.2.0**
7. **User enjoys enhanced Excel exports!**

## 🎨 What's New in v1.2.0

### Excel Export Enhancements

**Before (v1.1.0):**
- Basic header styling
- Simple color coding
- No borders
- Plain appearance

**After (v1.2.0):**
- Professional title rows with timestamps
- Enhanced color scheme:
  - 🔴 Red: Below minimum (Critical)
  - 🟠 Orange: At/above maximum (Warning)
  - 🟢 Green: Normal range (Success)
- Alternating row colors (white/light gray)
- Consistent borders on all cells
- Frozen header panes
- Better fonts (Calibri)
- Improved column widths
- White text on colored status cells

### Technical Changes

**Files Modified:**
- `refactored/export_manager.py` - Complete styling overhaul
- `refactored/config.py` - Version bump to 1.2.0

**New Classes:**
- `ExcelColors` - Professional color palette

**New Methods:**
- `apply_cell_border()` - Consistent border styling

## 📊 Comparison Test

Create a side-by-side comparison:

1. Export from v1.1.0 → Save as "Report_v1.1.0.xlsx"
2. Export from v1.2.0 → Save as "Report_v1.2.0.xlsx"
3. Open both files and compare:
   - Visual appeal
   - Readability
   - Professional appearance
   - Print quality

## 🐛 Testing Checklist

- [ ] v1.1.0 builds successfully
- [ ] v1.2.0 builds successfully
- [ ] Excel exports work in v1.2.0
- [ ] Title rows appear correctly
- [ ] Colors are vibrant and clear
- [ ] Borders are consistent
- [ ] Alternating rows work
- [ ] Frozen panes work
- [ ] Status colors are correct (Red/Orange/Green)
- [ ] History sheet has same styling
- [ ] Append to existing works
- [ ] Auto-update detects v1.2.0
- [ ] Release notes display correctly
- [ ] Download link works

## 📝 Notes

- Keep v1.1.0 build for testing auto-update
- Test on clean machine if possible
- Verify Excel files open in Excel 2016+
- Check print preview for professional appearance
- Test with multiple stations for alternating rows

## 🚀 Release Checklist

- [ ] All tests pass
- [ ] Excel exports look professional
- [ ] Version updated to 1.2.0
- [ ] Build successful
- [ ] Merge to main
- [ ] Create GitHub release
- [ ] Upload installer
- [ ] Update version.json
- [ ] Test auto-update from v1.1.0
- [ ] Announce to users!

## 💡 Tips

- Use the same test data for both versions
- Take screenshots for documentation
- Test printing the Excel files
- Verify colors work in both light/dark Excel themes
- Check file size hasn't increased significantly
