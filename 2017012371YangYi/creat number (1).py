import random
import string
class Generate:
    def dgenerate(size=100000):
        dic={}
        for i in range(size):
            x=random.randint(1,100)# 随机生成整型数据
            y=random.uniform(1,10)#  随机生成浮点型数据
            z= ''.join(random.sample(string.ascii_letters + string.digits, 5))# 随机生成五个字符的字符串
            dic={x,y,z}
            tp = (x, y, z, dic)#把四个值放入tuple
            yield tp#返回tuple

if __name__ == '__main__':
    f=open("output.txt","w")
    for i in Generate.dgenerate():
        f.write(str(i)+"\n")
    f.close()
