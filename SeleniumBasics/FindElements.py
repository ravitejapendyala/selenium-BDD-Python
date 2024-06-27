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
email = driver.find_element(By.XPATH,"//input[@id='Email']")
password = driver.find_element(By.XPATH,"//input[@id='Password']")
submit = driver.find_element(By.XPATH,"//button[@type='submit']")
email.clear()
email.send_keys("admin@yourstore.com")
password.clear()
password.send_keys("admin")
submit.click()
time.sleep(5)
# Adding logic to find elements
Catalog_lnk = driver.find_element(By.XPATH,"//p[normalize-space()='Catalog']//i[contains(@class,'right fas fa-angle-left')]")
Catalog_lnk.click()
Products_lnk = driver.find_element(By.XPATH,"//p[normalize-space()='Products']")
Products_lnk.click()
time.sleep(5)
Products = driver.find_elements(By.XPATH,".//table[@id='products-grid']//tbody/tr//td[3]")
time.sleep(5)
print(" Products count : ",len(Products))
#.//table[@id='products-grid']//tbody/tr//td[3]
for ele in Products:
    print("Products list are : ",ele.text)
driver.quit()

