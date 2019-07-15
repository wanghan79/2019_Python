# encoding:utf-8
import random
import time

dataCount= 200000    #定义需要产生的数据总数
def genRandomIntnumber():            #产生随机整数的函数
    return random.randint(0, 10)     #产生0-10之间的随机整数

def genRandomFloatnumber():          #产生随机浮点数
    return random.uniform(1, 10)      #浮点数的范围是0-10

def genRandomString():              #产生随机的字符串
    return random.choice(['apple', 'pear', 'peach', 'orange', 'lemon'])  #从其中选取一个作为返回值

def genRandomDict():                #产生随机的字典
    x = {'河北省': ['石家庄', '唐山', '秦皇岛', '承德'],          #给定一些字典对应的键值对
         '山东省': ['济南', '青岛', '临沂', '淄博'],
         '湖南省': ['长沙', '衡阳', '湘潭', '邵阳', '岳阳', '株洲'],
         '江西省': ['南昌', '九江', '上饶', '景德镇']}
    s = list(x.keys())                                               # 省列表
    province = random.choice(s)                                      # 随机选一个省
    city = random.choice(x[province] )                               # 随机选一城市
    return province+':'+city


def FunGenerate(fileName, dataCount):                      #定义函数，调用相应的函数产生
    outputfile = open(fileName, 'w')
    i = 0
    while i < dataCount:
        intNumber=genRandomIntnumber()
        floatNumber=genRandomFloatnumber()
        String=genRandomString()
        Dict=genRandomDict()
        mLine = "%i %d %f %s %s\n" % (i + 1,intNumber,floatNumber,String,Dict)
        outputfile.write(mLine)
        i += 1
    outputfile.close()


if __name__ == "__main__":
    random.seed()
    start = time.time()
    FunGenerate('db_test.txt', dataCount)
    end = time.time()
    print('use times:%d' % (end - start))
    print('congratulation,you finish the work.')