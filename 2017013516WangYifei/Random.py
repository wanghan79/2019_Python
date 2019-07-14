
import random
import string

class Generate:
    def dict(self):
        dict={}
        m=''.join(random.sample(string.ascii_lowercase, 6))
        n=''.join(random.sample(string.ascii_letters + string.digits, 6))        
        dict[m]=n
        return dict
    def data(self): 
        data={}
        data=self.dict()
        return data
f=open("OutputNumber.txt", "w")
list_1 = []
for i in range(25000):
   list_1.append(random.randint(0,9999))
   list_1.append(random.uniform(0, 99))
   list_1.append(''.join(random.sample(string.ascii_letters,6)))
   list_1.append(Generate().data())
print(list_1)
num=str(list_1)
f.write(num)
f.close()









