import json
import requests
import re

url='http://exercise.kingname.info/exercise_ajax_2.html'
html=requests.get(url).content.decode()
print(html)
# code_json=re.search("secert='(.*?)'",html,re.S).group(1)
# code_dict=json.loads(code_json)
# print(code_dict['code'])
# person={
#     'basic_info':{
#         'name':'kingname',
#         'age':24,
#         'sex':'male',
#         'merry':False
#     },
#     'work_info':{
#         'salary':99999,
#         'position':'engineer',
#         'department':None
#     }
# }

# person_json=json.dumps(person)
# print(person_json)
# 便于阅读缩进
# person_json_indent=json.dumps(person,indent=4)
# print(person_json_indent)