
import tkinter as tk
root = tk.Tk()
root.geometry("400x200")
# use opacity alpha values from 0.0 to 1.0
# opacity/tranparency applies to image and frame
root.wm_attributes('-alpha', 0.7)  
# use a GIF image you have in the working directory
# or give full path
photo = tk.PhotoImage(file="L.gif")
tk.Label(root,image=photo).pack()
root.mainloop()