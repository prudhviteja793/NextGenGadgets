# ----------------------------------------------------- 
# Assignment: Final Project
# Written by: Prudhvi Teja Reddy Kandula (ID: 5805128)
# Description: Page Object for JWT-based Login functionality.
# -----------------------------------------------------

from selenium.webdriver.common.by import By
from selenium_tests.pages.base_page import BasePage

class LoginPage(BasePage):
    # Updated Locators to match your EXACT HTML IDs
    # Note: Using CSS selector for the button since it lacks an ID
    USERNAME = (By.ID, "login-email")
    PASSWORD = (By.ID, "login-password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button.cta-button")

    def perform_login(self, username, password):
        self.send_keys(self.USERNAME, username)
        self.send_keys(self.PASSWORD, password)
        # Using the method name from your base_page.py (usually click_element or click)
        # Based on your previous error, let's ensure it matches your base class
        self.click(self.LOGIN_BTN)