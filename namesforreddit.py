from os.path import dirname
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
temp_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "firstHeading"))
)
temp = temp_element.text
for char in string.punctuation:
    temp = temp.replace(char, '') #REMOVES ALL PUNCTUATION
for char in string.digits:
    temp = temp.replace(char, '') #REMOVES SPACES
temp = "".join(filter(lambda char: char in string.printable, temp)) #REMOVES NON ASCII CHARACTERS
name = ''.join(temp.split())
name = name[:random.randint(5,7)] #KEEPS 5 TO 7 LETTERS OF THE ORIGINAL STRING


randomNumber = random.randint(10000,99999)

finalName = name+str(randomNumber)
# NAME GENERATION FINISHED

# REDDIT ACCOUNT CREATION
driver.get('https://www.reddit.com/register/')
driver.execute_script("window.open('about:blank', 'secondtab');")
driver.switch_to.window("secondtab")
driver.get("https://10minutemail.org")
email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "mailtext"))
)
email_attribute = email.get_attribute("value")
print(email_attribute)
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_id('regEmail').send_keys(email_attribute)
continue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue')]"))
)
continue_button.click()
time.sleep(2)
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'regUsername'))
)
username_input.send_keys(finalName)
#driver.find_element_by_id('regUsername').send_keys(finalName)
#driver.find_element_by_id('regPassword').send_keys(password)
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'regPassword'))
)
password_input.send_keys(password)
input("continue when you have finish the captcha \r")
signup_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@class='AnimatedForm__submitButton SignupButton']"))
)
signup_button.click()
#driver.find_element_by_xpath("//button[@class='AnimatedForm__submitButton SignupButton']").click()
time.sleep(2)
subscribe_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='AnimatedForm__submitButton SubscribeButton']"))
)
subscribe_button.click()
#driver.find_element_by_xpath("//button[@class='AnimatedForm__submitButton SubscribeButton']").click()
driver.switch_to.window(driver.window_handles[1])
email_open = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Reddit')]"))
)
email_open.click()
verify_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "btn-14"))
)
verify_button.click()
dirname = os.path.dirname(__file__)
text_file_path = os.path.join(dirname, 'combos.txt')
text_file = open(text_file_path, "a")
text_file.write(finalName + ":" + password) #OUTPUTS NAME AND NUMBER
text_file.write("\n")
text_file.close()
print("wait for the \"email verified\" popup to apear, then hit enter")
input("FINISHED UP! Thank you for helping the cause! - ItCameFr0mMars")
driver.close()