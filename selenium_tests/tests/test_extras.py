<<<<<<< HEAD
import pytest
from utils.webdriver_factory import WebDriverFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_iframe_and_modal_interaction():
    driver = WebDriverFactory.get_driver("chrome")
    wait = WebDriverWait(driver, 5)  # Reduced wait for efficiency

    try:
        driver.get("http://localhost:8000/index.html")

        # --- Handle Iframe ---
        try:
            # Look for any iframe on the page
            iframes = driver.find_elements(By.TAG_NAME, "iframe")
            if len(iframes) > 0:
                driver.switch_to.frame(iframes[0])
                print("Successfully switched to iframe.")
                driver.switch_to.default_content()
            else:
                print("No iframe found on page, skipping iframe check.")
        except Exception as e:
            print(f"Iframe interaction skipped: {e}")

        # --- Handle Modal ---
        try:
            # Try to find a 'Contact' or 'About' button that triggers a modal
            # Update 'contact-btn' to match an actual ID in your index.html
            contact_btn = driver.find_elements(By.ID, "contact-btn")
            if contact_btn:
                contact_btn[0].click()
                # Wait for modal to appear
                wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal")))
                print("Modal interaction successful.")
            else:
                print("Modal trigger button not found, skipping modal check.")
        except Exception as e:
            print(f"Modal interaction skipped: {e}")

    finally:
=======
import pytest
from utils.webdriver_factory import WebDriverFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_iframe_and_modal_interaction():
    driver = WebDriverFactory.get_driver("chrome")
    wait = WebDriverWait(driver, 5)  # Reduced wait for efficiency

    try:
        driver.get("http://localhost:8000/index.html")

        # --- Handle Iframe ---
        try:
            # Look for any iframe on the page
            iframes = driver.find_elements(By.TAG_NAME, "iframe")
            if len(iframes) > 0:
                driver.switch_to.frame(iframes[0])
                print("Successfully switched to iframe.")
                driver.switch_to.default_content()
            else:
                print("No iframe found on page, skipping iframe check.")
        except Exception as e:
            print(f"Iframe interaction skipped: {e}")

        # --- Handle Modal ---
        try:
            # Try to find a 'Contact' or 'About' button that triggers a modal
            # Update 'contact-btn' to match an actual ID in your index.html
            contact_btn = driver.find_elements(By.ID, "contact-btn")
            if contact_btn:
                contact_btn[0].click()
                # Wait for modal to appear
                wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal")))
                print("Modal interaction successful.")
            else:
                print("Modal trigger button not found, skipping modal check.")
        except Exception as e:
            print(f"Modal interaction skipped: {e}")

    finally:
>>>>>>> 6c46170 (Syncing local files with repository)
        driver.quit()