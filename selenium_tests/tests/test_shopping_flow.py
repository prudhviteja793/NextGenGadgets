# -----------------------------------------------------
# Assignment: Final Project
# Written by: Prudhvi Teja Reddy Kandula (ID: 5805128)
# Description: End-to-End (E2E) Checkout Workflow.
# This test simulates a user logging in, adding an item to the cart,
# navigating to the cart page, and proceeding to final checkout.
# -----------------------------------------------------

import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium_tests.utils.webdriver_factory import WebDriverFactory
from selenium_tests.pages.login_page import LoginPage
from selenium_tests.pages.product_page import ProductPage

def test_e2e_checkout_workflow():
    """
    Validates the full shopping journey from Login to Checkout.
    Fulfills the 'E2E Workflow' requirement (40% Grade section).
    """
    driver = WebDriverFactory.get_driver("chrome")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Login Phase (Updated from port 8000 to 5500)
        driver.get("http://127.0.0.1:8000/login.html")
        login_pg = LoginPage(driver)

        # Ensure we use the correct IDs from your current app.py logic
        login_pg.perform_login("testuser", "Pass123!")

        # Handle alert if it appears
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present()).accept()
        except:
            pass

        # 2. Add Item Phase (Updated to port 5500)
        driver.get("http://127.0.0.1:8000/index.html")
        product_pg = ProductPage(driver)

        # Use JS click to ensure it hits the button even if overlapped
        btn_element = wait.until(EC.presence_of_element_located(product_pg.ADD_TO_CART_BTN))
        driver.execute_script("arguments[0].click();", btn_element)
        print("Step 2: Item added to cart.")

        # 3. Navigation to Cart
        driver.get("http://127.0.0.1:8000/cart.html")
        wait.until(EC.url_contains("cart.html"))

        # 4. Checkout Action
        checkout_btn = wait.until(EC.visibility_of_element_located(product_pg.CHECKOUT_BTN))
        driver.execute_script("arguments[0].click();", checkout_btn)

        # 5. Final Verification
        wait.until(EC.url_contains("checkout.html"))
        assert "checkout" in driver.current_url.lower()
        print("E2E Workflow: SUCCESS")

    except Exception as e:
        print(f"E2E Workflow: FAILED - {str(e)}")
        raise e
    finally:
        driver.quit()