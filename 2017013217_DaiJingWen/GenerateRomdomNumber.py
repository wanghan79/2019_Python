#随机生成100000条数据并将其输入到out.txt中
import random
x={'中国':['北京','上海','广州','台湾','香港','澳门','重庆'],
   '美国':['华盛顿','纽约','洛杉矶','金州','夏威夷'],
   '英国':['曼彻斯特','伦敦','德比郡','利物浦','牛津','剑桥'],
   '德国':['慕尼黑','柏林','斯图加特','美因兹']}
s=list(x.keys())
def RandomNumber(i):
    while i!=0:
        country = random.choice(s)
        city = random.choice(x[country])
        randomInt = random.randint(0, 100)
        randomFloat = random.random()
        randomChar = random.choice('dhurgweFDSFEWFGH!@#$%^&*()_+哈我乐')
        tup1 = (randomInt, randomFloat, randomChar,country + ": [" + city + "]")
        yield tup1
        i = i - 1
    return 'done'


r = RandomNumber(100000)
f = open("out.txt", "w", encoding="utf-8")
while True :
    try:
        y = next(r)
        print(y, file = f)
    except StopIteration as e:
        print(e.value)
        break
f.close()
