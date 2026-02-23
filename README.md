# Medicine Price Comparison Web Application

A Flask-based web application that compares medicine prices across Apollo Pharmacy, PharmEasy, and NetMeds using Selenium web scraping.

## Features

- 🔍 Search medicine prices across 3 major pharmacies
- 💰 Automatic price comparison with cheapest price highlighting
- 🎨 Clean, responsive Bootstrap UI
- 🚀 Auto-opens browser on startup
- ⚡ Real-time scraping with loading indicators
- 🛡️ Exception handling for failed scrapes

## Project Structure

```
project/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Frontend HTML template
├── static/
│   └── style.css         # Custom CSS styles
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Prerequisites

- Python 3.8 or higher
- Google Chrome browser (required for Selenium)
- Internet connection

## Installation Guide

### Step 1: Install Python

1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, check "Add Python to PATH"
3. Verify installation:
   ```bash
   python --version
   ```

### Step 2: Create Virtual Environment

Open terminal/command prompt in the project directory:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- SeleniumBase (web scraping)
- Werkzeug (Flask utilities)

### Step 4: Run the Application

```bash
python app.py
```

The application will:
1. Start Flask server on `http://127.0.0.1:5050`
2. Automatically open your default browser
3. Display the medicine search interface

## How to Use

1. Enter medicine name in the search box (e.g., "Paracetamol", "Dolo 650")
2. Click "Search" button
3. Wait 20-30 seconds while prices are scraped
4. View results in a table with:
   - Pharmacy name
   - Price (or "Price not found")
   - Link to product page
   - Cheapest price highlighted in green

## Troubleshooting

### Issue: "Module not found" error

**Solution:**
```bash
# Make sure virtual environment is activated
# Then reinstall dependencies
pip install -r requirements.txt
```

### Issue: Browser doesn't open automatically

**Solution:**
- Manually open browser and go to `http://127.0.0.1:5050`
- Check if port 5000 is already in use

### Issue: "Chrome driver not found"

**Solution:**
- SeleniumBase automatically downloads Chrome driver
- Ensure Google Chrome is installed
- Run: `pip install --upgrade seleniumbase`

### Issue: Prices not loading / "Price not found"

**Possible causes:**
- Website structure changed (selectors need updating)
- Internet connection issues
- Website blocking automated access
- Medicine name not found on pharmacy site

**Solution:**
- Check internet connection
- Try different medicine name
- Wait and retry (some sites have rate limiting)

### Issue: Port 5000 already in use

**Solution:**
```bash
# Change port in app.py (last line):
app.run(debug=True, port=5001, use_reloader=False)
```

### Issue: Selenium timeout errors

**Solution:**
- Increase wait time in `app.py` (line 38):
  ```python
  time.sleep(10)  # Increase from 7 to 10 seconds
  ```

## Configuration

### Change Port Number

Edit `app.py` (last line):
```python
app.run(debug=True, port=YOUR_PORT, use_reloader=False)
```

### Adjust Scraping Wait Time

Edit `app.py` (line 38):
```python
time.sleep(7)  # Increase if prices not loading
```

### Disable Auto Browser Open

Comment out in `app.py`:
```python
# Timer(1.5, open_browser).start()
```

## Technical Details

### Technologies Used
- **Backend:** Flask (Python web framework)
- **Scraping:** SeleniumBase (undetectable Chrome automation)
- **Frontend:** Bootstrap 5, Font Awesome icons
- **Styling:** Custom CSS with gradient design

### Scraping Logic
- Uses undetectable Chrome mode (`uc=True`) to bypass bot detection
- Site-specific CSS selectors for each pharmacy
- 7-second wait for dynamic content loading
- Regex-based price extraction and cleaning

### API Endpoints
- `GET /` - Home page
- `POST /search` - Search medicine prices (JSON)

## Security Notes

- Application runs in debug mode (disable for production)
- No authentication required (add if deploying publicly)
- Scraping respects website terms of service

## Future Enhancements

- [ ] Add more pharmacy sites
- [ ] Save search history
- [ ] Export results to CSV/PDF
- [ ] Price tracking over time
- [ ] Email alerts for price drops
- [ ] User authentication
- [ ] Database integration

## License

This project is for educational purposes only. Respect website terms of service when scraping.

## Support

For issues or questions:
1. Check troubleshooting section above
2. Verify all dependencies are installed
3. Ensure Chrome browser is up to date
4. Check internet connection

## Credits

Built with Flask, SeleniumBase, and Bootstrap.
 
