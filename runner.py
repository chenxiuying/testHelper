from tkinter import *
from tkinter import ttk
root = Tk()
root.title("测试工具v1.0")
root.geometry('1280x800')                 #是x 不是*
notebook  = ttk.Notebook(root)
frameOne = Frame()
frameTwo = Frame()
frameThree=Frame()
notebook.add(frameOne, text='用户')
notebook.add(frameTwo, text='系统')
notebook.add(frameThree,text='pc升级')
notebook.pack(padx=10, pady=5, fill=BOTH, expand=True)
root.resizable(width=False, height=True) #宽不可变, 高可变,默认为True
root.mainloop()