# 🛡️ Windows Security Warning - Visual Guide

## What You'll See

When you run `LRU_Tracker.exe` for the first time, Windows shows this warning:

```
┌───────────────────────────────────────────────────────┐
│  🛡️ Windows protected your PC                         │
│                                                        │
│  Microsoft Defender SmartScreen prevented an          │
│  unrecognized app from starting. Running this app     │
│  might put your PC at risk.                          │
│                                                        │
│  App: LRU_Tracker.exe                                │
│  Publisher: Unknown publisher                         │
│                                                        │
│  [More info]                    [Don't run]          │
└───────────────────────────────────────────────────────┘
```

---

## ✅ How to Bypass Safely (2 Clicks)

### Step 1: Click "More info"

```
┌───────────────────────────────────────────────────────┐
│  🛡️ Windows protected your PC                         │
│                                                        │
│  Microsoft Defender SmartScreen prevented an          │
│  unrecognized app from starting.                     │
│                                                        │
│  App: LRU_Tracker.exe                                │
│  Publisher: Unknown publisher                         │
│                                                        │
│  👉 [More info] 👈                [Don't run]         │
└───────────────────────────────────────────────────────┘
           ↑
    Click this small blue link!
```

### Step 2: Click "Run anyway"

After clicking "More info", a new button appears:

```
┌───────────────────────────────────────────────────────┐
│  🛡️ Windows protected your PC                         │
│                                                        │
│  App: LRU_Tracker.exe                                │
│  Publisher: Unknown publisher                         │
│                                                        │
│  This app has been blocked for your protection.       │
│  Running it may put your PC at risk.                 │
│                                                        │
│  👉 [Run anyway] 👈                [Don't run]        │
└───────────────────────────────────────────────────────┘
           ↑
    Click this new button!
```

### Step 3: App Opens! ✅

The LRU Tracker application opens normally. You won't see this warning again!

---

## 🤔 Why This Happens

**This is NOT a virus or malware warning!**

Windows SmartScreen shows this for ANY application that:
- Doesn't have a paid code signing certificate ($200-400/year)
- Is new and hasn't built up "reputation" with Microsoft
- Comes from an individual developer (not a big company)

### Other Trusted Apps That Show This Same Warning:

- Python installers (before they were signed)
- Many open-source utilities
- Small developer tools
- Internal corporate applications
- Free software downloads

**This is extremely common and normal!**

---

## ✅ Why LRU Tracker is Safe

### 1. Open Source
- All code is public on GitHub: https://github.com/HaltTheGrey/lru-tracker
- Anyone can review the code
- Nothing hidden

### 2. No Installation Required
- Just extract and run
- No system modifications
- No admin rights needed
- No registry changes

### 3. Local Data Only
- All data stays on YOUR computer
- No internet connection required
- No data sent to external servers
- Data saved locally at: `C:\Users\[You]\AppData\Local\LRU_Tracker\`

### 4. Easy to Remove
- Just delete the folder
- No uninstaller needed
- No leftover files

### 5. Transparent
- You can see exactly what files are included
- Just the .exe and documentation
- No hidden components

---

## 🔒 How to Eliminate the Warning (Optional)

If you want to remove this warning for all users in the future:

### Option 1: Free (Time Investment)
- Apply for free code signing via SignPath.io
- Takes 2-4 weeks approval
- Free for open-source projects

### Option 2: Paid (Immediate)
- Purchase code signing certificate: $75-400/year
- Sign the executable
- Warning disappears immediately

### Option 3: IT Department
- Ask your FC IT department to:
  - Whitelist the application
  - Or sign it with company certificate
  - Or add to approved software list

**For now, the bypass instructions work perfectly fine!**

---

## 📧 What to Tell Your Team

### Email Template:

```
Subject: New LRU Tracker App - Installation Instructions

Hi team,

I've created an LRU tracking app to help with our station management.

IMPORTANT - Windows Security Warning:
When you first run the app, Windows will show a security warning. 
This is normal for new apps without a paid signature.

How to bypass safely:
1. Run LRU_Tracker.exe
2. Click "More info" on the warning
3. Click "Run anyway"
4. That's it! You only do this once.

Why it's safe:
✓ All code is public on GitHub
✓ No installation needed
✓ All data stays local
✓ No admin rights required
✓ Easy to remove

Download link: [Your GitHub Release URL]

Questions? Let me know!
```

---

## 🎯 Summary

**The Warning:**
- Appears once on first run
- Takes 2 clicks to bypass
- Never appears again after that

**It's Safe Because:**
- Open source (code is public)
- Local data only
- No system changes
- Easy to verify

**To Eliminate Warning (Optional):**
- Get code signing certificate ($$$)
- Or work with IT department
- Or use SignPath.io (free, takes time)

**For Now:**
- Instructions in this guide work great!
- All major open-source projects deal with this
- Users click through it every day

---

**Ready to distribute? The ZIP file is ready to go!** 🚀
