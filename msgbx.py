from tkinter import messagebox
import tkinter.messagebox
from tkinter import *
import ctypes
import ctypes.wintypes
from win10toast import ToastNotifier

#a = messagebox.showinfo("提示","我是一个提示框")
#messagebox.showwarning(title='警告', message='这是一条警告') 
#root=Tk()

#root.withdraw()#隐藏主窗口
#a = tkinter.messagebox.showinfo(title='提示',message='设置成功')

# 定义 MessageBoxW 函数
#MessageBox = ctypes.windll.user32.MessageBoxW
#MessageBoxW = ctypes.windll.user32.MessageBoxW
#
## 定义 MessageBox 参数
#MB_OK = 0
#MB_OKCANCEL = 1
#MB_YESNOCANCEL = 3
#MB_YESNO = 4
#
## 显示系统提示框
## 参数：窗口句柄、文本、标题、类型
#result = MessageBox(None, '这是一条提示信息', '提示', MB_OK)
#if result == 1:
#    print("用户点击了OK")
#elif result == 2:
#    print("用户点击了Cancel")

toaster = ToastNotifier()
# 显示通知
# 参数：标题、消息、图标（可选）、持续时间
toaster.show_toast("通知标题", "这是通知内容", duration=1)

# 注意：程序需要保持运行状态直到通知结束
import time
while toaster.notification_active(): time.sleep(0.1)
time.sleep(5)
print('done')
while toaster.notification_active(): time.sleep(0.1)