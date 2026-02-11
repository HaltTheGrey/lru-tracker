"""First-time setup helper for GitHub sync configuration."""
import json
import shutil
from pathlib import Path

def setup_github_sync_config():
    """Create github_sync_config.json from template if it doesn't exist."""
    config_file = Path("github_sync_config.json")
    template_file = Path("github_sync_config.json.template")
    
    if config_file.exists():
        print("✅ Config file already exists: github_sync_config.json")
        print("   Use '⚙️ Sync Settings' in the app to modify it.")
        return True
    
    if not template_file.exists():
        print("❌ Template file not found: github_sync_config.json.template")
        print("   Please ensure the template file is in the same directory.")
        return False
    
    try:
        # Copy template to config
        shutil.copy(template_file, config_file)
        print("✅ Created config file from template!")
        print()
        print("📝 Next steps:")
        print("   1. Open the app")
        print("   2. Click '⚙️ Sync Settings'")
        print("   3. Fill in your GitHub repository details")
        print("   4. Paste your Personal Access Token")
        print("   5. Click '💾 Save Settings'")
        print("   6. Click '🔌 Test Connection'")
        print()
        print("🔗 Get a token: https://github.com/settings/tokens")
        print("   → Generate new token (classic)")
        print("   → Check 'repo' scope")
        print("   → Copy the token (ghp_...)")
        return True
        
    except Exception as e:
        print(f"❌ Failed to create config file: {e}")
        return False

if __name__ == "__main__":
    print("🚀 LRU Tracker - GitHub Sync Setup")
    print("=" * 50)
    print()
    setup_github_sync_config()
