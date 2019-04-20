import random
import string

cout=0
for i in range(100000):
    cout+=1
    print(cout,":",end=' ')
    ran_str =  ''.join(random.sample(string.ascii_letters + string.digits, 16))
    print(ran_str,end=' ')
    print(random.uniform(1,10),end=' ')
    print(random.randint(1,100),end=' ')
    x=random.randint(1,10)
    dict1={random.choice(string.ascii_letters):random.sample(string.ascii_letters+string.digits,x)}
    print(dict1)