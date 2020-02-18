import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client['test']
collection = db.students
# 逻辑查询
content=[x for x in collection.find({'age':{'$gt:18'}})]
#对查询结果排序

print(content)