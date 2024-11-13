# Dropdowns test automation

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

class Dropdowns:
    def drop_downs(self):
        driver.get('https://formy-project.herokuapp.com/')
        driver.maximize_window()
        
        dropd_own = driver.find_element(By.XPATH,'/html/body/div/div/li[6]/a')
        dropd_own.click()
        
        time.sleep(2)
        
        dropdown_button = driver.find_element(By.CSS_SELECTOR,'#dropdownMenuButton')
        dropdown_button.click()
        
        time.sleep(2)
        
        checkbox = driver.find_element(By.XPATH,'/html/body/div/div/div/a[3]')
        checkbox.click()
        
        checkbox_selection1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="checkbox-1"]')))
        checkbox_selection1.click()
        
        checkbox_selection2 = driver.find_element(By.XPATH,'//*[@id="checkbox-2"]')
        checkbox_selection2.click()
        
        checkbox_selection3 = driver.find_element(By.XPATH,'//*[@id="checkbox-3"]')
        checkbox_selection3.click()
        
        time.sleep(2)
        driver.back()
        
        dropdown_button = driver.find_element(By.CSS_SELECTOR,'#dropdownMenuButton')
        dropdown_button.click()
        
        radio_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.CSS_SELECTOR,'/html/body/div/div/div/a[13]'))
        radio_button.click()
        
        radio_button0 = driver.find_element(By.CSS_SELECTOR,'#radio-button-1')
        radio_button0.click
        
        if radio_button0.is_selected():
            radio_button1 = driver.find_element(By.CSS_SELECTOR,'body > div > div:nth-child(6) > input')
            radio_button1.click()
        else:
            radio_button2 = driver.find_element(By.CSS_SELECTOR,"input[value='option3']")
            radio_button2.click()
            
        time.sleep(3)
        driver.qiut()
        
drop = Dropdowns()
drop.drop_downs() 
        
        