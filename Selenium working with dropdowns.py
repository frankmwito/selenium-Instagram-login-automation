# Working with Dropdowns
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Navigate to the Selenium website
    driver.get("https://www.selenium.dev/")

    # Wait for the dropdown element to be clickable and click to open it
    dropdown_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarDropdown"]')))
    dropdown_button.click()  # Open the dropdown menu

    # Wait for and click the "Events" item within the dropdown
    dropdown_item = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Events")))
    dropdown_item.click()  # Click the "Events" item in the dropdown
    # Pause for observation (optional)
    time.sleep(20)

finally:
    # Close the browser
    driver.quit()

