import random
import string
import matplotlib
import pymongo
import matplotlib.pyplot as plt

class Generaterandom():
    def __init__(self):
        pass

    def dict_generator(self,size,chars=string.ascii_letters + string.digits):
        dict = {}
        k = ''.join(random.choice(chars) for x in range(self.size))
        v = ''.join(random.sample(string.ascii_letters + string.digits, self.size))
        dict[k] = v
        return dict

    def id_g(self,size,chars=string.ascii_letters + string.digits):
        self.size=size
        return ''.join(random.choice(chars) for x in range(self.size))

    def number(self,size=1000):
        self.size=size
        for y in range(1, self.size + 1):
            dict={}
            int_num = random.randint(1, 10000000)
            dict['int']=int_num
            float_number = random.uniform(0, 10000000)
            dict['float']=float_number
            string= self.id_g(random.randint(1, 20))
            dict['str']=string
            dic = self.dict_generator(random.randint(1, 20))
            dict['dictionary']=dic
            yield  dict

rd=Generaterandom()
def connect():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["yydatabase"]
    mycol = mydb["random"]
    return mycol

def insert():
    mycol=connect()
    for x in rd.number(100000):
        mycol.insert_one(x)

def search():
    mycol=connect()
    for x in mycol.find():
        print(x)

def matplot():
    mycol = connect()
    intarray=[]
    for x in mycol.find():
        intarray.append(x['int'])
    # 设置matplotlib正常显示中文和负号
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
    matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号
    plt.hist(intarray, bins=40, normed=0, facecolor="blue", edgecolor="black", alpha=0.7)
    # 显示横轴标签
    plt.xlabel("区间")
    # 显示纵轴标签
    plt.ylabel("频数/频率")
    # 显示图标题
    plt.title("频数/频率分布直方图")
    plt.show()