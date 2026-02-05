# Template Import/Export Guide

## Overview

The LRU Tracker now supports **bulk import** of stations using Excel templates. This feature allows you to:

1. **Download a template** - Get a pre-formatted Excel file
2. **Fill in your stations** - Add all your FC stations at once
3. **Import to app** - Load everything with one click

Perfect for initial setup or migrating from existing spreadsheets!

---

## 📥 Step-by-Step: Download & Fill Template

### Step 1: Download Template

1. Open the LRU Tracker application
2. Look in the **"Export & Reports"** section (right panel)
3. Find the **"Template Import/Export"** section
4. Click **"📥 Download Template"** button
5. Choose where to save it (e.g., Desktop)
6. Click **Save**

The template file (`LRU_Station_Template.xlsx`) will be created.

### Step 2: Open Template in Excel

Double-click the template file. You'll see:

**Sheet 1: Station Setup** (where you add data)
- Row 1: Title
- Row 2: Instructions
- Row 3: Column Headers (DO NOT MODIFY)
- Rows 4-7: Example data (DELETE these before importing)
- Rows 8+: Empty rows for your data

**Sheet 2: Instructions** (reference guide)

### Step 3: Fill in Your Stations

**Column Guide:**

| Column | Name | Required? | Description | Example |
|--------|------|-----------|-------------|---------|
| A | Station Name | ✅ Yes | Unique name for the station | "Pack Station 1" |
| B | Min LRU | ✅ Yes | Minimum threshold (restock alert) | 5 |
| C | Max LRU | ✅ Yes | Maximum threshold (pull alert) | 20 |
| D | Current LRU | ❌ No | Starting count (defaults to 0) | 12 |
| E | Notes | ❌ No | Description or location | "Main floor, west side" |

**Important Rules:**
- ✅ Station names must be unique
- ✅ Min and Max must be positive numbers
- ✅ Min must be LESS than Max
- ✅ DELETE the example rows (4-7) before importing
- ✅ One station per row

**Example Data:**

```
Station Name          | Min LRU | Max LRU | Current LRU | Notes
---------------------|---------|---------|-------------|------------------
Pack Station 1       | 5       | 20      | 12          | Main packing area
Pack Station 2       | 5       | 20      | 8           | Secondary pack
Dock Door A          | 10      | 30      | 15          | Receiving dock
Dock Door B          | 10      | 30      | 22          | Shipping dock
Induct Station 1     | 3       | 15      | 6           | Line 1
Induct Station 2     | 3       | 15      | 9           | Line 2
Palletize Zone A     | 8       | 25      | 14          | Zone A
Palletize Zone B     | 8       | 25      | 10          | Zone B
```

### Step 4: Save the Template

- Click **File** → **Save**
- Or press **Ctrl+S**
- Keep the Excel format (.xlsx)

---

## 📤 Import Template to Application

### Step 1: Start Import

1. In LRU Tracker app, click **"📤 Import from Template"**
2. Browse to your filled template file
3. Click **Open**

### Step 2: Review Import Process

The app will:
- ✅ Validate all data
- ✅ Check for duplicate station names
- ✅ Verify Min < Max
- ✅ Show you any errors

### Step 3: Handle Existing Stations

If a station name already exists, you'll see a dialog:

**Options:**
- **Yes** = Update existing station with new Min/Max values
- **No** = Skip this station, keep existing
- **Cancel** = Stop entire import process

### Step 4: View Import Summary

After import completes, you'll see:

```
Import Complete!

✅ Imported: 15 stations
🔄 Updated: 2 stations
⏭️ Skipped: 1 stations
❌ Errors: 0

📋 Imported Stations:
  • Pack Station 1
  • Pack Station 2
  • Dock Door A
  ... and 12 more
```

---

## 🔄 Copy/Paste from Existing Spreadsheets

### If you already have station data in another Excel file:

1. **Download the template** (to get the right format)
2. **Open your existing spreadsheet**
3. **Select your data** (station names, min, max values)
4. **Copy** (Ctrl+C)
5. **Open the template**
6. **Click on cell A4** (first data row)
7. **Paste** (Ctrl+V)
8. **Adjust columns** if needed to match template format:
   - Column A = Station Name
   - Column B = Min
   - Column C = Max
   - Column D = Current (optional)
9. **Delete example rows** (if still present)
10. **Save and import**

### Mapping Your Spreadsheet to Template

**Your spreadsheet might have:**
- Different column order
- Extra columns you don't need
- Headers in different rows

**Solution:**
1. Copy each column individually to the right template column
2. OR rearrange your columns to match: Name, Min, Max, Current, Notes
3. Delete any extra data that doesn't fit the template

---

## 💡 Tips & Best Practices

### Before Import
- ✅ Delete or clear the example rows (rows 4-7)
- ✅ Ensure no duplicate station names
- ✅ Verify all Min values are less than Max values
- ✅ Use descriptive station names
- ✅ Keep a backup of your template file

### Setting Min/Max Values

**Guidelines by Station Type:**

