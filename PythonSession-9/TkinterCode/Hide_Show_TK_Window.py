import tkinter
import datetime 
from tkinter import ttk
win = tkinter.Tk()
def clik():
			import time
			win.withdraw()#to hide window
			time.sleep(3.4)#sleep time
			win.deiconify()#to show window
			
ttk.Button(text="Hide Window",command=clik).grid()


win.mainloop()