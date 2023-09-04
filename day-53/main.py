from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
ZILLOW_URL = 'https://www.zillow.com/los-angeles-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A34.515883304696345%2C%22east%22%3A-117.68388826171875%2C%22south%22%3A33.52335579517794%2C%22west%22%3A-119.13957673828125%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A9%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12447%2C%22regionType%22%3A6%7D%5D%2C%22usersSearchTerm%22%3A%22Los%20Angeles%20CA%22%7D'
DOCS_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSe3r0h6om6tRxezlzNjTL6gZZLjasajysVIeq6nDUa_tVmi5Q/viewform?usp=sf_link'

response = requests.get(url=ZILLOW_URL,headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36","Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"})
page = response.text
# pprint.pprint(page)
soup = BeautifulSoup(page, "html.parser")
links = soup.find_all(name= 'div' ,class_='property-card-data')
prices = soup.find_all(name= 'span' ,class_='property-card-price')
address = soup.find_all(name= 'address' ,class_='property-card-addr')
# pprint.pprint(links)
links_arr = []
addr_arr = []
prices_arr = []
for link in links:
    lin = link.find('a').get('href')
    links_arr.append(lin)
    add = link.find('address').text
    addr_arr.append(add)
    price = link.find('span').text
    prices_arr.append(price.split('+')[0])

driver = webdriver.Chrome()
driver.get(DOCS_URL)
time.sleep(2)
for i in range(len(links)) :
    first_inp = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    second_inp = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    third_inp = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    done = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    first_inp.send_keys(addr_arr[i])
    time.sleep(.2)
    second_inp.send_keys(prices_arr[i])
    time.sleep(.2)
    third_inp.send_keys(links_arr[i])
    time.sleep(.2)
    done.click()
    time.sleep(2)
    next_response = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    next_response.click()
    time.sleep(2)

