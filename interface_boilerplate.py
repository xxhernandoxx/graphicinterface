from tkinter import *

root = Tk()

# creating the entry widget

enter_data = Entry(root, width=25)
enter_data.grid(row=1, column=1)
enter_data.insert(0, "Enter Your Name: ")


# creating a label widget function
def myClick():
    hello = "Hello " + enter_data.get()
    myLabel = Label(root, text=hello)
    myLabel.grid(row=5, column=1)

# creating a button on widget
myButton = Button(root, text="Click Me!", padx=50, pady=10, command=myClick)


# displaying on the screen
myButton.grid(row=2, column=1)


# running loop for window
root.mainloop()

