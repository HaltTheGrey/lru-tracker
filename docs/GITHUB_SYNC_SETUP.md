# GitHub Sync Setup Guide

## 📋 Overview

This feature allows multiple computers to share LRU tracking data via GitHub. Perfect for shift handoffs where Computer A does the morning walk and Computer B continues in the afternoon.

## 🎯 Use Case Example

**Morning Shift (Computer A):**
- Opens app at 8 AM
- Creates daily template
- Does warehouse walk, updates LRU counts
- Clicks "📤 Push to GitHub" before leaving at 12 PM

**Afternoon Shift (Computer B):**
- Opens app at 1 PM
- Clicks "📥 Pull from GitHub"
- Sees all of Computer A's updates
- Continues updating stations
- Clicks "📤 Push to GitHub" at end of shift

## 🚀 Setup Instructions

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `lru-shared-data` (or any name you want)
3. Description: "Shared LRU tracking data"
4. Choose **Private** (recommended) or Public
5. ✅ Initialize with README
6. Click "Create repository"

### Step 2: Get Personal Access Token

GitHub requires a token for API access:

1. Go to https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Note: `LRU Tracker Access`
4. Expiration: Choose `No expiration` or `1 year`
5. Select scopes:
   - ✅ `repo` (Full control of private repositories)
6. Click "Generate token"
7. **⚠️ COPY THE TOKEN IMMEDIATELY** (you won't see it again!)
   - Example: `ghp_1234567890abcdefghijklmnopqrstuvwxyz`

### Step 3: Configure App

1. Open `github_sync_config.json` in the app folder
2. Update these fields:

```json
{
  "github_sync": {
    "enabled": true,
    "repo_owner": "YOUR_GITHUB_USERNAME",
    "repo_name": "lru-shared-data",
    "data_file_path": "shared_data/lru_data.json",
    "branch": "main",
    "token": "ghp_YOUR_TOKEN_HERE",
    "auto_pull_on_start": true,
    "prompt_push_on_close": true,
    "show_sync_status": true
  }
}
```

**Field Explanations:**
- `enabled`: Set to `true` to activate GitHub sync
- `repo_owner`: Your GitHub username (e.g., "HaltTheGrey")
- `repo_name`: Repository name you created
- `data_file_path`: Where to store file in repo (can customize)
- `branch`: Which branch to use (usually "main")
- `token`: Your personal access token from Step 2
- `auto_pull_on_start`: Automatically check for updates when app opens
- `prompt_push_on_close`: Ask to push changes when closing app
- `show_sync_status`: Display sync status in UI

### Step 4: First Sync

**On Computer A (First Setup):**
1. Open LRU Tracker app
2. Create your stations as normal
3. Click "📤 Push to GitHub" button
4. App creates the file in your GitHub repo
5. ✅ Data is now in the cloud!

**On Computer B (and all other computers):**
1. Install LRU Tracker app
2. Copy the same `github_sync_config.json` file
   - ⚠️ Same token, same repo settings
3. Open app
4. Click "📥 Pull from GitHub"
5. ✅ You now have Computer A's data!

## 💡 How to Use Daily

### Morning Workflow
```
Computer A:
1. Open app (auto-pulls latest if enabled)
2. Do morning walk and update stations
3. Click "📤 Push to GitHub" when done
```

### Afternoon Workflow
```
Computer B:
1. Open app
2. Click "📥 Pull from GitHub" (gets Computer A's updates)
3. Continue updating stations
4. Click "📤 Push to GitHub" when done
```

## 🔄 Sync Buttons in App

### 📥 Pull from GitHub
- Downloads latest data from GitHub
- Shows who last updated and when
- Asks before overwriting local changes

### 📤 Push to GitHub
- Uploads your current data to GitHub
- Includes automatic commit message with computer name and time
- Other users will see your changes on next pull

### 🔄 Sync Status
- Shows last sync time
- Indicates if remote has new changes
- Displays connection status

## ⚠️ Important Notes

### Conflict Resolution
If both computers edit at the same time:
- Last push wins (overwrites previous)
- App shows warning if remote changed since last pull
- Solution: Pull before pushing

### Best Practices
1. **Pull before starting work** - Get latest data
2. **Push when done** - Share your updates
3. **Don't edit simultaneously** - Coordinate shifts
4. **Pull frequently** - Stay in sync

### Token Security
- ⚠️ **Keep your token private!**
- Don't share screenshots with token visible
- If exposed, regenerate at https://github.com/settings/tokens
- Each computer can use the same token (for same team)

### Rate Limits
- GitHub allows 5,000 API calls/hour
- Each pull = 1 call, each push = 2 calls
- Your use case (~10-20 calls/day) is well within limits

## 🔧 Troubleshooting

### "Repository not found"
- Check `repo_owner` and `repo_name` in config
- Verify repository exists at github.com/owner/repo
- If private, ensure token has `repo` scope

### "Authentication failed"
- Token is wrong or expired
- Regenerate token and update config
- Ensure token has `repo` permission

### "Connection error"
- Check internet connection
- Verify GitHub is accessible (not blocked by firewall)
- Try visiting github.com in browser

### "Conflict detected"
- Remote file changed since your last pull
- Click "📥 Pull from GitHub" first
- Review changes, then push again

### Pull/Push buttons not showing
- Check `github_sync_config.json` exists
- Verify `"enabled": true`
- Restart app after config changes

## 📊 What Gets Synced

The following data is synchronized:
- ✅ All stations (names, min/max values, current counts)
- ✅ Complete history (all updates with timestamps)
- ✅ Global history log
- ❌ App settings (local to each computer)
- ❌ Templates (use separate export/import)

## 🔒 Security & Privacy

### Private Repository (Recommended)
- Only people with access can see data
- Add collaborators: Settings → Collaborators
- Free for unlimited private repos

### Public Repository
- Anyone can see your data
- Good for non-sensitive tracking
- Still requires token to push changes

### Token Permissions
- Token grants full access to your repositories
- Treat it like a password
- Regenerate if compromised

## 🎓 Advanced Usage

### Multiple Teams
Create separate repos for each team:
- Team A: `lru-team-a`
- Team B: `lru-team-b`

### Audit Trail
- GitHub shows who made each change
- View history: github.com/owner/repo/commits
- See exact time and computer name

### Backup Strategy
- GitHub acts as automatic cloud backup
- Download history anytime from repo
- Export to Excel from any computer

### Custom File Paths
Change `data_file_path` to organize by date:
```json
"data_file_path": "2026/february/lru_data_2026-02-11.json"
```

## 📞 Support

Need help?
1. Check troubleshooting section above
2. View GitHub repo commits for sync history
3. Test connection with "🔄 Test Connection" button in app
4. Check app logs for detailed error messages

## 🚀 Future Enhancements

Planned features:
- [ ] Auto-sync every X minutes
- [ ] Merge conflicts resolution UI
- [ ] Multi-repo support (different shifts/buildings)
- [ ] Sync history viewer
- [ ] Offline mode with queue

---

**Happy Collaborating! 🎉**

Multiple computers, one data source, seamless handoffs!
