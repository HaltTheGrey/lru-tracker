"""Data models for LRU Tracker."""
from dataclasses import dataclass, field
from typing import List, Dict, Any
from datetime import datetime
from config import TIMESTAMP_FORMAT


@dataclass
class HistoryEntry:
    """Represents a single history entry for LRU count."""
    timestamp: str
    count: int
    
    def to_dict(self) -> Dict[str, Any]:
        return {'timestamp': self.timestamp, 'count': self.count}
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'HistoryEntry':
        return cls(timestamp=data['timestamp'], count=data['count'])


@dataclass
class Station:
    """Represents an LRU station."""
    name: str
    current: int
    min_lru: int
    max_lru: int
    history: List[HistoryEntry] = field(default_factory=list)
    test_description: str = ""
    rack_location: str = ""
    
    def get_status(self) -> str:
        """Get status string based on current count."""
        if self.current < self.min_lru:
            return "⚠️ UNDER MIN"
        elif self.current >= self.max_lru:
            return "🔴 AT/OVER MAX"
        return "✅ Normal"
    
    def get_status_tag(self) -> str:
        """Get status tag for UI coloring."""
        if self.current < self.min_lru:
            return 'under_min'
        elif self.current >= self.max_lru:
            return 'at_max'
        return 'normal'
    
    def add_history(self, count: int, timestamp: str = None) -> None:
        """Add a history entry."""
        if timestamp is None:
            timestamp = datetime.now().strftime(TIMESTAMP_FORMAT)
        self.history.append(HistoryEntry(timestamp, count))
        self.current = count
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            'current': self.current,
            'min': self.min_lru,
            'max': self.max_lru,
            'history': [h.to_dict() for h in self.history],
            'test_description': self.test_description,
            'rack_location': self.rack_location
        }
    
    @classmethod
    def from_dict(cls, name: str, data: Dict[str, Any]) -> 'Station':
        """Create Station from dictionary."""
        history = [HistoryEntry.from_dict(h) for h in data.get('history', [])]
        return cls(
            name=name,
            current=data.get('current', 0),
            min_lru=data.get('min', 5),
            max_lru=data.get('max', 20),
            history=history,
            test_description=data.get('test_description', ''),
            rack_location=data.get('rack_location', '')
        )


@dataclass
class GlobalHistoryEntry:
    """Represents a global history entry across all stations."""
    station: str
    timestamp: str
    count: int
    min_lru: int
    max_lru: int
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'station': self.station,
            'timestamp': self.timestamp,
            'count': self.count,
            'min': self.min_lru,
            'max': self.max_lru
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'GlobalHistoryEntry':
        return cls(
            station=data['station'],
            timestamp=data['timestamp'],
            count=data['count'],
            min_lru=data['min'],
            max_lru=data['max']
        )
