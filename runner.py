from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from upgrading.compare_json_files import compare_update_client_json_gitlab
from utils import utils

def selectPath():
    path_=askopenfilename()
    compare_update_client_json_gitlab(path_)
    path.set(path_)


root = Tk()
root.title("测试工具v1.0")
root.geometry('1280x800')                 #是x 不是*
notebook  = ttk.Notebook(root)
frameOne = Frame()
frameTwo = Frame()
frameThree=Frame(height=1250, bd=1, relief=SUNKEN)
# 第一层frame
notebook.add(frameOne, text='用户')
notebook.add(frameTwo, text='系统')
notebook.add(frameThree,text='pc升级')
notebook.pack(padx=10, pady=5, fill=BOTH, expand=True)

path=StringVar()

# 第二层frame--第3个标签top

frame_t=Frame(frameThree,height=900,bd=1,relief=SUNKEN)
label1=Label(frame_t,text='git下载文件地址：',font=("微软雅黑", 12)).grid(row=0,column=0)
entry=Entry(frame_t,textvariable=path).grid(row=0,column=1)
button=Button(frame_t,text='路径选择',command=selectPath).grid(row=0,column=2)
frame_t.pack(fill=X,padx=1,pady=1)

#第二层frame--第3个标签down
# frame_d=Frame(frameThree,height=400,bd=1,relief=SUNKEN)
scroll = Scrollbar()
scroll.pack(side=RIGHT,fill=Y)
text = Text(wrap="word")
text.pack(side="left",fill=X, expand=True,padx=10)
text.tag_configure("stderr", foreground="#b22222")
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

sys.stdout = utils.TextRedirector(text, "stdout")
sys.stderr = utils.TextRedirector(text, "stderr")
# frame_d.pack(fill=X,padx=1,pady=1)

root.resizable(width=False, height=True) #宽不可变, 高可变,默认为True
root.mainloop()


