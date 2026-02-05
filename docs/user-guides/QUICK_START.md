# Quick Start Guide - FC LRU Tracker

## Installation (One-Time Setup)

### Step 1: Install Python
1. Download Python from https://www.python.org/downloads/
2. Run installer and **CHECK "Add Python to PATH"**
3. Click "Install Now"

### Step 2: Install Required Packages
Open PowerShell in this folder and run:
```powershell
pip install openpyxl pandas
```

OR simply double-click `START_APP.bat` which will install packages and start the app.

## Running the Application

### Option 1: Using the Batch File (Easiest)
- Double-click `START_APP.bat`

### Option 2: Using PowerShell
```powershell
python lru_tracker.py
```

### Option 3: Using Python Launcher
```powershell
py lru_tracker.py
```

## First Time Use - Quick Tutorial

### FAST SETUP: Use Template Import (Recommended!)

If you have 5+ stations, use the template method:

1. **Download Template** (10 seconds)
   - Click **"📥 Download Template"** (in Export & Reports section)
   - Save the Excel file

2. **Fill Template** (2-5 minutes)
   - Open `LRU_Station_Template.xlsx` in Excel
   - Delete example rows (4-7)
   - Add your stations starting at row 4:
     - Column A: Station name (e.g., "Pack Station 1")
     - Column B: Min (e.g., 5)
     - Column C: Max (e.g., 20)
     - Column D: Current count (optional, can leave empty)
   - Save the file

3. **Import to App** (20 seconds)
   - Click **"📤 Import from Template"**
   - Select your filled template
   - Click **Open**
   - Review summary and done!

**See TEMPLATE_GUIDE.md for detailed template instructions**

---

### MANUAL SETUP: Add One at a Time

For small setups or adding individual stations:

### 1. Add Your First Station (30 seconds)
1. Click **"➕ Add Station"** button
2. Enter station name: `Pack Station 1`
3. Set Min: `5` (restock when below this)
4. Set Max: `20` (pull when at/over this)
5. Click **"Add Station"**

### 2. Add More Stations (repeat as needed)
Examples:
- `Dock Door A` - Min: 10, Max: 30
- `Induct Station 1` - Min: 3, Max: 15
- `Palletize Zone B` - Min: 8, Max: 25

### 3. Update LRU Count (during operations)
1. Select station from dropdown
2. Enter current count (e.g., `12`)
3. Click **"📝 Update Count"**
4. Watch status update automatically

### 4. Understanding Status Colors

**Main Window:**
- 🟢 **Green** = Normal (between min and max) ✅
- 🟡 **Yellow** = At/Over Max (needs pull/redistribution) ⚠️
- 🔴 **Red** = Under Min (restock needed) 🚨

### 5. Export Your First Report
1. Update some counts first
2. Click **"📊 Export to New Excel Report"**
3. Choose where to save
4. Open the Excel file to see:
   - Color-coded current status
   - Complete history log
   - Ready to share with management

## Daily Workflow Example

### Morning Shift Start - First Day Setup
**Option A: Using Template (10+ stations)**
1. Download template
2. Fill in all stations in Excel (use EXAMPLE_STATIONS.txt as reference)
3. Import template
4. Update current counts for each station
5. Ready to track!

**Option B: Manual Entry (Few stations)**
1. Open app
2. Add stations one by one
3. Set initial counts
4. Ready to track!

### Morning Shift Start - After Setup
1. Open app (all your stations load automatically)
2. Add counts for each station
3. Note which stations are **under min** (🔴) - prioritize restocking

### During Shift (every 1-2 hours)
1. Update counts as you walk the floor
2. Check for **at max** stations (🟡) - trigger pulls
3. Monitor statistics panel

### End of Shift
1. Final count update for all stations
2. **Export to New Excel Report** or **Append to Existing**
3. Share with next shift lead
4. Email to supervisor

## Pull System Explained

### What is Min/Max?
- **Min**: Safety stock level - alert when inventory drops below
- **Max**: Trigger point - pull/redistribute when inventory reaches

### Example Scenario
Station: Pack Station 1
- Min: 5 LRUs
- Max: 20 LRUs

**Scenario A**: Current count = 3
- Status: 🔴 **UNDER MIN**
- Action: Immediate restock needed

**Scenario B**: Current count = 12
- Status: 🟢 **Normal**
- Action: No action needed

**Scenario C**: Current count = 20
- Status: 🟡 **AT/OVER MAX**
- Action: Pull LRUs to another station or storage

## Advanced Features

### Trend Analysis
1. Click **"📉 View Trends for Station"**
2. Select station
3. Get Excel with line chart showing LRU changes over time
4. Use to optimize min/max values

### Append to Existing Report
- Add daily snapshots to one master Excel file
- Each day gets a new timestamped sheet
- Perfect for weekly/monthly tracking

### Edit Station Parameters
1. Select station in table
2. Click **"✏️ Edit Station"**
3. Adjust min/max as needed
4. Based on usage patterns from trends

## Troubleshooting

### "Python not found"
- Reinstall Python and check "Add to PATH"
- Or download from Microsoft Store

### "No module named 'openpyxl'"
```powershell
pip install openpyxl pandas
```

### Excel won't open export
- Close any Excel files with same name
- Save to different location

### Data disappeared
- Check for `lru_data.json` in same folder
- If missing, data was not saved
- Always click **"💾 Save Data"** before closing

## Tips for Success

✅ **DO:**
- Update counts regularly (every 1-2 hours)
- Export reports at end of shift
- Use descriptive station names
- Review trends weekly
- Back up `lru_data.json` file

❌ **DON'T:**
- Delete `lru_data.json` (it has all your data!)
- Close app without saving
- Set min > max
- Use same name for multiple stations

## Support

If you need help:
1. Check the README.md file
2. Verify Python and packages are installed
3. Make sure `lru_data.json` has write permissions

## Next Steps

After you're comfortable:
1. Set up for all your stations
2. Train team members
3. Establish update schedule
4. Use trend reports to optimize min/max
5. Share reports with management

---

**Ready to start?** Double-click `START_APP.bat` or run `python lru_tracker.py`
