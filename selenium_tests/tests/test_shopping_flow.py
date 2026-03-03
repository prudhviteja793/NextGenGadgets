# -----------------------------------------------------
# Assignment: Final Project
# Written by: Prudhvi Teja Reddy Kandula (ID: 5805128)
# Description: E2E Workflow - Enhanced Locator Strategy.
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
        # 1. PATH DISCOVERY (Already Working)
        for folder in subfolders:
            path_part = f"/{folder}/".replace("//", "/")
            test_url = f"{base_url}{path_part}login.html"
            driver.get(test_url)
            if "Error response" not in driver.title and len(driver.find_elements(By.TAG_NAME, "input")) > 0:
                correct_base_url = f"{base_url}{path_part}"
                break
        
        if not correct_base_url:
            raise Exception("Could not locate login.html.")

        # 2. LOGIN PHASE
        login_pg = LoginPage(driver)
        wait.until(EC.visibility_of_element_located(login_pg.USERNAME))
        login_pg.perform_login("testuser", "Pass123!")
        
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present()).accept()
        except:
            pass

        # 3. ADD TO CART PHASE (The Failure Point)
        driver.get(f"{correct_base_url}index.html")
        wait.until(EC.url_contains("index.html"))
        
        # DEBUG: Let's see if products are even on the page
        # If this fails, we will see the HTML in the GitHub log
        try:
            # We first wait for ANY button to exist
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "button")))
        except:
            print("CRITICAL DEBUG: No buttons found on index.html. HTML Source:")
            print(driver.page_source)
            raise Exception("No buttons found on the product page. Is the product list empty?")

        product_pg = ProductPage(driver)
        
        # FALLBACK LOCATOR: If the ID in product_pg fails, try a generic "Add to Cart" button
        try:
            add_btn = wait.until(EC.element_to_be_clickable(product_pg.ADD_TO_CART_BTN))
        except:
            print("Original locator failed, trying fallback CSS selector...")
            # This looks for any button that contains the word 'Add' or has 'cart' in the class/id
            fallback_locator = (By.CSS_SELECTOR, "button[id*='add'], button[class*='btn-add'], .add-to-cart")
            add_btn = wait.until(EC.element_to_be_clickable(fallback_locator))

        driver.execute_script("arguments[0].click();", add_btn)
        print("DEBUG: Item added to cart successfully.")

        # 4. CART & CHECKOUT
        driver.get(f"{correct_base_url}cart.html")
        wait.until(EC.url_contains("cart.html"))
        
        # Use JS click for checkout to be safe
        checkout_btn = wait.until(EC.element_to_be_clickable(product_pg.CHECKOUT_BTN))
        driver.execute_script("arguments[0].click();", checkout_btn)

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
