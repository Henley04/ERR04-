from tkinter import *  # 导入tkinter库
from tkinter import font  # 从tkinter库中调用font模块，对字体的属性进行系统的设置
from tkinter.messagebox import *  # 从tkinter库中调用messagebox模块,生成弹窗界面


def reply():  # 定义函数，用于多次生成弹窗
    while True:  # 循环语句，循环return
        showinfo(title="BOMBER", message="HAHAHA!!!You foolish man!")  # 显示弹窗
        showerror(title="BOMBER", message="HAHAHA!!!You foolish man!")  # 显示弹窗


root = Tk()  # 调用Tk()函数建立根窗口
root.title("BOMB!!")  # 设置根窗口标题
root.geometry("400x400")  # 设置根窗口大小
root.resizable(False, False)  # 禁止更改根窗口的大小
ziti = font.Font(family='微软雅黑', size=10, weight=font.BOLD)  # 设置字体的属性
label = Label(root, text="请点击按钮有惊喜等着你", font=ziti)  # 建立文本标签
label.place(relx=0.5, rely=0.5, anchor=CENTER)  # 设置文本标签的摆放位置
create = Button(root, text='惊喜按钮', command=reply, bg="green")  # 创建按钮组件，点击按钮出现弹窗
create.place(relx=0.5, rely=0.5, anchor=CENTER, width=100)  # 设置按钮组件的摆放位置
label.pack()  # 将Label添加到窗口
root.mainloop()  # 让根窗口持续展示
