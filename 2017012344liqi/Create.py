#-*-coding:utf-8-*-
import random
import string
class Generate:
    def Ggenerate_text(size=100000):
        """
        函数作用：生成数据
        :param size:整形变量 生成数据量的大小参数
        :return:以tuple类型返回生成的数据四项内容分别为：整型，保留五位小数的浮点型，字符串，字典
        """
        dic = {}#建立一个空字典
        save ={}
        for i in range(size):
            dic[random.randint(1, 500000)] = (''.join(random.sample(string.ascii_letters + string.digits, 5)))#生成字典
            save[random.randint(1, 500000)] = (random.randint(1, 999), round(random.uniform(0,999),5),
                  ''.join(random.sample(string.ascii_letters + string.digits, 10)), dic)#生成所需数据
            yield save
            dic.clear()#清空字典内容避免影响下次操作
            save.clear()  # 清空字典内容避免影响下次操作