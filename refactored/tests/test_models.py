"""Unit tests for models module."""
import pytest
from models import Station, HistoryEntry, GlobalHistoryEntry


class TestStation:
    def test_station_creation(self):
        station = Station("Test Station", current=10, min_lru=5, max_lru=20)
        assert station.name == "Test Station"
        assert station.current == 10
        assert station.min_lru == 5
        assert station.max_lru == 20
    
    def test_status_under_min(self):
        station = Station("Test", current=3, min_lru=5, max_lru=20)
        assert station.get_status() == "⚠️ UNDER MIN"
        assert station.get_status_tag() == "under_min"
    
    def test_status_at_max(self):
        station = Station("Test", current=20, min_lru=5, max_lru=20)
        assert station.get_status() == "🔴 AT/OVER MAX"
        assert station.get_status_tag() == "at_max"
    
    def test_status_normal(self):
        station = Station("Test", current=10, min_lru=5, max_lru=20)
        assert station.get_status() == "✅ Normal"
        assert station.get_status_tag() == "normal"
    
    def test_add_history(self):
        station = Station("Test", current=0, min_lru=5, max_lru=20)
        station.add_history(15, "2024-01-01 10:00:00")
        
        assert station.current == 15
        assert len(station.history) == 1
        assert station.history[0].count == 15
        assert station.history[0].timestamp == "2024-01-01 10:00:00"
    
    def test_to_dict(self):
        station = Station("Test", current=10, min_lru=5, max_lru=20)
        data = station.to_dict()
        
        assert data['current'] == 10
        assert data['min'] == 5
        assert data['max'] == 20
        assert isinstance(data['history'], list)
    
    def test_from_dict(self):
        data = {
            'current': 10,
            'min': 5,
            'max': 20,
            'history': [{'timestamp': '2024-01-01 10:00:00', 'count': 10}]
        }
        station = Station.from_dict("Test", data)
        
        assert station.name == "Test"
        assert station.current == 10
        assert station.min_lru == 5
        assert station.max_lru == 20
        assert len(station.history) == 1


class TestHistoryEntry:
    def test_history_entry_creation(self):
        entry = HistoryEntry("2024-01-01 10:00:00", 15)
        assert entry.timestamp == "2024-01-01 10:00:00"
        assert entry.count == 15
    
    def test_to_dict(self):
        entry = HistoryEntry("2024-01-01 10:00:00", 15)
        data = entry.to_dict()
        
        assert data['timestamp'] == "2024-01-01 10:00:00"
        assert data['count'] == 15
    
    def test_from_dict(self):
        data = {'timestamp': '2024-01-01 10:00:00', 'count': 15}
        entry = HistoryEntry.from_dict(data)
        
        assert entry.timestamp == "2024-01-01 10:00:00"
        assert entry.count == 15


class TestGlobalHistoryEntry:
    def test_global_history_creation(self):
        entry = GlobalHistoryEntry(
            station="Test",
            timestamp="2024-01-01 10:00:00",
            count=15,
            min_lru=5,
            max_lru=20
        )
        
        assert entry.station == "Test"
        assert entry.count == 15
        assert entry.min_lru == 5
        assert entry.max_lru == 20


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
