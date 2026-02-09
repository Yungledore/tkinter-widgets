# Make sure you upload image into your current repl
# import all the necessary libraries
# PIL (Pythin imaging library) provides image editing capabilities to the python interpreter
from tkinter import *
from PIL import Image, ImageTk
# Create a window with a title bar andset its geometry as well
root = Tk()
root.title('image')
root.geometry('400x400')

# now we use image.open to open andidentify the given image file
upload = Image.open('img.png')
# convert this image to tkinter compatible image
image = ImageTk.PhotoImage(upload)
# add image to tkinter label
label = Label(root, image=image, height=350,width=300)
label.place(x=50,y=0)
label2 = Label(root,text="This is how you add image in tkinter window")
label2.place(x=40,y=360)
# run the application
root.mainloop()