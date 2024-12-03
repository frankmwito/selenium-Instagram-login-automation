# Capture screenshot of a page after an error
# password or username error

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

driver.get("https://www.instagram.com/")

driver.maximize_window()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//i[@aria-label='Instagram']")))

username = driver.find_element(By.CSS_SELECTOR,"input[name='username']")
username.send_keys("deinharddavid@gmail.com")

password = driver.find_element(By.CSS_SELECTOR,"input[name='password']")
password.send_keys("Vision@2030")

login_button = driver.find_element(By.CSS_SELECTOR,"button[type='submit'] div[class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']")
login_button.screenshot(".\\test.png")
login_button.click()
time.sleep(3)

driver.get_screenshot_as_file("C:\\Users\\Gaming 15\\Downloads\\selenium instagram login automation\\error.png")
driver.save_screenshot(".\\test1.png")


