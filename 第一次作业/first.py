import random
import string

for i in range(100000):
    str =  ''.join(random.sample(string.ascii_letters + string.digits, 16))
    print(str,end=' ')
    print(random.uniform(1,10),end=' ')
    print(random.randint(1,100),end=' ')
    x=random.randint(1,10)
    dictionary={random.choice(string.ascii_letters):random.sample(string.ascii_letters+string.digits,x)}
print(dictionary)