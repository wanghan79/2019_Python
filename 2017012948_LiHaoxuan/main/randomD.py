import random
import string

dic = {'lhx': 2017012948, 'asd': 132156456, 'adqwe': 99996, 'asd46': '14a56sd41'}  # 手写dic，待会从手写的dic中随机抽取键值对


class DataGenerate:
    "Generate Random Data"

    def dgenerate(args=4, size=100000):
        for i in range(size):
            a = random.randint(1, 99)
            b = random.uniform(0, 100)
            c = ''.join(random.sample(string.ascii_letters + string.digits, 5))  # 随机选择五个字符组成字符串
            d = random.sample(dic.items(), 1)  # 从手写的dic里取key和value，一次只取一个
            tp = (a, b, c, d)  # 把四个值放入tuple
            yield tp  # 返回tuple

    def savedata(self):  # 将data保存至docx中
        f = open("out.txt", "w")  # 打开一个文件只用于写入。如果文件不存在，则创建。

        for i in self.dgenerate():
            s = str(i)  # 把tp转换为字符串
            f.write(s+"\n")  # 写入文件加换行

        f.close()  # 关闭文件

