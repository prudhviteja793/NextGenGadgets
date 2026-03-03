# -----------------------------------------------------
# Assignment: Final Project
# Written by: Prudhvi Teja Reddy Kandula (ID: 5805128)
# Description: E2E Workflow - Dynamic Pathing + Class-Based Locators.
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

    # Possible subdirectories
    subfolders = ["website", "templates", "src", ""]
    correct_base = None

    try:
        # 1. DYNAMIC PATH DISCOVERY
        for folder in subfolders:
            path_part = f"/{folder}/".replace("//", "/")
            test_url = f"{base_url}{path_part}login.html"
            driver.get(test_url)
            
            # Check if the login input exists on this path
            if len(driver.find_elements(By.ID, "username")) > 0 or \
               len(driver.find_elements(By.NAME, "username")) > 0:
                correct_base = f"{base_url}{path_part}"
                print(f"DEBUG: Found correct base URL: {correct_base}")
                break
        
        if not correct_base:
            raise Exception("Could not find login.html with a valid username field.")

        # 2. LOGIN PHASE (Using Page Object)
        login_pg = LoginPage(driver)
        # We wait for the specific locator defined in your LoginPage
        wait.until(EC.presence_of_element_located(login_pg.USERNAME))
        login_pg.perform_login("testuser", "Pass123!")

        # Handle potential login alert
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present()).accept()
        except:
            pass

        # 3. ADD TO CART PHASE
        driver.get(f"{correct_base}index.html")
        wait.until(EC.url_contains("index.html"))
        
        # Use a flexible selector for the Add button
        add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add')]")))
        driver.execute_script("arguments[0].click();", add_btn)
        
        # Handle the "Added to Cart" alert
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present()).accept()
        except:
            pass

        # 4. CART & CHECKOUT PHASE
        driver.get(f"{correct_base}cart.html")
        wait.until(EC.url_contains("cart.html"))
        
        # Try finding the checkout button by text or ID
        checkout_xpath = "//button[contains(text(), 'Checkout')] | //a[contains(text(), 'Checkout')] | //*[@id='checkout-btn']"
        chk_btn = wait.until(EC.element_to_be_clickable((By.XPATH, checkout_xpath)))
        driver.execute_script("arguments[0].click();", chk_btn)

        # 5. FINAL VERIFICATION
        wait.until(EC.url_contains("checkout.html"))
        assert "checkout" in driver.current_url.lower()
        print("E2E Workflow: SUCCESS")

    except Exception as e:
        print(f"E2E Workflow: FAILED at {driver.current_url} - {str(e)}")
        driver.save_screenshot("e2e_final_debug.png")
        raise e
    finally:
        driver.quit()
