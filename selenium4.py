from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver =webdriver.Chrome(executable_path="D:\software\WOrk\driver\chromedriver_win32\chromedriver.exe")
driver.get("https://staywithmoon.me")
print(driver.title)
print(driver.current_url)
time.sleep(10)
driver.get("https://www.codewithharry.com/videos/")
print(driver.title)
print(driver.current_url)
time.sleep(10)
driver.back()
print(driver.title)
print(driver.current_url)
time.sleep(10)
driver.forward()
print(driver.title)
print(driver.current_url)
time.sleep(10)
driver.close()
driver.quit()
