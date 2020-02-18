#手动打码

import requests
import lxml.html

url='http://exercise.kingname.info/exercise_captcha.html'
url_check='http://exercise.kingname.info/exercise_captcha.check'

session=requests.Session()
html=session.get(url).content
selector=lxml.html.fromstring(html)
captcha_url=selector.xpath('//img/@src')[0]

# 下载验证文件
image=requests.get('http://exercise.kingname.info/'+captcha_url).content
with open('captcha.png','wb')as f:
    f.write(image)

captcha=input('输入图片内容:')
after_check=session.post(url_check,data={'captcha':captcha})

print(after_check.content.decode())