from os.path import dirname
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import random
import time
import re
import string
import secrets
import os
driver = webdriver.Chrome(ChromeDriverManager().install()) # USES CHROMEDRIVERMANAGER TO AUTO UPDATE CHROMEDRIVER

driver.get("https://10minutemail.net")
time.sleep(5)
email = driver.find_element_by_class_name("mailtext").get_attribute("value")
print(email)
input("")