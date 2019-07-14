import random
a={'ÓãÀà':['ÇàÓã','²ÝÓã','ÀðÓã','öêÓã'],
   'ÊÞÀà':['»¢','ÀÇ','Ïó','Âí','Â¹'],
   'ÄñÀà':['¼¦','Ñ¼','¶ì'],
   'Á½ÆÜ':['ÇàÍÜ','¹ê','ÍÞÍÞÓã','Éß','öùÓã']
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