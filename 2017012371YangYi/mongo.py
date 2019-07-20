from data_generate import Generate

from pymongo import MongoClient

class mongo(Generate):

    def build():

        db_name='python_data'

        col_name='sst'

        myclient = MongoClient("mongodb://localhost:27017/")

        mydb=myclient[db_name]

        dblist = myclient.list_database_names()

        if "python_data" in dblist:

          print("数据库已存在！")

        else:

          print("数据库没有存在！！！！")

        col=mydb[col_name]

        collist = mydb.list_collection_names()

        if "sst" in collist:   # 判断 sites 集合是否存在

           print("集合已存在！")

        else:

           print("集合不存在!!!!")    

        for i in range(100000):

          d=Generate().data_crecte()

          col.insert_one(d)      #生成随机数并导入mongo

if __name__ == '__main__':

    mongo.build()
