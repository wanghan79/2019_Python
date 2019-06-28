import random
a={'鱼类':['青鱼','草鱼','鲤鱼','鲫鱼'],
   '兽类':['虎','狼','象','马','鹿'],
   '鸟类':['鸡','鸭','鹅'],
   '两栖':['青蛙','龟','娃娃鱼','蛇','鳄鱼']
   }
l=list(a.keys())
def generaterandom(size):
    while size>0:
        randomint=random.randint(0,100)
        randomfloat=random.random()
        randomchar=random.choice('asdfghjQWERZXC!@#$%^&')
        door=random.choice(l)
        animal=random.choice(a[door])
        temp=(randomint,randomfloat,randomchar,door+'['+animal+']')
        yield temp
        size=size-1
if __name__ == '__main__':
    file = open("out.txt", "w")
    for data in generaterandom(100000):
        file.write(str(data)+'\n')
    file.close()