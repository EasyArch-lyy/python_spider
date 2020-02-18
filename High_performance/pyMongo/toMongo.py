import pymongo
import datetime
import random
import time

# 比较逐条插入和批量插入速度类

#连接
connection=pymongo.MongoClient()
db=connection.test
handler_1_by_1=db.student
handler_bat=db.Data_bat

today=datetime.date.today()

# 逐条插入
start_1_by_1=time.time()
for i in range(10000):
    delta=datetime.timedelta(days=i)
    fact_date=today-delta
    handler_1_by_1.insert({'time':str(fact_date),'data':random.randint(0,10000)})
end_1_by_1=time.time()

# 批量插入数据
start_bat=time.time()
insert_list=[]
for i in range(10000):
    delta = datetime.timedelta(days=i)
    fact_date=today-delta
    insert_list.append({'time':str(fact_date),'data':random.randint(0,10000)})
handler_bat.insert(insert_list)
end_bat=time.time()

print('逐条插入耗时:'+end_1_by_1-start_1_by_1)
print('批量插入耗时:'+end_bat-start_bat)