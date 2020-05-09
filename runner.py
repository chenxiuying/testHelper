from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from upgrading.compare_json_files import compare_json
from utils import utils

#测试工具v1.0
class Application(Frame):
    def __init__(self,master=None):
        super().__init__()
        self.master=master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #notebook
        self.notebook = ttk.Notebook(self.master)
        self.frameOne = Frame()
        self.frameTwo = Frame()
        self.frameThree = Frame(height=1250, bd=1, relief=SUNKEN)
        self.notebook.add(self.frameOne, text='用户')
        self.notebook.add(self.frameTwo, text='系统')
        self.notebook.add(self.frameThree, text='pc升级')
        self.notebook.pack(padx=10, pady=5, fill=BOTH, expand=True)

        #升级
        self.path = StringVar()
        self.cookie = StringVar()
        self.frame_t = Frame(self.frameThree, height=900, bd=1, relief=SUNKEN)
        self.label2 = Label(self.frame_t, text="设置cookie", font=("微软雅黑", 12)).grid(row=0, column=0)
        self.entry1 = Entry(self.frame_t,textvariable=self.cookie).grid(row=0,columnspan=2, column=1)

        self.label1 = Label(self.frame_t, text='git下载文件地址：', font=("微软雅黑", 12)).grid(row=1, column=0)
        self.entry = Entry(self.frame_t,textvariable=self.path).grid(row=1, columnspan=2,column=1)
        self.button = Button(self.frame_t, text='路径选择', command=self.selectPath).grid(row=1, column=3)
        self.frame_t.pack(fill=X, padx=1, pady=1)

        #日志框
        self.scroll = Scrollbar()
        self.scroll.pack(side=RIGHT, fill=Y)
        self.text = Text(wrap="word")
        self.text.pack(side="left", fill=X, expand=True, padx=10)
        #self.text.grid(row=8, columnspan=2)
        self.text.tag_configure("stderr", foreground="#b22222")
        self.scroll.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scroll.set)

        sys.stdout = utils.TextRedirector(self.text, "stdout")
        sys.stderr = utils.TextRedirector(self.text, "stderr")

        # 绑定鼠标右键事件
        self.text.bind('<ButtonPress-3>', self.bindRight)

    def bindRight(self,event):
        self.text.delete(0.0,END)


#选择文件
    def selectPath(self):
        try:
            path_ = askopenfilename()
            self.path.set(path_)
            #TODO
            print(self.cookie.get()=="")
            compare_json(path_, self.cookie)
        except Exception as e:
            print("未上传文件")



if __name__=='__main__':
    root=Tk()
    root.title("测试工具v1.0")
    root.geometry('1280x800')
    app=Application(master=root)
    root.resizable(width=False, height=True)
    app.mainloop()







