import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # Add this import
from utils.webdriver_factory import WebDriverFactory
from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_e2e_checkout_workflow():
    driver = WebDriverFactory.get_driver("chrome")
    driver.maximize_window()

    try:
        # 1. Login
        driver.get("http://localhost:8000/login.html")
        wait = WebDriverWait(driver, 10)

        login_pg = LoginPage(driver)
        login_pg.perform_login("testuser", "Pass123!")

        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present()).accept()
        except:
            pass

            # 2. Add Item on index.html
        driver.get("http://localhost:8000/index.html")
        product_pg = ProductPage(driver)

        btn_element = wait.until(EC.presence_of_element_located(product_pg.ADD_TO_CART_BTN))
        driver.execute_script("arguments[0].click();", btn_element)
        print("Item added to cart.")

        # 3. GO TO CART PAGE (This was the missing link!)
        driver.get("http://localhost:8000/cart.html")
        wait.until(EC.url_contains("cart.html"))
        print("Navigated to Cart page.")

        # 4. Action: Checkout on cart.html
        checkout_btn = wait.until(EC.visibility_of_element_located(product_pg.CHECKOUT_BTN))
        driver.execute_script("arguments[0].scrollIntoView(true);", checkout_btn)
        driver.execute_script("arguments[0].click();", checkout_btn)
        print("Successfully clicked Proceed to Checkout")

        # 5. Verify Final Checkout Page
        wait.until(EC.url_contains("checkout.html"))
        assert "checkout" in driver.current_url.lower()
        print("E2E Workflow: SUCCESS")

    finally:
        driver.quit()