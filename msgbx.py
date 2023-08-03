from tkinter import messagebox
import tkinter.messagebox
from tkinter import *

#a = messagebox.showinfo("提示","我是一个提示框")
#messagebox.showwarning(title='警告', message='这是一条警告') 
#print(a)

root=Tk()

root.withdraw()#隐藏主窗口
tkinter.messagebox.showinfo(title='提示',message='设置成功')