from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('https://tinder.com/')
time.sleep(3)
decline = driver.find_element(By.XPATH, '//*[@id="u-1535117240"]/div/div[2]/div/div/div[1]/div[2]/button')
decline.click()
login_btn = driver.find_element(By.XPATH, '//*[@id="u-1535117240"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_btn.click()
time.sleep(2)
fb_btn = driver.find_element(By.XPATH, '//*[@id="u1031468980"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
fb_btn.click()
time.sleep(2)
fb_window = driver.window_handles[1]
base_win = driver.window_handles[0]
driver.switch_to.window(fb_window)
time.sleep(2)
email = driver.find_element(By.NAME, 'email')
password = driver.find_element(By.NAME, 'pass')
btn = driver.find_element(By.ID, 'loginbutton')
email.send_keys('08104899622')
password.send_keys('blessedacademy')
btn.click()
driver.switch_to.window(base_win)
time.sleep(7)

allow = driver.find_element(By.XPATH, '//*[@id="u1031468980"]/main/div/div/div/div[3]/button[1]')
allow.click()
time.sleep(3)
enable = driver.find_element(By.XPATH, '//*[@id="u1031468980"]/main/div/div/div/div[3]/button[1]')
enable.click()
time.sleep(3)
not_int = driver.find_element(By.XPATH, '//*[@id="u-1535117240"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
for i in range(10):
    not_int.click()
    time.sleep(2)


driver.quit()