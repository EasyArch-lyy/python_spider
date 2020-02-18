from bs4 import BeautifulSoup
import requests

html=requests.get('http://exercise.kingname.info/exercise_bs_1.html').content.decode()
soup=BeautifulSoup(html,'lxml')
info=soup.find(class_='test')
print('使用find方法,返回对象类型为:'+{type(info)}.__str__())
print(info.string)