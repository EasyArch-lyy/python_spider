import time
import requests
from multiprocessing.dummy import Pool

#比较多线程和单线程爬虫速度

def query(url):
     requests.get(url)

start=time.time()
for i in range(100):
     query('https://baidu.com')
end=time.time()
print('单线程耗时')
print(end-start)

start=time.time()
url_list=[]
for i in range(100):
    url_list.append('https://baidu.com')
pool=Pool(5)
pool.map(query,url_list)
end=time.time()
print('多线程耗时')
print(end-start)