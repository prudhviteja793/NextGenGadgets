# -----------------------------------------------------
# Assignment: Final Project
# Written by: Prudhvi Teja Reddy Kandula (ID: 5805128)
# Description: Factory class to initialize WebDriver for cross-browser testing.
# This utility ensures the browser is correctly instantiated for all test suites.
# -----------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

class WebDriverFactory:
    @staticmethod
    def get_driver(browser="chrome"):
        """
        Returns a WebDriver instance based on the requested browser.
        Defaults to Chrome if the input is unrecognized.
        """
        browser_type = browser.lower()

        if browser_type == "chrome":
            return webdriver.Chrome()
        elif browser_type == "firefox":
            return webdriver.Firefox()
        else:
            print(f"Browser '{browser}' not supported. Defaulting to Chrome.")
            return webdriver.Chrome()