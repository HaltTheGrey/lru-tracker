"""Data persistence manager."""
import json
import os
import shutil
from typing import Dict, List, Tuple
from models import Station, GlobalHistoryEntry
from config import DATA_FILE, BACKUP_SUFFIX, TEMP_SUFFIX


class DataManager:
    """Handles data loading, saving, and backup operations."""
    
    def __init__(self, data_file: str = DATA_FILE):
        self.data_file = data_file
    
    def load_data(self) -> Tuple[Dict[str, Station], List[GlobalHistoryEntry]]:
        """Load stations and history from file."""
        if not os.path.exists(self.data_file):
            return {}, []
        
        try:
            with open(self.data_file, 'r') as f:
                content = f.read()
                data = json.loads(content)
            
            if not isinstance(data, dict):
                raise ValueError("Invalid data format")
            
            # Load stations
            stations = {}
            stations_data = data.get('stations', {})
            if isinstance(stations_data, dict):
                for name, station_data in stations_data.items():
                    stations[name] = Station.from_dict(name, station_data)
            
            # Load global history
            history = []
            history_data = data.get('history', [])
            if isinstance(history_data, list):
                for entry in history_data:
                    try:
                        history.append(GlobalHistoryEntry.from_dict(entry))
                    except (KeyError, TypeError):
                        continue
            
            return stations, history
            
        except (json.JSONDecodeError, ValueError, IOError) as e:
            raise DataLoadError(f"Failed to load data: {str(e)}")
    
    def save_data(self, stations: Dict[str, Station], 
                  history: List[GlobalHistoryEntry]) -> None:
        """Save stations and history to file with atomic write."""
        data = {
            'stations': {name: station.to_dict() for name, station in stations.items()},
            'history': [entry.to_dict() for entry in history]
        }
        
        try:
            # Create backup before saving
            if os.path.exists(self.data_file):
                backup_file = self.data_file + BACKUP_SUFFIX
                try:
                    shutil.copy2(self.data_file, backup_file)
                except IOError:
                    pass  # Backup is best-effort
            
            # Write to temporary file first for atomic write
            temp_file = self.data_file + TEMP_SUFFIX
            with open(temp_file, 'w') as f:
                json.dump(data, f, indent=2)
            
            # Atomic rename
            if os.path.exists(self.data_file):
                os.remove(self.data_file)
            os.rename(temp_file, self.data_file)
            
        except IOError as e:
            raise DataSaveError(f"Failed to save data: {str(e)}")


class DataLoadError(Exception):
    """Raised when data loading fails."""
    pass


class DataSaveError(Exception):
    """Raised when data saving fails."""
    pass
