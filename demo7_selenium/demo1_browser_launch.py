import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://github.com/")
print(driver.title)
time.sleep(6)