from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".modal-add-to-cart-btn.cta-button")
    # Updated to match your cart.html exactly
    CHECKOUT_BTN = (By.CSS_SELECTOR, ".cta-button.checkout-button")

    def add_first_item_to_cart(self):
        pass

    def proceed_to_checkout(self):
        pass