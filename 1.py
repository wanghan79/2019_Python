import random
import datetime
import time

dataCount = 10*100*100    #10M.
codeRange = range(ord('a'),ord('z'))
alphaRange = [chr(x) for x in codeRange]
alphaMax = len(alphaRange)
daysMax = 42003
theDay = datetime.date(1900,1,1)

def genRandomName(nameLength):
    global alphaRange,alphaMax
    length = random.randint(1, nameLength)
    name = ''
    for i in range(length):
        name += alphaRange[random.randint(0,alphaMax-1)]
    return name

def genRandomDay():
    global daysMax,theDay
    mDays = random.randint(0,daysMax)
    mDate = theDay + datetime.timedelta(days=mDays)
    return mDate.isoformat()

def genRandomSex():
    return random.randint(0,1)
                                                               
if __name__ == "__main__":
    random.seed()
    start = time.time()
    genDataBase1('db_test.txt',dataCount)
    end = time.time()
    print('use time:%d'%(end-start))
    print('Ok')
