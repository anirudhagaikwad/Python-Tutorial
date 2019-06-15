
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("733x566")
root.title("Python")

def myfunc():
    print("hello")

def help():
    print("I will help you")
    tmsg.showinfo("Help", "I will help you with this gui")

def rate():
    print("Rate us")
    value = tmsg.askquestion("Was your experience Good?", "You used this gui.. Was your experience Good?")
    if value == "yes":
        msg = "Great. Rate us on appstore please"
    else:
        msg = "Tell us what went wrong. We will call you soon"
    tmsg.showinfo("Experience", msg)

def oro():
    ans = tmsg.askretrycancel("Text")
    if ans:
        print("TXT1")

    else:
        print("TXT2")


mainmenu = Menu(root)

m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)


m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label = "Help", command=help)
m3.add_command(label = "Rate us", command=rate)
m3.add_command(label = "Order", command=oro)
mainmenu.add_cascade(label="Help", menu=m3)
root.config(menu=mainmenu)
root.mainloop()

