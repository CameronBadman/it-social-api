# it-social-api

# Requirments 
to run the URL scraper you will need a web driver and to run pip install requirments.txt

for the web driver 
macos
- brew install chromedriver

Linux 
- yay -S chromedriver OR
- sudo pacman -Sy chromedriver

Windows
- https://developer.chrome.com/docs/chromedriver/downloads


# Run the functions 
to run the functions you input the driver like this 

 # Set up the Selenium WebDriver options
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=options)

and either input the file_path or the url for the specific function

- to get a single url input the url essentials for example and the driver; 
- https://www.meetup.com/en-AU/it-social-australia-data-technology-cybersecurity/events/304118507/
technically speaking any url would work, but I've found the essentials are the most stable 