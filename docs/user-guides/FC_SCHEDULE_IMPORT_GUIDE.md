# FC Standard Work Spreadsheet Import Guide

## 🎯 Overview

Your FC Standard Work Spreadsheet can now be **directly imported** into the LRU Tracker! The app will automatically:
- Extract all LRUs and test stations
- Create stations from LRU + Rack Location
- Auto-calculate Min/Max values from batch sizes (B=X)
- Preserve test descriptions for reference

---

## 📊 Your Spreadsheet Format

The app recognizes this structure:

```
LRU         | Test Description              | Rack Location | 6AM | 8AM | ...
------------|-------------------------------|---------------|-----|-----|----
MERMOD      | MMA to NADIR (B=3)           | F8.2 (NADIR)  |     |     |
SGT (-219)  | 38/44__219 Baseline (B=6)    | G6.1.3 (Mech) |     |     |
FRED        | MMA to Nadir (B=1)           | H6.3 (MMA)    |     |     |
```

---

## 🚀 How to Import

### Step 1: Prepare Your CSV
- Keep your existing FC Standard Work Spreadsheet
- Save it as `.csv` format (if not already)
- No modifications needed!

### Step 2: Import to App
1. Open LRU Tracker
2. Click **"📋 Import FC Schedule CSV"** (orange button in Template section)
3. Select your FC Standard Work CSV file
4. Review the import summary
5. All stations loaded!

---

## 🎨 How Stations Are Created

### Station Naming
The app creates station names like this:

**Format:** `LRU - Rack Location`

**Examples from your sheet:**
- `MERMOD - F8.2 (NADIR)`
- `SGT (-219) - G6.1.3 (Mech)`
- `FRED - H6.3 (MMA)`
- `MAG - K7.1 {18/30}`
- `RWA - J6.1 (SSL)`

### Min/Max Auto-Calculation

The app extracts batch sizes from test descriptions (B=X) and calculates:

| Batch Size | Min (half) | Max (double) | Example LRU |
|------------|-----------|--------------|-------------|
| B = 1      | 1         | 2            | FRED (MMA to Nadir) |
| B = 2      | 1         | 4            | MERMOD (TVAC) |
| B = 3      | 2         | 6            | MERMOD, Comins |
| B = 4      | 2         | 8            | MERMOD, SGT, SADAC |
| B = 6      | 3         | 12           | SGT (multiple tests) |
| B = 10     | 5         | 20           | MAG (TVAC) |
| B = 12     | 6         | 24           | TTC, MAG, GNSS |
| B = 28     | 14        | 56           | RWA (MECH INCOMING) |

**Logic:**
- **Min** = Batch Size ÷ 2 (minimum 1)
- **Max** = Batch Size × 2

**Why this works:**
- Min ensures you maintain at least half a batch (safety stock)
- Max prevents overstocking beyond 2 batches
- You can adjust these after import if needed

---

## 📋 What Gets Imported

### From Your Current Spreadsheet:

**All LRUs automatically imported:**

**MERMOD Section:**
- MERMOD - F8.2 (NADIR) → Min: 2, Max: 6
- MERMOD - K6.5 (SSL) → Min: 1, Max: 4
- MERMOD - H6.2 (MMA) → Min: 2, Max: 8

**SGT Section:**
- SGT (-219) - G6.1.3 (Mech) → Min: 3, Max: 12
- SGT (-218) - G6.1.2 (Mech) → Min: 2, Max: 8
- SGT (-217) - K6.4 (SSL) → Min: 3, Max: 12
- SGT (-217) - K6.3 (SSL) → Min: 3, Max: 12
- SGT (-217) - K6.2.2 (SSL) → Min: 3, Max: 12
- SGT (-217) - K6.2.1 (SSL) → Min: 3, Max: 12

**FRED Section:**
- FRED - H6.3 (MMA) → Min: 1, Max: 2
- FRED - K7.1 (SSL) → Min: 1, Max: 4

**And all other LRUs:** TTC, Comins, Sadac, MAG, Selfie Cam, GNSS, RWA, Panel HDRM, Solar HDRM, Torque Rod, SGA, Hinge, etc.

**Total:** ~50-60 stations from your spreadsheet!

---

## 💡 After Import

### What You Can Do:

1. **Review Min/Max Values**
   - Check if auto-calculated values make sense
   - Adjust based on your actual needs
   - Click "Edit Station" to modify

2. **Add Current Counts**
   - Use "Update LRU Count" to set initial values
   - Track throughout your shift

3. **Monitor Status**
   - 🟢 Green = Normal (between min/max)
   - 🟡 Yellow = At/Over Max (needs pull)
   - 🔴 Red = Under Min (needs restock)

4. **Export Reports**
   - Daily snapshots
   - Trend analysis
   - Share with team

