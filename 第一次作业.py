import random
import string


for i in range(100000):
    ran_str =  ''.join(random.sample(string.ascii_letters + string.digits, 16))
    print(ran_str,end=' ')
    print(random.uniform(1,10),end=' ')
    print(random.randint(1,100),end=' ')
    f=random.randint(1,10)
    dict1={random.choice(string.ascii_letters):random.sample(string.ascii_letters+string.digits,f)}
    print(dict1)
