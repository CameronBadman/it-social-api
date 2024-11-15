from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scraping import scrape_from_csv

if __name__ == "__main__":
    # Set up the Selenium WebDriver options
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=options)

    try:
        # Perform scraping
        file_path = 'urls.csv'  # Update this to the path of your CSV file
        attendee_results = scrape_from_csv(driver, file_path)
    finally:
        # Close the WebDriver after scraping is done
        driver.quit()
