from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('http://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element(By.ID, 'cookie')


# upgrades = driver.find_elements(By.CSS_SELECTOR, '#store div')

# an = [int(dig[i].text.split('- ')[1].replace(',', '')) for i in range(len(dig[:-1]))]

start_time = time.time()
interval = 5
# for i in dig[:-1]:
#     print(i.text.split('- ')[1].replace(',', ''))
      

# for i in dig[:-1]:
#   print( int(i.text.split('- ')[1].replace(',', '')) )   
      


# def clicker():
#     clicked = check()
#     if clicked is not None:
#         print("clicker complete")
#         print(clicked)
#         dig[clicked].click()
#         # for up in upgrades[::-1]:
#         #     up.click()
#     print('upgrades complete')
    
while True:
    current_time = time.time()
    if current_time - start_time >= interval:
        money = driver.find_element(By.ID, 'money')
        dig = driver.find_elements(By.CSS_SELECTOR, '#store div b')
        for i in dig:
            if int(money.text) >= int(i.text.split('- ')[1].replace(',', '')):            
                i.click()
        print('done')
        start_time = current_time 
    cookie.click()
    
    time.sleep(0.1)
# time.sleep(10)