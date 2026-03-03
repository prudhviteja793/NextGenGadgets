# -----------------------------------------------------
# Assignment: Final Project
# Written by: Prudhvi Teja Reddy Kandula (ID: 5805128)
# Description: E2E Workflow with Server-Ready Retry Logic.
# -----------------------------------------------------

import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_tests.utils.webdriver_factory import WebDriverFactory
from selenium_tests.pages.login_page import LoginPage
from selenium_tests.pages.product_page import ProductPage

def test_e2e_checkout_workflow():
    driver = WebDriverFactory.get_driver("chrome")
    driver.set_window_size(1920, 1080)
    wait = WebDriverWait(driver, 20)
    base_url = "http://localhost:8000"

    try:
        # --- STABILITY FIX: SERVER WARM-UP LOOP ---
        # Try up to 3 times to get a valid page load
        for attempt in range(3):
            driver.get(f"{base_url}/login.html")
            try:
                # Use a short wait to check if the field is actually there
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
                break # Found it! exit the loop
            except:
                print(f"Attempt {attempt + 1}: Server not ready or blank page. Retrying...")
                time.sleep(2)
        
        login_pg = LoginPage(driver)
        
        # 1. Login Phase
        wait.until(EC.visibility_of_element_located(login_pg.USERNAME))
        login_pg.perform_login("testuser", "Pass123!")

        # Handle alert
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present()).accept()
        except:
            pass

        # 2. Add Item Phase
        wait.until(lambda d: "login.html" not in d.current_url)
        driver.get(f"{base_url}/index.html")
        product_pg = ProductPage(driver)

        btn_element = wait.until(EC.element_to_be_clickable(product_pg.ADD_TO_CART_BTN))
        driver.execute_script("arguments[0].click();", btn_element)

        # 3. Navigation to Cart
        driver.get(f"{base_url}/cart.html")
        wait.until(EC.url_contains("cart.html"))

        # 4. Checkout Action
        checkout_btn = wait.until(EC.element_to_be_clickable(product_pg.CHECKOUT_BTN))
        driver.execute_script("arguments[0].click();", checkout_btn)

        # 5. Final Verification
        wait.until(EC.url_contains("checkout.html"))
        assert "checkout" in driver.current_url.lower()
        print("E2E Workflow: SUCCESS")

    except Exception as e:
        print(f"E2E Workflow: FAILED - {str(e)}")
        driver.save_screenshot("final_debug_error.png")
        raise e
    finally:
        driver.quit()
