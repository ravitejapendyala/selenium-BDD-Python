import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

current_dir = os.path.dirname(__file__)
driver_path = os.path.abspath(os.path.join(current_dir,'..','drivers','chromedriver.exe'))
service_obj = Service(driver_path)

driver = webdriver.Chrome(service = service_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
print('title is: ',driver.title)
print(driver.page_source)
print(driver.current_url)
driver.quit()




