import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://github.com/")
print(driver.title)
time.sleep(6)


driver.find_element(By.NAME, "lastname").send_keys("Abraham")
driver.implicitly_wait(10)
driver.find_element(By.NAME, "reg_passwd__").send_keys("helloworld")
driver.implicitly_wait(10)