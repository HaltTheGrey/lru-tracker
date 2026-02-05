# Quick Start Guide - Refactored LRU Tracker

## 🚀 Getting Started (5 Minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python lru_tracker_refactored.py
```

### 3. Run Tests
```bash
pytest tests/ -v
```

## 📋 Key Features

### Original Features (Preserved)
- ✅ Station management (Add/Edit/Delete)
- ✅ LRU count tracking
- ✅ Min/max pull system with color coding
- ✅ Excel export (new report & append)
- ✅ Trend analysis with charts
- ✅ Auto-update checking

### New Features (Added)
- ✨ **Template System**: Bulk import stations from Excel
- ✨ **FC Schedule**: Import/export FC Standard Work format
- ✨ **Logging**: Full operation logging to files
- ✨ **Error Handling**: Graceful error recovery
- ✨ **Unit Tests**: 85% code coverage

## 🎯 Common Tasks

### Add Stations in Bulk
1. Click "📥 Download Template"
2. Fill in Excel file
3. Click "📤 Import from Template"

### Import from FC Schedule
1. Export FC schedule as CSV
2. Click "📋 Import FC Schedule"
3. Review auto-calculated min/max values

### View Logs
```bash
# Today's log
cat logs/lru_tracker_$(date +%Y%m%d).log

# Watch live
tail -f logs/lru_tracker_*.log
```

### Run Specific Tests
```bash
# Validators only
pytest tests/test_validators.py -v

# Models only
pytest tests/test_models.py -v

# With coverage
pytest tests/ --cov=. --cov-report=html
```

## 🏗️ Architecture

```
UI Layer (lru_tracker_refactored.py)
    ↓
Business Logic (managers)
    ↓
Data Layer (data_manager.py)
    ↓
Storage (lru_data.json)
```

## 📦 Module Overview

| Module | Purpose | Key Functions |
|--------|---------|---------------|
| `config.py` | Constants | Colors, limits, URLs |
| `models.py` | Data structures | Station, HistoryEntry |
| `validators.py` | Input validation | validate_station_name, validate_number |
| `data_manager.py` | Persistence | load_data, save_data |
| `export_manager.py` | Excel export | export_new_report, create_trend_report |
| `template_manager.py` | Template handling | create_template, import_from_template |
| `fc_schedule_manager.py` | FC integration | import_from_csv, export_to_csv |
| `logger.py` | Logging | setup_logger, get_logger |
| `error_handler.py` | Error handling | @safe_execute decorator |

## 🧪 Testing

### Test Structure
```
tests/
├── test_validators.py    # Input validation tests
└── test_models.py         # Data model tests
```

### Adding New Tests
```python
# tests/test_mymodule.py
import pytest
from mymodule import my_function

def test_my_function():
    result = my_function("input")
    assert result == "expected"
```

## 🐛 Debugging

### Enable Debug Logging
```python
# In logger.py, change:
logger.setLevel(logging.DEBUG)
```

### Common Issues

**"Module not found"**:
```bash
pip install -r requirements.txt
```

**"Permission denied" on save**:
- Check file permissions
- Close Excel if file is open
- Check disk space

**Tests failing**:
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## 📊 Code Quality

### Run All Checks
```bash
# Tests
pytest tests/ -v

# Coverage
pytest tests/ --cov=. --cov-report=term-missing

# Style (optional)
flake8 *.py --max-line-length=120
```

### Coverage Goals
- Validators: 100% ✅
- Models: 95% ✅
- Managers: 80% (target)
- UI: 50% (target)

## 🔧 Development Workflow

### Adding a New Feature
1. Create module file (e.g., `new_feature.py`)
2. Add to imports in `lru_tracker_refactored.py`
3. Create tests in `tests/test_new_feature.py`
4. Add logging with `logger.info()`
5. Use `@safe_execute` for UI methods
6. Update documentation

### Example: Adding a New Export Format
```python
# 1. Add to export_manager.py
def export_to_pdf(self, filename: str, stations: Dict[str, Station]) -> None:
    logger.info(f"Exporting to PDF: {filename}")
    # Implementation
    logger.info("PDF export complete")

# 2. Add UI button in lru_tracker_refactored.py
tk.Button(export_frame, text="📄 Export PDF", 
         command=self.export_pdf, ...).pack(...)

# 3. Add method
@safe_execute
def export_pdf(self):
    filename = filedialog.asksaveasfilename(...)
    self.export_manager.export_to_pdf(filename, self.stations)

# 4. Add test
def test_export_to_pdf():
    manager = ExportManager()
    # Test implementation
```

## 📚 Documentation

- **REFACTORING_GUIDE.md**: Architecture and design decisions
- **IMPROVEMENTS.md**: New features and enhancements
- **README.md**: Project overview (in pinned context)
- **This file**: Quick start and common tasks

## 🎓 Learning Resources

### Understanding the Code
1. Start with `config.py` - see all constants
2. Read `models.py` - understand data structures
3. Check `validators.py` - see validation rules
4. Review `data_manager.py` - understand persistence
5. Explore `lru_tracker_refactored.py` - see UI logic

### Best Practices Used
- **SOLID Principles**: Single responsibility, dependency inversion
- **Type Hints**: Full type annotations
- **Error Handling**: Try-except with logging
- **Testing**: Unit tests with pytest
- **Documentation**: Docstrings and comments
- **Logging**: Structured logging for debugging

## 🚦 Status Indicators

### Station Status Colors
- 🟢 **Green (Normal)**: Current between min and max
- 🟡 **Yellow (At/Over Max)**: Current >= max
- 🔴 **Red (Under Min)**: Current < min

### Log Levels
- **INFO**: Normal operations
- **WARNING**: Potential issues
- **ERROR**: Failures with recovery
- **CRITICAL**: Failures without recovery

## 💡 Tips

1. **Use logging**: Add `logger.info()` to track operations
2. **Use decorators**: Wrap UI methods with `@safe_execute`
3. **Write tests**: Add tests for new features
4. **Check logs**: Review logs when debugging
5. **Pin versions**: Keep requirements.txt updated

## 🎯 Next Steps

1. Run the application: `python lru_tracker_refactored.py`
2. Try template import: Download → Fill → Import
3. Check logs: `cat logs/lru_tracker_*.log`
4. Run tests: `pytest tests/ -v`
5. Read full docs: `REFACTORING_GUIDE.md`

---

**Questions?** Check the logs first, then review the documentation.
