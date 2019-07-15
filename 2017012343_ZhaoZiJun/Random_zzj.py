import random
import string
def string_creator (size = 6,chars = string.ascii_uppercase + string.digits):
    """
    返回默认长度为6的大写字母与数字混合的字符串
    """
    return "".join(random.choice(chars) for _ in range(size))
def dictionary_creator ():
    """
    返回一个随机的字典，其key和value都是由string_generator()生成的默认长度为6的大写字母与数字混合的字符串
    """
    dic = {}
    key = string_creator()
    value = string_creator()
    dic[key] = value
    return dic
def data_creat (args=4, size=100000):
    """
    返回生成字典的生成器，每个字典的key值为数据类型，value值为所产生的四中类型的数据，分别是整型，浮点型，字符串，字典
    """
    for i in range(size):
        data = {}
        data['data_int'] = random.randint(0,100000)
        data['data_float'] = random.uniform(0,100)
        data['data_string'] = string_creator()
        data['data_dictionary'] = dictionary_creator()
        yield data

"""
主函数：以写入的方式打开(创建)文件"output.txt"，调用生成字典的生成器data_creat()，将生成的数据写入"output.txt"中
"""
output = open("output.txt","w")
for data in data_creat():
    output.write(str(data)+'\n')
output.close()
