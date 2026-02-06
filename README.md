# LRU Tracker for Fulfillment Centers

Inventory tracking application for managing LRU (Lowest Replaceable Unit) counts at FC stations using a min/max pull system.

Version: 1.1.0 | Python 3.8+ | License: MIT

## Features

- Min/Max Pull System with color-coded status indicators
- Station Management with CRUD operations
- LRU Tracking with automatic history logging
- Excel Export (new files or append to existing)
- Trend Analysis with built-in charting
- Template System for bulk station setup
- FC Schedule Import from Standard Work Spreadsheet
- Auto-Updates with version checking
- Data Persistence in JSON format

## Quick Start

### For End Users

1. Install Python 3.8+ (if not already installed)
2. Clone or download this repository
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   cd refactored
   python lru_tracker_refactored.py
   ```

### For Developers

```bash
# Clone repository
git clone https://github.com/HaltTheGrey/lru-tracker.git
cd lru-tracker

# Install dependencies
pip install -r requirements.txt

# Run application
cd refactored
python lru_tracker_refactored.py

# Run tests
pytest tests/ -v
```

## Project Structure

```
lru-tracker/
├── refactored/              # Production code
│   ├── lru_tracker_refactored.py
│   ├── config.py
│   ├── models.py
│   ├── validators.py
│   ├── data_manager.py
│   ├── export_manager.py
│   ├── template_manager.py
│   ├── fc_schedule_manager.py
│   ├── update_checker.py
│   ├── logger.py
│   ├── error_handler.py
│   └── tests/
├── archive/                 # Original code
├── docs/                    # Documentation
├── distribution/            # Build scripts
└── requirements.txt
```

## Documentation

- [Quick Start Guide](docs/user-guides/QUICK_START.md)
- [Template Guide](docs/user-guides/TEMPLATE_GUIDE.md)
- [FC Schedule Import](docs/user-guides/FC_SCHEDULE_IMPORT_GUIDE.md)
- [Refactoring Guide](REFACTORING_GUIDE.md)
- [Improvements Summary](IMPROVEMENTS.md)

## Testing

```bash
cd refactored
pytest tests/ -v
pytest tests/ --cov=. --cov-report=html
```

Test Coverage: 85%

## Security Features

- Input validation with regex patterns
- Path traversal prevention
- HTTPS-only update checks
- Atomic file writes with backups
- Sanitized error messages
- Comprehensive logging

## Code Quality

| Metric | Value |
|--------|-------|
| Total Modules | 10 |
| Test Coverage | 85% |
| Lines of Code | ~2,500 |
| Test Cases | 35+ |

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Support

- Check the [documentation](docs/)
- Report bugs via [GitHub Issues](https://github.com/HaltTheGrey/lru-tracker/issues)
- Contact the maintainer
