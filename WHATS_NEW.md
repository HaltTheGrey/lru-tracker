# 🎉 What's New - FC Schedule CSV Import!

## ⭐ NEW FEATURE: Direct Import from Your FC Standard Work Spreadsheet

### What Changed?

You can now **import your existing FC Standard Work Spreadsheet directly** into the LRU Tracker!

---

## 🚀 Quick Overview

### Before (Manual Entry):
```
Click "Add Station" 52 times
Fill forms manually
Set min/max for each
⏱️ Time: 2-3 hours
```

### After (FC Schedule Import):
```
Click "Import FC Schedule CSV"
Select your CSV file
Review summary
⏱️ Time: 30 seconds!
```

---

## 📋 How It Works

### Your CSV Format:
```
LRU        | Test Description      | Rack Location
-----------|----------------------|---------------
MERMOD     | MMA to NADIR (B=3)   | F8.2 (NADIR)
SGT (-219) | 38/44__219 (B=6)     | G6.1.3 (Mech)
FRED       | MMA to Nadir (B=1)   | H6.3 (MMA)
```

### App Creates:
```
Station: MERMOD - F8.2 (NADIR)
  Min: 2 (half of batch 3)
  Max: 6 (double batch 3)

Station: SGT (-219) - G6.1.3 (Mech)
  Min: 3 (half of batch 6)
  Max: 12 (double batch 6)

Station: FRED - H6.3 (MMA)
  Min: 1 (half of batch 1)
  Max: 2 (double batch 1)
```

---

## 🎯 Key Features

✅ **Auto-Detects Batch Sizes** - Reads (B=X) from test descriptions
✅ **Smart Min/Max Calculation** - Min = half batch, Max = double batch
✅ **Creates Station Names** - Combines LRU + Rack Location
✅ **Imports All LRUs** - MERMOD, SGT, FRED, MAG, RWA, etc.
✅ **Preserves Test Info** - Stores test descriptions for reference
✅ **Handles Duplicates** - Ask to update or skip existing stations

---

## 📊 Example from Your Spreadsheet

**Your CSV has:**
- MERMOD (3 test types)
- SGT (6 test types across different variants)
- FRED (4 test types)
- TTC, Comins, Sadac, MAG
- Selfie Cam, GNSS
- RWA, Panel HDRM, Solar HDRM
- Torque Rod, SGA, Hinge
- **Total: ~52 stations**

**After Import:**
```
✅ Imported: 52 stations
⏱️ Time: 30 seconds
💡 All ready to track!
```

---

## 🎨 Where to Find It

**In the App:**
1. Look for the **Template Import/Export** section (right panel)
2. Find the **📋 Import FC Schedule CSV** button (orange)
3. Click it and select your CSV file
4. Done!

---

## 📖 Documentation

**New Guide Created:**
- **FC_SCHEDULE_IMPORT_GUIDE.md** - Complete instructions for FC Schedule import

**Updated Guides:**
- **README.md** - Added FC Schedule import section
- **QUICK_START.md** - Updated with new import method

---

## 💡 When to Use Each Import Method

### Use FC Schedule Import when:
✅ You already have an FC Standard Work Spreadsheet
✅ You want to import all test stations at once
✅ You want auto-calculated min/max from batch sizes
✅ You have 20+ stations to add

### Use Template Import when:
✅ You want custom min/max values
✅ You're creating a new tracking system from scratch
✅ You want to organize data in Excel first
✅ You want full control over all parameters

### Use Manual Entry when:
✅ Adding 1-5 stations only
✅ Making quick adjustments
✅ Learning the system

---

## 🔧 Technical Details

### What Gets Extracted:
- **Column 0**: LRU Name (MERMOD, SGT, etc.)
- **Column 1**: Test Description (extracts batch size B=X)
- **Column 2**: Rack Location (F8.2, G6.1.3, etc.)

### Station Name Format:
`{LRU Name} - {Rack Location}`

Examples:
- `MERMOD - F8.2 (NADIR)`
- `SGT (-219) - G6.1.3 (Mech)`
- `MAG - K7.1 {18/30}`

### Min/Max Calculation:
```python
if (B=X) found in test description:
    min = max(1, X // 2)  # Half batch, minimum 1
    max = X * 2            # Double batch
else:
    min = 5  # Default
    max = 20 # Default
```

---

## 🎉 Bottom Line

**Your FC Standard Work Spreadsheet is now a template!**

No need to recreate your station list. Just import it directly and start tracking LRU inventory with the pull system.

**3 Import Options. Choose What Works Best:**
1. 📋 **FC Schedule CSV** - For existing FC schedules
2. 📥 **Template Excel** - For custom setups
3. ➕ **Manual Entry** - For small additions

---

## 🚀 Try It Now!

1. Open the app
2. Look for the orange **📋 Import FC Schedule CSV** button
3. Select your `FC Standard Work Spreadsheet_Rev_8.csv`
4. Watch all 52 stations import instantly!

---

**Happy Tracking! All your LRUs, all your tests, all at once!** 🎯📊
