#获得某一楼所有中所偶信息文本块
import re
import csv

with open('../source.txt', 'r', encoding='utf-8')as f:
    source=f.read()
    every_reply=re.findall(' l_post l_post_bright j_l_post_clearfix "(.*?)p_props_tail_props_appraise_wrap',source,re.S)

result_list=[]
#从每层文本块中提取发帖人,内容和时间
for each in every_reply:
    result={}
    result['username']=re.findall('username="(.*?)"',each,re.S)[0]
    result['content']=re.findall('j_d_content">(.*?)<',re.S)[0].replace('','')
    result['reply_time']=re.findall('class="tail-info">(2017.*?)<',each,re.S)

with open('tieba.csv', 'w', encoding='utf-8')as d:
    writer=csv.DictWriter(f,fieldnames=['username','content','reply_time'])
    writer.writeheader()
    writer.writerows(result_list)