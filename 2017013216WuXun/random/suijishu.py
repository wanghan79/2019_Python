import random
x={'辽宁省':['沈阳','鞍山','大连','营口','铁岭'],
   '山东省':['济南','青岛','临沂','淄博'],
   '湖南省':['长沙','衡阳','湘潭','邵阳','岳阳','株洲'],
   '江西省':['南昌','九江','上饶','景德镇']}
s=list(x.keys())
def hanshu(i):
    while i!=0:
        sheng = random.choice(s)
        tup1 = (random.randint(0, 100), random.random(), random.choice('qwertyASDFGH~!@#$%^&*()_+-='),
            sheng + ": [" + random.choice(x[sheng]) + "]")
        yield tup1
        i = i-1
    return 'done'
g = hanshu(100000)
f = open("out.txt", "w", encoding="utf-8")
while True :
    try:
        y = next(g)
        print(y, file = f)
    except StopIteration as e:
        print(e.value)
        break
f.close()





