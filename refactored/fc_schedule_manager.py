"""FC Schedule import/export functionality."""
import csv
import re
from typing import Dict, List, Tuple
from collections import defaultdict
from datetime import datetime
from models import Station
from config import ALL_TIME_SLOTS, TIME_SLOT_MAP, TIMESTAMP_FORMAT
from logger import get_logger

logger = get_logger()


class FCScheduleManager:
    """Handles FC Standard Work Spreadsheet format."""
    
    def import_from_csv(self, filename: str, existing_stations: Dict[str, Station]) -> Tuple[List[Station], List[str]]:
        """Import stations from FC schedule CSV. Returns (stations, errors)."""
        imported_stations = []
        errors = []
        
        with open(filename, 'r', encoding='utf-8-sig') as f:
            csv_reader = csv.reader(f)
            rows = list(csv_reader)
        
        for row_num, row in enumerate(rows, 1):
            if len(row) < 3:
                continue
            
            lru_name = str(row[0]).strip() if row[0] else ""
            test_desc = str(row[1]).strip() if row[1] else ""
            rack_location = str(row[2]).strip() if row[2] else ""
            
            # Skip headers
            if not lru_name or "LRU" in lru_name or "Shift" in lru_name:
                continue
            
            # Create station name
            station_name = f"{lru_name} - {rack_location}" if rack_location else lru_name
            
            # Extract batch size from test description (B=X format)
            batch_match = re.search(r'B\s*=\s*(\d+)', test_desc, re.IGNORECASE)
            
            if batch_match:
                batch_size = int(batch_match.group(1))
                min_val = max(1, batch_size // 2)
                max_val = batch_size * 2
            else:
                min_val = 5
                max_val = 20
            
            if station_name in existing_stations:
                errors.append(f"Row {row_num}: Station '{station_name}' already exists")
                continue
            
            station = Station(
                name=station_name,
                current=0,
                min_lru=min_val,
                max_lru=max_val,
                test_description=test_desc,
                rack_location=rack_location
            )
            imported_stations.append(station)
        
        logger.info(f"Imported {len(imported_stations)} stations from FC schedule, {len(errors)} errors")
        return imported_stations, errors
    
    def export_to_csv(self, filename: str, stations: Dict[str, Station]) -> None:
        """Export stations in FC schedule format."""
        # Group stations by LRU name
        lru_groups = defaultdict(list)
        
        for station_name, station_data in stations.items():
            if " - " in station_name:
                lru_name = station_name.split(" - ")[0].strip()
                location = station_name.split(" - ", 1)[1].strip()
            else:
                lru_name = station_name
                location = ""
            
            lru_groups[lru_name].append({
                'station_name': station_name,
                'location': location,
                'data': station_data
            })
        
        # Prepare CSV data
        csv_data = []
        
        # Headers
        header1 = ['', '', '', '1st Shift - Record # of Batches to schedule', '', '', '', '', '', 
                  '2nd Shift - Record # of Batches to schedule', '', '']
        csv_data.append(header1)
        
        header2 = ['LRU', 'Test to Schedule', 'Rack Location'] + ALL_TIME_SLOTS
        csv_data.append(header2)
        
        # Data
        for lru_name in sorted(lru_groups.keys()):
            stations_list = lru_groups[lru_name]
            
            for station_info in stations_list:
                station_name = station_info['station_name']
                location = station_info['location']
                data = station_info['data']
                
                test_desc = data.test_description or f"Current: {data.current} (Min: {data.min_lru}, Max: {data.max_lru})"
                
                row = [lru_name, test_desc, location]
                
                # Add time slot data
                time_slot_data = self._get_time_slot_data(data)
                for time_slot in ALL_TIME_SLOTS:
                    row.append(time_slot_data.get(time_slot, ''))
                
                csv_data.append(row)
            
            csv_data.append([''] * len(header2))
        
        # Write CSV
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(csv_data)
        
        logger.info(f"Exported FC schedule to: {filename}")
    
    def _get_time_slot_data(self, station: Station) -> Dict[str, str]:
        """Extract time slot data from station history."""
        result = {}
        
        for time_slot, (start_hour, end_hour) in TIME_SLOT_MAP.items():
            latest_value = None
            
            for entry in station.history:
                try:
                    dt = datetime.strptime(entry.timestamp, TIMESTAMP_FORMAT)
                    hour = dt.hour
                    
                    if start_hour <= hour < end_hour:
                        latest_value = entry.count
                except:
                    continue
            
            if latest_value is not None:
                result[time_slot] = str(latest_value)
        
        return result
