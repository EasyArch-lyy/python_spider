#在网页中获取元素
import lxml.html
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome('./chromedriver')
driver.get('http://exercise.kingname.info/exercise_advanced_ajax.html')
try:
    WebDriverWait(driver,30).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"content"),'通关'))
except Exception as _:
    print('网页加载太慢，结束等待')
#
#
element=driver.find_element_by_xpath('//div[@class="content"]')
print({element.text})

driver.quit()