from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
INSTA_USER = 'redeks123456@gmail.com'
INSTA_PASSWD = 'blessedacademy12'
simiar = 'amandawiilliams'
user = 'username'
passd = 'password'
btn = '//*[@id="loginForm"]/div/div[3]/button'
INSTA = 'https://www.instagram.com/'
class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(INSTA)
        time.sleep(3)
        username = self.driver.find_element(By.NAME, user)
        password = self.driver.find_element(By.NAME, passd)
        btnl = self.driver.find_element(By.XPATH, btn)
        username.send_keys(INSTA_USER)
        password.send_keys(INSTA_PASSWD)
        btnl.click()
        time.sleep(6)
        never = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        never.click()
    
    def find_followers(self):
        time.sleep(5)
        search_btn = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_HI"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div')
        search_btn.click()
        time.sleep(2)
        search = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_V6"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
        search.send_keys(simiar)
        time.sleep(2)
        acct = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_V6"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]')
        acct.click()
        time.sleep(3)
    
    def follow(self):
        folowers_btn = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_V6"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        folowers_btn.click()
        time.sleep(1)
        acct = self.driver.find_elements(By.CSS_SELECTOR, 'div div button')
        print(acct)
