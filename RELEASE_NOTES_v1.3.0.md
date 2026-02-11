# LRU Tracker v1.3.0 Release Notes

**Release Date:** February 11, 2026

## 🚀 Major New Features

### 💾 Auto-Save with Idle Detection
Never lose your work again! The app now automatically saves your data every 3 minutes when you've been idle for 30 seconds.

**Features:**
- ✅ Automatic saving when you're away from keyboard
- ✅ Real-time status display ("✅ Saved 2m ago" or "💾 Unsaved")
- ✅ Configurable intervals (default: 3 min check, 30 sec idle)
- ✅ Background monitoring doesn't interfere with your work
- ✅ Smart detection - only saves if changes were made

**How it works:**
1. You make changes to station data
2. App monitors keyboard/mouse activity
3. When you're idle for 30+ seconds, it checks if 3 minutes have passed
4. If yes, auto-saves and shows confirmation in status bar
5. You never have to remember to click "Save Data"!

### 🔄 GitHub Sync for Multi-Computer Collaboration

Use GitHub as cloud storage for your LRU data. Perfect for users who work on multiple computers throughout the day.

**Use Case:** 
- Work on Computer A in the morning for your first walk
- Push data to GitHub before lunch
- Continue on Computer B in the afternoon for second walk
- Pull latest data and keep working seamlessly

**Features:**
- 📥 **Pull from GitHub** - Download latest data from your repository
- 📤 **Push to GitHub** - Upload your changes with timestamp and computer name
- 🔍 **Check Remote Changes** - See if others have pushed updates
- ⚠️ **Conflict Detection** - Warns you before overwriting remote data
- 🔄 **Auto-pull on start** - Optionally fetch latest data when app opens
- 💬 **Push prompt on close** - Reminds you to push before exiting
- 📊 **Sync status display** - See last sync time and repo info

### ⚙️ Editable Sync Settings Dialog

Configure GitHub sync directly in the app - no more manual config file editing!

**Features:**
- 📝 Input fields for repo owner, name, token, branch, and file path
- 🔐 Secure token field with show/hide toggle (password masking)
- 💾 Save Settings button applies changes immediately (no restart needed)
- 🔌 Test Connection button verifies your GitHub credentials
- 📚 Built-in quick setup guide with step-by-step instructions

**How to Setup:**
1. Create a GitHub repository (e.g., `lru-shared-data`)
2. Get a Personal Access Token from github.com/settings/tokens
3. Click "⚙️ Sync Settings" in the app
4. Fill in your repo details and paste your token
5. Click "💾 Save Settings"
6. Click "🔌 Test Connection" to verify
7. Start syncing!

## 📦 New Files

### Core Modules:
- `refactored/autosave_manager.py` - Auto-save logic with idle detection
- `refactored/github_sync_manager.py` - GitHub API wrapper for sync operations
- `github_sync_config.json` - Configuration template for GitHub sync

### Documentation:
- `docs/AUTOSAVE_FEATURE.md` - Complete auto-save feature documentation
- `docs/GITHUB_SYNC_SETUP.md` - Step-by-step GitHub sync setup guide (400+ lines)
- `docs/TESTING_GITHUB_SYNC.md` - Testing guide with expected outputs

## 🔐 Security & Privacy

### Token Storage:
- Tokens are stored **locally only** in `github_sync_config.json`
- Never pushed to GitHub or shared between computers
- Each computer should use its own token (can reuse the same token you generated)
- Token file should be added to `.gitignore` for security

### Token Expiration:
Since you mentioned needing to update the key every 30 days:
- Generate a new token when the old one expires
- Open "⚙️ Sync Settings"
- Paste the new token
- Click "💾 Save Settings"
- No other configuration changes needed!

## 📊 Rate Limits & Usage

GitHub API rate limits: **5,000 calls per hour** (authenticated)

Typical usage for 5-hour sync interval:
- Pull on start: 1 call
- Check remote: 1 call every 5 hours = ~5 calls/day
- Push: 1 call every 5 hours = ~5 calls/day
- **Total:** ~11 calls/day = **Well within limits!** ✅

Even with hourly syncing, you'd only use ~50 calls/day (1% of limit).

## 🔧 Technical Details

### Auto-Save:
- Background thread runs every 5 seconds to check conditions
- Tracks last user activity timestamp via keyboard/mouse bindings
- Only saves if: data changed + user idle + interval elapsed
- Thread-safe with proper locking
- Graceful shutdown on app close

### GitHub Sync:
- Uses GitHub REST API (Contents endpoint)
- Base64 encoding/decoding for file transfer
- SHA-based conflict detection
- Proper error handling (401 auth, 404 not found, network errors)
- Commit messages include computer name + timestamp for audit trail

## 🚀 Building the Release

### For Computer B Setup:

**Option 1: Use the installer** (recommended for new installations)
1. Download `LRU_Tracker_Setup.exe` from GitHub releases
2. Run installer
3. Copy `github_sync_config.json` template
4. Open app, click "⚙️ Sync Settings"
5. Configure with your repo info and token
6. Click "📥 Pull from GitHub" to get latest data

**Option 2: Use the .exe** (for incremental updates)
1. Download `LRU_Tracker.exe` from GitHub releases
2. Replace existing exe
3. Launch app
4. Sync settings will carry over from previous install

### Multi-Computer Workflow:

**Computer A (first time):**
1. Make changes (add stations, update LRUs)
2. Click "📤 Push to GitHub"
3. Data uploaded to `shared_data/lru_data.json` in your repo

**Computer B (first time):**
1. Install app
2. Configure GitHub sync (same repo, your own token)
3. Click "📥 Pull from GitHub"
4. All data from Computer A appears!

**Daily workflow:**
- Computer A morning: Pull → Work → Push
- Computer B afternoon: Pull → Work → Push
- Always pull first to get latest changes
- Always push before switching computers

## ⚠️ Important Notes

### Token Management:
- Each computer needs GitHub sync configured separately
- Token is stored locally in `github_sync_config.json`
- **When token expires (30 days):**
  - Generate new token on github.com/settings/tokens
  - Update in "⚙️ Sync Settings" on **each computer**
  - No need to recreate the repository

### Data Safety:
- Auto-save creates backup file before saving (`.backup`)
- GitHub sync warns before overwriting remote changes
- Always pull before making changes to avoid conflicts
- Commit history in GitHub provides audit trail

### First Push:
- The "Remote file not found" message is normal before first push
- Once you push, that message disappears
- The file is created at `shared_data/lru_data.json` in your repo

## 📚 Documentation

Full guides available in the `docs/` folder:
- `AUTOSAVE_FEATURE.md` - Auto-save internals and configuration
- `GITHUB_SYNC_SETUP.md` - Complete setup with screenshots
- `TESTING_GITHUB_SYNC.md` - Step-by-step testing checklist

## 🎯 What's Next

After releasing v1.3.0:
1. Test GitHub sync between two computers
2. Verify token expiration handling
3. Gather feedback on auto-save intervals
4. Consider adding sync conflict resolution UI

---

**Upgrade from v1.2.x:**
- Incremental update available (127 MB exe download)
- Settings and data files preserved
- GitHub sync is opt-in (disabled by default)
- Auto-save enabled automatically

**Questions?** Check the documentation or open an issue on GitHub!
