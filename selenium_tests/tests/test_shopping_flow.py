# -----------------------------------------------------
# Assignment: Final Project
# Written by: Prudhvi Teja Reddy Kandula (ID: 5805128)
# Description: E2E Workflow - Enhanced Server Sync & Discovery.
# -----------------------------------------------------

import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_tests.utils.webdriver_factory import WebDriverFactory
from selenium_tests.pages.login_page import LoginPage

def test_e2e_checkout_workflow():
    driver = WebDriverFactory.get_driver("chrome")
    driver.set_window_size(1920, 1080)
    wait = WebDriverWait(driver, 15)
    
    # Give the background server a moment to stabilize
    time.sleep(5)
    
    base_url = "http://localhost:8000"
    # Try the most likely paths based on your previous successful logs
    paths_to_try = ["/website/", "/", "/templates/", "/src/"]
    correct_url = None

    try:
        # 1. ROBUST PATH DISCOVERY
        for path in paths_to_try:
            target = f"{base_url}{path}login.html".replace("//login", "/login")
            driver.get(target)
            print(f"DEBUG: Checking {target}")
            
            # Look for ANY input field to confirm we aren't on a 404 page
            inputs = driver.find_elements(By.TAG_NAME, "input")
            if len(inputs) > 0:
                correct_url = f"{base_url}{path}".replace("//", "/")
                # Fix protocol after replace
                if "http:/" in correct_url and "http://" not in correct_url:
                    correct_url = correct_url.replace("http:/", "http://")
                print(f"DEBUG: Found valid login at {target}")
                break

        if not correct_url:
            # Fallback: Just try to find the login button by text on whatever page we are on
            print("DEBUG: Specific path failed. Searching for login components on current page.")
            if len(driver.find_elements(By.ID, "username")) == 0:
                 raise Exception(f"Could not locate login elements. Final URL attempted: {driver.current_url}")

        # 2. LOGIN
        # Using direct IDs to bypass potential PageObject locator mismatches
        wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("testuser")
        driver.find_element(By.ID, "password").send_keys("Pass123!")
        
        login_btn = driver.find_element(By.ID, "login-btn")
        driver.execute_script("arguments[0].click();", login_btn)

        # Handle Alert
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present()).accept()
        except:
            pass

        # 3. ADD TO CART
        driver.get(f"{correct_url}index.html")
        add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add')]")))
        driver.execute_script("arguments[0].click();", add_btn)
        
        # Handle "Added to Cart" Alert
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present()).accept()
        except:
            pass

        # 4. CHECKOUT
        driver.get(f"{correct_url}cart.html")
        checkout_xpath = "//*[contains(text(), 'Checkout')] | //button[@id='checkout-btn']"
        chk_btn = wait.until(EC.element_to_be_clickable((By.XPATH, checkout_xpath)))
        driver.execute_script("arguments[0].click();", chk_btn)

        # 5. VERIFY
        wait.until(EC.url_contains("checkout.html"))
        assert "checkout" in driver.current_url.lower()
        print("E2E Workflow: SUCCESS")

    except Exception as e:
        print(f"E2E Workflow: FAILED - {str(e)}")
        driver.save_screenshot("e2e_diagnostic_failure.png")
        raise e
    finally:
        driver.quit()
