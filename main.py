import re
import urllib.request
import time

# Get URL input from the user
user_input_url = input("Enter the URL to scrape: ")

# URL to scrape
url_to_scrape = f"https://sitechecker.pro/app/main/seo-report?k=0efbd6f4fb27b45d&pageUrl={user_input_url}"

# Set the User-Agent header to mimic a different browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

try:
    # Create a request with the modified headers
    request = urllib.request.Request(url_to_scrape, headers=headers)

    # Request the URL and wait for 5 seconds
    with urllib.request.urlopen(request) as response:
        time.sleep(5)  # Wait for 5 seconds to let the page load
        html_content = response.read().decode('utf-8')

    # Use regex to find the content of the specified <div> element
    div_pattern = r'<div\s+_ngcontent-qwt-c164=""\s+class="seo-report-info-score-block-value">([^<]+)</div>'
    match = re.search(div_pattern, html_content)

    # Print the content if found, else print an error message
    if match:
        content = match.group(1)
        print(f"Content of the specified <div> element: {content}")
    else:
        print("Specified <div> element not found in the HTML content.")

except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e}")
