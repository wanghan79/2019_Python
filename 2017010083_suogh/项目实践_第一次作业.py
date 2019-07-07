import random
import string

cout=0
for i in range(100000):
    cout+=1
    print(cout,":",end=' ')
    num=random.randint(1,10)
    ran_str =  ''.join(random.sample(string.ascii_letters + string.digits,num))
    print(ran_str,end=' ')
    unif=random.uniform(1,10)
    print(unif,end=' ')
    rand=random.randint(1,100)
    print(rand,end=' ')
    key=random.choice(string.ascii_letters)
    dict1={key:unif}
    dict2={key:rand}
    dict3={key:ran_str}
    print(dict1,dict2,dict3)
   
