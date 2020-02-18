import requests

# get方法索取网页,得到Response对象
html=requests.get('http://exercise.kingname.info/exercise_requests_get.html')
# 使用.contetn属性显示bytes型网页源代码
html_bytes=html.content
# 将bytes型数据解码为字符串型
html_str=html_bytes.decode()
print(html_str)
# 上三行可合并为
# html_str=requests.get('网址').content.decode()


