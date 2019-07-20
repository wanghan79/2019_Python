import string

import random

from pymongo import MongoClient



name = MongoClient('localhost')

db = name.RandomNumber   

emp = db.myrandom  

emp.remove(None)



def Random(i):

    id=0

    while i!=0:

        id+=1

        num=random.randint(1,10)

        str =  ''.join(random.sample(string.ascii_letters + string.digits,num))

        float=random.uniform(1,10)

        rand=random.randint(1,100000)

        key=random.choice(string.ascii_letters)

        dic={key:float}

        t1 = (str,float,rand,dic)

        yield t1

        randomNumber = {

            'D¨°o?':id,

            'int': rand,

            'float':float,

            'string': str,

            'dic': dic,

        }

        emp.insert_one(randomNumber)

        i= i - 1

    return 'done'

g = Random(100000)

f = open("out.txt", "w", encoding="utf-8")

while True :

    try:

        y = next(g)

        print(y, file = f)

    except StopIteration as e:

        print(e.value)

        break

f.close()