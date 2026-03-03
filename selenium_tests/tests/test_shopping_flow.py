# -----------------------------------------------------
# Assignment: Final Project
# Written by: Prudhvi Teja Reddy Kandula (ID: 5805128)
# Description: Final E2E Workflow with Debugging and Path Fallbacks.
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
        # 1. SERVER CHECK & LOGIN
        # We try the root first, then a common subdirectory as a fallback
        paths_to_try = ["/login.html", "/templates/login.html"]
        found = False
        
        for path in paths_to_try:
            driver.get(f"{base_url}{path}")
            try:
                # Search for any input field to prove the page loaded
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "input")))
                found = True
                break
            except:
                continue
        
        if not found:
            print("CRITICAL: Could not find login page. Current Page Source:")
            print(driver.page_source[:500]) # Log first 500 chars to see the error
            raise Exception("Login page not reachable at expected paths.")

        login_pg = LoginPage(driver)
        
        # Perform Login
        wait.until(EC.visibility_of_element_located(login_pg.USERNAME))
        login_pg.perform_login("testuser", "Pass123!")

        # Handle alert
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present()).accept()
        except:
            pass

        # 2. ADD TO CART
        # Navigate to index (use the same path logic if necessary)
        target_index = driver.current_url.replace("login.html", "index.html")
        driver.get(target_index)
        
        product_pg = ProductPage(driver)
        btn = wait.until(EC.element_to_be_clickable(product_pg.ADD_TO_CART_BTN))
        driver.execute_script("arguments[0].click();", btn)

        # 3. CART & CHECKOUT
        target_cart = driver.current_url.replace("index.html", "cart.html")
        driver.get(target_cart)
        
        checkout_btn = wait.until(EC.element_to_be_clickable(product_pg.CHECKOUT_BTN))
        driver.execute_script("arguments[0].click();", checkout_btn)

        # 4. VERIFICATION
        wait.until(EC.url_contains("checkout.html"))
        assert "checkout" in driver.current_url.lower()
        print("E2E Workflow: SUCCESS")

    except Exception as e:
        print(f"E2E Workflow: FAILED - {str(e)}")
        driver.save_screenshot("e2e_final_debug.png")
        raise e
    finally:
        driver.quit()
