from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# 越过登录进知乎----------未调通
driver=webdriver.Chrome('./chromedriver')
driver.get("https://www.zhihu.com/signin?next=%2F")

elem=driver.find_element_by_name("SignFlowInput-errorMask undefined SignFlowInput-requiredErrorMask")  #寻找帐号输入框
elem.clear()
elem.send_keys("18522015989")
password=driver.find_element_by_name("password")
password.clear()
password.send_keys("409421lz")
input()
elem.send_keys(Keys.RETURN)#模拟键盘回车键
time.sleep(10)
print(driver.page_source)
driver.quit()