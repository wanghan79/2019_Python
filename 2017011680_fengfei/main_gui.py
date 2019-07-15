import tkinter
from draw import draw_bar1
from draw import draw_scater1
from PIL import ImageTk
from tkinter import ttk
from tkinter import *
from PIL import Image

root = tkinter.Tk()
root.geometry("800x600")
def showImg(img1):
    draw_bar1()
    load = Image.open('D:out1.png')
    render = ImageTk.PhotoImage(load)
    img = tkinter.Label(image=render)
    img.image = render
    img.place(x=80, y=100)
def showImg1(img1):
    draw_scater1()
    load = Image.open('D:out2.png')
    render = ImageTk.PhotoImage(load)
    img = tkinter.Label(image=render)
    img.image = render
    img.place(x=80, y=100)
bar1 = tkinter.Button(root,text='画柱形图',width=15,height=2,command=lambda :showImg(showImg('D:out1.png')))
bar1.pack()
scater1 = tkinter.Button(root,text='画散点图',width=15,height=2,command=lambda :showImg1(showImg1('D:out2.png')))
scater1.pack()
root.mainloop()

