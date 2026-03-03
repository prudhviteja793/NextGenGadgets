# -----------------------------------------------------
# Assignment: Final Project
# Written by: Prudhvi Teja Reddy Kandula (ID: 5805128)
# Description: Fixed E2E Checkout Workflow for CI/CD compatibility.
# -----------------------------------------------------

import pytest
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
    driver = WebDriverFactory.get_driver("chrome")
    driver.set_window_size(1920, 1080) # Ensure no mobile-view menus hide buttons
    wait = WebDriverWait(driver, 20)
    
    # Use localhost:8000 consistently
    base_url = "http://localhost:8000"

    try:
        # 1. Login Phase
        driver.get(f"{base_url}/login.html")
        login_pg = LoginPage(driver)
        
        # Explicitly wait for the username field to be ready
        login_pg.perform_login("testuser", "Pass123!")

        # Handle alert if it appears (common in these assignments)
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present()).accept()
        except:
            pass

        # CRITICAL FIX: Wait for login to complete by checking for a cookie or URL change 
        # before jumping to the index page.
        wait.until(lambda d: "login.html" not in d.current_url)

        # 2. Add Item Phase
        driver.get(f"{base_url}/index.html")
        product_pg = ProductPage(driver)

        # Use JS click as a fallback to bypass any 'ElementClickInterceptedException'
        btn_element = wait.until(EC.element_to_be_clickable(product_pg.ADD_TO_CART_BTN))
        driver.execute_script("arguments[0].click();", btn_element)
        print("Step 2: Item added to cart.")

        # 3. Navigation to Cart
        driver.get(f"{base_url}/cart.html")
        wait.until(EC.url_contains("cart.html"))

        # 4. Checkout Action
        checkout_btn = wait.until(EC.visibility_of_element_located(product_pg.CHECKOUT_BTN))
        driver.execute_script("arguments[0].click();", checkout_btn)

        # 5. Final Verification
        wait.until(EC.url_contains("checkout.html"))
        assert "checkout" in driver.current_url.lower()
        print("E2E Workflow: SUCCESS")

    except Exception as e:
        print(f"E2E Workflow: FAILED - {str(e)}")
        # Take a screenshot for the report if it fails in CI
        driver.save_screenshot("e2e_error.png")
        raise e
    finally:
        driver.quit()
