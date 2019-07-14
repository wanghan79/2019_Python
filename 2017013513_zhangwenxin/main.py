import time
import random
from connect_to_mongodb import db
from generate_date import date
from visual import plot


def write():
    # 导入mongodb
    tmp = [{'value': i} for i in date]  # date整合进dict
    db.insert_many(tmp, ordered=False)  # 写入所有数据


def insert():
    # 增加一条数据
    ins_date = {'value': random.randint(0, 100)}
    db.insert(ins_date)
    print('成功增加数据: ', ins_date)


def delete():
    # 删除一条数据
    del_date = {'value': random.randint(0, 100)}
    db.delete_one(del_date)
    print('成功删除数据: ', del_date)


def search(condition=None):
    # 查找数据
    result = db.find(condition)
    return result


def change():
    # 修改数据
    try:
        condition = {'value': 1}  # 查询条件 x=1的数据
        result = list(search(condition))
        new_date = {'value': random.randint(0, 100)}
        db.update(result[0], {"$set": new_date})  # 对查询到的第一条数据进行修改
        print('成功将:{} 修改成: {}'.format(result[0], new_date))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    write()
    print('成功写入10w条随机数据！\n')

    insert()
    print()
    time.sleep(2)

    delete()
    print()
    time.sleep(2)

    result = search({'value': {'$gte': 0, '$lt': 10}})  # 查询条件 [0, 10)间的数据
    print('0-10间的数据有:\n', list(result))
    print()
    time.sleep(2)

    change()
    print()
    time.sleep(2)

    plot()

