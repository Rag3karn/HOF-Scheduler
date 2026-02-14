# 🚀 HOF Scheduler - Quick Start Guide

## ⚡ 5-Minute Setup

### 1️⃣ Install Python
- Download Python 3.8+ from [python.org](https://www.python.org/downloads/)
- During installation, check "Add Python to PATH"

### 2️⃣ Setup Project
```bash
# Navigate to project folder
cd path/to/hof-scheduler

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ Run Application
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

---

## 📋 Using the App

1. **Upload** your Excel file (must be .xlsx format)
2. **Click** "Generate Announcement"
3. **Copy** the generated message
4. **Paste** into WhatsApp, Telegram, or any messaging app

---

## ✅ Checklist for Excel File

Make sure your Excel file has these columns:
- ✓ cityName
- ✓ venueName
- ✓ matchTypeName
- ✓ startTime (date/time format)
- ✓ endTime (date/time format)
- ✓ playerCapacity (even number)
- ✓ slotPrice
- ✓ offerPrice

---

## ❓ Common Issues

**Problem:** "Module not found"
**Solution:** Make sure you activated the virtual environment and ran `pip install -r requirements.txt`

**Problem:** "Missing required columns"
**Solution:** Check your Excel file has all required column names (case-sensitive)

**Problem:** "playerCapacity must be even"
**Solution:** Change odd numbers (11, 13) to even numbers (12, 14)

---

## 🆘 Need Help?

1. Check the full [README.md](README.md) for detailed documentation
2. Run `python test_scheduler.py` to verify your setup
3. Check error messages in the app for specific issues

---

## 📝 Example Excel Format

| cityName  | venueName    | startTime        | endTime          | playerCapacity | slotPrice | offerPrice |
|-----------|--------------|------------------|------------------|----------------|-----------|------------|
| Bengaluru | Test Turf    | 15-02-2026 18:00 | 15-02-2026 20:00 | 12             | 250       | 200        |
| Bengaluru | Another Turf | 16-02-2026 19:00 | 16-02-2026 21:00 | 14             | 300       | 250        |

---

**Ready to go!** 🎉
