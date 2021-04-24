from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(
    executable_path="D:\software\WOrk\driver\chromedriver_win32\chromedriver.exe")
driver.get("https://evaly.com.bd/categories/speaker-2f615cf9a")

img_ele=driver.find_element_by_xpath("/html/body/reach-portal[1]/div/div/div/section/div/button")
img_ele.click()
time.sleep(3)


# wait = WebDriverWait(driver, 15)
# time.sleep(15)
# wait.until(EC.title_contains(ele5.text))
# el_cl=driver.find_element_by_xpath("/html/body/reach-portal[1]/div/div/div/section/div/button/svg")
# el_cl.click()
ele = driver.find_element_by_xpath(
    "//*[@id='__next']/div/div[3]/div[1]/div[2]/div/div/div/a[2]/div/div[1]/div/img")
value = ele.get_attribute("alt")
print(value)
# ele.send_keys("\n")
ele.click()
print("r*")
wait = WebDriverWait(driver, 10)
wait.until(EC.title_contains(value))
url = driver.current_url
print(url)
# ele2=driver.find_element_by_xpath("//*[@id='__next']/div/div[3]/div/div[3]")
# print(ele2.text)
lst = []
for x in range(1, 6):
    ele3 = driver.find_element_by_xpath(
        "//*[@id='__next']/div/div[3]/div/div[3]/a[{}]/div/div[3]/p".format(x))
    print(ele3.text[1:])
    lst.append(int(ele3.text[1:]))
print(lst)
lst.sort(reverse=True)
print(lst)
for x in range(1, 6):
    ele3 = driver.find_element_by_xpath(
        "//*[@id='__next']/div/div[3]/div/div[3]/a[{}]/div/div[3]/p".format(x))
    ele5 = driver.find_element_by_xpath(
        "//*[@id='__next']/div/div[3]/div/div[3]/a[{}]/div/div[2]/p".format(x))
    if lst[0] == int(ele3.text[1:]):
        ele3.click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_contains(ele5.text))
        url = driver.current_url
        print(url)
        break
print(driver.current_url)
ele4 = driver.find_element_by_xpath(
    "//*[@id='__next']/div/div[3]/div/div[1]/div/div/div[2]/div[3]/div/span[2]/a[1]")
print(ele4.text)
if value == ele4.text:
    print("Everything is alright")
else:
    print("There is something error in the brand name")
time.sleep(5)
driver.close()
