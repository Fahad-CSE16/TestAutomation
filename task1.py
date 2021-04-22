from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver =webdriver.Chrome(executable_path="D:\software\WOrk\driver\chromedriver_win32\chromedriver.exe")
driver.get("https://evaly.com.bd/categories/speaker-2f615cf9a")
# ele=driver.find_elements_by_xpath("//*[@id='__next']/div/div[3]/div[1]/div[2]/div/div/div/a[1]/div/div[1]/div/img")
ele=driver.find_elements_by_class_name("absolute")
new_links =''
value=1
for x in ele[0:12]:
    if x.get_attribute("alt") !="None":
        # print(x.get_attribute("alt"))
        new_links+= "{}:{}\n".format(value,x.get_attribute("alt"))
        value+=1
# print('\n')
# print(new_links)
fobj=open('txt/new_simple1.txt','wb')
if new_links:
    fobj.write(new_links.encode())
driver.close()
