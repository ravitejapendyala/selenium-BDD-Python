

import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


current_dir = os.path.dirname(__file__)
driver_path = os.path.abspath(os.path.join(current_dir,'..','drivers','chromedriver.exe'))
service_obj = Service(driver_path)
driver = webdriver.Chrome(service = service_obj)

driver.get("https://admin-demo.nopcommerce.com/login")

email = driver.find_element(By.XPATH,"//input[@id='Email']")
time.sleep(3)
email.clear()
email.send_keys("raviteja@gmail.com")
time.sleep(4)
login = driver.find_element(By.XPATH,"//button[@type='submit']")


print("After clearing result of text",email.text)
print("After clearing result of get_attribute()",email.get_attribute("value"))
print("login button text is :",login.text)
print("login button result of get_attribute() is :",login.get_attribute("value"))
driver.quit()