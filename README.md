# FC LRU Pull System Tracker

A comprehensive Python application for tracking LRU (Likely Reusable Units) counts at fulfillment center stations with pull system min/max inventory management.

## Features

### 📊 Pull System Management
- **Min/Max Tracking**: Set minimum and maximum LRU thresholds for each station
- **Status Indicators**: Visual color coding for stations
  - 🟢 Green: Normal (between min and max)
  - 🟡 Yellow: At or over max (needs pull)
  - 🔴 Red: Under min (restock needed)

### 🏭 Station Management
- Add new stations with custom min/max values
- Edit existing station parameters
- Delete stations (with confirmation)
- Real-time status updates

### 📈 Tracking & History
- Track LRU count changes over time
- Maintain complete history for each station
- Timestamp all updates automatically
- View statistics dashboard

### 📑 Excel Integration
- **Export to New Report**: Create a new Excel file with current status
- **Append to Existing**: Add snapshots to existing reports
- **Trend Analysis**: Generate charts showing LRU trends over time for selected stations
- **Download Template**: Get pre-formatted Excel template for bulk station import
- **Import from Template**: Load multiple stations at once from filled template
- **Import FC Schedule CSV**: ⭐ **NEW!** Import directly from your FC Standard Work Spreadsheet
- Color-coded status in Excel exports
- Multiple sheets for current status and history

### 💾 Data Persistence
- Automatic saving to JSON file
- Data persists between sessions
- Import/export capabilities

## Installation

1. **Install Python** (if not already installed)
   - Download from https://www.python.org/downloads/
   - Make sure to check "Add Python to PATH" during installation

2. **Install Required Packages**
   ```powershell
   pip install -r requirements.txt
   ```

## Usage

### Starting the Application
```powershell
python lru_tracker.py
```

### Basic Workflow

1. **Add Stations** (Two Methods)

   **Method A: Add Manually (One at a time)**
   - Click "➕ Add Station"
   - Enter station name (e.g., "Pack Station 1", "Dock Door A")
   - Set minimum LRU threshold (e.g., 5)
   - Set maximum LRU threshold (e.g., 20)

   **Method B: Bulk Import from Template (Recommended for initial setup)**
   - Click "📥 Download Template"
   - Open template in Excel
   - Fill in all your stations (see TEMPLATE_GUIDE.md)
   - Click "📤 Import from Template"
   - Select your filled template
   - Review and confirm import

2. **Update LRU Counts**
   - Select station from dropdown
   - Enter current LRU count
   - Click "📝 Update Count"
   - Status automatically updates with color coding

3. **Monitor Status**
   - View all stations in main table
   - Check statistics panel for overview
   - Identify stations needing attention (under min or at max)

4. **Generate Reports**

   **Option A: New Excel Report**
   - Click "📊 Export to New Excel Report"
   - Choose save location
   - Creates report with current status and full history

   **Option B: Append to Existing**
   - Click "📈 Append to Existing Report"
   - Select existing Excel file
   - Adds new timestamped snapshot sheet

   **Option C: Trend Analysis**
   - Click "📉 View Trends for Station"
   - Select station to analyze
   - Generates Excel with trend chart showing LRU changes over time

## Excel Report Structure

### Current Status Sheet
- Station Name
- Current LRU Count
- Min/Max Thresholds
- Status (color-coded)
- Last Updated Timestamp

### History Sheet
- Complete transaction log
- All LRU updates with timestamps
- Min/Max values at time of update

### Trend Charts (Station-specific reports)
- Line chart showing LRU count over time
- Min/Max threshold reference lines
- Timestamped data points

## Pull System Logic

### Status Determination
- **Under Min** (🔴): `current < min` → Restock needed
- **Normal** (🟢): `min ≤ current < max` → Optimal range
- **At/Over Max** (🟡): `current ≥ max` → Pull/redistribute needed

### Best Practices
1. Set Min threshold to trigger restock alerts
2. Set Max threshold to prevent overstocking
3. Update counts regularly throughout shift
4. Export reports at end of each shift/day
5. Review trends weekly to optimize min/max values

## Data Storage

- **lru_data.json**: Stores all station configurations and history
- Automatically saves on every update
- Backup this file regularly to prevent data loss

## Troubleshooting

### Application won't start
- Ensure Python is installed: `python --version`
- Install dependencies: `pip install -r requirements.txt`

### Excel export fails
- Ensure you have write permissions to save location
- Close any open Excel files with the same name
- Check that openpyxl is installed

### Data not saving
- Check file permissions in application directory
- Ensure lru_data.json is not open in another program

## Template Import/Export

### Quick Start with Templates

**For Initial Setup (Recommended):**
1. Click "📥 Download Template" in the app
2. Open the Excel file (`LRU_Station_Template.xlsx`)
3. Fill in your stations following the format:
   - Column A: Station Name (required)
   - Column B: Min LRU (required)
   - Column C: Max LRU (required)
   - Column D: Current LRU (optional)
   - Column E: Notes (optional)
4. Save the file
5. Click "📤 Import from Template" in the app
6. Select your filled template
7. All stations loaded instantly!

**See TEMPLATE_GUIDE.md for detailed instructions**

### Import from FC Standard Work Spreadsheet ⭐ NEW!

**If you already have an FC Standard Work Spreadsheet:**
1. Save your schedule as CSV format
2. Click "📋 Import FC Schedule CSV" in the app
3. Select your CSV file
4. App automatically:
   - Creates stations from LRU + Rack Location
   - Calculates Min/Max from batch sizes (B=X)
   - Imports all test stations at once
5. Done! 50+ stations imported in seconds

**See FC_SCHEDULE_IMPORT_GUIDE.md for details**

### Copy/Paste from Existing Spreadsheets

If you already track stations in Excel:
1. Download the template
2. Copy your data from existing spreadsheet
3. Paste into template (adjust columns as needed)
4. Import to app

This is perfect for migrating from paper/Excel tracking to the app!

## Tips

- **Initial Setup**: Use template import for 10+ stations (much faster!)
- Use descriptive station names (e.g., "Pack Station 1A" not just "PS1")
- Adjust min/max values based on actual usage patterns
- Export reports before making bulk changes
- Keep the application running during shift for quick updates
- Review trend reports to identify patterns and optimize thresholds
- Keep your filled template as backup/documentation

## Future Enhancements

Potential features to add:
- Barcode scanner integration
- Multi-shift tracking
- Alert notifications
- Network/database storage for multi-user access
- Mobile app companion
- Automated email reports

## Support

For issues or feature requests, please document:
- What you were trying to do
- Error messages (if any)
- Steps to reproduce the issue
