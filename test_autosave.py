"""Test script for auto-save functionality."""
import sys
sys.path.insert(0, 'refactored')

from autosave_manager import AutoSaveManager
import time

def mock_save():
    print("✅ Auto-save triggered!")

# Create auto-save manager with 10-second interval for testing
manager = AutoSaveManager(
    save_callback=mock_save,
    auto_save_interval=10,  # 10 seconds for testing
    idle_threshold=5        # 5 seconds idle
)

print("🧪 Testing Auto-Save Manager")
print("=" * 50)
print(f"Auto-save interval: {manager.auto_save_interval}s")
print(f"Idle threshold: {manager.idle_threshold}s")
print()

# Start auto-save
manager.start()
print("✅ Auto-save started")
print()

# Simulate data change
print("📝 Simulating data change...")
manager.mark_changed()
print(f"Status: {manager.get_status_text()}")
print()

# Simulate user activity
print("⌨️ Simulating user activity...")
for i in range(3):
    time.sleep(2)
    manager.register_activity()
    print(f"Activity registered (idle: {manager.is_user_idle()})")

print()
print("💤 Waiting for user to become idle (5 seconds)...")
time.sleep(6)
print(f"User idle: {manager.is_user_idle()}")
print(f"Status: {manager.get_status_text()}")
print()

print("⏰ Waiting for auto-save (10 seconds total since change)...")
time.sleep(5)
print(f"Should auto-save: {manager.should_auto_save()}")
print()

print("Waiting for auto-save to trigger...")
time.sleep(2)

# Stop
time.sleep(1)
manager.stop()
print()
print("✅ Auto-save stopped")
print(f"Final status: {manager.get_status_text()}")
