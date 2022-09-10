from tkinter import *
from PIL import Image
from PIL import ImageTk

root = Tk()
root.title("Images & Icons")
#root.iconbitmap("@/Pictures/adobe.ico")


# pulling images from folder to display and resize to fit screen
my_image1 = Image.open("./Pictures/Emerger.png")
resized1 = my_image1.resize((500, 450), Image.ANTIALIAS)
new_image1 = ImageTk.PhotoImage(resized1)

my_image2 = Image.open("./Pictures/nymph.jpg")
resized2 = my_image2.resize((500, 450), Image.ANTIALIAS)
new_image2 = ImageTk.PhotoImage(resized2)

my_image3 = Image.open("./Pictures/Scud.jpg")
resized3 = my_image3.resize((500, 450), Image.ANTIALIAS)
new_image3 = ImageTk.PhotoImage(resized3)

my_image4 = Image.open("./Pictures/Prince.jpg")
resized4 = my_image4.resize((500, 450), Image.ANTIALIAS)
new_image4 = ImageTk.PhotoImage(resized4)

my_image5 = Image.open("./Pictures/Stonefly.jpg")
resized5 = my_image5.resize((500, 450), Image.ANTIALIAS)
new_image5 = ImageTk.PhotoImage(resized5)

image_list = [new_image1, new_image2, new_image3, new_image4, new_image5]

#my_label = Label(image=my_img1)
my_label = Label(image=new_image1)
my_label.grid(row=0, column=0, columnspan=3)

# defining forward button functionality 
def forward(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    
    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)
        
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

# defining back button functionality
def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)
        
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    
    
# creating button variables and display
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)



root.mainloop()
