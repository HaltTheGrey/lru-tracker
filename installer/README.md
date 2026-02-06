# 📦 LRU Tracker Installer Guide

This folder contains the Inno Setup installer configuration for creating a professional Windows installer for LRU Tracker.

## 🎯 What You Get

The installer provides:
- ✅ **Professional wizard interface** - Guided installation process
- ✅ **Start Menu shortcuts** - Easy access to the app
- ✅ **Desktop icon** - Optional shortcut on desktop
- ✅ **Automatic uninstaller** - Clean removal via Control Panel
- ✅ **Version information** - Proper Windows metadata
- ✅ **LZMA compression** - Reduces file size from 127 MB to ~45-50 MB
- ✅ **No admin rights needed** - Installs per-user by default
- ✅ **Custom branding** - Uses your app icon and info

## 📋 Prerequisites

**1. Install Inno Setup (FREE)**
- Download: https://jrsoftware.org/isdl.php
- Click "Download Inno Setup 6.x"
- Run the installer (default location is fine)
- Takes ~2 minutes

**2. Build the Executable**
```batch
.\BUILD_REFACTORED.bat
```
This creates `dist\LRU_Tracker.exe`

## 🚀 Quick Start

### Option 1: Use the Build Script (Easiest)
```batch
.\BUILD_INSTALLER.bat
```

This will:
1. Check if Inno Setup is installed
2. Verify the executable exists
3. Compile the installer
4. Open the output folder

**Output:** `distribution\installer\LRU_Tracker_Setup_v1.2.2.exe`

### Option 2: Manual Compilation
1. Open Inno Setup Compiler
2. File → Open → Select `installer\LRU_Tracker_Setup.iss`
3. Build → Compile
4. Done!

## 📁 File Structure

```
lru-tracker/
├── installer/
│   ├── LRU_Tracker_Setup.iss    ← Installer script (edit this)
│   └── README.md                ← This file
├── dist/
│   └── LRU_Tracker.exe          ← Built executable (required)
├── distribution/
│   ├── lru_icon.ico             ← App icon (used by installer)
│   └── installer/               ← Output folder
│       └── LRU_Tracker_Setup_v1.2.2.exe  ← Final installer
├── docs/                        ← Included in installer
├── README.md                    ← Included in installer
├── LICENSE                      ← Shown during installation
└── BUILD_INSTALLER.bat          ← Build script
```

## ⚙️ Customization

Edit `LRU_Tracker_Setup.iss` to customize:

### Change Version Number
```pascal
#define MyAppVersion "1.2.2"
```

### Change Install Location
```pascal
DefaultDirName={autopf}\{#MyAppName}  ; Program Files
; or
DefaultDirName={userdocs}\{#MyAppName}  ; Documents folder
```

### Add More Files
```pascal
[Files]
Source: "path\to\file.txt"; DestDir: "{app}"; Flags: ignoreversion
```

### Change Desktop Icon Behavior
```pascal
[Tasks]
Name: "desktopicon"; ... Flags: unchecked  ; Optional
; Change to: Flags: checked  ; On by default
```

### Add Custom Messages
```pascal
[Messages]
WelcomeLabel2=Custom welcome text here
```

## 🎨 Features Included

### 1. Modern Wizard Style
- Clean, professional interface
- Windows 11 compatible design
- Progress indicators
- Custom branding

### 2. Smart Installation
- **Default:** Installs to Program Files (per-user, no admin)
- **Alternative:** User can choose custom location
- **Data:** Preserves existing lru_data.json on upgrade
- **Logs:** Cleans up old log files on uninstall

### 3. Shortcuts
- **Start Menu:** Always created
- **Desktop:** Optional (unchecked by default)
- **Quick Launch:** Optional (Windows 7 and below)

### 4. Uninstaller
- Automatically registered in "Add/Remove Programs"
- Removes all installed files
- Cleans up empty directories
- Option to keep user data

### 5. Version Information
- Embedded in the installer .exe
- Shows in Windows Explorer properties
- Includes publisher, version, description

## 🔧 Advanced Configuration

### Code Signing (Optional)
If you have a code signing certificate:

```pascal
[Setup]
SignTool=signtool sign /f "path\to\cert.pfx" /p "password" /t http://timestamp.digicert.com $f
SignedUninstaller=yes
```

### Multiple Languages
```pascal
[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"
```

### Registry Settings (Optional)
```pascal
[Registry]
Root: HKCU; Subkey: "Software\LRU Tracker"; ValueType: string; ValueName: "Version"; ValueData: "{#MyAppVersion}"
```

