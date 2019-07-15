import numpy as np
import matplotlib.pyplot as plt
import sqlite3


# 更改 matplotlib 的配置
plt.rcParams['font.sans-serif'] = ['STFangsong']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# 操作 SQLite 数据库 读取相关数据
conn = sqlite3.connect('Data/universe_civilization.db')
cursor = conn.cursor()
cursor.execute('SELECT COUNT(type) FROM Civilization WHERE type="碳基生命"')
numa = cursor.fetchone()
cursor.execute('SELECT COUNT(type) FROM Civilization WHERE type="硅基生命"')
numb = cursor.fetchone()
cursor.execute('SELECT COUNT(type) FROM Civilization WHERE type="硼基生命"')
numc = cursor.fetchone()
cursor.execute('SELECT COUNT(type) FROM Civilization WHERE type="金属生命"')
numd = cursor.fetchone()
cursor.execute('SELECT COUNT(type) FROM Civilization WHERE type="电磁生命"')
nume = cursor.fetchone()
cursor.execute('SELECT COUNT(type) FROM Civilization WHERE type="恒星生命"')
numf = cursor.fetchone()


# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()

print(numa[0], numb[0], numc[0], numd[0], nume[0], numf[0])
num = [numa[0], numb[0], numc[0], numd[0], nume[0], numf[0]]
lifeType = ['碳基生命', '硅基生命', '硼基生命', '金属生命', '电磁生命', '恒星生命']


plt.scatter(lifeType, num, c='y', marker=7, s=200)
plt.plot(lifeType, num, c='black')
# plt.scatter()

plt.show()
# 散点图 scatter
# 折线图 plot
# 条形图 bar
# 直方图 hist
