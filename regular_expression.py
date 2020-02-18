import re
# 正则表达式练习
content='我的微博密码是:123456,QQ密码是:33445566,银行卡密码是:888888,Github密码是999abc999,帮我记住他们'
password_list=re.findall(':(.*?),',content)
name_list=re.findall('名字是(.*?),',content)
password_search=re.search('密码是:(.*?),',content)
password_search_not_find=re.search('xxx:(.*?),',content)
without_question_mark=re.findall('密码是:(.*),',content)
with_question_mark=re.findall('密码是:(.*?),',content)
print('不使用问号的结果:{},长度为:{}'.format(without_question_mark,len(without_question_mark)))
print('使用问号的结果:{},长度为:{}'.format(with_question_mark,len(with_question_mark)))
print('找到内容,返回:{}'.format(password_list))
print('找不到任何内容,返回{}'.format(name_list))
print(password_search)
print(password_search.group())
print(password_search.group(1))
print(password_search_not_find)


account_content='我的微博账号是:kingname,密码是:123456,QQ账号是:99999,密码是:33445566,银行卡账号是:55555,密码是:888888,Github账号是:4564546,密码是999abc999,'
account_password=re.findall('账号是:(.*?),密码是(.*?),',account_content)
print('包含多个括号情况下,返回{}'.format(account_password))

big_string_mutil='''
我是kingname,我的微博密码是:123
45678,
'''
password_findall_no_flag=re.findall('密码是:(.*?),',big_string_mutil)
password_findall_flag=re.findall('密码是:(.*?),',big_string_mutil,re.S)
print('不使用re.S的时候:{}'.format(password_findall_no_flag))
print('使用re.S的时候:{}'.format(password_findall_flag))

