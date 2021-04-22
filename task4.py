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
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "text-blue-500"))
    )

    ele_div=driver.find_element_by_xpath("//*[@id='__next']/div/div[3]/div/div[2]/div[1]")
    print(len(ele_div.find_elements_by_tag_name("div")))
    ele=driver.find_elements_by_class_name("text-blue-500")
    print(len(ele))
    for x in range(1,11):
        ele=driver.find_element_by_xpath("//*[@id='__next']/div/div[3]/div/div[2]/div[1]/div[{}]/div[2]/p/a".format(x))
        print(ele.text)
    print(driver.current_url)
finally:
    driver.quit()