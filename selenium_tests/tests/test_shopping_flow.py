# -----------------------------------------------------
# Assignment: Final Project
# Written by: Prudhvi Teja Reddy Kandula (ID: 5805128)
# Description: E2E Workflow - Using robust CSS and JS-based discovery.
# -----------------------------------------------------

import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_tests.utils.webdriver_factory import WebDriverFactory

def test_e2e_checkout_workflow():
    driver = WebDriverFactory.get_driver("chrome")
    driver.set_window_size(1920, 1080)
    wait = WebDriverWait(driver, 20)
    
    try:
        # 1. NAVIGATION & SELECTOR DISCOVERY
        # We know from logs /website/ works
        base_url = "http://localhost:8000/website/"
        driver.get(f"{base_url}login.html")
        
        # Ensure the page is actually "ready"
        wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')

        # 2. LOGIN (Using very broad CSS selectors to avoid ID flakiness)
        user_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text'], #username")))
        pass_input = driver.find_element(By.CSS_SELECTOR, "input[type='password'], #password")
        
        user_input.clear()
        user_input.send_keys("testuser")
        pass_input.clear()
        pass_input.send_keys("Pass123!")
        
        login_btn = driver.find_element(By.CSS_SELECTOR, "button, input[type='submit'], #login-btn")
        driver.execute_script("arguments[0].click();", login_btn)

        # Handle Alert
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present()).accept()
        except:
            pass

        # 3. ADD TO CART
        driver.get(f"{base_url}index.html")
        # Find any button that looks like an "Add" button
        add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add')]")))
        driver.execute_script("arguments[0].click();", add_btn)
        
        # Handle "Added to Cart" Alert
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present()).accept()
        except:
            pass

        # 4. CHECKOUT
        driver.get(f"{base_url}cart.html")
        checkout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Checkout')]")))
        driver.execute_script("arguments[0].click();", checkout_btn)

        # 5. VERIFY
        wait.until(EC.url_contains("checkout.html"))
        assert "checkout" in driver.current_url.lower()
        print("E2E Workflow: SUCCESS")

    except Exception as e:
        print(f"E2E Workflow: FAILED - {str(e)}")
        driver.save_screenshot("e2e_ultimate_debug.png")
        # Print page source to see what Selenium is actually seeing
        print("PAGE SOURCE SNIPPET:", driver.page_source[:500])
        raise e
    finally:
        driver.quit()
