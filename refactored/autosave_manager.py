"""Auto-save manager for LRU Tracker application.

Handles intelligent auto-saving based on:
- User idle detection
- Change tracking
- Configurable save intervals
"""
import time
import threading
from datetime import datetime
from typing import Optional, Callable
from logger import get_logger

logger = get_logger(__name__)


class AutoSaveManager:
    """Manages automatic saving of data based on user activity and changes."""
    
    def __init__(self, 
                 save_callback: Callable[[], None],
                 auto_save_interval: int = 180,  # 3 minutes default
                 idle_threshold: int = 30):       # 30 seconds of no activity = idle
        """
        Initialize auto-save manager.
        
        Args:
            save_callback: Function to call when auto-saving
            auto_save_interval: Seconds between auto-saves (default 180 = 3 min)
            idle_threshold: Seconds of inactivity before considering user idle (default 30)
        """
        self.save_callback = save_callback
        self.auto_save_interval = auto_save_interval
        self.idle_threshold = idle_threshold
        
        # State tracking
        self.has_unsaved_changes = False
        self.last_activity_time = time.time()
        self.last_save_time = time.time()
        self.is_running = False
        
        # Threading
        self._timer_thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()
        
        # Callbacks for UI updates
        self.on_save_status_change: Optional[Callable[[str], None]] = None
        
    def start(self) -> None:
        """Start the auto-save timer."""
        if self.is_running:
            logger.warning("Auto-save already running")
            return
            
        self.is_running = True
        self._stop_event.clear()
        self._timer_thread = threading.Thread(target=self._auto_save_loop, daemon=True)
        self._timer_thread.start()
        logger.info(f"Auto-save started (interval: {self.auto_save_interval}s, idle threshold: {self.idle_threshold}s)")
    
    def stop(self) -> None:
        """Stop the auto-save timer."""
        if not self.is_running:
            return
            
        self.is_running = False
        self._stop_event.set()
        if self._timer_thread:
            self._timer_thread.join(timeout=2)
        logger.info("Auto-save stopped")
    
    def mark_changed(self) -> None:
        """Mark that data has been changed (needs saving)."""
        self.has_unsaved_changes = True
        self.last_activity_time = time.time()
        self._update_status()
        logger.debug("Data marked as changed")
    
    def mark_saved(self) -> None:
        """Mark that data has been saved."""
        self.has_unsaved_changes = False
        self.last_save_time = time.time()
        self._update_status()
        logger.debug("Data marked as saved")
    
    def register_activity(self) -> None:
        """Register user activity (keyboard/mouse)."""
        self.last_activity_time = time.time()
    
    def is_user_idle(self) -> bool:
        """Check if user is currently idle."""
        return (time.time() - self.last_activity_time) >= self.idle_threshold
    
    def should_auto_save(self) -> bool:
        """Determine if auto-save should happen now."""
        if not self.has_unsaved_changes:
            return False
        
        if not self.is_user_idle():
            return False
        
        time_since_last_save = time.time() - self.last_save_time
        return time_since_last_save >= self.auto_save_interval
    
    def force_save(self) -> None:
        """Force an immediate save regardless of idle state."""
        if self.has_unsaved_changes:
            self._perform_save()
    
    def _auto_save_loop(self) -> None:
        """Background thread that checks and performs auto-saves."""
        while not self._stop_event.is_set():
            try:
                if self.should_auto_save():
                    self._perform_save()
                
                # Check every 5 seconds
                self._stop_event.wait(5)
                
            except Exception as e:
                logger.error(f"Error in auto-save loop: {e}")
    
    def _perform_save(self) -> None:
        """Execute the save callback."""
        try:
            logger.info("Auto-saving data...")
            self.save_callback()
            self.mark_saved()
            logger.info("Auto-save completed")
        except Exception as e:
            logger.error(f"Auto-save failed: {e}")
    
    def _update_status(self) -> None:
        """Update UI status callback if registered."""
        if self.on_save_status_change:
            status = self.get_status_text()
            self.on_save_status_change(status)
    
    def get_status_text(self) -> str:
        """Get human-readable status text for UI."""
        if self.has_unsaved_changes:
            time_since_change = int(time.time() - self.last_activity_time)
            if time_since_change < 60:
                return f"💾 Unsaved changes ({time_since_change}s ago)"
            else:
                mins = time_since_change // 60
                return f"💾 Unsaved changes ({mins}m ago)"
        else:
            # Show time since last save
            time_since_save = int(time.time() - self.last_save_time)
            if time_since_save < 60:
                return f"✅ Saved {time_since_save}s ago"
            elif time_since_save < 3600:
                mins = time_since_save // 60
                return f"✅ Saved {mins}m ago"
            else:
                hours = time_since_save // 3600
                return f"✅ Saved {hours}h ago"
    
    def get_last_save_time(self) -> datetime:
        """Get the last save time as datetime."""
        return datetime.fromtimestamp(self.last_save_time)
    
    def configure(self, auto_save_interval: Optional[int] = None, 
                  idle_threshold: Optional[int] = None) -> None:
        """
        Update configuration on the fly.
        
        Args:
            auto_save_interval: New auto-save interval in seconds
            idle_threshold: New idle threshold in seconds
        """
        if auto_save_interval is not None:
            self.auto_save_interval = auto_save_interval
            logger.info(f"Auto-save interval updated to {auto_save_interval}s")
        
        if idle_threshold is not None:
            self.idle_threshold = idle_threshold
            logger.info(f"Idle threshold updated to {idle_threshold}s")
