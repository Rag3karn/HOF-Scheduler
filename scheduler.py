"""
HOF Scheduler - Main Logic Module
Processes match schedule data and generates formatted announcements
"""

import pandas as pd
from datetime import datetime
from typing import Dict, List, Tuple
import re


class ValidationError(Exception):
    """Custom exception for validation errors"""
    pass


class HOFScheduler:
    """Main class for processing HOF match schedules"""
    
    REQUIRED_COLUMNS = [
        'cityName', 'venueName', 'matchTypeName', 'startTime', 
        'endTime', 'playerCapacity', 'slotPrice', 'offerPrice'
    ]
    
    def __init__(self):
        self.df = None
        self.errors = []
    
    def load_excel(self, file_path: str) -> bool:
        """
        Load and validate Excel file
        
        Args:
            file_path: Path to the Excel file
            
        Returns:
            True if loaded successfully, False otherwise
        """
        try:
            self.df = pd.read_excel(file_path)
            self._validate_columns()
            self._validate_data()
            return True
        except Exception as e:
            self.errors.append(f"Error loading file: {str(e)}")
            return False
    
    def _validate_columns(self):
        """Validate that all required columns exist"""
        missing_columns = [col for col in self.REQUIRED_COLUMNS if col not in self.df.columns]
        if missing_columns:
            raise ValidationError(f"Missing required columns: {', '.join(missing_columns)}")
    
    def _validate_data(self):
        """Validate data in each row"""
        for idx, row in self.df.iterrows():
            row_num = idx + 2  # +2 because Excel is 1-indexed and has header row
            
            # Check for missing values in required columns
            for col in self.REQUIRED_COLUMNS:
                if pd.isna(row[col]) or (isinstance(row[col], str) and not row[col].strip()):
                    raise ValidationError(
                        f"Row {row_num}: Missing value in column '{col}'"
                    )
            
            # Validate playerCapacity
            if not isinstance(row['playerCapacity'], (int, float)) or row['playerCapacity'] <= 0:
                raise ValidationError(
                    f"Row {row_num}: 'playerCapacity' must be a positive number (found: {row['playerCapacity']})"
                )
            
            if row['playerCapacity'] % 2 != 0:
                raise ValidationError(
                    f"Row {row_num}: 'playerCapacity' must be an even number (found: {row['playerCapacity']})"
                )
            
            # Validate prices
            for price_col in ['slotPrice', 'offerPrice']:
                if not isinstance(row[price_col], (int, float)) or row[price_col] < 0:
                    raise ValidationError(
                        f"Row {row_num}: '{price_col}' must be a non-negative number (found: {row[price_col]})"
                    )
            
            # Validate datetime fields
            for time_col in ['startTime', 'endTime']:
                if not isinstance(row[time_col], (pd.Timestamp, datetime)):
                    raise ValidationError(
                        f"Row {row_num}: '{time_col}' must be a valid date/time (found: {row[time_col]})"
                    )
            
            # Validate endTime is after startTime
            if row['endTime'] <= row['startTime']:
                raise ValidationError(
                    f"Row {row_num}: 'endTime' must be after 'startTime'"
                )
    
    @staticmethod
    def get_ordinal_suffix(day: int) -> str:
        """
        Get ordinal suffix for a day number (st, nd, rd, th)
        
        Args:
            day: Day number (1-31)
            
        Returns:
            Ordinal suffix string
        """
        if 10 <= day % 100 <= 20:
            suffix = 'th'
        else:
            suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
        return suffix
    
    @staticmethod
    def format_time(dt: datetime) -> str:
        """
        Format time, omitting minutes if they are 00
        
        Args:
            dt: Datetime object
            
        Returns:
            Formatted time string
        """
        hour = dt.hour
        minute = dt.minute
        
        # Convert to 12-hour format
        if hour == 0:
            hour_12 = 12
            period = 'AM'
        elif hour < 12:
            hour_12 = hour
            period = 'AM'
        elif hour == 12:
            hour_12 = 12
            period = 'PM'
        else:
            hour_12 = hour - 12
            period = 'PM'
        
        # Format time
        if minute == 0:
            return f"{hour_12} {period}"
        else:
            return f"{hour_12}:{minute:02d} {period}"
    
    @staticmethod
    def get_day_info(dt: datetime) -> Tuple[int, str, str]:
        """
        Get day number, day name, and ordinal for a datetime
        
        Args:
            dt: Datetime object
            
        Returns:
            Tuple of (day_number, day_name, day_with_ordinal)
        """
        day_num = dt.day
        day_name = dt.strftime('%A')
        suffix = HOFScheduler.get_ordinal_suffix(day_num)
        day_with_ordinal = f"{day_num}{suffix}"
        
        return day_num, day_name, day_with_ordinal
    
    def generate_announcement(self) -> str:
        """
        Generate the formatted announcement message
        
        Returns:
            Formatted announcement string
        """
        if self.df is None or self.df.empty:
            raise ValueError("No data loaded. Please load an Excel file first.")
        
        # Group by city for the header
        city_name = self.df.iloc[0]['cityName']
        
        # Start building the message
        lines = [
            f"*🚨⚽ HUMANS OF FOOTBALL – {city_name.upper()} FULL WEEK ANNOUNCEMENT ⚽🚨*",
            f"{city_name}, are you ready? 🔥",
            "This week we're going LIVE again across multiple turfs 💛",
            "━━━━━━━━━━━━━━━━━━"
        ]
        
        # Process each row
        for idx, row in self.df.iterrows():
            venue_name = row['venueName']
            start_time = row['startTime']
            end_time = row['endTime']
            player_capacity = int(row['playerCapacity'])
            half_capacity = player_capacity // 2
            
            # Get day information
            day_num, day_name, day_with_ordinal = self.get_day_info(start_time)
            
            # Format times
            start_time_str = self.format_time(start_time)
            end_time_str = self.format_time(end_time)
            
            # Add venue and match details
            lines.append(f"📍 *NAME* – {venue_name}")
            lines.append(
                f"🗓 {day_with_ordinal} {day_name} | {start_time_str}–{end_time_str} | "
                f"{half_capacity}v{half_capacity}"
            )
            
            # Add separator after each entry
            lines.append("━━━━━━━━━━━━━━━━━━")
        
        return '\n'.join(lines)
    
    def get_errors(self) -> List[str]:
        """Get list of validation errors"""
        return self.errors
    
    def reset(self):
        """Reset the scheduler state"""
        self.df = None
        self.errors = []


def process_schedule_file(file_path: str) -> Tuple[bool, str, List[str]]:
    """
    Process a schedule file and return the announcement
    
    Args:
        file_path: Path to the Excel file
        
    Returns:
        Tuple of (success, announcement_text, errors)
    """
    scheduler = HOFScheduler()
    
    try:
        if not scheduler.load_excel(file_path):
            return False, "", scheduler.get_errors()
        
        announcement = scheduler.generate_announcement()
        return True, announcement, []
    
    except ValidationError as e:
        return False, "", [str(e)]
    except Exception as e:
        return False, "", [f"Unexpected error: {str(e)}"]
