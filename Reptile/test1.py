import requests
#post方法获取源代码
data={
   'name':'value1',
   'password':'value2' }
# 使用formdata提交
html_formdata=requests.post('http://exercise.kingname.info/exercise_requests_post',data=data).content.decode()
# 使用json提交
html_json=requests.post('http://exercise.kingname.info/exercise_requests_post',json=data).content.decode()
print(html_formdata)
# print(html_json)