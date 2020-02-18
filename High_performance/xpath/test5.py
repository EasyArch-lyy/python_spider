# 不同标签下文字
import lxml.html

html3='''
<!DOCTYPE html>
<html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>测试</title>
    </head>
    <body>
        <div id="test3">
            左青龙
            <span id="tiger">
                右白虎
                <ul>上朱雀,
                    <li>下玄武</li>
                </ul>
                老牛在当中,
            </span>
            龙头在胸口
        </div>
    </body>
</html>
'''
# 使用xpath获取
seletor =lxml.html.fromstring(html3)
# content=seletor.xpath('//div[@id="test3"]/text()')
# for each in content:
#     print(each)

    # -----------------------------
#使用string(.)获取全部数据     
data=seletor.xpath('//div[@id="test3"]')[0]
into=data.xpath('string(.)')
print(into)
