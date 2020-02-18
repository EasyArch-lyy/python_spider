#基于异步加载的简单登录

import requests
import json

url='http://exercise.kingname.info/exercise_ajax_4.html'
code_json=requests.post(url,json={'username':'kingname','password':'123456'}).content.decode()
code_dict=json.loads(code_json)
print(code_dict['code'])