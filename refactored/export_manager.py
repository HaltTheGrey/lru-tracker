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


class ExportManager:
    """Handles all export operations."""
    
    @staticmethod
    def create_header_style() -> tuple:
        """Create standard header styling."""
        fill = PatternFill(start_color=Colors.HEADER_BG, end_color=Colors.HEADER_BG, fill_type="solid")
        font = Font(color="FFFFFF", bold=True, size=12)
        alignment = Alignment(horizontal='center', vertical='center')
        return fill, font, alignment
    
    @staticmethod
    def get_status_fill(current: int, min_val: int, max_val: int) -> PatternFill:
        """Get status fill color based on values."""
        if current < min_val:
            return PatternFill(start_color=Colors.UNDER_MIN_BG.replace('#', ''), 
                             end_color=Colors.UNDER_MIN_BG.replace('#', ''), fill_type="solid")
        elif current >= max_val:
            return PatternFill(start_color=Colors.AT_MAX_BG.replace('#', ''), 
                             end_color=Colors.AT_MAX_BG.replace('#', ''), fill_type="solid")
        return PatternFill(start_color=Colors.NORMAL_BG.replace('#', ''), 
                         end_color=Colors.NORMAL_BG.replace('#', ''), fill_type="solid")
    
    def export_new_report(self, filename: str, stations: Dict[str, Station], 
                         history: List[GlobalHistoryEntry]) -> None:
        """Export new Excel report with current status and history."""
        wb = openpyxl.Workbook()
        ws: Worksheet = wb.active
        ws.title = "Current Status"
        
        # Header
        headers = ["Station Name", "Current LRU", "Min", "Max", "Status", "Last Updated"]
        ws.append(headers)
        
        # Style header
        header_fill, header_font, header_align = self.create_header_style()
        for col in range(1, len(headers) + 1):
            cell = ws.cell(1, col)
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = header_align
        
        # Data
        for name in sorted(stations.keys()):
            station = stations[name]
            status = station.get_status()
            last_updated = station.history[-1].timestamp if station.history else "Never"
            
            row = [name, station.current, station.min_lru, station.max_lru, status, last_updated]
            ws.append(row)
            
            # Color code status
            status_cell = ws.cell(ws.max_row, 5)
            status_cell.fill = self.get_status_fill(station.current, station.min_lru, station.max_lru)
        
        # Adjust column widths
        ws.column_dimensions['A'].width = 25
        ws.column_dimensions['B'].width = 15
        ws.column_dimensions['C'].width = 10
        ws.column_dimensions['D'].width = 10
        ws.column_dimensions['E'].width = 15
        ws.column_dimensions['F'].width = 20
        
        # Create history sheet if there's history
        if history:
            self._add_history_sheet(wb, history)
        
        wb.save(filename)
    
    def _add_history_sheet(self, wb: openpyxl.Workbook, 
                          history: List[GlobalHistoryEntry]) -> None:
        """Add history sheet to workbook."""
        ws_history = wb.create_sheet("History")
        history_headers = ["Station", "Timestamp", "Count", "Min", "Max"]
        ws_history.append(history_headers)
        
        # Style header
        header_fill, header_font, header_align = self.create_header_style()
        for col in range(1, len(history_headers) + 1):
            cell = ws_history.cell(1, col)
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = header_align
        
        # Add history data
        for record in history:
            ws_history.append([
                record.station, record.timestamp, record.count,
                record.min_lru, record.max_lru
            ])
        
        # Adjust column widths
        ws_history.column_dimensions['A'].width = 25
        ws_history.column_dimensions['B'].width = 20
        ws_history.column_dimensions['C'].width = 12
        ws_history.column_dimensions['D'].width = 10
        ws_history.column_dimensions['E'].width = 10
    
    def append_to_existing(self, filename: str, stations: Dict[str, Station]) -> str:
        """Append snapshot to existing Excel file."""
        wb = openpyxl.load_workbook(filename)
        
        # Create new sheet with timestamp
        sheet_name = f"Snapshot_{datetime.now().strftime(FILE_TIMESTAMP_FORMAT)}"
        ws = wb.create_sheet(sheet_name)
        
        # Header
        headers = ["Station Name", "Current LRU", "Min", "Max", "Status", "Timestamp"]
        ws.append(headers)
        
        # Style header
        header_fill, header_font, header_align = self.create_header_style()
        for col in range(1, len(headers) + 1):
            cell = ws.cell(1, col)
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = header_align
        
        # Data
        timestamp = datetime.now().strftime(TIMESTAMP_FORMAT)
        for name in sorted(stations.keys()):
            station = stations[name]
            status = station.get_status()
            
            row = [name, station.current, station.min_lru, station.max_lru, status, timestamp]
            ws.append(row)
            
            status_cell = ws.cell(ws.max_row, 5)
            status_cell.fill = self.get_status_fill(station.current, station.min_lru, station.max_lru)
        
        # Adjust column widths
        for col in ['A', 'B', 'C', 'D', 'E', 'F']:
            ws.column_dimensions[col].width = 18
        
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
