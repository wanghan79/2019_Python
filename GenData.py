import string
import random
class DataGenerate:
    '''
    功能：生成20万条随机数据
    作者：高晓雨2017012834
    日期：2019年7月
    '''
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


