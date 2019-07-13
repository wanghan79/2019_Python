import random
import string

# 随机整数：并输出到xcnhr.txt中
def generateRandomNumber(i):
    while i!=0:
        randomInt=random.randint(1,100000)
        randomFloat=random.random()
        randomChar=random.choice('hhcsbxiaguosbfhdjfdjfdshfdkjfkjfdfjkfkjhfdskjfdioefiofeiifeiofiiefsiojfseioj')
        randomStr=''.join(random.sample(string.ascii_letters + string.digits,random.randint(1,10)))
        dict={str(randomInt):randomStr}
        tup1=(randomInt,randomFloat,randomChar,randomStr,dict)
        yield tup1
        i= i - 1
    return 'done'
g = generateRandomNumber(100000)
f = open("xcnhr.txt", "w", encoding="utf-8")
while True :
    try:
        y = next(g)
        print(y, file = f)
    except StopIteration as e:
        print(e.value)
        break
f.close()