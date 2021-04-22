from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
driver =webdriver.Chrome(executable_path="D:\software\WOrk\driver\chromedriver_win32\chromedriver.exe")
driver.get("https://evaly.com.bd/products/tvs-apache-rtr-160cc-4v-single-disc")


drpdown=driver.find_element_by_xpath("//*[@id='__next']/div/div[3]/div/div[1]/div/div/div[2]/div[5]/div/div[1]/button")
drpdown.click()
time.sleep(5)
drp_itm=driver.find_element_by_xpath("//*[@id='custom-popover']/div/div/ul")
itms=len(drp_itm.find_elements_by_tag_name("li"))
for x in range(1,itms+1):
    ele_item=driver.find_element_by_xpath("//*[@id='custom-popover']/div/div/ul/div[{}]/li/div/p".format(x))
    text=ele_item.text
    if  text =="Only 4":
        ele_item.click()
        break

drpdown=driver.find_element_by_xpath("//*[@id='__next']/div/div[3]/div/div[1]/div/div/div[2]/div[5]/div/div[2]/button")
drpdown.click()
time.sleep(5)
drp_itm=driver.find_element_by_xpath("//*[@id='custom-popover']/div/div/ul")
itms=len(drp_itm.find_elements_by_tag_name("li"))
for x in range(1,itms+1):
    ele_item=driver.find_element_by_xpath("//*[@id='custom-popover']/div/div/ul/li[{}]/div/p".format(x))
    text=ele_item.text
    if  text =="Blue ":
        ele_item.click()
        print("Blue Found")
        break
    if x==itms:
        print("blue Not Found")