from selenium import webdriver
import time
# Set the path to your ChromeDriver executable
chrome_driver_path = 'Users\HP\Videos\programming\chromedriver-win64\chromedriver-win64\chromedriver'

# Initialize the Chrome WebDriver with the driver executable path
driver = webdriver.Chrome()

# URL of the website you want to open
website_url = 'https://www.amazon.com'

# Open the website
driver.get(website_url)
time.sleep(20)
# Close the browser window when done
driver.quit()
