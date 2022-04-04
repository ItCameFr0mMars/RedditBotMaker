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

# GENERATE PASSWORD
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(16))
# PASSWORD GENERATION FINISHED

# NAME GENERATION
driver.get('https://en.wikipedia.org/wiki/Special:Random')
temp = driver.find_element_by_class_name("firstHeading").text
for char in string.punctuation:
    temp = temp.replace(char, '') #REMOVES ALL PUNCTUATION
for char in string.digits:
    temp = temp.replace(char, '') #REMOVES SPACES
temp = "".join(filter(lambda char: char in string.printable, temp)) #REMOVES NON ASCII CHARACTERS
name = ''.join(temp.split())
name = name[:random.randint(5,7)] #KEEPS 5 TO 7 LETTERS OF THE ORIGINAL STRING


randomNumber = random.randint(10000,99999)

dirname = os.path.dirname(__file__)
text_file_path = os.path.join(dirname, 'namesforreddit.txt')
text_file = open(text_file_path, "a")
text_file.write("USR: " + name + str(randomNumber) + " PWD: " + password) #OUTPUTS NAME AND NUMBER
text_file.write("\n")
text_file.close()

finalName = name+str(randomNumber)
# NAME GENERATION FINISHED

# REDDIT ACCOUNT CREATION
driver.get('https://www.reddit.com/register/')
driver.execute_script("window.open('about:blank', 'secondtab');")
driver.switch_to.window("secondtab")
driver.get("https://10minutemail.net")
email = driver.find_element_by_class_name("mailtext").get_attribute("value")
print(email)
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_id('regEmail').send_keys(finalName+"@flawless.wtf")
driver.find_element_by_xpath("//button[contains(text(),'Continue')]").click()
time.sleep(10)
driver.find_element_by_id('regUsername').send_keys(finalName)
driver.find_element_by_id('regPassword').send_keys(password)
input("when you finish the captcha press enter")
driver.find_element_by_xpath("//button[@class='AnimatedForm__submitButton SignupButton']").click()
time.sleep(5)
driver.find_element_by_xpath("//button[@class='AnimatedForm__submitButton SubscribeButton']").click()
time.sleep(5)
driver.get("https://pooblic.org/place/auth")
driver.find_element_by_xpath("//input[@class='fancybutton newbutton allow']").click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.find_element_by_xpath("//a[contains(text(), 'Reddit')]").click()
input("")
try:
    driver.find_element_by_xpath("//body").click()
except:
    print("no ad to skip")
    pass
driver.execute_script("")
time.sleep(5)
driver.find_element_by_class_name("btn-14").click()
input("wait for the page to load to verify your email, then press enter")
driver.close()