from pymongo import MongoClient

client=MongoClient()
database=client.runoob
collection=database.name
data={'id':123,'name':'kingname','age':20,'salary':999999}
collection.insert(data)