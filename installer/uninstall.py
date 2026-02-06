"""
LRU Tracker - Uninstaller
Removes LRU Tracker from the system
"""
import tkinter as tk
from tkinter import messagebox
import os
import shutil
import winreg
from pathlib import Path
import sys


class UninstallerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Uninstall LRU Tracker")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        
        # Get install location from registry
        self.install_path = self.get_install_location()
        
        self.create_widgets()
        
    def get_install_location(self):
        """Get installation path from registry"""
        try:
            key_path = r"Software\Microsoft\Windows\CurrentVersion\Uninstall\LRU Tracker"
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path) as key:
                install_loc, _ = winreg.QueryValueEx(key, "InstallLocation")
                return Path(install_loc)
        except:
            # Fallback to default location
            return Path(os.environ.get('PROGRAMFILES', 'C:\\Program Files')) / "LRU Tracker"
    
    def create_widgets(self):
        # Header
        header_frame = tk.Frame(self.root, bg='#e74c3c', height=80)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        tk.Label(header_frame, text="🗑️ Uninstall LRU Tracker", 
                font=('Arial', 18, 'bold'), bg='#e74c3c', fg='white').pack(pady=25)
        
        # Content
        content_frame = tk.Frame(self.root, bg='white')
        content_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        tk.Label(content_frame, 
                text=f"This will remove LRU Tracker from your computer.\n\n"
                     f"Installation location:\n{self.install_path}\n\n"
                     f"The following will be removed:\n"
                     f"• Application files\n"
                     f"• Desktop shortcut\n"
                     f"• Start Menu shortcut\n"
                     f"• Registry entries\n\n"
                     f"Note: Your data files (lru_data.json) will be preserved.",
                font=('Arial', 10), bg='white', justify='left').pack(pady=20)
        
        # Buttons
        button_frame = tk.Frame(self.root, bg='white')
        button_frame.pack(fill='x', padx=20, pady=(0, 20))
        
        tk.Button(button_frame, text="Cancel", command=self.root.quit,
                 bg='#95a5a6', fg='white', font=('Arial', 10, 'bold'),
                 width=12, pady=5).pack(side='right', padx=(5, 0))
        
        tk.Button(button_frame, text="Uninstall", command=self.start_uninstall,
                 bg='#e74c3c', fg='white', font=('Arial', 10, 'bold'),
                 width=12, pady=5).pack(side='right')
    
    def start_uninstall(self):
        if not messagebox.askyesno("Confirm Uninstall", 
                                   "Are you sure you want to uninstall LRU Tracker?"):
            return
        
        try:
            # Remove shortcuts
            self.remove_shortcut("Desktop")
            self.remove_shortcut("StartMenu")
            
            # Remove from registry
            self.remove_registry_entry()
            
            # Remove installation directory
            if self.install_path.exists():
                shutil.rmtree(self.install_path)
            
            messagebox.showinfo("Success", 
                              "LRU Tracker has been successfully uninstalled.\n\n"
                              "Your data files have been preserved.")
            
            self.root.quit()
            
        except Exception as e:
            messagebox.showerror("Uninstall Error", 
                               f"An error occurred during uninstallation:\n\n{str(e)}")
    
    def remove_shortcut(self, location):
        """Remove Windows shortcuts"""
        try:
            if location == "Desktop":
                shortcut_path = Path.home() / "Desktop" / "LRU Tracker.lnk"
            else:  # StartMenu
                shortcut_path = Path(os.environ['APPDATA']) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "LRU Tracker.lnk"
            
            if shortcut_path.exists():
                shortcut_path.unlink()
        except Exception as e:
            print(f"Could not remove {location} shortcut: {e}")
    
    def remove_registry_entry(self):
        """Remove from Windows registry"""
        try:
            key_path = r"Software\Microsoft\Windows\CurrentVersion\Uninstall\LRU Tracker"
            winreg.DeleteKey(winreg.HKEY_CURRENT_USER, key_path)
        except Exception as e:
            print(f"Could not remove registry entry: {e}")


def main():
    root = tk.Tk()
    app = UninstallerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
