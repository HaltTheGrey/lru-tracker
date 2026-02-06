"""Test script to verify update checker works with v1.2.0"""
import sys
import os

# Add refactored directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'refactored'))

from update_checker import UpdateChecker
from validators import is_newer_version

print("=" * 60)
print("UPDATE CHECKER TEST")
print("=" * 60)

# Test 1: Version comparison
print("\n1. Testing version comparison:")
print(f"   Current: 1.1.0")
print(f"   Latest:  1.2.0")
print(f"   Is newer? {is_newer_version('1.2.0', '1.1.0')}")

# Test 2: Load local version file
print("\n2. Testing local version file:")
import json
with open('version_v1.2.0.json', 'r') as f:
    version_info = json.load(f)
    print(f"   Version: {version_info['version']}")
    print(f"   Download URL: {version_info['download_url']}")
    print(f"   Release notes preview: {version_info['release_notes'][:100]}...")

# Test 3: Simulate update check
print("\n3. Simulating update check:")
print(f"   Current version: 1.1.0")
print(f"   Latest version:  {version_info['version']}")
if is_newer_version(version_info['version'], '1.1.0'):
    print("   ✅ UPDATE AVAILABLE!")
    print(f"   User would see: 'Update to v{version_info['version']} available'")
else:
    print("   ❌ No update available")

print("\n" + "=" * 60)
print("TEST COMPLETE")
print("=" * 60)

print("\n📝 To test in the actual app:")
print("1. Temporarily modify update_checker.py:")
print("   - Comment out the HTTPS check (line 22-23)")
print("   - Use file:// URL for local testing")
print("\n2. Or merge to main and test with GitHub URL")
