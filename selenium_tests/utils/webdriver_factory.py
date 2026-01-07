<<<<<<< HEAD
from selenium import webdriver

class WebDriverFactory:
    @staticmethod
    def get_driver(browser="chrome"):
        if browser.lower() == "chrome":
            return webdriver.Chrome()
        elif browser.lower() == "firefox":
            return webdriver.Firefox()
=======
from selenium import webdriver

class WebDriverFactory:
    @staticmethod
    def get_driver(browser="chrome"):
        if browser.lower() == "chrome":
            return webdriver.Chrome()
        elif browser.lower() == "firefox":
            return webdriver.Firefox()
>>>>>>> 6c46170 (Syncing local files with repository)
        return webdriver.Chrome()