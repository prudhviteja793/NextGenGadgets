# -----------------------------------------------------
# Assignment: Final Project
# Written by: Prudhvi Teja Reddy Kandula (ID: 5805128)
# Description: E2E Workflow - Aggressive Locator Strategy.
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
        # 1. PATH DISCOVERY (Optimized for your verified '/website/' path)
        correct_base_url = f"{base_url}/website/"
        driver.get(f"{correct_base_url}login.html")
        
        # 2. LOGIN PHASE
        login_pg = LoginPage(driver)
        wait.until(EC.visibility_of_element_located(login_pg.USERNAME))
        login_pg.perform_login("testuser", "Pass123!")

        # Handle alert
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present()).accept()
        except:
            pass

        # 3. ADD TO CART PHASE (Multi-locator Fallback)
        driver.get(f"{correct_base_url}index.html")
        wait.until(EC.url_contains("index.html"))
        
        # Fallback Strategy: Try PageObject first, then common IDs/Text
        add_to_cart_selectors = [
            (By.ID, "add-to-cart-button"),
            (By.CLASS_NAME, "btn-add-to-cart"),
            (By.XPATH, "//button[contains(text(), 'Add to Cart')]"),
            (By.XPATH, "//button[1]") # Last resort: click the first button found
        ]

        btn = None
        for selector in add_to_cart_selectors:
            try:
                btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located(selector))
                if btn: break
            except:
                continue

        if not btn:
            # If all fallbacks fail, try the original PageObject locator
            product_pg = ProductPage(driver)
            btn = wait.until(EC.presence_of_element_located(product_pg.ADD_TO_CART_BTN))

        driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        driver.execute_script("arguments[0].click();", btn)
        print("DEBUG: Add to Cart clicked.")

        # 4. CART & CHECKOUT
        driver.get(f"{correct_base_url}cart.html")
        wait.until(EC.url_contains("cart.html"))
        
        # Aggressive Checkout click
        checkout_selectors = [
            (By.ID, "checkout-button"),
            (By.XPATH, "//button[contains(text(), 'Checkout')]"),
            (By.CLASS_NAME, "btn-checkout")
        ]
        
        chk_btn = None
        for selector in checkout_selectors:
            try:
                chk_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located(selector))
                if chk_btn: break
            except:
                continue
        
        driver.execute_script("arguments[0].click();", chk_btn)

        # 5. FINAL VERIFICATION
        wait.until(EC.url_contains("checkout.html"))
        assert "checkout" in driver.current_url.lower()
        print("E2E Workflow: SUCCESS")

    except Exception as e:
        print(f"E2E Workflow: FAILED at {driver.current_url}")
        print(f"Error: {str(e)}")
        driver.save_screenshot("e2e_ultimate_fallback_error.png")
        raise e
    finally:
        driver.quit()
