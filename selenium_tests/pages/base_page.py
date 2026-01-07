<<<<<<< HEAD
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.wait_for_element(locator).click()

    def send_keys(self, locator, text):
        self.wait_for_element(locator).clear()
=======
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.wait_for_element(locator).click()

    def send_keys(self, locator, text):
        self.wait_for_element(locator).clear()
>>>>>>> 6c46170 (Syncing local files with repository)
        self.wait_for_element(locator).send_keys(text)