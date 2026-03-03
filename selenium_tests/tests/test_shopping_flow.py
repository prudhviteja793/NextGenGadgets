# -----------------------------------------------------
# Assignment: Final Project
# Written by: Prudhvi Teja Reddy Kandula (ID: 5805128)
# Description: E2E Workflow - Alert Handling & Final Cleanup.
# -----------------------------------------------------

import pytest
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
        # 1. SETUP PATHS
        correct_base_url = f"{base_url}/website/"
        driver.get(f"{correct_base_url}login.html")
        
        # 2. LOGIN PHASE
        login_pg = LoginPage(driver)
        wait.until(EC.visibility_of_element_located(login_pg.USERNAME))
        login_pg.perform_login("testuser", "Pass123!")

        # Handle initial login alert if present
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present()).accept()
        except:
            pass

        # 3. ADD TO CART PHASE
        driver.get(f"{correct_base_url}index.html")
        wait.until(EC.url_contains("index.html"))
        
        # We'll use a direct XPath for maximum reliability in this E2E
        add_btn_xpath = "//button[contains(text(), 'Add to Cart') or contains(@onclick, 'addToCart')]"
        btn = wait.until(EC.presence_of_element_located((By.XPATH, add_btn_xpath)))
        
        driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        driver.execute_script("arguments[0].click();", btn)
        
        # --- CRITICAL FIX: Dismiss the "Added to Cart" Alert ---
        try:
            alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
            print(f"DEBUG: Dismissing alert: {alert.text}")
            alert.accept()
        except:
            print("DEBUG: No alert appeared after clicking Add to Cart.")

        # 4. CART & CHECKOUT
        driver.get(f"{correct_base_url}cart.html")
        wait.until(EC.url_contains("cart.html"))
        
        checkout_xpath = "//button[contains(text(), 'Checkout') or @id='checkout-button']"
        chk_btn = wait.until(EC.element_to_be_clickable((By.XPATH, checkout_xpath)))
        driver.execute_script("arguments[0].click();", chk_btn)

        # 5. FINAL VERIFICATION
        wait.until(EC.url_contains("checkout.html"))
        assert "checkout" in driver.current_url.lower()
        print("E2E Workflow: SUCCESS")

    except Exception as e:
        print(f"E2E Workflow: FAILED at {driver.current_url}")
        print(f"Error Type: {type(e).__name__}")
        print(f"Error Message: {str(e)}")
        driver.save_screenshot("e2e_final_alert_fix.png")
        raise e
    finally:
        driver.quit()
