#pymongo
from pymongo import MongoClient

client=MongoClient()
# 远程连接
# 用户名://密码@服务器或域名:端口
# client=MongoClient('mongodb://kingname:12345@0.0.0.0:27019')
# 没密码验证
# client=MongoClient('mongodb://0.0.0.0:27019')

# 初始化数据库
def initDB():
    database=client.test
    collection=database.students
#     方法二:允许批量操作
# database=client[test]
# collection=database[students]

#插入数据
def insert():
    database = client.test
    collection = database.students
    data={'id':123,'name':'kingname','age':20,'salary':9999999}
    collection.insert(data)

# 批量插入
#more_data[
# {'id':1,'name':'xx','age':22,'salary':0},
# {'id':2,'name':'xx','age':22,'salary':0},
# {'id':3,'name':'xx','age':22,'salary':0},
# {'id':4,'name':'xx','age':22,'salary':0}
#]


# 普通查找
def ordinarySelect():
    # find(查询条件,返回字段)
    database = client.test
    collection = database.students
    content=collection.find()
    print(content)

# 逻辑查询
def logicSelect():
    database = client.test
    collection = database.students
    content=[x for x in collection.find({'age':{'$gte':20,'$lte':49}})]

# 查询结果排序
def sortSelect():
    database = client.test
    collection = database.students
    content=[x for x in collection.find({'age':{'$gte':'20','$lte':'49'}}).sort('age',-1)]
    print(content)

# 更新记录
def updateMessage():
    database = client.test
    collection = database.students
    # 参数为字典
    collection.update_one({'age':20},{'$set':{'name':'kingname'}})
    collection.update_many({'age':20},{'$set':{'age':30}})

#  删除记录
def deleteMessage():
    database = client.test
    collection = database.students
    collection.delete_one({'name':'kingname'})   #单个
    collection.delete_many({'name':'kingname'})  #全部

# 查询去重
def Duplicate_removal():
    database = client.test
    collection = database.students
    collection.distinct('age')

if __name__ == '__main__':
    sortSelect()