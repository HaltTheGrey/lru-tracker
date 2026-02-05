"""Unit tests for validators module."""
import pytest
from validators import (
    validate_station_name,
    validate_number,
    sanitize_filename,
    validate_version_format,
    is_newer_version
)


class TestValidateStationName:
    def test_valid_names(self):
        assert validate_station_name("Station 1") == True
        assert validate_station_name("Pack-Station_A") == True
        assert validate_station_name("Dock Door #5") == True
    
    def test_invalid_names(self):
        assert validate_station_name("") == False
        assert validate_station_name("   ") == False
        assert validate_station_name("A" * 300) == False
        assert validate_station_name("<script>alert()</script>") == False
        assert validate_station_name(None) == False
        assert validate_station_name(123) == False


class TestValidateNumber:
    def test_valid_numbers(self):
        valid, num = validate_number("10")
        assert valid == True
        assert num == 10
        
        valid, num = validate_number("0")
        assert valid == True
        assert num == 0
        
        valid, num = validate_number("999999")
        assert valid == True
        assert num == 999999
    
    def test_invalid_numbers(self):
        valid, num = validate_number("abc")
        assert valid == False
        
        valid, num = validate_number("-5")
        assert valid == False
        
        valid, num = validate_number("1000000")
        assert valid == False
        
        valid, num = validate_number("")
        assert valid == False
    
    def test_custom_range(self):
        valid, num = validate_number("50", 0, 100)
        assert valid == True
        
        valid, num = validate_number("150", 0, 100)
        assert valid == False


class TestSanitizeFilename:
    def test_valid_filenames(self):
        assert sanitize_filename("report.xlsx") == "report.xlsx"
        assert sanitize_filename("my_report_2024.xlsx") == "my_report_2024.xlsx"
    
    def test_path_traversal(self):
        result = sanitize_filename("../../../etc/passwd")
        assert ".." not in result
        assert "/" not in result
    
    def test_dangerous_characters(self):
        result = sanitize_filename("file<>name.xlsx")
        assert "<" not in result
        assert ">" not in result
    
    def test_empty_filename(self):
        assert sanitize_filename("") == "export.xlsx"
        assert sanitize_filename(None) == "export.xlsx"


class TestVersionValidation:
    def test_valid_versions(self):
        assert validate_version_format("1.0.0") == True
        assert validate_version_format("10.20.30") == True
        assert validate_version_format("0.0.1") == True
    
    def test_invalid_versions(self):
        assert validate_version_format("1.0") == False
        assert validate_version_format("v1.0.0") == False
        assert validate_version_format("1.0.0.0") == False
        assert validate_version_format("abc") == False
    
    def test_version_comparison(self):
        assert is_newer_version("1.1.0", "1.0.0") == True
        assert is_newer_version("2.0.0", "1.9.9") == True
        assert is_newer_version("1.0.1", "1.0.0") == True
        
        assert is_newer_version("1.0.0", "1.0.0") == False
        assert is_newer_version("1.0.0", "1.1.0") == False
        assert is_newer_version("0.9.0", "1.0.0") == False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
