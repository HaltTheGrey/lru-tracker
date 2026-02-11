# Testing GitHub Sync Feature

## 🎯 Quick Start Test

### Step 1: Create Test Repository

1. Go to https://github.com/new
2. Name: `lru-test-sync` (or any name)
3. Privacy: **Private** (recommended)
4. ✅ Initialize with README
5. Click "Create repository"

### Step 2: Get Personal Access Token

1. Go to https://github.com/settings/tokens
2. "Generate new token" → "Generate new token (classic)"
3. Note: `LRU Test`
4. Scopes: ✅ `repo`
5. Click "Generate token"
6. **COPY THE TOKEN!** (ghp_xxxxxxxxxxxx)

### Step 3: Configure

Edit `github_sync_config.json`:

```json
{
  "github_sync": {
    "enabled": true,
    "repo_owner": "YOUR_USERNAME",
    "repo_name": "lru-test-sync",
    "data_file_path": "shared_data/lru_data.json",
    "branch": "main",
    "token": "ghp_YOUR_TOKEN_HERE",
    "auto_pull_on_start": true,
    "prompt_push_on_close": true,
    "show_sync_status": true
  }
}
```

### Step 4: Test on Computer A (or same computer, different data)

```
1. Open LRU Tracker
2. Create a station: "Station A" (min: 5, max: 20)
3. Update count to 10
4. Click "📤 Push to GitHub"
5. ✅ Should see success message
```

Check GitHub:
- Go to your repo
- Navigate to `shared_data/lru_data.json`
- You should see your data!

### Step 5: Test Pull (simulate Computer B)

```
Option A - Same Computer:
1. Delete lru_data.json locally
2. Restart app
3. Click "📥 Pull from GitHub"
4. ✅ Station A should appear!

Option B - Different Computer:
1. Install app on another computer
2. Copy github_sync_config.json (with same token)
3. Open app
4. Click "📥 Pull from GitHub"
5. ✅ All data from Computer A appears!
```

### Step 6: Test Collaboration

**Computer A:**
```
1. Update Station A to count: 15
2. Click "📤 Push to GitHub"
```

**Computer B:**
```
1. Click "📥 Pull from GitHub"
2. ✅ Should see count changed to 15!
3. Add Station B (min: 3, max: 15)
4. Click "📤 Push to GitHub"
```

**Computer A:**
```
1. Click "🔄 Check Remote"
   → Should say "Remote has changes"
2. Click "📥 Pull from GitHub"
3. ✅ Station B should appear!
```

## ✅ Expected Results

### Push Success
```
✅ Data pushed to GitHub!

Stations: 2
History entries: 5

Other computers can now pull your changes.
```

### Pull Success
```
✅ Data pulled from GitHub!

Stations: 2
History entries: 5

Last sync: 2026-02-11 14:30:45
```

### Check Remote - Has Changes
```
🔔 Remote data has been updated!

Someone else has pushed changes.

Use 'Pull from GitHub' to get the latest data.
```

### Check Remote - Up to Date
```
✅ You have the latest data!

No remote changes detected.
```

## 🐛 Troubleshooting

### "Repository not found"
- Check repo_owner and repo_name in config
- Verify repo exists on GitHub
- If private, check token has `repo` scope

### "Authentication failed"
- Token is wrong or expired
- Regenerate at github.com/settings/tokens
- Update config file

### "Connection error"
- Check internet connection
- Try github.com in browser
- Check firewall settings

### Buttons not showing
- Verify github_sync_config.json exists
- Check `"enabled": true`
- Restart app

## 📊 What Gets Synced

✅ Synced:
- All stations (names, min/max, current counts)
- Complete history for each station
- Global history log
- Timestamps

❌ Not Synced:
- App settings (local preferences)
- Templates
- UI layout

## 🔒 Security Notes

- ⚠️ Token = password, keep it private!
- Private repos = only you and collaborators see data
- Each push creates a commit (audit trail)
- Can see who changed what on GitHub

## 🎓 Advanced Testing

### Test Conflict Detection

**Computer A:**
```
1. Make changes locally
2. DON'T push yet
```

**Computer B:**
```
1. Make different changes
2. Push to GitHub
```

**Computer A:**
```
1. Now try to push
2. ✅ Should warn "Remote changed since last sync"
3. Pull first, then push again
```

### Test Auto-Pull on Startup

```
1. Set "auto_pull_on_start": true in config
2. Computer B pushes changes
3. Restart app on Computer A
4. ✅ Should prompt to pull latest data
```

### View History on GitHub

```
1. Go to your repo
2. Click on "commits"
3. See: "Updated by COMPUTER-A at 2026-02-11 14:30:00"
4. Click commit to see exact changes
```

## 📝 Real-World Workflow

**Morning Shift (8 AM - 12 PM):**
```
Computer A:
- Opens app (auto-pulls if enabled)
- Does warehouse walk
- Updates LRU counts
- Clicks "📤 Push to GitHub" before lunch
```

**Afternoon Shift (1 PM - 5 PM):**
```
Computer B:
- Opens app
- Clicks "📥 Pull from GitHub"
- Sees morning shift updates
- Continues walk
- Clicks "📤 Push to GitHub" at end of shift
```

**Next Morning:**
```
Computer A:
- Opens app
- Sees yesterday afternoon's updates
- Continues tracking
```

## 🚀 Success Criteria

You'll know it's working when:
- ✅ Push shows success message
- ✅ Data appears in GitHub repo
- ✅ Pull on other computer shows same data
- ✅ Changes sync between computers
- ✅ Sync status shows last sync time
- ✅ Test connection succeeds

## 📞 Need Help?

1. Check this guide
2. View app logs for errors
3. Use "🔌 Test Connection" in settings
4. Check GitHub repo commits
5. Review GITHUB_SYNC_SETUP.md for details

Happy syncing! 🎉
