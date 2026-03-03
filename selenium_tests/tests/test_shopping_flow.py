# -----------------------------------------------------
# Assignment: Final Project - E2E Shopping Flow
# Written by: Prudhvi Teja Reddy Kandula (ID: 5805128)
# -----------------------------------------------------

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_tests.utils.webdriver_factory import WebDriverFactory

def test_e2e_checkout_workflow():
    driver = WebDriverFactory.get_driver("chrome")
    driver.set_window_size(1920, 1080)
    wait = WebDriverWait(driver, 20)
    base_url = "http://localhost:8000/website/"

    try:
        # 1. LOGIN
        driver.get(f"{base_url}login.html")
        wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("testuser")
        driver.find_element(By.ID, "password").send_keys("Pass123!")
        driver.find_element(By.ID, "login-btn").click()
        try: WebDriverWait(driver, 3).until(EC.alert_is_present()).accept()
        except: pass

        # 2. ADD TO CART
        driver.get(f"{base_url}index.html")
        # Click the first 'Add to Cart' button found on the page
        add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add')]")))
        driver.execute_script("arguments[0].click();", add_btn)
        
        # Handle the confirmation alert (Essential to clear the driver state)
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present()).accept()
            print("DEBUG: Add-to-cart alert dismissed.")
        except:
            print("DEBUG: No alert found after clicking add-to-cart.")

        # 3. CHECKOUT
        driver.get(f"{base_url}cart.html")
        wait.until(EC.url_contains("cart.html"))
        
        # --- DEBUG: HELP US FIND THE BUTTON ---
        buttons = driver.find_elements(By.TAG_NAME, "button")
        print(f"DEBUG: Found {len(buttons)} buttons on cart page: {[b.text for b in buttons]}")

        # Try multiple strategies to find the checkout button
        checkout_selectors = [
            (By.ID, "checkout-btn"),
            (By.ID, "checkout-button"),
            (By.XPATH, "//button[contains(text(), 'Checkout')]"),
            (By.XPATH, "//a[contains(text(), 'Checkout')]"), # Sometimes it's a link styled as a button
            (By.CLASS_NAME, "checkout-button")
        ]

        chk_btn = None
        for selector in checkout_selectors:
            try:
                chk_btn = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(selector))
                if chk_btn: break
            except:
                continue

        if not chk_btn:
            raise Exception(f"Checkout button not found. Page Source snippet: {driver.page_source[:500]}")

        driver.execute_script("arguments[0].click();", chk_btn)

        # 4. VERIFY
        wait.until(EC.url_contains("checkout.html"))
        assert "checkout" in driver.current_url.lower()
        print("E2E Workflow: SUCCESS")

    except Exception as e:
        print(f"E2E Workflow: FAILED at {driver.current_url}")
        print(f"Error: {str(e)}")
        driver.save_screenshot("e2e_cart_debug.png")
        raise e
    finally:
        driver.quit()
