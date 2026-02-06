"""Export functionality for Excel and CSV reports."""
import openpyxl
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.chart import LineChart, Reference
from openpyxl.worksheet.worksheet import Worksheet
from typing import Dict, List
from datetime import datetime
from models import Station, GlobalHistoryEntry
from config import Colors, TIMESTAMP_FORMAT, FILE_TIMESTAMP_FORMAT


class ExcelColors:
    """Enhanced color scheme for Excel exports."""
    HEADER_PRIMARY = '1F4788'      # Deep blue
    HEADER_SECONDARY = '2E5C8A'    # Medium blue
    CRITICAL = 'E74C3C'            # Red
    WARNING = 'F39C12'             # Orange
    SUCCESS = '27AE60'             # Green
    INFO = '3498DB'                # Light blue
    NEUTRAL = 'ECF0F1'             # Light gray
    TEXT_DARK = '2C3E50'           # Dark gray
    BORDER_COLOR = 'BDC3C7'        # Gray border


class ExportManager:
    """Handles all export operations."""
    
    @staticmethod
    def create_header_style() -> tuple:
        """Create enhanced header styling."""
        fill = PatternFill(start_color=ExcelColors.HEADER_PRIMARY, end_color=ExcelColors.HEADER_PRIMARY, fill_type="solid")
        font = Font(color="FFFFFF", bold=True, size=13, name='Calibri')
        alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        border = Border(
            left=Side(style='thin', color=ExcelColors.BORDER_COLOR),
            right=Side(style='thin', color=ExcelColors.BORDER_COLOR),
            top=Side(style='thin', color=ExcelColors.BORDER_COLOR),
            bottom=Side(style='medium', color='FFFFFF')
        )
        return fill, font, alignment, border
    
    @staticmethod
    def get_status_fill(current: int, min_val: int, max_val: int) -> PatternFill:
        """Get enhanced status fill color based on values."""
        if current < min_val:
            return PatternFill(start_color=ExcelColors.CRITICAL, end_color=ExcelColors.CRITICAL, fill_type="solid")
        elif current >= max_val:
            return PatternFill(start_color=ExcelColors.WARNING, end_color=ExcelColors.WARNING, fill_type="solid")
        return PatternFill(start_color=ExcelColors.SUCCESS, end_color=ExcelColors.SUCCESS, fill_type="solid")
    
    @staticmethod
    def apply_cell_border(cell) -> None:
        """Apply consistent border to cell."""
        cell.border = Border(
            left=Side(style='thin', color=ExcelColors.BORDER_COLOR),
            right=Side(style='thin', color=ExcelColors.BORDER_COLOR),
            top=Side(style='thin', color=ExcelColors.BORDER_COLOR),
            bottom=Side(style='thin', color=ExcelColors.BORDER_COLOR)
        )
    
    def export_new_report(self, filename: str, stations: Dict[str, Station], 
                         history: List[GlobalHistoryEntry]) -> None:
        """Export enhanced Excel report with current status and history."""
        wb = openpyxl.Workbook()
        ws: Worksheet = wb.active
        ws.title = "Current Status"
        
        # Add title row
        ws.merge_cells('A1:F1')
        title_cell = ws['A1']
        title_cell.value = f"LRU Tracker Report - {datetime.now().strftime('%B %d, %Y at %I:%M %p')}"
        title_cell.font = Font(size=16, bold=True, color=ExcelColors.HEADER_PRIMARY, name='Calibri')
        title_cell.alignment = Alignment(horizontal='center', vertical='center')
        ws.row_dimensions[1].height = 30
        
        # Header
        headers = ["Station Name", "Current LRU", "Min", "Max", "Status", "Last Updated"]
        ws.append(headers)
        
        # Style header
        header_fill, header_font, header_align, header_border = self.create_header_style()
        for col in range(1, len(headers) + 1):
            cell = ws.cell(2, col)
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = header_align
            cell.border = header_border
        ws.row_dimensions[2].height = 25
        
        # Data
        for name in sorted(stations.keys()):
            station = stations[name]
            status = station.get_status()
            last_updated = station.history[-1].timestamp if station.history else "Never"
            
            row = [name, station.current, station.min_lru, station.max_lru, status, last_updated]
            ws.append(row)
            row_num = ws.max_row
            
            # Style data cells
            for col in range(1, 7):
                cell = ws.cell(row_num, col)
                self.apply_cell_border(cell)
                cell.alignment = Alignment(horizontal='center' if col > 1 else 'left', vertical='center')
                cell.font = Font(name='Calibri', size=11)
                
                # Alternate row colors
                if row_num % 2 == 0:
                    cell.fill = PatternFill(start_color=ExcelColors.NEUTRAL, end_color=ExcelColors.NEUTRAL, fill_type="solid")
            
            # Color code status with white text
            status_cell = ws.cell(row_num, 5)
            status_cell.fill = self.get_status_fill(station.current, station.min_lru, station.max_lru)
            status_cell.font = Font(bold=True, color='FFFFFF', size=11, name='Calibri')
        
        # Adjust column widths
        ws.column_dimensions['A'].width = 30
        ws.column_dimensions['B'].width = 15
        ws.column_dimensions['C'].width = 12
        ws.column_dimensions['D'].width = 12
        ws.column_dimensions['E'].width = 18
        ws.column_dimensions['F'].width = 22
        
        # Freeze panes
        ws.freeze_panes = 'A3'
        
        # Create history sheet if there's history
        if history:
            self._add_history_sheet(wb, history)
        
        wb.save(filename)
    
    def _add_history_sheet(self, wb: openpyxl.Workbook, 
                          history: List[GlobalHistoryEntry]) -> None:
        """Add enhanced history sheet to workbook."""
        ws_history = wb.create_sheet("History")
        
        # Add title
        ws_history.merge_cells('A1:E1')
        title_cell = ws_history['A1']
        title_cell.value = "LRU Update History"
        title_cell.font = Font(size=16, bold=True, color=ExcelColors.HEADER_PRIMARY, name='Calibri')
        title_cell.alignment = Alignment(horizontal='center', vertical='center')
        ws_history.row_dimensions[1].height = 30
        
        history_headers = ["Station", "Timestamp", "Count", "Min", "Max"]
        ws_history.append(history_headers)
        
        # Style header
        header_fill, header_font, header_align, header_border = self.create_header_style()
        for col in range(1, len(history_headers) + 1):
            cell = ws_history.cell(2, col)
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = header_align
            cell.border = header_border
        ws_history.row_dimensions[2].height = 25
        
        # Add history data
        for record in history:
            ws_history.append([
                record.station, record.timestamp, record.count,
                record.min_lru, record.max_lru
            ])
            row_num = ws_history.max_row
            
            # Style cells
            for col in range(1, 6):
                cell = ws_history.cell(row_num, col)
                self.apply_cell_border(cell)
                cell.alignment = Alignment(horizontal='center' if col > 1 else 'left', vertical='center')
                cell.font = Font(name='Calibri', size=11)
                
                # Alternate row colors
                if row_num % 2 == 0:
                    cell.fill = PatternFill(start_color=ExcelColors.NEUTRAL, end_color=ExcelColors.NEUTRAL, fill_type="solid")
        
        # Adjust column widths
        ws_history.column_dimensions['A'].width = 30
        ws_history.column_dimensions['B'].width = 22
        ws_history.column_dimensions['C'].width = 15
        ws_history.column_dimensions['D'].width = 12
        ws_history.column_dimensions['E'].width = 12
        
        # Freeze panes
        ws_history.freeze_panes = 'A3'
    
    def append_to_existing(self, filename: str, stations: Dict[str, Station]) -> str:
        """Append enhanced snapshot to existing Excel file."""
        wb = openpyxl.load_workbook(filename)
        
        # Create new sheet with timestamp
        sheet_name = f"Snapshot_{datetime.now().strftime(FILE_TIMESTAMP_FORMAT)}"
        ws = wb.create_sheet(sheet_name)
        
        # Add title
        ws.merge_cells('A1:F1')
        title_cell = ws['A1']
        title_cell.value = f"Snapshot - {datetime.now().strftime('%B %d, %Y at %I:%M %p')}"
        title_cell.font = Font(size=16, bold=True, color=ExcelColors.HEADER_PRIMARY, name='Calibri')
        title_cell.alignment = Alignment(horizontal='center', vertical='center')
        ws.row_dimensions[1].height = 30
        
        # Header
        headers = ["Station Name", "Current LRU", "Min", "Max", "Status", "Timestamp"]
        ws.append(headers)
        
        # Style header
        header_fill, header_font, header_align, header_border = self.create_header_style()
        for col in range(1, len(headers) + 1):
            cell = ws.cell(2, col)
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = header_align
            cell.border = header_border
        ws.row_dimensions[2].height = 25
        
        # Data
        timestamp = datetime.now().strftime(TIMESTAMP_FORMAT)
        for name in sorted(stations.keys()):
            station = stations[name]
            status = station.get_status()
            
            row = [name, station.current, station.min_lru, station.max_lru, status, timestamp]
            ws.append(row)
            row_num = ws.max_row
            
            # Style cells
            for col in range(1, 7):
                cell = ws.cell(row_num, col)
                self.apply_cell_border(cell)
                cell.alignment = Alignment(horizontal='center' if col > 1 else 'left', vertical='center')
                cell.font = Font(name='Calibri', size=11)
                
                # Alternate row colors
                if row_num % 2 == 0:
                    cell.fill = PatternFill(start_color=ExcelColors.NEUTRAL, end_color=ExcelColors.NEUTRAL, fill_type="solid")
            
            # Color code status
            status_cell = ws.cell(row_num, 5)
            status_cell.fill = self.get_status_fill(station.current, station.min_lru, station.max_lru)
            status_cell.font = Font(bold=True, color='FFFFFF', size=11, name='Calibri')
        
        # Adjust column widths
        ws.column_dimensions['A'].width = 30
        ws.column_dimensions['B'].width = 15
        ws.column_dimensions['C'].width = 12
        ws.column_dimensions['D'].width = 12
        ws.column_dimensions['E'].width = 18
        ws.column_dimensions['F'].width = 22
        
        # Freeze panes
        ws.freeze_panes = 'A3'
        
        wb.save(filename)
        return sheet_name
    
    def create_trend_report(self, filename: str, station: Station) -> None:
        """Create trend report with chart for a station."""
        wb = openpyxl.Workbook()
        ws: Worksheet = wb.active
        ws.title = f"{station.name} Trends"
        
        # Headers
        ws.append(["Timestamp", "LRU Count", "Min", "Max"])
        
        # Data
        for record in station.history:
            ws.append([record.timestamp, record.count, station.min_lru, station.max_lru])
        
        # Create chart
        chart = LineChart()
        chart.title = f"LRU Trend for {station.name}"
        chart.style = 10
        chart.x_axis.title = "Time"
        chart.y_axis.title = "LRU Count"
        chart.height = 15
        chart.width = 25
        
        data = Reference(ws, min_col=2, max_col=4, min_row=1, max_row=len(station.history) + 1)
        cats = Reference(ws, min_col=1, min_row=2, max_row=len(station.history) + 1)
        
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(cats)
        
        ws.add_chart(chart, "F2")
        
        wb.save(filename)
