import random
import string
def create_number():
    list = []
    int = random.randint(1000, 5000)
    float = random.uniform(10, 100)
    str = ''.join(random.sample(string.ascii_letters + string.digits, 6))
    dict = {}
    key = ''.join(random.sample(string.ascii_letters + string.digits, 5))
    value = ''.join(random.sample(string.ascii_letters + string.digits, 5))
    dict[key] = value
    list = [int,float,str,dict]
    return list
f = open("output_data.txt","w")
for i in range(100000):
    data=create_number()
    print(data)
    data=str(data)
    f.write(data+'\n')
f.close()

