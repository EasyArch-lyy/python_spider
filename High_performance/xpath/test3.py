# 获取所有属性值包含-key的元素
import lxml.html


html1='''
<!DOCTYPE html>
<html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>测试</title>
    </head>
    <body>
        <div id="abc-key-x">需要的内容1</div>
        <div id="123-key-000">需要的内容2</div>
        <div id="haha-key">需要的内容3</div>
        <div id="useless">不需要的内容</div>
    </body>
</html>
'''
selector =lxml.html.fromstring(html1)
content=selector.xpath('//div[contains(@id,"-key")]/text()')
for each in content:
    print(each)