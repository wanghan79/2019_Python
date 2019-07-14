import pymongo

client = pymongo.MongoClient('localhost')  # 数据库
db = client['usage']['date']
