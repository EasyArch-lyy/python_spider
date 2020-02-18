# 连接MongoDB
# 使用pymongo库里面的MongoClient连接MongoDB。需要传入MongoDB的IP及端口
# 其中第一个参数为地址host，第二个参数为端口port（如果不传递参数，默认为27017）
import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient(host='localhost', port=27017)
# 另外也可使用此方法连接MongoDB，MongoClient的第一个参数host还可以直接传入MongoDB的连接字符串，以mongodb开头
# client = MongoClient('mongodb://localhost:27017/')
# 两种方法可以达到同样的连接效果

# 指定数据库
# 在实际操作中我们需要指定操作那个数据库，这里我们用test数据库为例说明，在程序中指定要使用的数据库，：

# 这里调用client的test属性即可返回test数据库。当然，也可以这样指定

db = client['test']
# 这样我们就指定了一个数据库，这两种方法是等价的。如果数据库不存在，则创建数据库，否则切换到指定数据库。

# 指定集合 
# MongoDB的每个数据库包含许多集合（collection），集合类似关系型数据库中的表。

# 指定要操作的集合，这里指定一个集合名称为students。与指定数据库类似，有两种指定方式。

collection = db.students
# collection = db['students']
# 这样我们便声明了一个Collection对象，这两种方法是等价的。如果集合不存在，则创建集合，否则切换到指定集合。

# 插入数据 
# 接下来对集合students进行插入数据操作，新建一条以字典形式表示的学生数据

student = {
    'id': '1',
    'name': '林先生',
    'age': 20,
    'gender': 'male'
}
# 指定了学生的学号、姓名、年龄和性别。接下来调用collection的insert()
# 方法插入数据，代码如下：

# results = collection.insert(student)
# print(results)
# 在MongoDB中，每条数据都有一个_id属性来表示唯一标识。如果没有显式指明该属性，MongoDB会自动产生一个ObjectId类型的_id属性。insert()
# 方法会在执行后返回_id值

# 我们也可以插入多条数据，只需要以列表形式传递即可，实例如下

student1 = {
    'id': '2',
    'name': '张先生',
    'age': 21,
    'gender': 'male'
}
student2 = {
    'id': '3',
    'name': '李先生',
    'age': 22,
    'gender': 'male'
}
#
# result = collection.insert([student1, student2])
# print(result)


# 查找数据
# content=collection.find({},{'name':'','age':20})
content_obj=collection.find({'age':20},{'_id':3,'name':22,'gender':'male'})
content=[]
for each in content_obj:
    content.append(each)
# print(content)