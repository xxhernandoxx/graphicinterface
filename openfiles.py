from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Open File")

def open():
    global new_image1
    root.filename = filedialog.askopenfilename(initialdir="./Pictures/", title="Select A File", filetypes=(("jpg files","*.jpg"), ("all files", "*.*")))
    #myLabel = Label(root, text=root.filename).pack()
    my_image1 = Image.open(root.filename)
    resized1 = my_image1.resize((500, 450), Image.ANTIALIAS)
    new_image1 = ImageTk.PhotoImage(resized1)
    #myLabel = Label(root, text=root.filename).pack()
    #my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=new_image1).pack()


myButton = Button(root, text="Open File", command=open).pack()

root.mainloop()