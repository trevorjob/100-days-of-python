from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InternetSpeed:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = ''
        self.down = ''
    
    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        go = self.driver.find_element('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()
        time.sleep(60)
        

        