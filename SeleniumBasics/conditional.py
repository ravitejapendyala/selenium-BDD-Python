import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

current_dir = os.path.dirname(__file__)
driver_path = os.path.abspath(os.path.join(current_dir,'..','drivers','chromedriver.exe'))
service_obj = Service(driver_path)
driver = webdriver.Chrome(service = service_obj)



driver.get("https://admin-demo.nopcommerce.com/regiser")
driver.maximize_window()
time.sleep(5)
searchbox = driver.find_element(By.XPATH,"//input[@id='Email']")
print("Enabled status:",searchbox.is_enabled())
print("Display status:",searchbox.is_displayed())
driver.quit()

