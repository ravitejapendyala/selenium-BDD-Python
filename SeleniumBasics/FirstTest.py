import os.path
import time
from concurrent.futures import thread

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

current_dir = os.path.dirname(__file__)
driver_path = os.path.abspath(os.path.join(current_dir,'..','drivers','chromedriver.exe'))

service_obj = Service(driver_path)
driver = webdriver.Chrome(service = service_obj)
# driver = webdriver.Chrome(excutable_path=driver_path)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)
username_field = driver.find_element(By.NAME,"username")
password_field = driver.find_element(By.NAME,"password")
login_btn = driver.find_element(By.XPATH,"//button[@type='submit']")
username_field.send_keys("Admin")
password_field.send_keys("admin123")
login_btn.click()
