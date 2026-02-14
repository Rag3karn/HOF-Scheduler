# HOF - Scheduler ⚽

A user-friendly web application for generating match announcements from Excel schedule data for Humans of Football.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.29.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Excel File Format](#excel-file-format)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)
- [Project Structure](#project-structure)

## ✨ Features

- 🎯 **User-Friendly Interface**: Clean and intuitive Streamlit web interface
- 📊 **Excel Processing**: Reads and validates match schedule data from Excel files
- ✅ **Data Validation**: Comprehensive validation with helpful error messages
- 📝 **Automatic Formatting**: Generates properly formatted announcements
- 🕐 **Smart Time Formatting**: Automatically handles 12/24-hour conversion and AM/PM
- 📅 **Date Intelligence**: Correctly applies ordinal suffixes (st, nd, rd, th) to dates
- 📋 **One-Click Copy**: Easy copy-to-clipboard functionality
- 🔄 **Reset Feature**: Quick reset to process new files

## 🔧 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher**
  - Download from [python.org](https://www.python.org/downloads/)
  - Verify installation: `python --version` or `python3 --version`

- **pip** (Python package installer)
  - Usually comes with Python
  - Verify installation: `pip --version` or `pip3 --version`

## 📥 Installation

### Step 1: Clone or Download the Project

Download all project files to a directory on your computer:
```
hof-scheduler/
├── app.py
├── scheduler.py
├── requirements.txt
└── README.md
```

### Step 2: Create a Virtual Environment (Recommended)

Open your terminal/command prompt and navigate to the project directory:

**Windows:**
```bash
cd path\to\hof-scheduler
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
cd path/to/hof-scheduler
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

With your virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```

This will install:
- `pandas` - For Excel file processing
- `openpyxl` - For reading Excel files
- `streamlit` - For the web interface

## 🚀 Usage

### Running the Application

1. **Activate your virtual environment** (if not already activated):
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

2. **Start the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

3. **Access the application**:
   - The app will automatically open in your default web browser
   - If not, navigate to: `http://localhost:8501`

### Using the Application

1. **Upload Excel File**:
   - Click the "Choose an Excel file (.xlsx)" button
   - Select your match schedule Excel file

2. **Generate Announcement**:
   - Click the "🚀 Generate Announcement" button
   - Wait for processing (usually takes 1-2 seconds)

3. **Copy the Result**:
   - If successful, the formatted announcement will appear
   - Click "📋 Copy to Clipboard" to copy the entire message
   - Or use the "View Raw Text" expander to manually copy

4. **Reset** (if needed):
   - Click "🔄 Reset" to clear everything and start over

### Example Workflow

```
1. Upload: match_schedule.xlsx
   ↓
2. Click: Generate Announcement
   ↓
3. View: Formatted announcement message
   ↓
4. Click: Copy to Clipboard
   ↓
5. Paste: Into WhatsApp, Telegram, etc.
```

## 📊 Excel File Format

### Required Columns

Your Excel file must contain the following columns (exact spelling required):

| Column Name      | Type     | Description                          | Example                    |
|------------------|----------|--------------------------------------|----------------------------|
| cityName         | Text     | Name of the city                     | Mumbai                     |
| venueName        | Text     | Name of the venue                    | South United Football Club |
| matchTypeName    | Text     | Type of match                        | HOF Play                   |
| startTime        | DateTime | Match start date and time            | 15-02-2026 18:00          |
| endTime          | DateTime | Match end date and time              | 15-02-2026 20:00          |
| playerCapacity   | Number   | Total player capacity (must be even) | 12                         |
| slotPrice        | Number   | Regular slot price                   | 250                        |
| offerPrice       | Number   | Discounted offer price               | 200                        |

### Additional Columns (Optional but Present)

The following columns should be in your Excel file but are not used in the announcement:
- matchType
- footballChiefPhone
- gameControllerPhone
- venueCost
- bufferCapacity
- teamAName
- teamBName
- footballChiefCost

### Data Validation Rules

✅ **Valid Data Requirements**:
- All required columns must be present
- No empty cells in required columns
- `playerCapacity` must be a positive even number
- `slotPrice` and `offerPrice` must be non-negative numbers
- `startTime` and `endTime` must be valid dates/times
- `endTime` must be after `startTime`

❌ **Common Errors**:
- Missing column names
- Empty cells
- Odd player capacity (e.g., 11 instead of 12)
- Invalid date formats
- End time before start time

### Sample Data

```
cityName: Bengaluru
venueName: South United Football Club
matchTypeName: HOF Play
startTime: 15-02-2026 18:00
endTime: 15-02-2026 20:00
playerCapacity: 12
slotPrice: 250
offerPrice: 200
```

## ⚙️ How It Works

### Architecture

```
┌─────────────────┐
│   User Upload   │
│   Excel File    │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│   Streamlit Frontend    │
│   (app.py)              │
│   - File Upload UI      │
│   - Display Results     │
│   - Error Handling      │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│   Backend Logic         │
│   (scheduler.py)        │
│   - Data Validation     │
│   - Data Processing     │
│   - Message Generation  │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│   Generated Output      │
│   - Formatted Message   │
│   - Error Messages      │
└─────────────────────────┘
```

### Processing Flow

1. **File Upload & Validation**
   - Excel file is uploaded via Streamlit interface
   - File is temporarily saved for processing
   - Column names are validated

2. **Data Validation**
   - Each row is checked for:
     - Missing values
     - Correct data types
     - Valid ranges
     - Logical consistency (e.g., endTime > startTime)

3. **Data Processing**
   - Extract required fields from each row
   - Calculate half capacity (playerCapacity ÷ 2)
   - Format times (24-hour to 12-hour with AM/PM)
   - Generate ordinal suffixes (1st, 2nd, 3rd, etc.)
   - Determine day names from dates

4. **Message Generation**
   - Construct announcement header with city name
   - For each venue/match:
     - Add venue name
     - Add date with ordinal and day name
     - Add time range
     - Add player configuration (6v6, etc.)
   - Add separators between entries

5. **Output Display**
   - Show formatted message in web interface
   - Enable copy-to-clipboard functionality
   - Display any validation errors

### Key Functions

**scheduler.py:**
- `HOFScheduler.load_excel()` - Loads and validates Excel file
- `HOFScheduler._validate_data()` - Validates each row of data
- `HOFScheduler.get_ordinal_suffix()` - Generates ordinal suffixes (st, nd, rd, th)
- `HOFScheduler.format_time()` - Formats time with smart AM/PM handling
- `HOFScheduler.generate_announcement()` - Creates the final message
- `process_schedule_file()` - Main processing function

**app.py:**
- `initialize_session_state()` - Sets up Streamlit session variables
- `reset_app()` - Clears all data for fresh start
- `main()` - Main application loop and UI rendering

### Time Formatting Logic

The application intelligently formats times:

**Input (24-hour):** 18:00
**Output:** 6 PM

**Input (24-hour):** 18:30
**Output:** 6:30 PM

**Input (24-hour):** 09:00
**Output:** 9 AM

**Rules:**
- Minutes are omitted if they are 00
- Automatically converts 24-hour to 12-hour format
- Correctly handles AM/PM designation

### Date Formatting Logic

**Examples:**
- 1st Saturday
- 2nd Sunday
- 3rd Monday
- 11th Tuesday (not 11st)
- 21st Wednesday (not 21th)

**Rules:**
- 1, 21, 31 → st
- 2, 22 → nd
- 3, 23 → rd
- 4-20, 24-30 → th

## 🐛 Troubleshooting

### Common Issues and Solutions

#### Issue: "Missing required columns"
**Solution:** Ensure your Excel file has all required column names spelled exactly as shown in the [Excel File Format](#excel-file-format) section.

#### Issue: "playerCapacity must be an even number"
**Solution:** Player capacity must be divisible by 2 (e.g., 10, 12, 14, not 11, 13).

#### Issue: "endTime must be after startTime"
**Solution:** Check your date/time entries. The end time must be later than the start time.

#### Issue: "Invalid date format"
**Solution:** Ensure dates are in Excel date format or dd-mm-yyyy hh:mm format.

#### Issue: Application won't start
**Solution:** 
```bash
# Check if Streamlit is installed
pip list | grep streamlit

# Reinstall if needed
pip install --upgrade streamlit

# Try running again
streamlit run app.py
```

#### Issue: Excel file won't upload
**Solution:**
- Ensure file is .xlsx format (not .xls or .csv)
- Check file isn't corrupted
- Try saving a fresh copy of the Excel file

#### Issue: Copy button doesn't work
**Solution:**
- Use the "View Raw Text" expander
- Manually select and copy the text
- Try a different browser (Chrome/Firefox recommended)

### Getting Help

If you encounter issues:

1. Check the error message displayed in the app
2. Verify your Excel file format matches requirements
3. Review the [Data Validation Rules](#data-validation-rules)
4. Check console output for detailed error messages

## 📁 Project Structure

```
hof-scheduler/
│
├── app.py                 # Streamlit web application (frontend)
│   ├── UI components
│   ├── File upload handling
│   ├── Display logic
│   └── Session management
│
├── scheduler.py           # Core business logic (backend)
│   ├── HOFScheduler class
│   ├── Data validation
│   ├── Message generation
│   └── Utility functions
│
├── requirements.txt       # Python dependencies
│   ├── pandas
│   ├── openpyxl
│   └── streamlit
│
└── README.md             # This file
```

## 🔒 Data Privacy

- **No data is stored**: All processing happens in memory
- **Temporary files**: Excel files are temporarily saved during processing and immediately deleted
- **Session-based**: All data is cleared when you close the browser tab

## 🚀 Performance

- **Fast processing**: Handles files with 100+ rows in under 2 seconds
- **Memory efficient**: Processes data in chunks to minimize memory usage
- **Optimized validation**: Early exit on errors to save processing time

## 📝 License

This project is provided as-is for use by Humans of Football.

## 🤝 Support

For support, please contact the development team or refer to this README.

---

**Version:** 1.0  
**Last Updated:** February 2026  
**Maintained by:** HOF Development Team
