# 📖 HOF Scheduler - User Manual

## Table of Contents
1. [Introduction](#introduction)
2. [Installation Guide](#installation-guide)
3. [Using the Application](#using-the-application)
4. [Excel File Requirements](#excel-file-requirements)
5. [Troubleshooting](#troubleshooting)
6. [FAQs](#faqs)

---

## 🎯 Introduction

### What is HOF Scheduler?
HOF Scheduler is a web-based tool that automatically generates formatted match announcements from your Excel schedule files. Simply upload your match data, and get a perfectly formatted announcement ready to share!

### Key Features
- ✨ **Automatic Formatting** - Converts raw data into polished announcements
- 🕐 **Smart Time Handling** - Converts 24-hour to 12-hour format automatically
- 📅 **Date Intelligence** - Adds correct ordinal suffixes (1st, 2nd, 3rd, etc.)
- ✅ **Data Validation** - Catches errors before processing
- 📋 **Easy Copying** - Multiple ways to copy your announcement
- 🔄 **Quick Reset** - Start fresh anytime with one click

---

## 💻 Installation Guide

### Prerequisites
Before installing, make sure you have:
- **Computer**: Windows, Mac, or Linux
- **Python**: Version 3.8 or newer ([Download here](https://www.python.org/downloads/))
- **Internet**: For downloading packages

### Step-by-Step Installation

#### Step 1: Download the Project
1. Download all project files to a folder on your computer
2. Remember where you saved them!

#### Step 2: Open Terminal/Command Prompt

**Windows:**
- Press `Win + R`
- Type `cmd` and press Enter

**Mac:**
- Press `Cmd + Space`
- Type `terminal` and press Enter

**Linux:**
- Press `Ctrl + Alt + T`

#### Step 3: Navigate to Project Folder
```bash
cd C:\path\to\hof-scheduler    # Windows
cd /path/to/hof-scheduler      # Mac/Linux
```

#### Step 4: Create Virtual Environment
```bash
python -m venv venv
```
⏳ This takes 30-60 seconds

#### Step 5: Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

✅ You should see `(venv)` at the start of your command line

#### Step 6: Install Required Packages
```bash
pip install -r requirements.txt
```
⏳ This takes 1-2 minutes

#### Step 7: Verify Installation (Optional)
```bash
python test_scheduler.py
```

✅ **Installation Complete!**

---

## 🚀 Using the Application

### Starting the App

1. **Open Terminal** (see Installation Guide above)

2. **Navigate to Project Folder**
   ```bash
   cd path/to/hof-scheduler
   ```

3. **Activate Virtual Environment**
   ```bash
   venv\Scripts\activate    # Windows
   source venv/bin/activate # Mac/Linux
   ```

4. **Start the App**
   ```bash
   streamlit run app.py
   ```

5. **Access the App**
   - Opens automatically in your browser
   - Or go to: `http://localhost:8501`

### Using the Interface

#### 1. Upload Your File
```
┌─────────────────────────────────┐
│  📁 Choose an Excel file        │
│                                 │
│  [Click to browse...]           │
│                                 │
└─────────────────────────────────┘
```
- Click the upload button
- Select your `.xlsx` file
- Wait for it to upload (shows progress)

#### 2. Generate Announcement
```
┌──────────────────┐  ┌──────────────────┐
│ 🚀 Generate      │  │ 🔄 Reset         │
│    Announcement  │  │                  │
└──────────────────┘  └──────────────────┘
```
- Click "Generate Announcement"
- Wait 1-2 seconds for processing
- See your result below!

#### 3. Copy Your Announcement

**Option A: Text Area**
- Click inside the text area
- Press `Ctrl+A` (or `Cmd+A` on Mac) to select all
- Press `Ctrl+C` (or `Cmd+C` on Mac) to copy

**Option B: Raw Text Expander**
- Click "View Raw Text"
- Click the copy icon in the top-right
- Text is copied!

**Option C: Download File**
- Click "Download as Text File"
- Save to your computer
- Open and copy from there

#### 4. Share Your Announcement
- Open WhatsApp, Telegram, or any messaging app
- Press `Ctrl+V` (or `Cmd+V` on Mac) to paste
- Send! 🎉

### Stopping the App
- In your terminal, press `Ctrl+C`
- Type `deactivate` to exit virtual environment

---

## 📊 Excel File Requirements

### Required Columns

| Column Name      | Type     | Example              | Notes                        |
|------------------|----------|----------------------|------------------------------|
| cityName         | Text     | Bengaluru            | City where match is held     |
| venueName        | Text     | South United FC      | Name of the venue            |
| matchTypeName    | Text     | HOF Play             | Type of match                |
| startTime        | DateTime | 15-02-2026 18:00     | Match start (24hr format)    |
| endTime          | DateTime | 15-02-2026 20:00     | Match end (24hr format)      |
| playerCapacity   | Number   | 12                   | Must be EVEN number          |
| slotPrice        | Number   | 250                  | Regular price                |
| offerPrice       | Number   | 200                  | Discounted price             |

### Important Rules

✅ **DO:**
- Use exact column names (case-sensitive!)
- Ensure playerCapacity is an even number (12, 14, 16, etc.)
- Use proper date/time format in Excel
- Fill in all required fields
- Make sure endTime is after startTime

❌ **DON'T:**
- Leave required fields empty
- Use odd numbers for playerCapacity
- Mix up column names
- Use text instead of dates in time fields
- Put endTime before startTime

### Date/Time Format

**Excel Date Format:**
```
15-02-2026 18:00
│   │   │    │
│   │   │    └─ Time (24-hour format)
│   │   └────── Year
│   └────────── Month
└────────────── Day
```

**What You Get:**
```
15th Sunday | 6 PM–8 PM
│    │       │    │
│    │       │    └─ End time (12-hour format)
│    │       └────── Start time (12-hour format)
│    └────────────── Day name (automatic)
└─────────────────── Day with ordinal (automatic)
```

---

## 🔧 Troubleshooting

### Common Errors and Solutions

#### Error: "Missing required columns"
**Problem:** Your Excel file doesn't have all required columns

**Solution:**
1. Open your Excel file
2. Check column names match exactly (case-sensitive):
   - cityName (not CityName or city_name)
   - venueName (not VenueName or venue_name)
   - etc.
3. Ensure you have all 8 required columns

---

#### Error: "playerCapacity must be an even number"
**Problem:** You have odd numbers like 11, 13, 15

**Solution:**
1. Open your Excel file
2. Find the playerCapacity column
3. Change odd numbers to even numbers:
   - 11 → 12
   - 13 → 14
   - 15 → 16

---

#### Error: "endTime must be after startTime"
**Problem:** Your end time is before or same as start time

**Solution:**
1. Check the times in your Excel file
2. Make sure endTime is later than startTime
3. Example:
   - startTime: 18:00 ✅
   - endTime: 20:00 ✅
   - (Not 17:00 ❌)

---

#### Error: "Invalid date format"
**Problem:** Excel doesn't recognize your date/time

**Solution:**
1. In Excel, select the startTime and endTime columns
2. Right-click → Format Cells
3. Choose "Date" or "Custom"
4. Use format: `dd-mm-yyyy hh:mm`

---

#### Application Won't Start
**Problem:** Error when running `streamlit run app.py`

**Solution:**
1. Make sure virtual environment is activated:
   - You should see `(venv)` in terminal
2. Reinstall packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Try running test:
   ```bash
   python test_scheduler.py
   ```

---

#### File Upload Fails
**Problem:** Can't upload your Excel file

**Solution:**
1. Check file format is `.xlsx` (not .xls or .csv)
2. Try saving a fresh copy of your Excel file
3. Ensure file isn't open in Excel while uploading
4. Check file isn't corrupted

---

### Getting More Help

If you're still stuck:

1. **Check the Error Message**
   - Read it carefully
   - It tells you exactly what's wrong

2. **Run Test Script**
   ```bash
   python test_scheduler.py
   ```
   - Checks if everything is installed correctly

3. **Check Sample File**
   - Look at `sample_schedule.xlsx`
   - Compare with your file
   - Copy the structure

4. **Start Fresh**
   - Click "Reset" in the app
   - Try with the sample file first
   - Then try your file again

---

## ❓ FAQs

### General Questions

**Q: Do I need internet to use this?**
A: Only for initial installation. Once installed, it works offline.

**Q: Does this work on mobile phones?**
A: No, it needs to run on a computer with Python installed.

**Q: Is my data stored anywhere?**
A: No! Everything is processed locally on your computer. Nothing is saved or sent online.

**Q: Can I use this for multiple cities?**
A: Yes! Each row can have a different city. The app groups them automatically.

### Excel Questions

**Q: Can I use .xls or .csv files?**
A: No, only .xlsx files are supported. Save your file as Excel Workbook (.xlsx).

**Q: What if I have extra columns?**
A: That's fine! The app only uses the required columns and ignores others.

**Q: Can I have multiple rows with the same venue?**
A: Yes! Each row is processed separately.

**Q: What's the maximum number of rows I can have?**
A: The app can handle hundreds of rows. Typical files (20-100 rows) process in 1-2 seconds.

### Time Format Questions

**Q: Can I use 12-hour format in Excel?**
A: It's better to use 24-hour format. The app converts it automatically.

**Q: What if my match starts at midnight?**
A: Use 00:00 for midnight. The app will convert it to "12 AM".

**Q: Can I have matches that span multiple days?**
A: Each match should be within the same day. For overnight matches, use endTime like 23:59.

### Output Questions

**Q: Can I edit the generated message?**
A: Yes! After copying, you can paste and edit in any text editor.

**Q: Can I change the announcement format?**
A: Not in the app, but you can modify the `scheduler.py` file if you know Python.

**Q: What if I made a mistake after generating?**
A: Click "Reset", fix your Excel file, and generate again!

**Q: Can I save announcements for later?**
A: Yes! Use the "Download as Text File" button to save it.

### Technical Questions

**Q: What Python version do I need?**
A: Python 3.8 or newer. Check with: `python --version`

**Q: Can I run this on a server?**
A: Yes, but this guide is for local use. Server deployment requires different setup.

**Q: Will this work on my company computer?**
A: Depends on your company's security settings. You might need admin permission to install Python.

**Q: Can multiple people use this at once?**
A: Each person needs their own installation. The app runs locally.

---

## 🎓 Quick Reference

### Command Cheat Sheet

```bash
# Start the app
cd path/to/hof-scheduler
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
streamlit run app.py

# Stop the app
Ctrl + C

# Test installation
python test_scheduler.py

# Update packages
pip install --upgrade -r requirements.txt

# Deactivate virtual environment
deactivate
```

### File Checklist

Before uploading your Excel file, verify:
- [ ] File is .xlsx format
- [ ] All 8 required columns are present
- [ ] Column names are spelled correctly
- [ ] All required fields have values
- [ ] playerCapacity values are even numbers
- [ ] Date/time formats are correct
- [ ] endTime is after startTime for each row

---

## 📞 Support

Need help? Here's what to do:

1. **Check this manual** - Most answers are here!
2. **Run test script** - `python test_scheduler.py`
3. **Check error messages** - They tell you exactly what's wrong
4. **Use sample file** - Compare with `sample_schedule.xlsx`
5. **Contact support** - Reach out to your technical team

---

**Version:** 1.0  
**Last Updated:** February 2026  
**Created for:** Humans of Football
