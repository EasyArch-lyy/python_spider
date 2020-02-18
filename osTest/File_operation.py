import os
'''
文件操作
'''
# 将~/表示/home路径的方式转化为Python能认识的绝对路径
real_path=os.path.expanduser('~/readme.txt')
with open('/home/lyy/readme.txt',encoding='utf-8')as f:
    # 读取所有行,并以列表形式返回
    content_list=f.readlines()
    # 直接把文件里面所有内容用字符串返回
    content=f.read()
    # print(content_list)
    print(content)
    f.close()
'''
文件读写操作
'''
with open('../new.txt', 'w', encoding='utf-8')as d:
    # 直接将一大端文字写入文本
    d.write("sdadafsdfwefasdg34eqwfadsgsdfvdasf")
    # 把列表所有字符串写入文本
    d.writelines(['sda\n','dsfsd\n','sdfr23wq\n'])