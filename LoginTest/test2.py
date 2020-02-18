import requests

# 模拟登录
login_url='http://exercise.kingname.info/exercise_login'
login_success_url='http://exercise.kingname.info/exercise_login_success'

data={
    'username':'kingname',
    'password':'genius',
    'remember':'yes'
}

session=requests.Session()
before_login=session.get('http://exercise.kingname.info/exercise_login_success').text
print(before_login)
print('==========开始登录===========')
session.post(login_url,data=data).text
after_login=session.get('http://exercise.kingname.info/exercise_login_success').text
print(after_login)