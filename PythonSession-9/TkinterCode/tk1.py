
import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
from tkinter import ttk # import TTk Module
win = tkinter.Tk()
# Code to add widgets will go here...
#Change Title
win.title("ITS TKinter GUI") 

#Create Labels
y=ttk.Label(win,text='First Label :')
y.grid(row=0,column=0,sticky=tkinter.W)
y.configure(foreground='#b388ff')

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar
var1=tkinter.StringVar()
#Create TextBox
ttk.Entry(win,width=16,textvariable=var1).grid(row=0,column=1)

#Create ComboBox
var2=tkinter.StringVar()
combo=ttk.Combobox(win,width=14,textvariable=var2,state='readonly')
combo.grid(row=4,column=1)
combo['values']=('1','2','3')
combo.current(0)

#Create Check Button
var3=tkinter.IntVar()
b=ttk.Checkbutton(win,text='hello',variable=var3)
b.grid(row=5,columnspan=2)


def testFun():
		x=var1.get()
		print("X is {x}")
#Create Button
ttk.Button(win,text='Submit').grid(row=1,column=1,command=testFun())

win.mainloop()
