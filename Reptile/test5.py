import re
import os
import requests

def get_toc(html):
    '''
    获取每章节链接,存储到一个列表中并返回
    :param html: 目录源代码
    :return: 每章链接
    '''
    start_url='https://www.kanunu8.com/book3/6879/'
    toc_url_list=[]
    toc_block=re.findall('正文(.*?)</tbody>',html,re.S)[0]
    toc_url=re.findall('href="(.*?)"',toc_block,re.S)
    for url in toc_url:
        toc_url_list.append(start_url+url)
        print(start_url+url)
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

def save(chapter,article):
# def save(chapter):
    '''
    将每一章保存在本地
    :param chapter:章节名,第x章
    :param article: 正文内容
    :return: None
    '''
    os.makedirs('动物农场',exist_ok=True)
    # 若没有文件夹则创建
    with open(os.path.join('/home/lyy/桌面/动物农场',chapter+'.txt'),'w',encoding='GBK')as f:
        f.write(article)
        print('创建完成')


if __name__ == '__main__':
    html = requests.get('https://www.kanunu8.com/book3/6879/').content.decode('GBK')
    s=get_toc(html)
    test=()
    print('开始循环')
    for i in s:
        print(s.index(i))
        html1=requests.get(i).content.decode('GBK')
        test=get_article(html1)
        save(test[0],test[1])