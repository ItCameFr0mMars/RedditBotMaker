from os.path import dirname
from numpy import intp
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random
import time
import string
import secrets
import os

print("""
  __  __              _____     _____ 
 |  \/  |     /\     |  __ \   / ____|
 | \  / |    /  \    | |__) | | (___  
 | |\/| |   / /\ \   |  _  /   \___ \ 
 | |  | |  / ____ \  | | \ \   ____) |
 |_|  |_| /_/    \_\ |_|  \_\ |_____/ 
                                      
                                      
""")

options = webdriver.ChromeOptions()
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
driver.get("https://10minutemail.org")
email = driver.find_element_by_class_name("mailtext").get_attribute("value")
print(email)
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_id('regEmail').send_keys(email)
time.sleep(3)
driver.find_element_by_xpath("//button[contains(text(),'Continue')]").click()
time.sleep(7)
driver.find_element_by_id('regUsername').send_keys(finalName)
driver.find_element_by_id('regPassword').send_keys(password)
input("continue when you have finish the captcha")
time.sleep(1)
driver.find_element_by_xpath("//button[@class='AnimatedForm__submitButton SignupButton']").click()
time.sleep(7)
driver.find_element_by_xpath("//button[@class='AnimatedForm__submitButton SubscribeButton']").click()
time.sleep(7)
driver.get("https://pooblic.org/place/auth")
time.sleep(3)
driver.find_element_by_xpath("//input[@class='fancybutton newbutton allow']").click()
driver.switch_to.window(driver.window_handles[1])
driver.execute_script("window.scrollTo(30,document.body.scrollHeight)")
time.sleep(5)
driver.find_element_by_xpath("//a[contains(text(), 'Reddit')]").click()
try:
    driver.find_element_by_xpath("//body").click()
except:
    print("no ad to skip")
    pass
time.sleep(4)
driver.find_element_by_class_name("btn-14").click()
input("FINISHED UP! Thank you for helping the cause! - ItCameFr0mMars")
driver.close()