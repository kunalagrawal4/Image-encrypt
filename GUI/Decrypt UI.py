from tkinter import *
from tkinter import filedialog
import os
from PIL import ImageTk, Image
import decryption



def choose_File():
    filename = filedialog.askopenfilename()
    entry1.insert(0,str(filename))

def choose_File1():
    filename = filedialog.askopenfilename()
    entry2.insert(0,str(filename))


def openFileForchipher():
    path = entry3.get()
    window = Toplevel(root)
    window.title(path)
    window.geometry("1200x1200")
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()



root =Tk()

frame1=Frame(root)
frame1.pack(side=TOP)

topFrame = Frame(root)
topFrame.pack(side= TOP)


middleFrame = Frame(root)
middleFrame.pack(side=TOP)

decrypt =Frame(root)
decrypt.pack(side=TOP)

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


label0 = Label(decrypt, text = "" ,width = 125)

def processing():
    label0['text'] = "processing"
    
    
def decrypt_image_1():
    processing()
    f1=entry1.get()
    f2=entry2.get()
    decryption.decrypt_image(f1,f2)
    label0['text'] = "succesfull"
    path = os.getcwd() + "\original.png"
    entry3.insert(0,str(path))

    
label_1 = Label(frame1, text ="Images to be dencrypted : ",width = 125)
entry1 = Entry(topFrame,width =100)
button1 = Button(topFrame, text = "Select Image",command = choose_File)

entry2 = Entry(middleFrame,width =100 )
button2 = Button(middleFrame, text = "Select Image",command = choose_File1)
# label_1 = Label(decrypt, text ="Images to be dencrypted : ",width = 125)

label_2 = Label(bottomFrame, text ="Images to be dencrypted : ",width = 125)
entry3 = Entry(bottomFrame,width =100)
button4 = Button(bottomFrame, text="Open Image",command = openFileForchipher)


button3 = Button(bottomFrame, text = "Generate Arnold Cat Map",command = decrypt_image_1 , width=20)


label_1.pack(side = TOP)
entry1.pack(side = LEFT)
button1.pack(side = LEFT)
entry2.pack(side=LEFT)
button2.pack(side = LEFT)


button3.pack(side= TOP)
label0.pack(side =TOP)
entry3.pack(side = LEFT)
button4.pack(side = LEFT)


root.mainloop()