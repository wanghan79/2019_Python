import random
import string
def randomnumber(i)
'''产生随机数,包括整型，浮点型，字符串，字典''' 
	for(i=0;i<100000;i++)
		randomInt=random.randint(1,100000)
		randomFloat=random.random()
		randomChar=random.chioce(['Chinese','Mathematics','English','Science','Physics','Biology','Chemistry','Computer'])
		stuInfo = {'student' + str(i):random.randint(60,100) for i in range(20)}
		randomDict=name:score for  name,score in stuInfo.items()  if score > 90}
	return 'done'
def dataRandom():
    '''产生的随机数据用tuple存储'''
    for i in range(100000):
        tup=(getRandomInt(),getRandonFloat(),getRandomStr(),getRandomDict())
        #yield tup
        #print(tup)
    return tup
if __name__ == '__main__':
    f = open("output1.txt", "w")
    for i in range(100000):
       d=Generate().data_crecte()#生成的随机数存入txt
       print(d)
       s=str(d)
       f.write(s+'\n')

class DataStorage:
    """Store the data to mongoDB"""

    @staticmethod
    def random_data_storage(mysites, filename):  # 存储size条随机数据
        with open(filename) as file_object:
            for line in file_object:
                mysites.insert_one(eval(line))


import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
mydb = client['ys_db']

filename='gen_data.txt'
f = open(filename, 'r')
lists=f.readlines()
for i in lists:
    mydb.data.insert({'ys':i})


class DataGenerate:
    def dgenerate(size=100000):
        for i in range(size):
            dic = {}
            value=random.randint(1, 10000)
            key=''.join(random.sample(tuple(string.ascii_lowercase + string.digits), 10))
            dic[key]=value
            data=(random.randint(1, 10000),round(random.uniform(1, 1000), 5),
                ''.join(random.sample(tuple(string.ascii_lowercase + string.digits), 10)),dic)
            yield data
if __name__ == '__main__':
    f = open("data.txt", "w")
    for i in DataGenerate.dgenerate():
        s=str(i)
        f.write(s+'\n')
    f.close()
