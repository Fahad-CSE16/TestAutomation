from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver =webdriver.Chrome(executable_path="D:\software\WOrk\driver\chromedriver_win32\chromedriver.exe")
driver.get("https://evaly.com.bd")

srch=driver.find_element_by_xpath("//*[@id='__next']/div/div[2]/div[1]/div/div[1]/div/div/input")
srch.send_keys("Motor Bike\n")
time.sleep(5)

ele_price=driver.find_element_by_xpath("//*[@id='__next']/div/div[3]/div/div[1]/div/div[1]/div/form/input[1]")
ele_price.clear()
ele_price.send_keys("90000")
# time.sleep(3)
ele_price=driver.find_element_by_xpath("//*[@id='__next']/div/div[3]/div/div[1]/div/div[1]/div/form/input[2]")
ele_price.clear()
ele_price.send_keys("200000")
btn=driver.find_element_by_xpath("//*[@id='__next']/div/div[3]/div/div[1]/div/div[1]/div/form/button")
btn.click()
time.sleep(3)

ele_div=driver.find_element_by_xpath("//*[@id='__next']/div/div[3]/div/div[1]/div/div[2]/div[1]/ul")
items=len(ele_div.find_elements_by_tag_name("li"))
print(items)
for x in range(1,items+1):
    ele_item=driver.find_element_by_xpath("//*[@id='__next']/div/div[3]/div/div[1]/div/div[2]/div[1]/ul/li[{}]/label".format(x))
    text=ele_item.find_element_by_tag_name("span").text
    if  text =="Motor Bike":
        ele_item.click()
        break
time.sleep(5)
ele_div=driver.find_element_by_xpath("//*[@id='__next']/div/div[3]/div/div[1]/div/div[2]/div[2]/ul")
items=len(ele_div.find_elements_by_tag_name("li"))
print(items)
for x in range(1,items+1):
    ele_item=driver.find_element_by_xpath("//*[@id='__next']/div/div[3]/div/div[1]/div/div[2]/div[2]/ul/li[{}]/label".format(x))
    text=ele_item.find_element_by_tag_name("span").text
    print(text)
    if  text =="TVS":
        ele_item.click()
        break
time.sleep(5)
ele_div=driver.find_element_by_xpath("//*[@id='__next']/div/div[3]/div/div[1]/div/div[2]/div[4]/ul/li/label/input")
ele_div.click()
time.sleep(5)
final_ele= driver.find_element_by_xpath("//*[@id='__next']/div/div[3]/div/div[2]/div[2]/div/a")
final_ele.click()
time.sleep(5)

print(driver.current_url)

brand_ele=driver.find_element_by_xpath("//*[@id='__next']/div/div[3]/div/div[1]/div/div/div[2]/div[3]/div/span[2]/a[1]")
brand_name=brand_ele.text
if brand_name=="TVS":
    print("Brand Name Ok")




drpdown=driver.find_element_by_xpath("//*[@id='__next']/div/div[3]/div/div[1]/div/div/div[2]/div[5]/div/div[1]/button")
drpdown.click()
time.sleep(2)
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
time.sleep(2)
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