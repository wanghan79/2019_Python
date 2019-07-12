from tkinter import *
from random_num import *
from moveto_db import *
from matplot_data import *
b = Tk()
Button(b, anchor='center', width=30, height=4, text='生成十万条随机数', bg='blue',activebackground='gray', fg='red', borderwidth=5,compound='bottom', font='20px',command=main_1).pack()
Button(b, anchor='center', width=30, height=4, text='打开生成数据的文本文件', bg='blue',activebackground='gray', fg='red', borderwidth=5,compound='bottom', font='20px',command=read_file).pack()
Button(b, anchor='center', width=30, height=4, text='生成数据并导入数据库', bg='blue',activebackground='gray', fg='red', borderwidth=5,compound='bottom', font='20px',command=main_2).pack()
Button(b, anchor='center', width=30, height=4, text='显示数据库中的内容', bg='blue',activebackground='gray', fg='red', borderwidth=5,compound='bottom', font='20px',command=show_data).pack()
Button(b, anchor='center', width=30, height=4, text='数据可视化', bg='blue',activebackground='gray', fg='red', borderwidth=5,compound='bottom', font='20px',command=main_3).pack()
b.mainloop()