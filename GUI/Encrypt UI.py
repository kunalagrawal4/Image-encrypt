from tkinter import *
from tkinter import filedialog
import os
from PIL import ImageTk, Image
import encryption

def choose_File():
    filename = filedialog.askopenfilename()
    entry1.insert(0,str(filename))
    

def openFileForsecret():
    path = entry2.get()
    window = Toplevel(root)
    window.title(path)
    window.geometry("1200x1200")
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()

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
topFrame = Frame(root)
topFrame.pack()
label0 = Label(topFrame, text = "" ,width = 125)

def processing():
    label0['text'] = "processing"
    
    
def encrypt_image():
    processing()
    encryption.encrypt(entry1.get())
    label0['text'] = "succesfull"
    path = os.getcwd()
    path = path + "\secret_ArnoldcatEnc.png"
    entry2.insert(0,str(path))
    path = os.getcwd()
    path = path + "\ciphered_ArnoldcatEnc.png"
    entry3.insert(0,str(path))

middleFrame = Frame(root)
middleFrame.pack(side=BOTTOM)

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

encryptionFrame = Frame(root)
encryptionFrame.pack(side=BOTTOM)

label_1 = Label(topFrame, text ="Image to be Encrypted : ",width = 125)
entry1 = Entry(topFrame,width =100)
button1 = Button(topFrame, text = "Select Image",command = choose_File)

button2 = Button(topFrame, text = "Generate Arnold Cat Map",command = encrypt_image , width=20)
entry2 = Entry(middleFrame,width =80 )
button3 = Button(middleFrame, text="Open Image",command = openFileForsecret)

entry3 = Entry(bottomFrame,width =80)
button4 = Button(bottomFrame, text="Open Image",command = openFileForchipher)

label_1.pack(side = TOP)
entry1.pack(side = TOP)
button1.pack(side = TOP)
label0.pack(side =TOP)
button2.pack(side =TOP)

entry2.pack(side=LEFT)
button3.pack(side=LEFT)

entry3.pack(side = LEFT)
button4.pack(side = LEFT)


root.mainloop()