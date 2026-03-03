from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def setup_driver():
    chrome_options = Options()
    
    # REQUIRED FOR GITHUB ACTIONS (HEADLESS MODE)
    chrome_options.add_argument("--headless")           # No GUI window
    chrome_options.add_argument("--no-sandbox")         # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage") # Fixes memory issues in Docker
    
    driver = webdriver.Chrome(options=chrome_options)
    return driver
