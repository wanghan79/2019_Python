import random
import string

# 随机整数：并输出到mpx.txt中
def generateRandomNumber(i):
    while i!=0:
        Int=random.randint(1,100000)
        Float=random.random()
        Char=random.choice('ud7hfji8jkgikgjksdjgshjgdsgjgdsjjkdkdgsjkgdsgdjdsghgdsgdjskjdgsjkdgkgd')
        Str=''.join(random.sample(string.ascii_letters + string.digits,random.randint(1,10)))
        dict={str(Int):Str}
        lop=(Int,Float,Char,Str,dict)
        yield lop
        i= i - 1
    return 'done'
g = generateRandomNumber(100000)
f = open("mpx.txt", "w", encoding="utf-8")
while True :
    try:
        y = next(g)
        print(y, file = f)
    except StopIteration as e:
        print(e.value)
        break
f.close()
