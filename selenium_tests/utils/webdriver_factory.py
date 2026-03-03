# -----------------------------------------------------
# Assignment: Final Project
# Written by: Prudhvi Teja Reddy Kandula (ID: 5805128)
# Description: Factory class to initialize WebDriver for cross-browser testing.
# Updated for GitHub Actions (Headless Mode Support).
# -----------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class WebDriverFactory:
    @staticmethod
    def get_driver(browser="chrome"):
        """
        Returns a WebDriver instance based on the requested browser.
        Configured with Headless options for CI/CD compatibility.
        """
        browser_type = browser.lower()

        if browser_type == "chrome":
            options = ChromeOptions()
            # These arguments are required for GitHub Actions servers
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
            return webdriver.Chrome(options=options)

        elif browser_type == "firefox":
            options = FirefoxOptions()
            options.add_argument("--headless")
            return webdriver.Firefox(options=options)

        else:
            print(f"Browser '{browser}' not supported. Defaulting to Chrome Headless.")
            options = ChromeOptions()
            options.add_argument("--headless=new")
            return webdriver.Chrome(options=options)
