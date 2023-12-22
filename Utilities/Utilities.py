# -*- coding:utf-8 -*-
from tkinter import *
import tkinter as tk

root_window =tk.Tk()
# 设置窗口title
root_window.title('工具')
# 设置窗口大小:宽x高,注,此处不能为 "*",必须使用 "x"
root_window.geometry('450x300')
# 设置窗口大小为不可更改的
root_window.resizable(False,False)
# 设置窗口处于顶层
root_window.attributes('-topmost',True)

# 设置主窗口的背景颜色,颜色值可以是英文单词，或者颜色值的16进制数,除此之外还可以使用Tk内置的颜色常量
root_window["background"] = "#C9C9C9"
# 添加文本内,设置字体的前景色和背景色，和字体类型、大小

#进入主循环，显示主窗口
root_window.mainloop()