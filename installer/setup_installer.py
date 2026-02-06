"""
LRU Tracker - Professional Installer
Creates a GUI installer using tkinter (built-in to Python)
Platform: Windows and macOS support
"""
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import sys
import shutil
import platform
from pathlib import Path
import subprocess

# Detect platform
IS_WINDOWS = platform.system() == 'Windows'
IS_MAC = platform.system() == 'Darwin'

if IS_WINDOWS:
    import winreg

class InstallerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("LRU Tracker Setup v1.2.2")
        
        # Make window larger and scrollable
        self.root.geometry("700x650")
        self.root.resizable(True, True)
        self.root.minsize(650, 600)
        
        # Center window on screen
        self.center_window()
        
        # Default install path based on platform
        if IS_WINDOWS:
            self.install_path = Path(os.environ.get('PROGRAMFILES', 'C:\\Program Files')) / "LRU Tracker"
            self.exe_name = "LRU_Tracker.exe"
        elif IS_MAC:
            self.install_path = Path.home() / "Applications" / "LRU Tracker"
            self.exe_name = "LRU_Tracker.app"
        else:
            self.install_path = Path.home() / ".local" / "share" / "LRU Tracker"
            self.exe_name = "LRU_Tracker"
        
        # Source files (where the exe is)
        # When running as a PyInstaller bundle, files are in sys._MEIPASS
        # When running as a script, files are in parent/dist
        if getattr(sys, 'frozen', False):
            # Running as compiled executable (PyInstaller)
            self.source_dir = Path(sys._MEIPASS)
        else:
            # Running as Python script
            self.source_dir = Path(__file__).parent.parent / "dist"
        
        # Version info
        self.version = "1.2.2"
        
        self.create_widgets()
    
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def create_widgets(self):
        # Create main container with scrollbar
        main_container = tk.Frame(self.root)
        main_container.pack(fill='both', expand=True)
        
        # Canvas for scrolling
        canvas = tk.Canvas(main_container, bg='#ecf0f1', highlightthickness=0)
        scrollbar = ttk.Scrollbar(main_container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#ecf0f1')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Enable mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Header with gradient effect
        header_frame = tk.Frame(scrollable_frame, bg='#2c3e50', height=100)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        # App icon and title
        title_frame = tk.Frame(header_frame, bg='#2c3e50')
        title_frame.pack(expand=True)
        
        tk.Label(title_frame, text="🏭", font=('Arial', 36), bg='#2c3e50').pack()
        tk.Label(title_frame, text="LRU Tracker Setup", 
                font=('Arial', 24, 'bold'), bg='#2c3e50', fg='white').pack()
        tk.Label(title_frame, text=f"Version {self.version}", 
                font=('Arial', 10), bg='#2c3e50', fg='#bdc3c7').pack()
        
        # Main content with better spacing
        content_frame = tk.Frame(scrollable_frame, bg='#ecf0f1')
        content_frame.pack(fill='both', expand=True, padx=30, pady=20)
        
        # Welcome section with better formatting
        welcome_card = tk.Frame(content_frame, bg='white', relief='flat', bd=0)
        welcome_card.pack(fill='x', pady=(0, 15))
        
        welcome_inner = tk.Frame(welcome_card, bg='white')
        welcome_inner.pack(padx=20, pady=20)
        
        tk.Label(welcome_inner, text="Welcome to LRU Tracker Setup Wizard", 
                font=('Arial', 16, 'bold'), bg='white', fg='#2c3e50').pack(anchor='w', pady=(0, 15))
        
        # Platform detection display
        platform_text = "Windows" if IS_WINDOWS else "macOS" if IS_MAC else "Linux"
        tk.Label(welcome_inner, 
                text=f"📱 Detected Platform: {platform_text}",
                font=('Arial', 10, 'bold'), bg='white', fg='#16a085').pack(anchor='w', pady=(0, 15))
        
        description = tk.Text(welcome_inner, wrap='word', height=11, font=('Arial', 10), 
                            bg='white', relief='flat', cursor='arrow')
        description.insert('1.0', 
            "This wizard will guide you through the installation of LRU Tracker.\n\n"
            "✨ Key Features:\n"
            "  • Professional LRU tracking and management system\n"
            "  • Excel export with enhanced styling and formatting\n"
            "  • Auto-download updates (62% faster update process)\n"
            "  • Permission-fixed file handling\n"
            "  • No Python installation required\n"
            "  • Clean, modern user interface\n\n"
            "💾 Estimated disk space required: ~140 MB\n\n"
            "Click 'Install' when ready to begin.")
        description.config(state='disabled')
        description.pack(fill='x')
        
        # System requirements card
        req_card = tk.Frame(content_frame, bg='white', relief='flat', bd=0)
        req_card.pack(fill='x', pady=(0, 15))
        
        req_inner = tk.Frame(req_card, bg='white')
        req_inner.pack(padx=20, pady=15)
        
        tk.Label(req_inner, text="💻 System Requirements", 
                font=('Arial', 12, 'bold'), bg='white', fg='#2c3e50').pack(anchor='w', pady=(0, 10))
        
        req_text = tk.Text(req_inner, wrap='word', height=4, font=('Arial', 9), 
                          bg='#f8f9fa', relief='flat', cursor='arrow')
        if IS_WINDOWS:
            req_text.insert('1.0', 
                "• Windows 10 or later (64-bit)\n"
                "• 200 MB free disk space\n"
                "• Internet connection for updates\n"
                "• Screen resolution: 1024x768 or higher")
        elif IS_MAC:
            req_text.insert('1.0', 
                "• macOS 10.14 (Mojave) or later\n"
                "• 200 MB free disk space\n"
                "• Internet connection for updates\n"
                "• Screen resolution: 1024x768 or higher")
        req_text.config(state='disabled')
        req_text.pack(fill='x')
        
        # Install location card
        location_card = tk.Frame(content_frame, bg='white', relief='flat', bd=0)
        location_card.pack(fill='x', pady=(0, 15))
        
        location_inner = tk.Frame(location_card, bg='white')
        location_inner.pack(padx=20, pady=15)
        
        tk.Label(location_inner, text="📁 Installation Location", 
                font=('Arial', 12, 'bold'), bg='white', fg='#2c3e50').pack(anchor='w', pady=(0, 10))
        
        path_frame = tk.Frame(location_inner, bg='white')
        path_frame.pack(fill='x', pady=5)
        
        self.path_var = tk.StringVar(value=str(self.install_path))
        path_entry = tk.Entry(path_frame, textvariable=self.path_var, font=('Arial', 10), 
                             state='readonly', relief='solid', bd=1)
        path_entry.pack(side='left', fill='x', expand=True, padx=(0, 10))
        
        browse_btn = tk.Button(path_frame, text="📂 Browse...", command=self.browse_location,
                              bg='#3498db', fg='white', font=('Arial', 10, 'bold'),
                              relief='flat', cursor='hand2', padx=15, pady=5)
        browse_btn.pack(side='left')
        
        # Disk space info
        try:
            if IS_WINDOWS:
                import shutil
                total, used, free = shutil.disk_usage(self.install_path.drive if hasattr(self.install_path, 'drive') else 'C:')
                free_gb = free // (2**30)
                space_text = f"💾 Available space: {free_gb} GB"
                space_color = '#27ae60' if free_gb > 1 else '#e74c3c'
            else:
                space_text = "💾 Ensure sufficient disk space available"
                space_color = '#7f8c8d'
        except:
            space_text = "💾 Ensure sufficient disk space available"
            space_color = '#7f8c8d'
            
        tk.Label(location_inner, text=space_text, 
                font=('Arial', 9), bg='white', fg=space_color).pack(anchor='w', pady=(5, 0))
        
        # Installation options card
        options_card = tk.Frame(content_frame, bg='white', relief='flat', bd=0)
        options_card.pack(fill='x', pady=(0, 15))
        
        options_inner = tk.Frame(options_card, bg='white')
        options_inner.pack(padx=20, pady=15)
        
        tk.Label(options_inner, text="⚙️ Installation Options", 
                font=('Arial', 12, 'bold'), bg='white', fg='#2c3e50').pack(anchor='w', pady=(0, 10))
        
        self.desktop_shortcut = tk.BooleanVar(value=True)
        self.start_menu = tk.BooleanVar(value=True)
        self.auto_update = tk.BooleanVar(value=True)
        self.launch_after = tk.BooleanVar(value=False)
        
        options = [
            (self.desktop_shortcut, "🖥️ Create Desktop Shortcut", "Quick access from your desktop"),
            (self.start_menu, "📋 Create Start Menu Entry", "Add to applications menu"),
            (self.auto_update, "🔄 Enable Automatic Updates", "Check for updates on startup (recommended)"),
            (self.launch_after, "🚀 Launch LRU Tracker after installation", "Start the application immediately")
        ]
        
        for var, text, desc in options:
            option_frame = tk.Frame(options_inner, bg='white')
            option_frame.pack(fill='x', pady=3)
            
            cb = tk.Checkbutton(option_frame, text=text, variable=var, bg='white',
                              font=('Arial', 10, 'bold'), cursor='hand2')
            cb.pack(anchor='w')
            
            tk.Label(option_frame, text=f"    {desc}", 
                    font=('Arial', 9), bg='white', fg='#7f8c8d').pack(anchor='w')
        
        # Progress section
        progress_frame = tk.Frame(content_frame, bg='white', relief='flat', bd=0)
        progress_frame.pack(fill='x', pady=(0, 20))
        
        progress_inner = tk.Frame(progress_frame, bg='white')
        progress_inner.pack(padx=20, pady=15)
        
        # Custom styled progress bar
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Custom.Horizontal.TProgressbar", 
                       troughcolor='#ecf0f1',
                       background='#3498db',
                       bordercolor='#2c3e50',
                       lightcolor='#3498db',
                       darkcolor='#2980b9')
        
        self.progress = ttk.Progressbar(progress_inner, mode='determinate', 
                                       length=600, style="Custom.Horizontal.TProgressbar")
        self.progress.pack(fill='x', pady=(5, 10))
        
        self.status_label = tk.Label(progress_inner, text="Ready to install", 
                                     font=('Arial', 10), bg='white', fg='#7f8c8d')
        self.status_label.pack()
        
        # Button frame at bottom (outside scrollable area for always visible)
        button_container = tk.Frame(self.root, bg='#ecf0f1')
        button_container.pack(fill='x', side='bottom')
        
        button_frame = tk.Frame(button_container, bg='#ecf0f1')
        button_frame.pack(fill='x', padx=30, pady=20)
        
        # Help button
        help_btn = tk.Button(button_frame, text="❓ Help", command=self.show_help,
                           bg='#95a5a6', fg='white', font=('Arial', 10, 'bold'),
                           relief='flat', cursor='hand2', width=10, pady=8)
        help_btn.pack(side='left')
        
        # Spacer
        tk.Frame(button_frame, bg='#ecf0f1').pack(side='left', expand=True)
        
        # Cancel button
        cancel_btn = tk.Button(button_frame, text="✖ Cancel", command=self.cancel_install,
                             bg='#e74c3c', fg='white', font=('Arial', 10, 'bold'),
                             relief='flat', cursor='hand2', width=12, pady=8)
        cancel_btn.pack(side='right', padx=(10, 0))
        
        # Install button
        self.install_button = tk.Button(button_frame, text="⚡ Install Now", 
                                       command=self.start_install,
                                       bg='#27ae60', fg='white', 
                                       font=('Arial', 11, 'bold'),
                                       relief='flat', cursor='hand2',
                                       width=15, pady=8)
        self.install_button.pack(side='right')
        
    def show_help(self):
        """Show help dialog"""
        help_text = """
LRU Tracker Installation Help

INSTALLATION TIPS:
• Choose a location with sufficient disk space (minimum 200 MB)
• Desktop shortcut provides quick access
• Start Menu entry adds to your applications list
• Auto-update keeps your software current with bug fixes

TROUBLESHOOTING:
• Permission Denied: Try installing to your user folder
• Not Enough Space: Free up disk space or choose another drive
• Installation Failed: Check antivirus isn't blocking the installer

SUPPORT:
• GitHub: https://github.com/HaltTheGrey/lru-tracker
• Report Issues: Use GitHub Issues tab
• Documentation: Check README.md in the repository

UNINSTALLING:
• Windows: Settings > Apps > LRU Tracker
• macOS: Drag app to Trash from Applications folder
"""
        messagebox.showinfo("Installation Help", help_text)
        
    def browse_location(self):
        folder = filedialog.askdirectory(initialdir=str(self.install_path.parent),
                                        title="Select Installation Folder")
        if folder:
            self.install_path = Path(folder) / "LRU Tracker"
            self.path_var.set(str(self.install_path))
    
    def update_status(self, message, progress):
        self.status_label.config(text=message)
        self.progress['value'] = progress
        self.root.update()
    
    def start_install(self):
        if not self.check_source_files():
            messagebox.showerror("Error", 
                               f"Cannot find {self.exe_name} in {self.source_dir}\n\n"
                               "Please build the application first.")
            return
        
        self.install_button.config(state='disabled')
        
        try:
            # Step 1: Create installation directory
            self.update_status("🗂️ Creating installation directory...", 10)
            self.install_path.mkdir(parents=True, exist_ok=True)
            
            # Step 2: Copy executable and related files
            self.update_status(f"📦 Copying {self.exe_name}...", 25)
            source_exe = self.source_dir / self.exe_name
            dest_exe = self.install_path / self.exe_name
            shutil.copy2(source_exe, dest_exe)
            
            # Copy uninstaller if it exists
            uninstaller_src = Path(__file__).parent / "uninstall.py"
            if uninstaller_src.exists():
                self.update_status("📦 Copying uninstaller...", 35)
                shutil.copy2(uninstaller_src, self.install_path / "uninstall.py")
            
            # Step 3: Make executable (macOS/Linux)
            if not IS_WINDOWS:
                self.update_status("🔧 Setting permissions...", 45)
                os.chmod(dest_exe, 0o755)
            
            # Step 4: Create shortcuts
            if self.desktop_shortcut.get():
                self.update_status("🖥️ Creating desktop shortcut...", 55)
                self.create_shortcut("Desktop")
            
            if self.start_menu.get():
                self.update_status("📋 Creating application menu entry...", 70)
                self.create_shortcut("StartMenu")
            
            # Step 5: Configure auto-update setting
            if self.auto_update.get():
                self.update_status("🔄 Configuring auto-update...", 80)
                self.configure_auto_update()
            
            # Step 6: Register uninstaller (Windows only)
            if IS_WINDOWS:
                self.update_status("📝 Registering application...", 90)
                self.register_uninstaller()
            
            # Step 7: Complete
            self.update_status("✅ Installation complete!", 100)
            
            success_msg = (
                f"🎉 LRU Tracker has been successfully installed!\n\n"
                f"📁 Installation location:\n   {self.install_path}\n\n"
                f"🚀 You can now run LRU Tracker from:\n"
            )
            
            if self.desktop_shortcut.get():
                success_msg += "   • Desktop shortcut\n"
            if self.start_menu.get():
                success_msg += "   • Application menu\n"
            success_msg += f"   • {dest_exe}\n"
            
            if self.auto_update.get():
                success_msg += "\n🔄 Auto-update is enabled - you'll receive notifications about new versions"
            
            messagebox.showinfo("Installation Successful", success_msg)
            
            # Launch after install if selected
            if self.launch_after.get():
                try:
                    if IS_WINDOWS:
                        os.startfile(dest_exe)
                    elif IS_MAC:
                        subprocess.Popen(['open', dest_exe])
                    else:
                        subprocess.Popen([dest_exe])
                except Exception as e:
                    print(f"Could not launch application: {e}")
            
            self.root.quit()
            
        except PermissionError:
            messagebox.showerror("Permission Denied", 
                               "⚠️ Cannot install to this location.\n\n"
                               "Try one of these:\n"
                               "• Run this installer as Administrator (Windows)\n"
                               "• Choose a different installation folder\n"
                               "• Install to your user folder instead")
            self.install_button.config(state='normal')
            self.update_status("❌ Installation failed", 0)
            
        except Exception as e:
            messagebox.showerror("Installation Error", 
                               f"❌ An error occurred during installation:\n\n{str(e)}\n\n"
                               f"Platform: {platform.system()}\n"
                               f"Please report this issue on GitHub.")
            self.install_button.config(state='normal')
            self.update_status("❌ Installation failed", 0)
    
    def configure_auto_update(self):
        """Create a config file for auto-update preference"""
        try:
            config_file = self.install_path / "update_config.txt"
            config_file.write_text("auto_update_enabled=true\n")
        except Exception as e:
            print(f"Could not create auto-update config: {e}")
    
    def check_source_files(self):
        """Check if the executable exists"""
        source_exe = self.source_dir / self.exe_name
        return source_exe.exists()
    
    def create_shortcut(self, location):
        """Create a shortcut/alias (cross-platform)"""
        if IS_WINDOWS:
            self.create_windows_shortcut(location)
        elif IS_MAC:
            self.create_mac_alias(location)
        else:
            self.create_linux_desktop_entry(location)
    
    def create_windows_shortcut(self, location):
        """Create Windows shortcut"""
        try:
            import win32com.client
            
            shell = win32com.client.Dispatch("WScript.Shell")
            
            if location == "Desktop":
                shortcut_path = Path(shell.SpecialFolders("Desktop")) / "LRU Tracker.lnk"
            else:  # StartMenu
                start_menu = Path(shell.SpecialFolders("StartMenu")) / "Programs"
                start_menu.mkdir(parents=True, exist_ok=True)
                shortcut_path = start_menu / "LRU Tracker.lnk"
            
            shortcut = shell.CreateShortCut(str(shortcut_path))
            shortcut.TargetPath = str(self.install_path / self.exe_name)
            shortcut.WorkingDirectory = str(self.install_path)
            shortcut.Description = "LRU Tracker - FC Pull System Tracker"
            shortcut.Save()
            
        except ImportError:
            # Fallback: create using PowerShell
            self.create_shortcut_powershell(location)
    
    def create_mac_alias(self, location):
        """Create macOS alias/symlink"""
        try:
            if location == "Desktop":
                alias_path = Path.home() / "Desktop" / "LRU Tracker.app"
            else:  # Applications folder link
                alias_path = Path.home() / "Applications" / "LRU Tracker.app"
            
            # Create symlink
            if alias_path.exists():
                alias_path.unlink()
            
            alias_path.symlink_to(self.install_path / self.exe_name)
            
        except Exception as e:
            print(f"Could not create macOS alias: {e}")
    
    def create_linux_desktop_entry(self, location):
        """Create Linux .desktop file"""
        try:
            desktop_content = f"""[Desktop Entry]
Name=LRU Tracker
Comment=FC Pull System Tracker
Exec={self.install_path / self.exe_name}
Icon={self.install_path / self.exe_name}
Terminal=false
Type=Application
Categories=Utility;Office;
"""
            if location == "Desktop":
                desktop_path = Path.home() / "Desktop" / "LRU Tracker.desktop"
            else:
                apps_dir = Path.home() / ".local" / "share" / "applications"
                apps_dir.mkdir(parents=True, exist_ok=True)
                desktop_path = apps_dir / "LRU Tracker.desktop"
            
            desktop_path.write_text(desktop_content)
            os.chmod(desktop_path, 0o755)
            
        except Exception as e:
            print(f"Could not create desktop entry: {e}")
    
    def create_shortcut_powershell(self, location):
        """Create shortcut using PowerShell (fallback)"""
        if location == "Desktop":
            shortcut_path = Path.home() / "Desktop" / "LRU Tracker.lnk"
        else:
            shortcut_path = Path(os.environ['APPDATA']) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "LRU Tracker.lnk"
        
        ps_command = f'''
        $WshShell = New-Object -ComObject WScript.Shell
        $Shortcut = $WshShell.CreateShortcut("{shortcut_path}")
        $Shortcut.TargetPath = "{self.install_path / self.exe_name}"
        $Shortcut.WorkingDirectory = "{self.install_path}"
        $Shortcut.Description = "LRU Tracker - FC Pull System Tracker"
        $Shortcut.Save()
        '''
        
        subprocess.run(["powershell", "-Command", ps_command], 
                      capture_output=True, check=True)
    
    def register_uninstaller(self):
        """Add to Windows Programs & Features"""
        try:
            key_path = r"Software\Microsoft\Windows\CurrentVersion\Uninstall\LRU Tracker"
            
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path) as key:
                winreg.SetValueEx(key, "DisplayName", 0, winreg.REG_SZ, "LRU Tracker")
                winreg.SetValueEx(key, "DisplayVersion", 0, winreg.REG_SZ, "1.2.2")
                winreg.SetValueEx(key, "Publisher", 0, winreg.REG_SZ, "LRU Tracker Development")
                winreg.SetValueEx(key, "InstallLocation", 0, winreg.REG_SZ, str(self.install_path))
                winreg.SetValueEx(key, "UninstallString", 0, winreg.REG_SZ, 
                                f'"{sys.executable}" "{Path(__file__).parent / "uninstall.py"}"')
                winreg.SetValueEx(key, "DisplayIcon", 0, winreg.REG_SZ, 
                                str(self.install_path / self.exe_name))
                
                # Estimate size (in KB)
                exe_size = (self.source_dir / self.exe_name).stat().st_size // 1024
                winreg.SetValueEx(key, "EstimatedSize", 0, winreg.REG_DWORD, exe_size)
                
        except Exception as e:
            # Not critical if this fails
            print(f"Could not register uninstaller: {e}")
    
    def cancel_install(self):
        if messagebox.askyesno("Cancel Installation", 
                              "Are you sure you want to cancel the installation?"):
            self.root.quit()


def main():
    root = tk.Tk()
    app = InstallerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
