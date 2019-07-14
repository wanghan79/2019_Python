import pymongo
from RandomNumber import create_number
MONGO_URL="mongodb://localhost:27017/"
MONGO_DB="data"

myclient = pymongo.MongoClient(MONGO_URL)
mydb = myclient[MONGO_DB]
mycol=mydb["RandomNumbers"]
def link_MongoDB():
    f = open("output_data.txt", "w")
    x =mycol.delete_many({})
    for i in range(100000):
        new_data=create_number()
        mydict = {'_id': i, 'content': new_data}
        x=mycol.insert_one(mydict)
        new_data = str(new_data)
        f.write(new_data + '\n')
    f.close()
link_MongoDB()
