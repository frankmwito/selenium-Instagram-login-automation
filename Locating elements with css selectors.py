from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LocatingElements():
    def css_selectors(self):
        # Set up the WebDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.selenium.dev/")  # Load the Selenium website

        # 1. Locate and interact with the “Downloads” link using CSS Selector (by class)
        downloads_link = driver.find_element(By.CSS_SELECTOR, "#navbarDropdown")
        print("Downloads link text:", downloads_link.text)
        downloads_link.click()  # Click the link
        driver.back()  # Navigate back
        
        # locate first the blog to locate the search input
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#main_navbar > ul > li:nth-child(6) > a > span')))
        blog = driver.find_element(By.CSS_SELECTOR, '#main_navbar > ul > li:nth-child(6) > a > span')
        blog.click()
        
        # 2. Locate the first search input field by attribute (ID)
        search_input = driver.find_element(By.CSS_SELECTOR, "#docsearch-0 > button")
        search_input.send_keys("WebDriver" + Keys.RETURN)  # Enter a search term and submit
        time.sleep(2)  # Allow time for search results to load

        # 3. Locate any link in the navigation bar by combining class and tag selectors
        nav_link = driver.find_element(By.CSS_SELECTOR, "nav.navbar a")
        print("Nav link text:", nav_link.text)

        # 4. Locate a list of items using class or attribute selectors (e.g., all buttons)
        buttons = driver.find_elements(By.CSS_SELECTOR, "a.btn")  # Select all elements with class 'btn'
        for button in buttons:
            print("Button text:", button.text)

        # 5. Locate nested elements using a complex CSS selector (e.g., div > a or ul li a)
        nested_element = driver.find_element(By.CSS_SELECTOR, "footer div.container div.row div:nth-child(1) ul li a")
        print("Nested element text:", nested_element.text)

        # Close the driver after a delay
        time.sleep(5)
        driver.quit()

# Run the script
demo = LocatingElements()
demo.css_selectors()
