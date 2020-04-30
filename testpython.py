import re


#
# def test():
#     str='C:/Users/chenxiuying/Desktop/3.44.18.2004_EasyClientBeta.json'
#     version = re.findall(r"[\d+][\.\d+]*", str)
#     print(version[0])
#     start_index=str.find('_EasyClient')+1;
#     print(str[start_index:-5])
#
# test()


import tkinter as tk
import sys

# class ExampleApp(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         toolbar = tk.Frame(self)
#         toolbar.pack(side="top", fill="x")
#         b1 = tk.Button(self, text="print to stdout", command=self.print_stdout)
#         b2 = tk.Button(self, text="print to stderr", command=self.print_stderr)
#         b1.pack(in_=toolbar, side="left")
#         b2.pack(in_=toolbar, side="left")
#         self.text = tk.Text(self, wrap="word")
#         self.text.pack(side="top", fill="both", expand=True)
#         self.text.tag_configure("stderr", foreground="#b22222")
#
#         sys.stdout = TextRedirector(self.text, "stdout")
#         sys.stderr = TextRedirector(self.text, "stderr")
#
#     def print_stdout(self):
#         '''Illustrate that using 'print' writes to stdout'''
#         print("this is hhh stdout")
#
#     def print_stderr(self):
#         '''Illustrate that we can write directly to stderr'''
#         sys.stderr.write("this is stderr\n")
#
# class TextRedirector(object):
#     def __init__(self, widget, tag="stdout"):
#         self.widget = widget
#         self.tag = tag
#
#     def write(self, str):
#         self.widget.configure(state="normal")
#         self.widget.insert("end", str, (self.tag,))
#         self.widget.configure(state="disabled")
#
# app = ExampleApp()
# app.mainloop()


import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
gitlab_main_url="http://gitlab.easytech-main.com/users/sign_in"
r = requests.get(url=gitlab_main_url, headers=headers)
cookie1 = r.headers['Set-Cookie']


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'cookie':cookie1
}
r1 = requests.get(url=gitlab_main_url, headers=header)
print(r1.headers['Set-Cookie'])










