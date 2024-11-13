# Suce demo user authentication test automation

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Set up the Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the target URL
driver.get("https://www.saucedemo.com/")

# Enter username
username = driver.find_element(By.XPATH, '//*[@id="user-name"]')
username.send_keys("standard_user")

# Enter password
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("secret_sauce")

# Click login button
login_button = driver.find_element(By.CLASS_NAME, 'submit-button')
login_button.click()

# Wait and get the header text after login
header_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.title'))
)
header_text = header_element.text
print("Header text:", header_text)

# Wait and get the src attribute of the first item image
item1_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="item_4_img_link"]/img'))
)
item1_src = item1_element.get_attribute('src')
print("Item 1 image source:", item1_src)

# Wait briefly and then close the browser
time.sleep(5)
driver.quit()
