import sqlite3
import NewData
import MySQLdb


# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('Data/universe_civilization.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 执行一条SQL语句，创建表:
cursor.execute('create table Civilization ('
               'id int(20) primary key, '
               'name varchar(20), age float(20), '
               'grade char(1), type varchar(20), '
               'positionX int(10), '
               'positionY int(10), '
               'positionZ int(10))')

count = 0
while count < 200000:
    civ = NewData.Civilization()
    # print('文明名称：', test.name, file=f)
    # print('文明历史：', test.age, file=f)
    # print('文明等级：', test.grade, file=f)
    # print('生命类型：', test.type, file=f)
    # print('文明坐标：', test.position, file=f)
    cursor.execute("insert into Civilization ("
                   "id, name, age, grade, type, positionX, positionY, positionZ) "
                   "values ('%d', '%s', '%lf',  '%s', '%s', '%d', '%d', '%d')" % (
                    count, civ.name, civ.age, civ.grade, civ.type, civ.position['X'], civ.position['Y'],
                    civ.position['Z']))
    count = count + 1


# 通过rowcount获得插入的行数:
cursor.rowcount
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()
