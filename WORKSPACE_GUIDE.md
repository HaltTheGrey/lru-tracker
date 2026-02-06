# 📂 Workspace Guide

## Quick Navigation

### 🚀 To Run the Application
```bash
cd refactored
python lru_tracker_refactored.py
```

### 🧪 To Run Tests
```bash
cd refactored
pytest tests/ -v
```

### 📦 To Install Dependencies
```bash
pip install -r requirements.txt
```

## 📁 Directory Structure

```
lru-tracker/
├── refactored/          ⭐ MAIN CODE - Use this!
│   ├── lru_tracker_refactored.py  # Main application
│   ├── config.py                   # Configuration
│   ├── models.py                   # Data models
│   ├── validators.py               # Input validation
│   ├── data_manager.py             # Data persistence
│   ├── export_manager.py           # Excel export
│   ├── template_manager.py         # Template handling
│   ├── fc_schedule_manager.py      # FC integration
│   ├── update_checker.py           # Update checking
│   ├── logger.py                   # Logging
│   ├── error_handler.py            # Error handling
│   └── tests/                      # Unit tests
│
├── archive/             📚 Original code (reference only)
├── docs/                📖 Documentation
├── distribution/        🔨 Build scripts
├── scripts/             🛠️ Utility scripts
├── logs/                📝 Application logs
│
├── README.md            📄 Main documentation
├── requirements.txt     📦 Dependencies
└── .gitignore          🚫 Git ignore rules
```

## 🎯 Key Files

| File | Purpose |
|------|---------|
| `refactored/lru_tracker_refactored.py` | Main application - start here |
| `refactored/config.py` | All configuration settings |
| `refactored/models.py` | Data structures |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

## 🔧 Common Tasks

### Add a New Feature
1. Identify the appropriate module in `refactored/`
2. Add your code following existing patterns
3. Add tests in `refactored/tests/`
4. Run tests to verify

### Modify Configuration
- Edit `refactored/config.py`
- All constants are centralized there

### Debug Issues
- Check logs in `logs/` directory
- Run with verbose logging
- Check test output

### Build Executable
```bash
cd distribution
BUILD_WINDOWS_ONE_CLICK.bat
```

## 📚 Documentation

- **User Guides**: `docs/user-guides/`
- **Developer Guides**: `docs/developer-guides/`
- **Security Docs**: `docs/security/`
- **Architecture**: `REFACTORING_GUIDE.md`
- **Improvements**: `IMPROVEMENTS.md`

## 🆘 Need Help?

1. Check `README.md` for overview
2. Check `docs/` for detailed guides
3. Check `logs/` for error messages
4. Run tests to verify setup
5. Open an issue on GitHub

## ✅ Quick Checklist

Before committing code:
- [ ] Code follows existing patterns
- [ ] Tests added/updated
- [ ] Tests pass (`pytest tests/ -v`)
- [ ] Documentation updated if needed
- [ ] No sensitive data in code

## 🎓 Learning Path

1. Read `README.md`
2. Explore `refactored/config.py`
3. Review `refactored/models.py`
4. Study `refactored/lru_tracker_refactored.py`
5. Read `REFACTORING_GUIDE.md` for architecture
6. Check tests in `refactored/tests/`

---

**Status**: ✅ Production Ready | **Version**: 1.1.0 | **Coverage**: 85%
