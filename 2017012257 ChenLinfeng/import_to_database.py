import pymongo
client=pymongo.MongoClient('localhost',12345)
mydb=client.linfengchen
mycollection=mydb.text

# 打开需要存入的文件, 并将数据存入到数据库
with open('db_test.txt', 'r') as f:
    for line in f.readlines():
        items = line.strip('\r').strip('\n').split(' ')
        # 添加到数据库
        mycollection.insert_one({'ID':items[0], 'intnumber': items[1], 'doublenumber': items[2], 'string': items[3],'dict':items[4]})
# 查询数据库中自己导入的记录并输出
for s in mycollection.find():
    print(s)