### Pre-Installation Checks
```pascal
[Code]
function InitializeSetup(): Boolean;
begin
  // Check if .NET Framework is installed, etc.
  Result := True;
end;
```

## 📊 Comparison: Installer vs Standalone

| Feature | Standalone .exe | Installer |
|---------|----------------|-----------|
| File Size | 127 MB | 45-50 MB (compressed) |
| Start Menu | No | Yes ✅ |
| Desktop Icon | No | Optional ✅ |
| Uninstaller | No | Yes ✅ |
| Version Info | Basic | Professional ✅ |
| User Trust | Lower | Higher ✅ |
| Distribution | Zip file | Single .exe |
| Updates | Manual | Can track versions |

## 🐛 Troubleshooting

### Error: "Cannot find Inno Setup"
- Install Inno Setup from: https://jrsoftware.org/isdl.php
- Ensure it's installed to: `C:\Program Files (x86)\Inno Setup 6\`

### Error: "Cannot find LRU_Tracker.exe"
- Run `BUILD_REFACTORED.bat` first
- Ensure `dist\LRU_Tracker.exe` exists

### Error: "Cannot find icon file"
- Ensure `distribution\lru_icon.ico` exists
- Or comment out the `SetupIconFile` line

### Warning: "File not found"
- Check all paths in `[Files]` section
- Use relative paths from installer folder
- `..` means parent directory

### Installer is too large
- Already using LZMA compression (best available)
- Size is normal for PyInstaller apps with dependencies
- Consider removing unused dependencies in Python code

## 📝 Release Checklist

Before releasing with installer:

- [ ] Update version in `LRU_Tracker_Setup.iss` (#define MyAppVersion)
- [ ] Update version in `config.py` (APP_VERSION)
- [ ] Update version in `version.json`
- [ ] Build executable: `BUILD_REFACTORED.bat`
- [ ] Build installer: `BUILD_INSTALLER.bat`
- [ ] Test installer on clean Windows machine
- [ ] Test installation to Program Files
- [ ] Test installation to custom location
- [ ] Test desktop shortcut (optional)
- [ ] Test Start Menu shortcut
- [ ] Test uninstaller
- [ ] Test upgrade (install over existing version)
- [ ] Check file size (~45-50 MB is normal)
- [ ] Upload to GitHub release
- [ ] Update download URL in version.json

## 🎯 Distribution

### GitHub Release
```markdown
## Downloads

**Recommended:** Use the installer for easiest setup
- [LRU_Tracker_Setup_v1.2.2.exe](link) - 45 MB
  - Professional installation wizard
  - Creates Start Menu shortcuts
  - Includes automatic uninstaller
  - No admin rights required

**Alternative:** Portable version
- [LRU_Tracker.exe](link) - 127 MB
  - No installation needed
  - Run directly from any folder
```

### Update version.json
```json
{
  "version": "1.2.2",
  "download_url": "https://github.com/HaltTheGrey/lru-tracker/releases/download/v1.2.2/LRU_Tracker_Setup_v1.2.2.exe"
}
```

## 🆘 Support

### Inno Setup Documentation
- Official Docs: https://jrsoftware.org/ishelp/
- Examples: `C:\Program Files (x86)\Inno Setup 6\Examples\`
- Forum: https://groups.google.com/g/innosetup

### Common Tasks
- **Exclude files from uninstall:** Add to `[UninstallDelete]` with "not" flag
- **Run program after install:** Already configured in `[Run]` section
- **Check system requirements:** Add code in `InitializeSetup()`
- **Custom dialogs:** Use `CreateInputQueryPage()` in `InitializeWizard()`

## ✨ Benefits for Users

**With Installer:**
1. Double-click to install
2. Wizard guides through process
3. Choose install location
4. Creates shortcuts automatically
5. Appears in "Add/Remove Programs"
6. Easy to uninstall later
7. Looks professional and trustworthy

**Without Installer (Standalone .exe):**
1. Download file
2. Extract from zip
3. Move to desired location manually
4. No shortcuts
5. No uninstaller
6. Less professional appearance

---

## 🎉 Summary

You now have a **professional Windows installer** that:
- ✅ Reduces file size by 60% (127 MB → 45 MB)
- ✅ Provides guided installation experience
- ✅ Creates shortcuts automatically
- ✅ Includes automatic uninstaller
- ✅ Looks professional and trustworthy
- ✅ Still gets SmartScreen warning (same as .exe), but users trust installers more!

**To build:** Just run `BUILD_INSTALLER.bat` and you're done! 🚀
