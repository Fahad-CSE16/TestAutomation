from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver =webdriver.Chrome(executable_path="D:\software\WOrk\driver\chromedriver_win32\chromedriver.exe")
driver.get("https://staywithmoon.me")
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath("//*[@id='navbarSupportedContent']/ul/li[3]/a").click()
time.sleep(10)
driver.close()
driver.quit()
