#模拟浏览器
# chromedriver可以获得加载完成的源代码
from selenium import webdriver
import time

driver=webdriver.Chrome('./chromedriver')
driver.get('http://exercise.kingname.info/exercise_advanced_ajax.html')
time.sleep(5)
html=driver.page_source
print(html)
input('按任意建结束')