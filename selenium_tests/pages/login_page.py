from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.ID, "login-email")
    PASSWORD = (By.ID, "login-password")
    LOGIN_BTN = (By.CLASS_NAME, "cta-button")

    def perform_login(self, email, password):
        self.send_keys(self.EMAIL, email)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_BTN) # This will now work!