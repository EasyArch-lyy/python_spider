import pymongo
import redis
import datetime
import random
import time

#默认连接
# client=redis.StrictRedis()
# 远程连接(ip,port,password)
# client=redis.StrictRedis(host='192.168.56.1',port=2739,password='123456')

connection=pymongo.MongoClient()
db=connection.test
handler_1_by_1=db.Data_1_by_1