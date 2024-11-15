import time
from bs4 import BeautifulSoup
import csv

def scrape_attendee_count(driver, url):
    """
    Navigates to the specified URL using the provided WebDriver and retrieves attendee count.
    :param driver: WebDriver instance - The Selenium WebDriver instance.
    :param url: str - URL of the page to scrape.
    :return: int - Attendee count, adjusted if necessary, or None if not found.
    """
    driver.get(url)
    time.sleep(5)  # Adjust as needed for page load

    # Parse the loaded page with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    attendees_div = soup.find("div", id="attendees")
    if attendees_div:
        attendee_header = attendees_div.find("h2", class_="text-xl font-semibold")
        if attendee_header:
            # Extract the attendee count from text, e.g., "Attendees (4)"
            attendee_count_text = attendee_header.get_text(strip=True)
            try:
                count = int(attendee_count_text.split("(")[-1].split(")")[0])
                return max(count - 3, 0)  # Adjust as necessary
            except (ValueError, IndexError):
                print(f"Error parsing attendee count for URL: {url}")
    return None  # Return None if the count is not found

def scrape_from_csv(driver, file_path):
    """
    Reads URLs from a CSV file and scrapes attendee counts using the provided WebDriver.
    :param driver: WebDriver instance - The Selenium WebDriver instance.
    :param file_path: str - Path to the CSV file with URLs.
    :return: dict - Dictionary mapping URLs to attendee counts.
    """
    results = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            url = row['url']
            count = scrape_attendee_count(driver, url)
            results[url] = count
            print(f"Attendee Count for {url}: {count if count is not None else 'Not Found'}")
    return results
