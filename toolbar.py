from tkinter import *
def function1():
    print("Menu item is clicked")
root = Tk()

mymenu = Menu(root)
root.config(menu=mymenu)


submenu = Menu(mymenu)
mymenu.add_cascade(label="file", menu="submenu")
submenu.add_command(label="open", command=function1)
submenu.add_command(label="save", command=function1)
submenu.add_command(label="exit", command=function1)

newmenu = Menu(mymenu)

mymenu.add_cascade(label="edit",menu=newmenu)

submenu.add_command(label="cut", command=function1)
submenu.add_command(label="copy", command=function1)
submenu.add_command(label="paste", command=function1)

main.overloop



