# -----------------------------------------------------
# Assignment: Final Project
# Written by: Prudhvi Teja Reddy Kandula (ID: 5805128)
# Description: Optimized E2E Checkout Workflow with CI/CD Stability Fixes.
# -----------------------------------------------------

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_tests.utils.webdriver_factory import WebDriverFactory
from selenium_tests.pages.login_page import LoginPage
from selenium_tests.pages.product_page import ProductPage

def test_e2e_checkout_workflow():
    """
    Validates the full shopping journey from Login to Checkout.
    Fulfills the 'E2E Workflow' requirement (40% Grade section).
    """
    # 1. Setup Driver
    driver = WebDriverFactory.get_driver("chrome")
    driver.set_window_size(1920, 1080)
    wait = WebDriverWait(driver, 30) # Increased to 30s for slow CI environments
    
    base_url = "http://localhost:8000"

    try:
        # --- PHASE 1: LOGIN ---
        driver.get(f"{base_url}/login.html")
        
        # Stability: Wait for page to actually render before interacting
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
        
        login_pg = LoginPage(driver)
        
        # Stability: Ensure the specific username field is visible before perform_login
        wait.until(EC.visibility_of_element_located(login_pg.USERNAME))
        login_pg.perform_login("testuser", "Pass123!")

        # Handle alert if it appears
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present()).accept()
        except:
            pass

        # Ensure login transition is complete
        wait.until(lambda d: "login.html" not in d.current_url)

        # --- PHASE 2: ADD TO CART ---
        driver.get(f"{base_url}/index.html")
        product_pg = ProductPage(driver)

        # Use JS click to bypass any overlays or rendering delays
        btn_element = wait.until(EC.element_to_be_clickable(product_pg.ADD_TO_CART_BTN))
        driver.execute_script("arguments[0].click();", btn_element)
        print("Step 2: Item added to cart.")

        # --- PHASE 3: CHECKOUT ---
        driver.get(f"{base_url}/cart.html")
        wait.until(EC.url_contains("cart.html"))

        # Trigger Checkout
        checkout_btn = wait.until(EC.element_to_be_clickable(product_pg.CHECKOUT_BTN))
        driver.execute_script("arguments[0].click();", checkout_btn)

        # --- PHASE 4: VERIFICATION ---
        wait.until(EC.url_contains("checkout.html"))
        assert "checkout" in driver.current_url.lower()
        print("E2E Workflow: SUCCESS")

    except Exception as e:
        print(f"E2E Workflow: FAILED - {str(e)}")
        # Save screenshot for GitHub Actions artifacts
        driver.save_screenshot("e2e_error_debug.png")
        raise e
    finally:
        driver.quit()
