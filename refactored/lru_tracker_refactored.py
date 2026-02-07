"""LRU Tracker Application - Refactored with modular design."""
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import webbrowser
import urllib.request
import urllib.error
import os
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional

from config import *
from models import Station, GlobalHistoryEntry
from data_manager import DataManager, DataLoadError, DataSaveError
from validators import validate_station_name, validate_number
from export_manager import ExportManager
from update_checker import UpdateChecker, NetworkError, SecurityError
from template_manager import TemplateManager
from fc_schedule_manager import FCScheduleManager
from logger import setup_logger, get_logger
from error_handler import safe_execute

logger = setup_logger()


class LRUTrackerApp:
    """Main application class for LRU Tracker."""
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("FC LRU Pull System Tracker")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg='#f0f0f0')
        
        self.stations: Dict[str, Station] = {}
        self.history = []
        
        self.data_manager = DataManager()
        self.export_manager = ExportManager()
        self.update_checker = UpdateChecker()
        self.template_manager = TemplateManager()
        self.fc_schedule_manager = FCScheduleManager()
        
        logger.info("Application initialized")
        self._load_data()
        self._create_ui()
        self.refresh_display()
    
    def _load_data(self) -> None:
        """Load data from file."""
        try:
            self.stations, self.history = self.data_manager.load_data()
            logger.info(f"Loaded {len(self.stations)} stations, {len(self.history)} history entries")
        except DataLoadError as e:
            logger.error(f"Data load failed: {e}")
            messagebox.showerror("Error", 
                f"Failed to load data. Starting fresh.\n"
                f"Check {DATA_FILE}{BACKUP_SUFFIX} if data was lost.")
            self.stations = {}
            self.history = []
    
    def _save_data(self) -> None:
        """Save data to file."""
        try:
            self.data_manager.save_data(self.stations, self.history)
            logger.info("Data saved successfully")
        except DataSaveError as e:
            logger.error(f"Data save failed: {e}")
            messagebox.showerror("Error", f"Failed to save data:\n{str(e)}")
    
    def _create_ui(self) -> None:
        """Create the user interface."""
        self._create_title()
        main_container = self._create_main_container()
        self._create_left_panel(main_container)
        self._create_right_panel(main_container)
    
    def _create_title(self) -> None:
        """Create title bar."""
        title_frame = tk.Frame(self.root, bg=Colors.PRIMARY, height=60)
        title_frame.pack(fill='x', pady=(0, 5))
        title_frame.pack_propagate(False)
        
        tk.Label(title_frame, text="🏭 FC LRU Pull System Tracker", 
                font=('Arial', 20, 'bold'), bg=Colors.PRIMARY, fg='white').pack(pady=15)
    
    def _create_main_container(self) -> tk.Frame:
        """Create main container frame."""
        main_container = tk.Frame(self.root, bg='#f0f0f0')
        main_container.pack(fill='both', expand=True, padx=10, pady=5)
        return main_container
    
    def _create_left_panel(self, parent: tk.Frame) -> None:
        """Create left panel with station management."""
        left_panel = tk.Frame(parent, bg='white', relief='raised', bd=2)
        left_panel.pack(side='left', fill='both', expand=True, padx=(0, 5))
        
        self._create_station_controls(left_panel)
        self._create_station_tree(left_panel)
    
    def _create_station_controls(self, parent: tk.Frame) -> None:
        """Create station control buttons."""
        control_frame = tk.Frame(parent, bg='white', pady=5)
        control_frame.pack(fill='x', padx=5)
        
        tk.Label(control_frame, text="Station Management", 
                font=('Arial', 13, 'bold'), bg='white').pack(anchor='w', pady=(0, 5))
        
        btn_frame = tk.Frame(control_frame, bg='white')
        btn_frame.pack(fill='x')
        
        buttons = [
            ("➕ Add", self.add_station_dialog, Colors.SUCCESS),
            ("✏️ Edit", self.edit_station_dialog, Colors.INFO),
            ("🗑️ Delete", self.delete_station, Colors.DANGER)
        ]
        
        for text, command, color in buttons:
            tk.Button(btn_frame, text=text, command=command,
                     bg=color, fg='white', font=('Arial', 9, 'bold'),
                     padx=10, pady=5, cursor='hand2').pack(side='left', padx=2)
    
    def _create_station_tree(self, parent: tk.Frame) -> None:
        """Create station treeview."""
        tree_frame = tk.Frame(parent, bg='white')
        tree_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        v_scroll = ttk.Scrollbar(tree_frame, orient='vertical')
        h_scroll = ttk.Scrollbar(tree_frame, orient='horizontal')
        
        self.tree = ttk.Treeview(tree_frame, 
                                columns=('Current', 'Min', 'Max', 'Status'),
                                show='tree headings',
                                yscrollcommand=v_scroll.set,
                                xscrollcommand=h_scroll.set,
                                height=20)
        
        v_scroll.config(command=self.tree.yview)
        h_scroll.config(command=self.tree.xview)
        
        self.tree.heading('#0', text='Station Name')
        self.tree.heading('Current', text='Current LRU')
        self.tree.heading('Min', text='Min')
        self.tree.heading('Max', text='Max')
        self.tree.heading('Status', text='Status')
        
        self.tree.column('#0', width=200)
        self.tree.column('Current', width=100, anchor='center')
        self.tree.column('Min', width=80, anchor='center')
        self.tree.column('Max', width=80, anchor='center')
        self.tree.column('Status', width=120, anchor='center')
        
        self.tree.bind('<<TreeviewSelect>>', self._on_station_select)
        
        self.tree.pack(side='left', fill='both', expand=True)
        v_scroll.pack(side='right', fill='y')
        h_scroll.pack(side='bottom', fill='x')
        
        self.tree.tag_configure('under_min', background=Colors.UNDER_MIN_BG)
        self.tree.tag_configure('at_max', background=Colors.AT_MAX_BG)
        self.tree.tag_configure('normal', background=Colors.NORMAL_BG)
    
    def _create_right_panel(self, parent: tk.Frame) -> None:
        """Create right panel with controls."""
        right_panel = tk.Frame(parent, bg='white', relief='raised', bd=2, width=RIGHT_PANEL_WIDTH)
        right_panel.pack(side='right', fill='both', padx=(5, 0))
        right_panel.pack_propagate(False)
        
        canvas = tk.Canvas(right_panel, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(right_panel, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        canvas.bind_all("<MouseWheel>", 
            lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
        
        self._create_update_section(scrollable_frame)
        self._create_stats_section(scrollable_frame)
        self._create_export_section(scrollable_frame)
        self._create_version_section(scrollable_frame)
    
    def _create_update_section(self, parent: tk.Frame) -> None:
        """Create LRU update section."""
        update_frame = tk.LabelFrame(parent, text="Update LRU Count", 
                                    font=('Arial', 12, 'bold'), bg='white', padx=10, pady=10)
        update_frame.pack(fill='x', padx=5, pady=5)
        
        tk.Label(update_frame, text="Station:", bg='white', font=('Arial', 10)).pack(anchor='w')
        self.update_station_var = tk.StringVar()
        self.update_station_combo = ttk.Combobox(update_frame, textvariable=self.update_station_var,
                                                 state='readonly', font=('Arial', 10))
        self.update_station_combo.pack(fill='x', pady=(3, 8))
        
        tk.Label(update_frame, text="New LRU Count:", bg='white', font=('Arial', 10)).pack(anchor='w')
        self.update_count_var = tk.StringVar()
        tk.Entry(update_frame, textvariable=self.update_count_var, 
                font=('Arial', 11), justify='center').pack(fill='x', pady=(3, 8))
        
        tk.Button(update_frame, text="📝 Update Count", command=self.update_lru_count,
                 bg=Colors.INFO, fg='white', font=('Arial', 10, 'bold'),
                 padx=15, pady=8, cursor='hand2').pack(fill='x')
    
    def _create_stats_section(self, parent: tk.Frame) -> None:
        """Create statistics section."""
        stats_frame = tk.LabelFrame(parent, text="Statistics", 
                                   font=('Arial', 12, 'bold'), bg='white', padx=10, pady=8)
        stats_frame.pack(fill='x', padx=5, pady=5)
        
        self.stats_label = tk.Label(stats_frame, text="", bg='white', 
                                   font=('Arial', 9), justify='left', anchor='w')
        self.stats_label.pack(fill='x')
    
    def _create_export_section(self, parent: tk.Frame) -> None:
        """Create export section."""
        export_frame = tk.LabelFrame(parent, text="Export & Reports", 
                                    font=('Arial', 12, 'bold'), bg='white', padx=10, pady=8)
        export_frame.pack(fill='x', padx=5, pady=5)
        
        buttons = [
            ("📊 New Excel Report", self.export_new_report, Colors.SUCCESS),
            ("📈 Append to Existing", self.append_to_existing, '#16a085'),
            ("📉 View Trends", self.view_trends, '#2980b9'),
            ("📅 Export FC Schedule", self.export_fc_schedule, Colors.WARNING)
        ]
        
        for text, command, color in buttons:
            tk.Button(export_frame, text=text, command=command,
                     bg=color, fg='white', font=('Arial', 9, 'bold'),
                     padx=10, pady=6, cursor='hand2').pack(fill='x', pady=3)
        
        # Template section
        template_frame = tk.LabelFrame(parent, text="Template Import/Export", 
                                      font=('Arial', 12, 'bold'), bg='white', padx=10, pady=8)
        template_frame.pack(fill='x', padx=5, pady=5)
        
        template_buttons = [
            ("📥 Download Template", self.download_template, '#8e44ad'),
            ("📤 Import from Template", self.import_from_template, '#9b59b6'),
            ("📋 Import FC Schedule", self.import_fc_schedule, Colors.WARNING)
        ]
        
        for text, command, color in template_buttons:
            tk.Button(template_frame, text=text, command=command,
                     bg=color, fg='white', font=('Arial', 9, 'bold'),
                     padx=10, pady=6, cursor='hand2').pack(fill='x', pady=3)
    
    def _create_version_section(self, parent: tk.Frame) -> None:
        """Create version and update section."""
        updates_frame = tk.LabelFrame(parent, text="Application", 
                                      font=('Arial', 12, 'bold'), bg='white', padx=10, pady=8)
        updates_frame.pack(fill='x', padx=5, pady=5)
        
        tk.Button(updates_frame, text="🔄 Check for Updates", 
                 command=self.check_for_updates,
                 bg=Colors.SUCCESS, fg='white', font=('Arial', 9, 'bold'),
                 padx=10, pady=6, cursor='hand2').pack(fill='x', pady=3)
        
        tk.Label(parent, text=f"Version {APP_VERSION}", 
                font=('Arial', 8), bg='#ecf0f1', fg='#7f8c8d').pack(pady=(5, 10))
        
        tk.Button(parent, text="💾 Save Data", command=self._save_data,
                 bg=Colors.SECONDARY, fg='white', font=('Arial', 9, 'bold'),
                 padx=10, pady=6, cursor='hand2').pack(fill='x', padx=5, pady=10)

    @safe_execute
    def add_station_dialog(self) -> None:
        """Show dialog to add new station."""
        dialog = tk.Toplevel(self.root)
        dialog.title("Add New Station")
        dialog.geometry("400x300")
        dialog.configure(bg='white')
        dialog.transient(self.root)
        dialog.grab_set()
        
        tk.Label(dialog, text="Add New Station", font=('Arial', 16, 'bold'), 
                bg='white').pack(pady=15)
        
        frame = tk.Frame(dialog, bg='white', padx=20)
        frame.pack(fill='both', expand=True)
        
        tk.Label(frame, text="Station Name:", bg='white', font=('Arial', 11)).pack(anchor='w', pady=(10, 5))
        name_var = tk.StringVar()
        tk.Entry(frame, textvariable=name_var, font=('Arial', 11)).pack(fill='x', pady=(0, 15))
        
        tk.Label(frame, text="Minimum LRU:", bg='white', font=('Arial', 11)).pack(anchor='w', pady=(0, 5))
        min_var = tk.StringVar(value="5")
        tk.Entry(frame, textvariable=min_var, font=('Arial', 11)).pack(fill='x', pady=(0, 15))
        
        tk.Label(frame, text="Maximum LRU:", bg='white', font=('Arial', 11)).pack(anchor='w', pady=(0, 5))
        max_var = tk.StringVar(value="20")
        tk.Entry(frame, textvariable=max_var, font=('Arial', 11)).pack(fill='x', pady=(0, 15))
        
        def save_station():
            name = name_var.get().strip()
            
            if not validate_station_name(name):
                messagebox.showerror("Error", 
                    "Invalid station name!\n\n"
                    "Station names must:\n"
                    "• Not be empty\n"
                    f"• Be less than {MAX_STATION_NAME_LENGTH} characters\n"
                    "• Contain only letters, numbers, spaces, and basic punctuation")
                return
            
            min_valid, min_val = validate_number(min_var.get())
            if not min_valid:
                messagebox.showerror("Error", 
                    f"Invalid minimum value!\nMust be between {MIN_LRU_VALUE} and {MAX_LRU_VALUE}")
                return
            
            max_valid, max_val = validate_number(max_var.get())
            if not max_valid:
                messagebox.showerror("Error", 
                    f"Invalid maximum value!\nMust be between {MIN_LRU_VALUE} and {MAX_LRU_VALUE}")
                return
            
            if name in self.stations:
                messagebox.showerror("Error", "Station already exists!")
                return
            
            if min_val > max_val:
                messagebox.showerror("Error", "Minimum cannot be greater than Maximum!")
                return
            
            self.stations[name] = Station(name=name, current=0, min_lru=min_val, max_lru=max_val)
            self._save_data()
            self.refresh_display()
            dialog.destroy()
            messagebox.showinfo("Success", f"Station '{name}' added successfully!")
        
        btn_frame = tk.Frame(dialog, bg='white')
        btn_frame.pack(fill='x', padx=20, pady=15)
        
        tk.Button(btn_frame, text="Add Station", command=save_station,
                 bg=Colors.SUCCESS, fg='white', font=('Arial', 11, 'bold'),
                 padx=20, pady=8).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="Cancel", command=dialog.destroy,
                 bg=Colors.SECONDARY, fg='white', font=('Arial', 11, 'bold'),
                 padx=20, pady=8).pack(side='right', padx=5)
    
    def edit_station_dialog(self) -> None:
        """Show dialog to edit station."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a station to edit!")
            return
        
        station_name = self.tree.item(selected[0])['text']
        station = self.stations[station_name]
        
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Edit Station: {station_name}")
        dialog.geometry("400x250")
        dialog.configure(bg='white')
        dialog.transient(self.root)
        dialog.grab_set()
        
        tk.Label(dialog, text=f"Edit Station: {station_name}", 
                font=('Arial', 16, 'bold'), bg='white').pack(pady=15)
        
        frame = tk.Frame(dialog, bg='white', padx=20)
        frame.pack(fill='both', expand=True)
        
        tk.Label(frame, text="Minimum LRU:", bg='white', font=('Arial', 11)).pack(anchor='w', pady=(0, 5))
        min_var = tk.StringVar(value=str(station.min_lru))
        tk.Entry(frame, textvariable=min_var, font=('Arial', 11)).pack(fill='x', pady=(0, 15))
        
        tk.Label(frame, text="Maximum LRU:", bg='white', font=('Arial', 11)).pack(anchor='w', pady=(0, 5))
        max_var = tk.StringVar(value=str(station.max_lru))
        tk.Entry(frame, textvariable=max_var, font=('Arial', 11)).pack(fill='x', pady=(0, 15))
        
        def save_changes():
            min_valid, min_val = validate_number(min_var.get())
            max_valid, max_val = validate_number(max_var.get())
            
            if not min_valid or not max_valid:
                messagebox.showerror("Error", "Min and Max must be valid numbers!")
                return
            
            if min_val > max_val:
                messagebox.showerror("Error", "Min cannot be greater than Max!")
                return
            
            station.min_lru = min_val
            station.max_lru = max_val
            
            self._save_data()
            self.refresh_display()
            dialog.destroy()
            messagebox.showinfo("Success", "Station updated successfully!")
        
        btn_frame = tk.Frame(dialog, bg='white')
        btn_frame.pack(fill='x', padx=20, pady=15)
        
        tk.Button(btn_frame, text="Save Changes", command=save_changes,
                 bg=Colors.INFO, fg='white', font=('Arial', 11, 'bold'),
                 padx=20, pady=8).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="Cancel", command=dialog.destroy,
                 bg=Colors.SECONDARY, fg='white', font=('Arial', 11, 'bold'),
                 padx=20, pady=8).pack(side='right', padx=5)
    
    def delete_station(self) -> None:
        """Delete selected station."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a station to delete!")
            return
        
        station_name = self.tree.item(selected[0])['text']
        
        if messagebox.askyesno("Confirm Delete", 
                              f"Are you sure you want to delete '{station_name}'?\nAll history will be lost."):
            del self.stations[station_name]
            self._save_data()
            self.refresh_display()
            messagebox.showinfo("Success", f"Station '{station_name}' deleted!")
    
    @safe_execute
    def update_lru_count(self) -> None:
        """Update LRU count for selected station."""
        station_name = self.update_station_var.get()
        if not station_name:
            messagebox.showwarning("Warning", "Please select a station!")
            return
        
        count_valid, new_count = validate_number(self.update_count_var.get())
        if not count_valid:
            messagebox.showerror("Error", "Please enter a valid number!")
            return
        
        station = self.stations[station_name]
        timestamp = datetime.now().strftime(TIMESTAMP_FORMAT)
        station.add_history(new_count, timestamp)
        
        # Add to global history
        self.history.append(GlobalHistoryEntry(
            station=station_name,
            timestamp=timestamp,
            count=new_count,
            min_lru=station.min_lru,
            max_lru=station.max_lru
        ))
        
        self._save_data()
        self.refresh_display()
        self.update_count_var.set("")
        
        messagebox.showinfo("Success", f"Updated '{station_name}' to {new_count} LRUs!")
    
    def _on_station_select(self, event) -> None:
        """Handle station selection in tree."""
        selected = self.tree.selection()
        if selected:
            station_name = self.tree.item(selected[0])['text']
            self.update_station_var.set(station_name)
    
    def refresh_display(self) -> None:
        """Refresh the display with current data."""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        under_min_count = at_max_count = normal_count = 0
        
        for name in sorted(self.stations.keys()):
            station = self.stations[name]
            status = station.get_status()
            tag = station.get_status_tag()
            
            if tag == 'under_min':
                under_min_count += 1
            elif tag == 'at_max':
                at_max_count += 1
            else:
                normal_count += 1
            
            self.tree.insert('', 'end', text=name, 
                           values=(station.current, station.min_lru, station.max_lru, status),
                           tags=(tag,))
        
        station_names = list(self.stations.keys())
        self.update_station_combo['values'] = station_names
        if station_names and not self.update_station_var.get():
            self.update_station_var.set(station_names[0])
        
        total_stations = len(self.stations)
        stats_text = f"""
Total Stations: {total_stations}

✅ Normal: {normal_count}
⚠️  Under Min: {under_min_count}
🔴 At/Over Max: {at_max_count}
        """
        self.stats_label.config(text=stats_text.strip())
    
    @safe_execute
    def export_new_report(self) -> None:
        """Export new Excel report."""
        if not self.stations:
            messagebox.showwarning("Warning", "No stations to export!")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
            initialfile=f"LRU_Report_{datetime.now().strftime(FILE_TIMESTAMP_FORMAT)}.xlsx"
        )
        
        if not filename:
            return
        
        try:
            self.export_manager.export_new_report(filename, self.stations, self.history)
            messagebox.showinfo("Success", f"Report exported successfully to:\n{filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export report:\n{str(e)}")
    
    def append_to_existing(self) -> None:
        """Append to existing Excel file."""
        if not self.stations:
            messagebox.showwarning("Warning", "No stations to export!")
            return
        
        filename = filedialog.askopenfilename(
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
        )
        
        if not filename:
            return
        
        try:
            sheet_name = self.export_manager.append_to_existing(filename, self.stations)
            messagebox.showinfo("Success", f"Data appended to existing report!\nNew sheet: {sheet_name}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to append to report:\n{str(e)}")
    
    def view_trends(self) -> None:
        """View trends for selected station."""
        if not self.stations:
            messagebox.showwarning("Warning", "No stations available!")
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.title("View Trends")
        dialog.geometry("400x200")
        dialog.configure(bg='white')
        dialog.transient(self.root)
        dialog.grab_set()
        
        tk.Label(dialog, text="Select Station for Trend Analysis", 
                font=('Arial', 14, 'bold'), bg='white').pack(pady=15)
        
        station_var = tk.StringVar()
        station_combo = ttk.Combobox(dialog, textvariable=station_var,
                                    values=list(self.stations.keys()),
                                    state='readonly', font=('Arial', 11))
        station_combo.pack(padx=20, pady=10, fill='x')
        station_combo.current(0)
        
        def generate_trend():
            station_name = station_var.get()
            if not station_name:
                messagebox.showwarning("Warning", "Please select a station!")
                return
            
            station = self.stations[station_name]
            if not station.history:
                messagebox.showinfo("Info", f"No history data available for '{station_name}'")
                return
            
            filename = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel files", "*.xlsx")],
                initialfile=f"Trend_{station_name}_{datetime.now().strftime('%Y%m%d')}.xlsx"
            )
            
            if not filename:
                return
            
            try:
                self.export_manager.create_trend_report(filename, station)
                dialog.destroy()
                messagebox.showinfo("Success", f"Trend report created:\n{filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create trend report:\n{str(e)}")
        
        tk.Button(dialog, text="Generate Trend Report", command=generate_trend,
                 bg='#2980b9', fg='white', font=('Arial', 11, 'bold'),
                 padx=20, pady=10).pack(pady=20)
    
    def check_for_updates(self) -> None:
        """Check for application updates."""
        checking_window = tk.Toplevel(self.root)
        checking_window.title("Checking for Updates")
        checking_window.geometry("300x100")
        checking_window.transient(self.root)
        checking_window.grab_set()
        
        tk.Label(checking_window, text="🔍 Checking for updates...", 
                font=('Arial', 12)).pack(pady=30)
        checking_window.update()
        
        def check_updates_thread():
            try:
                update_info = self.update_checker.check_for_updates()
                checking_window.destroy()
                
                if update_info:
                    self._show_update_dialog(update_info)
                else:
                    messagebox.showinfo("No Updates", 
                                      f"You're running the latest version ({APP_VERSION})!")
            
            except NetworkError:
                checking_window.destroy()
                messagebox.showwarning("Network Error", 
                                     "Could not connect to update server.\n\n"
                                     "Please check your internet connection.")
            except SecurityError as e:
                checking_window.destroy()
                messagebox.showwarning("Security Warning", str(e))
            except Exception:
                checking_window.destroy()
                messagebox.showerror("Update Check Failed", 
                                   "An unexpected error occurred while checking for updates.")
        
        thread = threading.Thread(target=check_updates_thread, daemon=True)
        thread.start()
    
    def _show_update_dialog(self, update_info: dict) -> None:
        """Show update available dialog with incremental or traditional update options."""
        is_incremental = update_info.get('update_type') == 'incremental'
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Update Available")
        dialog.geometry("550x500" if is_incremental else "500x450")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Header
        title_frame = tk.Frame(dialog, bg=Colors.SUCCESS)
        title_frame.pack(fill='x')
        
        header_text = "🚀 Smart Update Available!" if is_incremental else "🎉 Update Available!"
        tk.Label(title_frame, text=header_text, 
                font=('Arial', 16, 'bold'), bg=Colors.SUCCESS, fg='white',
                pady=15).pack()
        
        content_frame = tk.Frame(dialog, bg='white')
        content_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Version info
        tk.Label(content_frame, text=f"Current Version: {APP_VERSION}", 
                font=('Arial', 11), bg='white').pack(anchor='w')
        tk.Label(content_frame, text=f"Latest Version: {update_info.get('version', 'Unknown')}", 
                font=('Arial', 11, 'bold'), bg='white', fg=Colors.SUCCESS).pack(anchor='w', pady=(0, 10))
        
        # Incremental update info (if available)
        if is_incremental:
            info_frame = tk.Frame(content_frame, bg='#e8f5e9', relief='solid', bd=1)
            info_frame.pack(fill='x', pady=(0, 15))
            
            info_inner = tk.Frame(info_frame, bg='#e8f5e9')
            info_inner.pack(padx=15, pady=10)
            
            tk.Label(info_inner, text="⚡ Smart Incremental Update", 
                    font=('Arial', 10, 'bold'), bg='#e8f5e9', fg='#2e7d32').pack(anchor='w')
            
            file_count = update_info.get('file_count', 0)
            total_size_mb = update_info.get('total_size', 0) / 1024 / 1024
            
            savings = update_info.get('savings_info', {}).get('comparison', {})
            savings_mb = savings.get('savings_mb', 0)
            savings_percent = savings.get('savings_percent', 0)
            
            details = (
                f"📦 Files to update: {file_count}\n"
                f"📥 Download size: {total_size_mb:.1f} MB\n"
                f"💾 Bandwidth saved: {savings_mb:.1f} MB ({savings_percent:.1f}%)\n"
                f"⏱️ Estimated time: ~{max(10, int(total_size_mb * 2))} seconds"
            )
            
            tk.Label(info_inner, text=details, 
                    font=('Arial', 9), bg='#e8f5e9', fg='#1b5e20',
                    justify='left').pack(anchor='w', pady=(5, 0))
        
        # Release notes
        if update_info.get('release_notes'):
            tk.Label(content_frame, text="What's New:", 
                    font=('Arial', 11, 'bold'), bg='white').pack(anchor='w', pady=(5, 5))
            
            notes_frame = tk.Frame(content_frame, bg='#ecf0f1', relief='sunken', bd=1)
            notes_frame.pack(fill='both', expand=True, pady=(0, 15))
            
            notes_text = tk.Text(notes_frame, wrap='word', height=6 if is_incremental else 8, 
                                font=('Arial', 10), bg='#ecf0f1', relief='flat')
            notes_text.pack(fill='both', expand=True, padx=10, pady=10)
            notes_text.insert('1.0', update_info.get('release_notes', ''))
            notes_text.config(state='disabled')
        
        # Progress label for download status
        self.download_status_label = tk.Label(content_frame, text="", 
                                             font=('Arial', 9), bg='white', fg=Colors.INFO)
        self.download_status_label.pack(anchor='w', pady=(5, 0))
        
        button_frame = tk.Frame(dialog, bg='white')
        button_frame.pack(fill='x', padx=20, pady=(0, 20))
        
        def start_update():
            """Start update (incremental or traditional)."""
            if is_incremental:
                self._perform_incremental_update(dialog, update_info)
            else:
                self._perform_traditional_download(dialog, update_info)
        
        # Update button text based on type
        button_text = "⚡ Install Update" if is_incremental else "📥 Download Update"
        
        tk.Button(button_frame, text=button_text, 
                 command=start_update,
                 bg=Colors.SUCCESS, fg='white', font=('Arial', 11, 'bold'),
                 padx=20, pady=10).pack(side='left', padx=(0, 10))
        
        tk.Button(button_frame, text="Later", 
                 command=dialog.destroy,
                 bg=Colors.SECONDARY, fg='white', font=('Arial', 11),
                 padx=20, pady=10).pack(side='left')
    
    def _perform_incremental_update(self, dialog: tk.Toplevel, update_info: dict) -> None:
        """Perform incremental file-based update."""
        try:
            from incremental_updater import IncrementalUpdater
            
            # Update status
            self.download_status_label.config(text="🔍 Checking files...")
            dialog.update()
            
            # Create updater
            updater = IncrementalUpdater(current_version=APP_VERSION)
            
            # Build update info for incremental updater
            incremental_info = {
                'version': update_info['version'],
                'release_date': update_info.get('release_date'),
                'release_notes': update_info.get('release_notes'),
                'changed_files': update_info.get('files', {}),
                'total_download_size': update_info.get('total_size', 0),
                'full_manifest': update_info.get('manifest', {})
            }
            
            # Progress callback
            def on_progress(current, total, filename):
                status = f"⏳ Downloading {current}/{total}: {Path(filename).name}"
                self.download_status_label.config(text=status)
                dialog.update()
            
            # Perform update
            self.download_status_label.config(text="📥 Downloading updates...")
            dialog.update()
            
            success = updater.download_updates(incremental_info, progress_callback=on_progress)
            
            if success:
                dialog.destroy()
                
                result = messagebox.askyesno(
                    "✅ Update Complete!",
                    f"Update to v{update_info['version']} installed successfully!\n\n"
                    f"The application needs to restart to apply changes.\n\n"
                    f"Restart now?",
                    icon='info'
                )
                
                if result:
                    updater.restart_application()
            else:
                raise Exception("Update download failed")
                
        except Exception as e:
            logger.error(f"Incremental update failed: {e}")
            dialog.destroy()
            
            # Fall back to traditional download
            result = messagebox.askyesno(
                "Update Method Changed",
                "Smart update encountered an issue.\n\n"
                "Would you like to download the full installer instead?",
                icon='warning'
            )
            
            if result:
                webbrowser.open(update_info.get('download_url', ''))
    
    def _perform_traditional_download(self, dialog: tk.Toplevel, update_info: dict) -> None:
        """Download update to Downloads folder automatically."""
        download_url = update_info.get('download_url', '')
        
        # Check if it's a direct download URL or release page
        if '/releases/tag/' in download_url:
            # It's a release page, open in browser
            webbrowser.open(download_url)
            dialog.destroy()
            return
        
        # It's a direct download URL, download automatically
        try:
            # Get Downloads folder
            downloads_folder = Path.home() / 'Downloads'
            downloads_folder.mkdir(exist_ok=True)
            
            # Extract filename from URL
            filename = download_url.split('/')[-1]
            if not filename.endswith('.exe'):
                filename = f"LRU_Tracker_v{update_info.get('version', 'latest')}.exe"
            
            dest_path = downloads_folder / filename
            
            # Update status
            self.download_status_label.config(text="⏳ Downloading update...")
            dialog.update()
            
            # Download file
            def download_thread():
                try:
                    urllib.request.urlretrieve(download_url, dest_path)
                    
                    # Update status on main thread
                    dialog.after(0, lambda: self._download_complete(dialog, dest_path))
                    
                except Exception as e:
                    logger.error(f"Download failed: {e}")
                    dialog.after(0, lambda: self._download_failed(dialog, download_url))
            
            # Start download in background thread
            thread = threading.Thread(target=download_thread, daemon=True)
            thread.start()
            
        except Exception as e:
            logger.error(f"Failed to start download: {e}")
            messagebox.showerror("Download Error", 
                               f"Could not download update.\n\n"
                               f"Opening download page in browser instead...")
            webbrowser.open(download_url)
            dialog.destroy()
    
    def _download_complete(self, dialog: tk.Toplevel, file_path: Path) -> None:
        """Handle successful download completion."""
        dialog.destroy()
        
        result = messagebox.askyesno(
            "✅ Download Complete!", 
            f"Update downloaded successfully!\n\n"
            f"Location: {file_path}\n\n"
            f"Would you like to open the Downloads folder to install it now?",
            icon='info'
        )
        
        if result:
            # Open Downloads folder and select the file
            try:
                if os.name == 'nt':  # Windows
                    subprocess.run(['explorer', '/select,', str(file_path)])
                else:
                    subprocess.run(['xdg-open', str(file_path.parent)])
            except Exception as e:
                logger.error(f"Failed to open folder: {e}")
                # Fallback: just open in browser
                webbrowser.open(str(file_path.parent))
    
    def _download_failed(self, dialog: tk.Toplevel, download_url: str) -> None:
        """Handle download failure."""
        dialog.destroy()
        
        result = messagebox.askyesno(
            "Download Failed", 
            "Could not download the update automatically.\n\n"
            "Would you like to open the download page in your browser?",
            icon='warning'
        )
        
        if result:
            webbrowser.open(download_url)


    @safe_execute
    def download_template(self) -> None:
        """Download Excel template for bulk station import."""
        filename = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
            initialfile="LRU_Station_Template.xlsx"
        )
        
        if not filename:
            return
        
        self.template_manager.create_template(filename)
        messagebox.showinfo("Success", 
                          f"Template downloaded successfully!\n\n"
                          f"Location: {filename}\n\n"
                          f"Fill in your stations and use 'Import from Template' to load them.")
    
    @safe_execute
    def import_from_template(self) -> None:
        """Import stations from template file."""
        filename = filedialog.askopenfilename(
            title="Select Station Template to Import",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
        )
        
        if not filename:
            return
        
        imported_stations, errors = self.template_manager.import_from_template(filename, self.stations)
        
        # Add imported stations
        for station in imported_stations:
            self.stations[station.name] = station
            if station.current > 0:
                timestamp = datetime.now().strftime(TIMESTAMP_FORMAT)
                self.history.append(GlobalHistoryEntry(
                    station=station.name,
                    timestamp=timestamp,
                    count=station.current,
                    min_lru=station.min_lru,
                    max_lru=station.max_lru
                ))
        
        if imported_stations:
            self._save_data()
            self.refresh_display()
        
        # Show summary
        summary = f"Import Complete!\n\n"
        summary += f"✅ Imported: {len(imported_stations)} stations\n"
        if errors:
            summary += f"❌ Errors: {len(errors)}\n\n"
            summary += "Errors:\n" + "\n".join(errors[:5])
            if len(errors) > 5:
                summary += f"\n... and {len(errors) - 5} more errors"
        
        messagebox.showinfo("Import Summary", summary)
    
    @safe_execute
    def import_fc_schedule(self) -> None:
        """Import stations from FC Standard Work Spreadsheet CSV."""
        filename = filedialog.askopenfilename(
            title="Select FC Standard Work Spreadsheet CSV",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if not filename:
            return
        
        imported_stations, errors = self.fc_schedule_manager.import_from_csv(filename, self.stations)
        
        # Add imported stations
        for station in imported_stations:
            self.stations[station.name] = station
        
        if imported_stations:
            self._save_data()
            self.refresh_display()
        
        # Show summary
        summary = f"FC Schedule Import Complete!\n\n"
        summary += f"✅ Imported: {len(imported_stations)} stations\n"
        if errors:
            summary += f"❌ Errors: {len(errors)}\n"
        
        if imported_stations:
            summary += f"\n📋 Imported Stations:\n"
            for station in imported_stations[:10]:
                summary += f"  • {station.name}\n    Min: {station.min_lru}, Max: {station.max_lru}\n"
            if len(imported_stations) > 10:
                summary += f"  ... and {len(imported_stations) - 10} more\n"
        
        summary += f"\n💡 Tip: Min/Max values were auto-calculated from batch sizes."
        
        messagebox.showinfo("Import Summary", summary)
    
    @safe_execute
    def export_fc_schedule(self) -> None:
        """Export in FC Standard Work Spreadsheet format."""
        if not self.stations:
            messagebox.showwarning("Warning", "No stations to export!")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv"), ("All files", "*.*")],
            initialfile=f"FC_Schedule_Report_{datetime.now().strftime(FILE_TIMESTAMP_FORMAT)}.xlsx"
        )
        
        if not filename:
            return
        
        self.fc_schedule_manager.export_to_csv(filename, self.stations)
        messagebox.showinfo("Success", f"FC Schedule exported to:\n{filename}")


def main():
    """Application entry point."""
    root = tk.Tk()
    app = LRUTrackerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
