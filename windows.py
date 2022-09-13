from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Windows")


def open():
    global my_image
    top = Toplevel()
    top.title("Second Window")
    my_image1 = Image.open("./Pictures/Emerger.png")
    resized1 = my_image1.resize((500, 450), Image.ANTIALIAS)
    new_image1 = ImageTk.PhotoImage(resized1)
    my_label = Label(top, image=new_image1).pack()
    button2 = Button(top, text="Close Window", command=top.destroy).pack()
    
    
    
button = Button(root, text="Open Second Window", command=open).pack()


mainloop()