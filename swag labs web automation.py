from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DemoPractice():
    def webPage(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service)
        driver.get("https://www.saucedemo.com/")
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        
        username = driver.find_element(By.ID,'user-name')
        username.send_keys('standard_user')
        
        password = driver.find_element(By.NAME,'password')
        password.send_keys('secret_sauce')
        
        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,"submit-button")))
        login_button.click()
        
        item1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt='Sauce Labs Backpack']")))
        item1.click()
        
        time.sleep(5)
        driver.quit()
        
demo = DemoPractice()
demo.webPage()