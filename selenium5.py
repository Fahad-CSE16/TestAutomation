# //*[@id='contact-me']/div/form/div[2]/div/button

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver =webdriver.Chrome(executable_path="D:\software\WOrk\driver\chromedriver_win32\chromedriver.exe")
driver.get("https://staywithmoon.me")
driver.maximize_window()
name_ele=driver.find_element_by_name("name")
print(name_ele.is_displayed())
print(name_ele.is_enabled())
pwd_ele=driver.find_element_by_name("email")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())
des_ele=driver.find_element_by_name("description")
print(des_ele.is_displayed())
print(des_ele.is_enabled())
# print(des_ele.is_selected())

name_ele.send_keys("Fahad")
pwd_ele.send_keys("mdfahadhossain71@gmail.com")
des_ele.send_keys("Boss public")
# driver.find_elements_by_css_selector("input[value=actualvalue") #for radio button
driver.find_element_by_name("Submit").send_keys("\n")#work as click() u can use it when click() is not working


driver.close()
