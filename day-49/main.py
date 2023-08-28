from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/')
email = 'jobnandom1@gmail.com'
password = 'blessedacademy'
email_entry = driver.find_element(By.NAME, 'session_key')
password_entry = driver.find_element(By.NAME, 'session_password')
email_entry.send_keys(email)
# time.sleep(1)
password_entry.send_keys(password)
# time.sleep(1)
password_entry.send_keys(Keys.ENTER)
# time.sleep(100)
driver.quit()

