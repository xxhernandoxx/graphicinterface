from tkinter import *

root = Tk()

# creating a label widget
myLabel_1 = Label(root, text="Hello World!")
myLabel_2 = Label(root, text="My name is Matthew Hernandez")


def myClick():
    myLabel = Label(root, text="Look! I clicked a button!!")
    myLabel.grid(row=3, column=1)

#creating a button on widget
myButton = Button(root, text="Click Me!", padx=50, pady=10, command=myClick, fg="red", bg="black")


# displaying on the screen
myLabel_1.grid(row=0, column=1)
myLabel_2.grid(row=1, column=1)
myButton.grid(row=2, column=1)


# running loop for window
root.mainloop()

