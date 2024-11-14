from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Set up the Selenium WebDriver with options if needed
options = Options()
options.add_argument("--headless")  # Run in headless mode, if you don't need to see the browser
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=options)

# Open the event page
url = "https://www.meetup.com/en-AU/it-social-australia-data-technology-cybersecurity/events/304118505/"
driver.get(url)

# Allow time for the page to load JavaScript content
time.sleep(5)  # Adjust if necessary based on page load speed

# Parse the fully loaded HTML with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Close the browser after scraping
driver.quit()

# Find the attendee count within the specific div and h2
attendees_div = soup.find("div", id="attendees")
if attendees_div:
    attendee_header = attendees_div.find("h2", class_="text-xl font-semibold")

    if attendee_header:
        # Extract the attendee count from the text, e.g., "Attendees (4)"
        attendee_count_text = attendee_header.get_text(strip=True)
        count = int(attendee_count_text.split("(")[-1].split(")")[0])
        print("Attendee Count:", count - 3)
    else:
        print("Attendee header not found within the attendees div.")
else:
    print("Could not find the attendees div.")
