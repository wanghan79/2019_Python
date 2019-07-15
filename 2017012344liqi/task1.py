import random
import string
def creat_dic():
    '''
    生成字典类型数据
    键值对大小均为六
    :return:返回字典类型数据
    '''
    dic = {}
    key = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    value = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    dic[key] = value
    return dic

def data_creat(size=100000):
    '''
    生成四种不同类型数据
    :param size:默认参数100000生成十万条数据
    :return;一条一条的返回四种不同类型的数据
    '''
    for i in range(size):
        data = {}
        data['data_int'] = random.randint(0, 100000)
        data['data_float'] = random.uniform(0, 100)
        data['data_str'] = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        data['data_dic'] = creat_dic()
        yield data

f = open("output.txt", "w")  # 以写的形式打开文件如果没有则自动生成
for i in data_creat(100000):
    f.write(str(i) + "\n")  # 将随机生成的数据写入文件
f.close()  # 关闭文件