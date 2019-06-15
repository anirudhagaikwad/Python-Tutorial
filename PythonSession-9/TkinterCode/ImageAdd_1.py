

from tkinter import *
#from PIL import Image, ImageTk
root = Tk()
root.geometry("1255x944")
# photo = PhotoImage(file="1.png")

# For Jpg Images

image = Image.open("img1.jpg")
photo = ImageTk.PhotoImage(image)

varun_label = Label(image=photo)
varun_label.pack()



mahmudul_root.mainloop()
