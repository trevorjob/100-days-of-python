from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# Set the path to your ChromeDriver executable
chrome_driver_path = 'Users\HP\Videos\programming\chromedriver-win64\chromedriver-win64\chromedriver'

# Initialize the Chrome WebDriver with the driver executable path
driver = webdriver.Chrome()

# # URL of the website you want to open
# website_url = 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'

# # # Open the website
# driver.get(website_url)

# # # time.sleep(30)
# price = driver.find_elements(By.CLASS_NAME,'a-size-base')

# for p in price:
#     print(p.text)
# print(price.get_attribute('class'))
# Close the browser window when done
driver.get("https://www.python.org/")
event_times = driver.find_elements(By.CSS_SELECTOR ,".event-widget time")
event_place = driver.find_elements(By.CSS_SELECTOR ,".event-widget li a")

obj = {
   i: {'time': event_times[i].text, 'name' : event_place[i].text} for i in range(len(event_place))
}
print(obj)
driver.quit()
