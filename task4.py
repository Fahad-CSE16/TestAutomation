# //*[@id="__next"]/div/div[3]/div/div[2]/div[1]/div[1]/div[2]/p/a
# //*[@id='__next']/div/div[3]/div/div[2]/div[1]/div[1]/div[2]/p/a
# //*[@id="__next"]/div/div[3]/div/div[2]/div[1]/div[1]/div[2]/p/a
# //*[@id="__next"]/div/div[3]/div/div[2]/div[1]/div[2]/div[2]/p/a
# //*[@id="__next"]/div/div[3]/div/div[2]/div[1]/div[11]/div[2]/p/a
# //*[@id='__next']/div/div[3]/div/div[2]/div[1]
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver =webdriver.Chrome(executable_path="D:\software\WOrk\driver\chromedriver_win32\chromedriver.exe")
driver.get("https://evaly.com.bd/career")


img_ele=driver.find_element_by_xpath("/html/body/reach-portal[1]/div/div/div/section/div/button")
img_ele.click()
time.sleep(3)


try:
    for x in range(1,12):
        ele=driver.find_element_by_xpath("//*[@id='__next']/div/div[3]/div/div[2]/div[1]/div[{}]".format(x))
        ele.click()
        ele2=driver.find_element_by_xpath("//*[@id='__next']/div/div[3]/div/div[2]/div[1]/div[{}]/div[2]/p/a".format(x))
        print(ele2.text)
        if "@evaly.com.bd" in ele2.text:
            print("OK at num {}".format(x))
    print(driver.current_url)
finally:
    driver.close()