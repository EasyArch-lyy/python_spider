#加请求头爬虫访问ajax加载后的页面

import requests
import json

url='http://exercise.kingname.info/exercise_headers_backend'

headers={
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'anhao': 'kingname',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=utf-8',
    'Cookie': '__cfduid=d840e7495dddd50fdaaa1dd95286c1bc81580270731',
    'Host': 'exercise.kingname.info',
    'Referer': 'http://exercise.kingname.info/exercise_headers.html',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
html_json=requests.get(url,headers=headers).content.decode()
html_dict=json.loads(html_json)
print(html_dict)