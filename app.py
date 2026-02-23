from flask import Flask, render_template, request, jsonify
from seleniumbase import Driver
import time
import re
import webbrowser
from threading import Timer

app = Flask(__name__)

# Logic to clean price text like "₹150.00" or "150" into a number
def clean_price(text):
    if not text:
        return None
    nums = re.findall(r'\d+', text.replace(',', ''))
    return int(nums[0]) if nums else None

def scrape_medicine_prices(medicine):
    """
    Scrape medicine prices from Apollo, PharmEasy, and NetMeds
    Returns list of dictionaries with pharmacy, price, and link
    """
    # Initialize Driver in Undetectable (UC) mode to bypass bot-checks
    driver = Driver(uc=True)
    
    # Search Links
    links = {
        "Apollo": f"https://www.apollopharmacy.in/search-medicines/{medicine}",
        "PharmEasy": f"https://pharmeasy.in/search/all?name={medicine}",
        "NetMeds": f"https://www.netmeds.com/products?q={medicine}"
    }
    
    results = []
    
    for site, url in links.items():
        try:
            driver.get(url)
            time.sleep(7)  # Wait for prices to load dynamically
            
            # Site-specific selectors
            if site == "Apollo":
                price_text = driver.get_text("div[class*='aV_']")
            elif site == "PharmEasy":
                price_text = driver.get_text("div[class*='ProductCard_ourPrice']")
            elif site == "NetMeds":
                price_text = driver.get_text("span.priceDisplay")
            
            final_price = clean_price(price_text)
        except Exception as e:
            print(f"Error scraping {site}: {str(e)}")
            final_price = None
        
        results.append({
            "pharmacy": site,
            "price": final_price,
            "link": url
        })
    
    driver.quit()
    return results

@app.route('/')
def index():
    """Render the home page"""
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    """Handle medicine search request"""
    try:
        data = request.get_json()
        medicine = data.get('medicine', '').strip()
        
        if not medicine:
            return jsonify({'error': 'Please enter a medicine name'}), 400
        
        # Scrape prices
        results = scrape_medicine_prices(medicine)
        
        # Find cheapest price
        valid_prices = [r['price'] for r in results if r['price'] is not None]
        cheapest_price = min(valid_prices) if valid_prices else None
        
        # Add cheapest flag to results
        for result in results:
            result['is_cheapest'] = (result['price'] == cheapest_price and 
                                    result['price'] is not None and 
                                    cheapest_price is not None)
        
        return jsonify({
            'medicine': medicine.upper(),
            'results': results,
            'cheapest_price': cheapest_price
        })
    
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

def open_browser():
    """Open browser automatically after server starts"""
    webbrowser.open('http://127.0.0.1:5050/')

if __name__ == '__main__':
    # Open browser after 1.5 seconds
    Timer(1.5, open_browser).start()
    
    # Run Flask app
    app.run(debug=True, port=5050, use_reloader=False)
