# import necessary libraries
from tkinter import *
# setting up main window
root = Tk()
root.geometry('400x300')
root.title("main")
# function to open new (Top Level) window
def topwin():
    # setting up top window
    top = Toplevel()
    top.geometry('180x100')
    top.title("toplevel")
    # addinga label widget to top window
    l2 = Label(top, text = "this is toplevel window")
    l2.pack()
    top.mainloop()
# adding label and button widget to root (main) window
l = Label(root,text = "this is root window")
btn = Button(root, text ="Click here to spawn another window", command = topwin)
# arranging widgets
l.pack()
btn.pack()
root.mainloop()