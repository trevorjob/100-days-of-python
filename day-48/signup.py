from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://secure-retreat-92358.herokuapp.com/')
search = driver.find_element(By.NAME, 'fName')
search.send_keys('job')
time.sleep(3)
search = driver.find_element(By.NAME, 'lName')
search.send_keys('kumdan')
time.sleep(3)
search = driver.find_element(By.NAME, 'email')
search.send_keys('redes123456@gmail.com')
time.sleep(3)
search.send_keys(Keys.ENTER)

time.sleep(10)


