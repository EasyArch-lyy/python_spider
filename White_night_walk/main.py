import pymongo
import requests
import re
import os
import lxml.html
import redis


def get_toc(html):
    '''
    获取每章节链接,存储到一个列表中并返回
    :param html: 目录源代码
    :return: 每章链接
    '''
    toc_url_list=[]
    toc_block = re.findall('<ul>(.*?)</ul>', html, re.S)[0]
    # print(toc_block)
    toc_url=re.findall('<li><a href="(.*?)" title="', toc_block, re.S)
    for url in toc_url:
        toc_url_list.append(url)
        print(url)
    return toc_url_list

def get_article(html):
    '''
    获取每一章正文返回章节名和正文
    :param html: 正文源代码
    :return: 章节名,正文    返回元组
    '''
    # 正则表达式中的三组括号把匹配结果分成三组
    #
    # group() 同group（0）就是匹配正则表达式整体结果
    # group(1) 列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分，group(3) 列出第三个括号匹配部分。
    # 没有匹配成功的，re.search（）返回None
    chapter_name=re.search('size="4"> (.*?)<',html,re.S).group(1)
    text_block=re.search('<p>(.*?)</p>',html,re.S).group(1)


    return chapter_name,text_block

# 使用xpth获取index页面各章链接
def xpathTest(html):
    selector = lxml.html.fromstring(html)
    url_list=selector.xpath('//div[@class="book_list"]/ul/li/a/@href')
    for url in url_list:
        # client.lpush
        print(url)
    return url_list

    # 连接池
    # pool = redis.ConnectionPool(host="127.0.0.1", port=6379, max_connections=1024)
    # conn = redis.Redis(connection_pool=pool)
    # q=conn.get("se")
    # print(q)
def redisTest(list):
    client = redis.StrictRedis()
    for url in list:
        client.lpush('url_queue',url)

#借助缓存获取链接写mongo
def getRedis():
    '''
    将每一章保存在mongo
    :param chapter:章节名,第x章
    :param article:正文内容
    :return: None
    '''
    contetn_list=[]
    client = redis.StrictRedis()
    connection = pymongo.MongoClient()
    db = connection.test
    collection = db.redsi
    while client.llen('url_queue')>0:
        url=client.lpop('url_queue').decode()
        source=requests.get(url).content.decode()
        selector = lxml.html.fromstring(source)
        # url_list=selector.xpath('//div[@class="book_list"]/ul/li/a/@href')
        # s1=selector.xpath('')
        print(source)
        s={
            'text':source
        }
        collection.insert(s)
        # break
        # results = collection.insert(index)
        # break

        # selector=html.fromstring(index)
        # chapter_name=selector.xpath('//div[@class="hltitle"]/hl/text()')[0]
        # content=selector.xpath('//div[@id="htmlContent"]/p/text()')
        # contetn_list.append({'title':chapter_name,'content':'\n'.join(content)})
    # client.insert(contetn_list)


if __name__ == '__main__':
    html = requests.get('http://dongyeguiwu.zuopinj.com/5525/').content.decode()
    # 获取每章链接 或s=get_toc(html)
    # s=xpathTest(html)
    # redisTest(s)
    getRedis()
