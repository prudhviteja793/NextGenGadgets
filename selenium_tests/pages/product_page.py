# ----------------------------------------------------- 
# Assignment: Final Project
# Written by: Prudhvi Teja Reddy Kandula (ID: 5805128)
# Description: Page Object for Product and Cart interactions.
# -----------------------------------------------------

from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".modal-add-to-cart-btn.cta-button")
    CHECKOUT_BTN = (By.CSS_SELECTOR, ".cta-button.checkout-button")

    def add_first_item_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BTN)