# 项目实践
姓名：沈萌

学号：2017011959

1.项目概述

2019项目实践课程期末大作业

2.功能概述

步骤1：random_generator.py:定义一个数据生成的类，在函数中实现了随机生成范围为1-100001的不重复的整数、随机生成指定范围的浮点数、随机生成0~100之间精度为4位小数的浮点数、随机生成长度为6，由大写字母和数字组成的字符串、随机生成字典一系列功能，最后将数据以字典存入.txt文件中

步骤2：mongo_operation.py:连接MongoDB，定义一个实现MongoDB操作的类，实现增、删、改、查功能，同理，在cmd命令行中也可实现

使用以下命令行

显示所有数据库：show dbs

使用我的数据库：use simon_db

显示集合：show collections

查看数据记录总数：db.students.count()

查看所有数据记录：db.students.find()

插入一个记录：var single={'stu_number':[2017011959],'height':159.00,'weight':63.0000,'password':'123ABC'}

db.students.insert(single)

查看插入后是否数量增加：db.students.count()

查找指定条件的数据记录：db.students.find({'stu_number':2017011959})

删除制定条件的数据记录：db.students.remove({'stu_number':2017011959})

步骤3：visual_plot.py:取出mongodb中height和weight运用matplotlib进行散点图和饼图可视化



