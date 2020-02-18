from selenium import webdriver
import time
# 初始化使用ChromeDriver
# 路径不同时使用绝对路径
driver=webdriver.Chrome('./chromedriver')
driver.get('https://www.ctrip.com/')
# 异步加载的内容在自动打开的页面
html=driver.page_source
print(html)