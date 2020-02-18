#XPath语法练习

import lxml.html

source='''
<html>
    <head>
        <title>测试</title>
    </head>
    <body>
        <div class="userful">
            <ul>
                <li class="info">我所需要的内容1</li>
                <li class="info">我所需要的内容2</li>
                <li class="info">我所需要的内容3</li>
            </ul>
        </div>
        <div class="useless">
            <li class="info">垃圾1</li>
            <li class="info">垃圾2</li>
        </div>
    </body>
</html>
'''
selector=lxml.html.fromstring(source)
info=selector.xpath('//div[@class="useless"]/li/text()')
print(info)