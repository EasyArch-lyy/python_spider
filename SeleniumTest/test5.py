#多次请求的异步加载

import json
import re
import requests

# html_json='{"code": "\u884c\u52a8\u4ee3\u53f7\uff1a\u54ce\u54df\u4e0d\u9519\u54e6", "success": true}'
# html_dict=json.loads(html_json)
# print(html_dict)

url='http://exercise.kingname.info/exercise_ajax_3.html'
first_ajax_url='http://exercise.kingname.info/ajax_3_backend'
second_ajax_url='http://exercise.kingname.info/ajax_3_postbackend'

page_html=requests.get(url).content.decode()
secret_2=re.search("secret_2 = '(.*?)'",page_html,re.S).group(1)

ajax_1_json=requests.get(first_ajax_url).content.decode()
ajax_1_dict=json.loads(ajax_1_json)
secret_1=ajax_1_dict['code']

ajax_2_json=requests.post(second_ajax_url,json={'name':'xxx',
                                                'age':20,
                                                  'secret2':secret_1,
                                                  'secret2':secret_2}).content.decode()
ajax_2_dict=json.loads(ajax_2_json)
code=ajax_2_dict['code']
print('最终页面显示的内容'+{code})