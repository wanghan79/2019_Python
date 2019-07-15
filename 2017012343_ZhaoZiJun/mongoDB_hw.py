import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
#创建数据库和集合
dblist = myclient.list_database_names()
mydb = myclient["zzjDB"]
print("数据库  zzjDB  创建成功！")
mycol = mydb["zzjST"]
print("集合  zzjST  创建成功！")

def insertDB(value1,value2):
	"""
	将具有两个value值的数据传入数据库中，无返回值
	"""
	mydict={"name":value1,"value":value2}
	x = mycol.insert_one(mydict)
#	print(x)
#	print(x.inserted_id)

def findDB(value):
	"""
	传入一个参数，在数据库的name中寻找匹配值，并将其对应的value值
	"""
	for x in mycol.find():
		if x['name']==value :
			print(x['value'])

def showALL():
	"""
	展示当前集合全部内容
	"""
	for x in mycol.find({},{ "_id": 0, "name": 1, "value": 1 }):
		print(x)	


"""
举例：将学生的姓名与学号存入数据库,并进行查询、修改和删除
"""
#因为在本地跑程序时，多次运行导致数据库混乱，故每次清空集合 zzjST
mycol.delete_many({})
insertDB('student1',2017001)
insertDB('student2',2017002)
insertDB('student3',2017003)
insertDB('student4',2017004)
print('数据成功传入，显示如下')
showALL()
print('下面开始查找student3的学号')
findDB('student3')
print('下面，将student2的学号修改为22222，然后展示当前集合全部内容')
myquery={"name":"student2"}
newvalue={"$set":{"value":22222}}
mycol.update_one(myquery,newvalue)
showALL()
print('student4退学了，将其信息从数据库中删除')
myquery={"name":"student4"}
mycol.delete_one(myquery)
showALL()