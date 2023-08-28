from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# num = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# print(num.text)
# # num.click()
# minister = driver.find_element(By.LINK_TEXT ,'Srettha Thavisin')
# print(minister.text)
# minister.click()
search = driver.find_element(By.NAME, 'search')
search.send_keys('python')
search.send_keys(Keys.ENTER)
time.sleep(10)
driver.quit()