| Station Type | Typical Min | Typical Max | Reasoning |
|-------------|-------------|-------------|-----------|
| **Pack Stations** | 5-10 | 15-25 | High turnover, frequent use |
| **Dock Doors** | 10-15 | 25-40 | Large capacity, slower turnover |
| **Induct Stations** | 3-5 | 10-20 | Fast moving, smaller footprint |
| **Palletize Zones** | 8-12 | 20-30 | Medium capacity |
| **Pick Stations** | 5-8 | 15-25 | Varies by volume |
| **Receive Areas** | 10-20 | 30-50 | Buffer zone, higher capacity |

**Factors to Consider:**
- Available space at station
- Daily volume/throughput
- Restocking frequency
- Safety stock requirements
- Peak vs. non-peak needs

### After Import
- ✅ Review all imported stations in the app
- ✅ Check status colors are correct
- ✅ Update current counts if you left them at 0
- ✅ Test export functionality
- ✅ Save the application data

---

## 🔧 Troubleshooting

### "Could not find header row with 'Station Name'"
**Problem:** Template format was modified
**Solution:** Download a fresh template, don't modify row 3 headers

### "Station already exists"
**Problem:** Duplicate station name found
**Solution:** 
- Choose to **Update** the existing station
- Or **Skip** to keep the old one
- Or rename the duplicate in your template

### "Min > Max error"
**Problem:** Minimum value is greater than maximum
**Solution:** Fix the values in your template - Min must be LESS than Max

### "Invalid data" errors
**Problem:** Non-numeric values in Min/Max/Current columns
**Solution:** 
- Ensure columns B, C, D contain only numbers
- Remove any text, formulas, or special characters
- Use whole numbers (no decimals)

### Import shows 0 stations imported
**Problem:** All rows were empty or invalid
**Solution:**
- Make sure you have data starting at row 4
- Verify columns A, B, C have values
- Delete example rows if you haven't already

### Excel file won't open
**Problem:** File is corrupted or wrong format
**Solution:**
- Download template again
- Save as .xlsx format (not .xls or .csv)
- Don't use Excel's "Strict Open XML" format

---

## 📋 Quick Reference

### Required Columns (Must Have Data)
- ✅ **Column A**: Station Name (text)
- ✅ **Column B**: Min LRU (number)
- ✅ **Column C**: Max LRU (number)

### Optional Columns (Can Be Empty)
- ❌ **Column D**: Current LRU (defaults to 0)
- ❌ **Column E**: Notes (ignored during import)

### Data Validation Rules
1. Station name: Not empty, unique
2. Min LRU: Positive integer
3. Max LRU: Positive integer, greater than Min
4. Current LRU: Positive integer or empty

### Button Locations
- **Download Template**: Right panel → Export & Reports → Template Import/Export
- **Import from Template**: Right panel → Export & Reports → Template Import/Export

---

## 🎯 Common Use Cases

### Use Case 1: Initial Setup (New FC)
1. Download template
2. Fill in all your stations
3. Import once
4. Start tracking immediately

### Use Case 2: Migrating from Old Spreadsheet
1. Download template
2. Copy/paste from old spreadsheet
3. Adjust columns to match template
4. Import to app

### Use Case 3: Bulk Update Min/Max Values
1. Export current data or use template
2. Modify Min/Max values in Excel
3. Import (choose "Update" for existing stations)
4. All stations updated at once

### Use Case 4: Adding New Area/Department
1. Download template
2. Fill in only new stations
3. Import (existing stations will prompt for action)
4. Choose "Skip" for existing, import only new ones

### Use Case 5: Sharing Setup with Other FCs
1. Download template
2. Fill in your optimal Min/Max values
3. Share template file with other FCs
4. They can import your setup directly

---

## 🚀 Advanced: Bulk Updates

### Updating Multiple Stations at Once

**Scenario:** You want to increase all Pack Station Max values by 5

**Steps:**
1. Download template
2. Add your pack stations with new Max values
3. Import
4. Choose **"Yes - Update"** for each existing station
5. All updated in seconds vs. editing one by one

**Alternative Method:**
1. Export current data to Excel
2. Edit the Excel file
3. Save as new template
4. Import back

---

## 📞 Support

### If you have issues:

1. **Check this guide** for troubleshooting section
2. **Verify template format** - download a fresh one
3. **Test with 1-2 stations first** before bulk import
4. **Keep backups** of your lru_data.json file

### Common Questions:

**Q: Can I import the same template twice?**
A: Yes, but you'll be prompted to update or skip each existing station.

**Q: What happens to history when I update a station?**
A: History is preserved. Only Min/Max values are updated.

**Q: Can I use CSV instead of Excel?**
A: Not currently. Use .xlsx format only.

**Q: How many stations can I import at once?**
A: No limit. Tested with 100+ stations successfully.

**Q: Can I import just Current LRU counts?**
A: For updating counts, use the regular update feature. Template is for station setup.

---

**Ready to try it?** Download your template and start importing! 🚀
