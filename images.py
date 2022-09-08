from tkinter import *
from PIL import Image

root = Tk()
root.title("Images & Icons")
img = PhotoImage(file='./Pictures/adobe.png')
root.tk.call('wm', 'iconphoto', root._w, img)



my_img = PhotoImage(Image.open("./Pictures/Emerger.png"))
my_label = Label(image=my_img)
my_label.pack()






button_exit = Button(root, text="Exit Program", command=root.quit)
button_exit.pack()



root.mainloop()
