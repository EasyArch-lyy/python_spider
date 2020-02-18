from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome('./chromedriver')

try:
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CLASS_NAME,"content")))
except Exception as _:
    print('加载太慢')

print(driver.page_source)