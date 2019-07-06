'''
任雨莹
2017012309
随机生成包括整数、浮点数、字符串、字典在内的多维数组
'''
import random
import string
row = 0
while row < 100:
    line = ""
    column = 0
    while column < 1000:
        # 产生0到100随机整数
        integer = random.randint(0,100)
        # 产生0到100随机浮点数
        f = random.uniform(0,100)
        # 产生随机字典
        dict1 = {random.choice(string.ascii_letters):random.sample(string.ascii_letters+string.digits,3)}
        # 产生随机字符串
        str1 = ''.join(random.sample(string.ascii_letters + string.digits, 3))
        s = str(integer)
        t = str(f)
        u = str(dict1)
        r = s + " " + t + " " + u + " " + str1 + "   "
        while len(r) < 10:
            r = " " + r
        line += r
        column += 1
    print(line)
    row += 1