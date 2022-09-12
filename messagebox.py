from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title("Message Box")

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno("This is a popup", "Hello World!")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked yes!").pack()
    else:
        Label(root, text="You clicked no!").pack()


Button(root, text="Popup", command=popup).pack()






mainloop()