from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class DemoFindElementByName():
    def locate_by_name(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service = service)
        driver.get("https://www.instagram.com/accounts/login/")
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
        
        username = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys('deinharddavid@gmail.com')
        
        password = driver.find_element(By.CSS_SELECTOR,"input[name='password']")
        password.send_keys('Vision@2030')
        
        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')))
        login_button.click()
        
        time.sleep(10)
        
        driver.quit()
demo = DemoFindElementByName()
demo.locate_by_name()
        