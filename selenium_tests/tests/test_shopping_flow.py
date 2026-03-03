# -----------------------------------------------------
# Assignment: Final Project
# Written by: Prudhvi Teja Reddy Kandula (ID: 5805128)
# Description: E2E Workflow - Final URL Formatting Fix.
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

    subfolders = ["website", "templates", "src", "web", ""]
    correct_base_url = None

    try:
        # 1. PATH DISCOVERY
        for folder in subfolders:
            # Construct URL safely without breaking http://
            path_part = f"/{folder}/".replace("//", "/")
            test_url = f"{base_url}{path_part}login.html"
            
            driver.get(test_url)
            if "Error response" not in driver.title and len(driver.find_elements(By.TAG_NAME, "input")) > 0:
                correct_base_url = f"{base_url}{path_part}"
                print(f"DEBUG: Confirmed valid base path: {correct_base_url}")
                break
        
        if not correct_base_url:
            raise Exception("Could not locate login.html. Check folder structure.")

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
        # Ensure we navigate to the absolute URL of index.html
        product_url = f"{correct_base_url}index.html"
        driver.get(product_url)
        
        product_pg = ProductPage(driver)
        # Verify we are on the right page before clicking
        wait.until(EC.url_contains("index.html"))
        
        add_btn = wait.until(EC.element_to_be_clickable(product_pg.ADD_TO_CART_BTN))
        driver.execute_script("arguments[0].click();", add_btn)
        print("DEBUG: Item added to cart.")

        # 4. CART & CHECKOUT
        driver.get(f"{correct_base_url}cart.html")
        wait.until(EC.url_contains("cart.html"))
        
        checkout_btn = wait.until(EC.element_to_be_clickable(product_pg.CHECKOUT_BTN))
        driver.execute_script("arguments[0].click();", checkout_btn)

        # 5. FINAL VERIFICATION
        wait.until(EC.url_contains("checkout.html"))
        assert "checkout" in driver.current_url.lower()
        print("E2E Workflow: SUCCESS")

    except Exception as e:
        print(f"E2E Workflow: FAILED at {driver.current_url} - {str(e)}")
        driver.save_screenshot("e2e_final_fix_error.png")
        raise e
    finally:
        driver.quit()
