#xpath获取开头相同内容

import lxml.html

html1='''
<!DOCTYPE html>
<html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>测试</title>
    </head>
    <body>
        <div id="test1">需要的内容1</div>
        <div id="test2">需要的内容2</div>
        <div id="testfault">需要的内容3</div>
        <div id="useless">不需要的内容</div>
    </body>
</html>
'''
selector =lxml.html.fromstring(html1)
content=selector.xpath('//div[starts-with(@id,"test")]/text()')
for each in content:
    print(each)