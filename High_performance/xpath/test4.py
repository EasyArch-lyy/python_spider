# 对XPath返回的对象执行XPath

import lxml.html

html1='''
<!DOCTYPE html>
<html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>测试</title>
    </head>
    <body>
        <div class="useless">
            <ul>
                <li class="info">垃圾1</li>
                <li class="info">垃圾2</li>
            </ul>
        </div>
        <div class="useful">
            <ul>
                <li class="info">需要的内容1</li>
                <li class="info">需要的内容2</li>
                <li class="info">需要的内容3</li>
            </ul>    
        </div>
    </body>
</html>
'''
selector =lxml.html.fromstring(html1)
useful=selector.xpath('//div[@class="useful"]')
info_list=useful[0].xpath('ul/li/text()')
print(info_list)
