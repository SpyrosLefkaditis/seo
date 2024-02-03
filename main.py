import urllib.request
import time

# URL to scrape
url_to_scrape = "https://sitechecker.pro/app/main/seo-report?k=0efbd6f4fb27b45d&pageUrl=https:%2F%2Fwww.orange.com%2F"

try:
    # Request the URL and wait for 5 seconds
    with urllib.request.urlopen(url_to_scrape) as response:
        time.sleep(5)  # Wait for 5 seconds to let the page load
        html_content = response.read().decode('utf-8')

    print("Successfully accessed the website.")

except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e}")
