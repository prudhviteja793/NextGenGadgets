# -----------------------------------------------------
# Assignment: Final Project
# Written by: Prudhvi Teja Reddy Kandula (ID: 5805128)
# Description: E2E Workflow with Automatic Path Discovery.
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

    # List of possible subdirectories where your HTML might be
    # Added 'website' and '' (root) as primary targets
    subfolders = ["", "website", "templates", "src", "web"]
    
    correct_path = None

    try:
        # 1. DISCOVER THE CORRECT URL PATH
        for folder in subfolders:
            test_path = f"{base_url}/{folder}/login.html".replace("//", "/")
            driver.get(test_path)
            if "Error response" not in driver.title and len(driver.find_elements(By.TAG_NAME, "input")) > 0:
                correct_path = f"{base_url}/{folder}/".replace("//", "/")
                print(f"DEBUG: Found valid path at {test_path}")
                break
        
        if not correct_path:
            print(f"CRITICAL: 404 on all attempts. Last Page Source: {driver.page_source[:200]}")
            raise Exception("Could not locate login.html in any known subdirectory.")

        # 2. LOGIN PHASE
        login_pg = LoginPage(driver)
        wait.until(EC.visibility_of_element_located(login_pg.USERNAME))
        login_pg.perform_login("testuser", "Pass123!")

        # Handle alert
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present()).accept()
        except:
            pass

        # 3. ADD TO CART PHASE
        driver.get(f"{correct_path}index.html")
        product_pg = ProductPage(driver)
        add_btn = wait.until(EC.element_to_be_clickable(product_pg.ADD_TO_CART_BTN))
        driver.execute_script("arguments[0].click();", add_btn)

        # 4. CART & CHECKOUT
        driver.get(f"{correct_path}cart.html")
        checkout_btn = wait.until(EC.element_to_be_clickable(product_pg.CHECKOUT_BTN))
        driver.execute_script("arguments[0].click();", checkout_btn)

        # 5. FINAL VERIFICATION
        wait.until(EC.url_contains("checkout.html"))
        assert "checkout" in driver.current_url.lower()
        print("E2E Workflow: SUCCESS")

    except Exception as e:
        print(f"E2E Workflow: FAILED - {str(e)}")
        driver.save_screenshot("e2e_path_error.png")
        raise e
    finally:
        driver.quit()
