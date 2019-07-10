import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
mydb = client['ys_db']

filename='gen_data.txt'
f = open(filename, 'r')
lists=f.readlines()
for i in lists:
    mydb.data.insert({'ys':i})
f.close()