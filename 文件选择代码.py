import tkinter as tk
from tkinter import filedialog
'''打开选择文件夹对话框'''
root=tk.Tk()
root.withdraw() #撤除窗口
Folderpath=filedialog.askdirectory() #获得选择好的文件夹
Filepath=filedialog.askopenfilename() #获得选择好的文件
print(Folderpath)
print(Filepath)
