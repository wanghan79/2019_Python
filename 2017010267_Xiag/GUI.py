from tkinter import *
import tkinter
root = Tk()
def pic():
      # 注意Tk的大小写

    photo = PhotoImage(file='123.gif')
    img_label = Label(root, imag=photo)
    img_label.pack()
    mainloop()

B = tkinter.Button(root, text="点我", command=pic)
B.pack()

if __name__ == '__main__':
    pic()