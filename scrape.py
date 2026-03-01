from playwright.sync_api import sync_playwright

def main():
    total_sum = 0
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # Loop through seeds 70 to 79
        for seed in range(70, 80):
            url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
            page.goto(url)
            
            # Wait for the JavaScript table to fully render
            page.wait_for_selector("table")
            
            # Extract all text from every table cell (td and th)
            cell_texts = page.evaluate("() => Array.from(document.querySelectorAll('table td, table th')).map(el => el.innerText)")
            
            # Add numbers to the total sum
            for text in cell_texts:
                try:
                    total_sum += int(text.strip())
                except ValueError:
                    pass # Ignore text that isn't a number
                    
        browser.close()
        
    print(f"GRAND TOTAL: {total_sum}")

if __name__ == "__main__":
    main()
