#假的异步加载
import requests
import re
import json

url='http://exercise.kingname.info/exercise_ajax_2.html'
html=requests.get(url).content.decode()

code_json=re.search("secret = '(.*?)'",html,re.S).group(1)
code_dict=json.loads(code_json)
print(code_dict['code'])