import re
import csv
#获取网页源代码中的用户名生成csv


with open('source.txt','r',encoding='utf-8')as f:
    source=f.read()
    result_list=re.findall('username="(.*?)"',source,re.S)
    test_list=[]
    # content_list = re.findall('d_post_content j_d_post_content">(.*?)<', index, re.S)
    for i in range(len(result_list)):
        print(result_list[i])
        result = {'username': result_list[i]}
        test_list.append(result)

with open('csvTest/tieba.csv', 'w', encoding='utf-8')as d:
    writer=csv.DictWriter(d,fieldnames=['username'])
    writer.writeheader()
    writer.writerows(test_list)
