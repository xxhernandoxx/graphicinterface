from tkinter import *

root = Tk()

# creating a label widget
myLabel_1 = Label(root, text="Hello World!")
myLabel_2 = Label(root, text="My name is Matthew Hernandez")

# displaying on the screen
myLabel_1.grid(row=0, column=0)
myLabel_2.grid(row=1, column=0)


# running loop for window
root.mainloop()

