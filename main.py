from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

USERNAME = "your_username"
PASSWORD = "your_password"
AUTO_REPLY_MESSAGE = "Hanan is not online now. This is his bot replying 🤖"

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver.get("https://www.instagram.com")

time.sleep(5)

# Login
driver.find_element(By.NAME, "username").send_keys(USERNAME)
driver.find_element(By.NAME, "password").send_keys(PASSWORD)
driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

time.sleep(10)

# TODO: Add logic to check new messages, reply once only etc.

driver.quit()
