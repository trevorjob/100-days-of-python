# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from foll import InstaFollower

instafollower = InstaFollower()
instafollower.login()
instafollower.find_followers()
# instafollower.follow()
