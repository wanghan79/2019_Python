

import random
import string

for i in range(100000):
    print(rand,end=' ')
    rand_str =  ''.join(random.sample(string.ascii_letters + string.digits,10))
    print(rand_str,end=' ')
    rand=random.randint(1,100)
    key=random.choice(string.ascii_letters)
    dict1={key:rand_str}
    dict2={key:rand}
    print(dict1,dict2)
   