---

## 🔧 Customization After Import

### Option 1: Edit Individual Stations
```
1. Select station in list
2. Click "Edit Station"
3. Adjust Min/Max values
4. Save changes
```

### Option 2: Bulk Update via Template
```
1. Export current stations to Excel
2. Modify Min/Max columns
3. Re-import (choose "Update existing")
4. All values updated
```

---

## 📊 Example Import Result

**Before Import:**
- Empty app, no stations

**After Import (from your CSV):**
```
✅ Imported: 52 stations

📋 Sample Stations Created:
  • MERMOD - F8.2 (NADIR)
    Min: 2, Max: 6
    
  • SGT (-219) - G6.1.3 (Mech)
    Min: 3, Max: 12
    
  • MAG - K7.1 {18/30}
    Min: 5, Max: 20
    
  • RWA - J6.1 (SSL)
    Min: 2, Max: 8
    
  • GNSS - H6.1.1
    Min: 6, Max: 24
    
  ... and 47 more!
```

---

## 🎯 Workflow Integration

### Daily Use:

**Morning:**
1. Import your FC Schedule CSV (one-time setup)
2. Walk facility and update current counts
3. Note which stations are under min (🔴)

**Throughout Shift:**
1. Update counts as you move LRUs
2. Monitor for max alerts (🟡)
3. Coordinate pulls/restocks

**End of Shift:**
1. Final count updates
2. Export report to Excel
3. Share with next shift

---

## 🔄 Keeping in Sync

### When Your FC Schedule Changes:

**Option A: Re-import CSV**
- Import updated CSV
- Choose "Update existing" for changed stations
- Choose "Skip" for unchanged stations

**Option B: Manual Updates**
- Edit individual stations in app
- Adjust min/max as needed

**Option C: Hybrid**
- Use CSV for new stations
- Manual edits for fine-tuning

---

## ⚙️ Advanced: Understanding the Import Logic

### What the App Does:

1. **Reads CSV file** row by row
2. **Looks for pattern:** LRU name, Test description, Rack location
3. **Extracts batch size** using regex: `B\s*=\s*(\d+)`
4. **Creates station name:** `{LRU} - {Rack Location}`
5. **Calculates thresholds:**
   - Min = max(1, batch_size // 2)
   - Max = batch_size * 2
6. **Stores metadata:**
   - Test description (for reference)
   - Rack location (for reference)

### What Gets Skipped:

- Empty rows
- Header rows (containing "LRU", "Shift", etc.)
- Rows without LRU names

---

## 💡 Tips & Best Practices

### Before Import:
✅ Review your CSV to ensure data is clean
✅ Backup existing lru_data.json if you have data
✅ Keep original CSV for reference

### After Import:
✅ Verify min/max values make sense for your operation
✅ Adjust based on actual usage patterns
✅ Add current counts for immediate tracking
✅ Export a baseline report

### For Ongoing Use:
✅ Update counts regularly (every 1-2 hours)
✅ Review trends weekly
✅ Adjust min/max seasonally if needed
✅ Re-import CSV when facility layout changes

---

## 🆘 Troubleshooting

### "No stations imported"
**Cause:** CSV format not recognized
**Solution:** 
- Ensure file is CSV format
- Check that columns match: LRU, Test Description, Rack Location
- Look for actual data rows (not just headers)

### "Batch size not found"
**Cause:** Test description doesn't have (B=X) format
**Solution:**
- App will use defaults (Min: 5, Max: 20)
- You can manually edit after import

### "Station already exists"
**Cause:** Duplicate station name in CSV or app
**Solution:**
- Choose "Update" to replace min/max
- Choose "Skip" to keep existing
- Or rename in CSV before import

---

## 📞 Support

### Common Questions:

**Q: Can I import the same CSV multiple times?**
A: Yes! You'll be asked to update or skip existing stations.

**Q: What if I change the CSV format?**
A: As long as columns 0-2 are: LRU, Test Desc, Rack Location, it works.

**Q: Can I add time slot data?**
A: Currently, the app focuses on LRU counts. Time slots are for scheduling.

**Q: Will this replace my Excel sheet?**
A: No! This tracks current inventory. Keep your Excel for scheduling.

---

## 🎉 Quick Start Checklist

- [ ] Have your FC Standard Work Spreadsheet in CSV format
- [ ] Open LRU Tracker app
- [ ] Click "📋 Import FC Schedule CSV"
- [ ] Select your CSV file
- [ ] Review import summary
- [ ] Verify stations created correctly
- [ ] Adjust min/max if needed
- [ ] Start updating counts!

---

**Your FC Schedule → LRU Tracker in 3 clicks!** 🚀

No more manual station entry. Just import and start tracking!
