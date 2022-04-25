from tkinter import *  
from tkinter import filedialog as fd
from PIL import ImageTk,Image  
from tkinter import messagebox
import numpy as np
import cv2

root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# root.geometry("1366x700")

frame1 = Frame(master=root)
frame1.config(background='silver')
frame1.place(height=660, width=600, bordermode=INSIDE, x=20, y=20)
frame1_header = Label(master=frame1, text="Image to Scan")
frame1_header.config(background='silver')
frame1_header.pack()
fr_Image = Frame(master=frame1)
fr_Image.config(background='silver')
fr_Image.place(height=560, width=600, x=0, y=20)

# face_cascade = cv2.CascadeClassifier('cascade.xml')
# img = cv2.imread('pic1.jpeg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# i = 0
# faces = face_cascade.detectMultiScale(gray, 1.3, 5)
# for (x,y,w,h) in faces:
#     img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#     i = i+1

def select_image():
    for Widget in fr_Image.winfo_children():
        Widget.destroy()
    filename = fd.askopenfilename(title='Select Image')
    global str_filename
    str_filename = filename
    # messagebox.showinfo("Title", filename)
    image = Image.open(filename)
    photo = ImageTk.PhotoImage(image)
    # im = Image.fromarray(img)
    # photo = ImageTk.PhotoImage(image=im) 
    label = Label(master=fr_Image, image=photo)
    label.image = photo # keep a reference!
    label.place(relx=0.5, rely=0.5, anchor=CENTER)

btSelect = Button(frame1, text="Select Image", command=select_image)
btSelect.place(height=30, width=100, x=250, y=605)

frame2 = Frame(master=root)
frame2.config(background='gray')
frame2.place(height=660, width=600, bordermode=INSIDE, x=745, y=20)
frame2_header = Label(master=frame2, text="Result")
frame2_header.config(background='gray')
frame2_header.pack()
fr_Count = Frame(master=frame2)
fr_Count.config(background='gray')
fr_Count.place(height=560, width=600, x=0, y=20)
label2 = Label(master=frame2, text="Count = 0")
label2.place(height=30, width=100, x=250, y=605)

def haar_cascade():
    frame2_header = Label(master=frame2, text="Result")
    frame2_header.config(background='gray')
    frame2_header.pack()
    fr_Count = Frame(master=frame2)
    fr_Count.config(background='gray')
    fr_Count.place(height=560, width=600, x=0, y=20)
    # xml_file = fd.askopenfilename(title='Select XML file')

    img = cv2.imread(str_filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    fruits_cascade = cv2.CascadeClassifier('fruits.xml')
    fruits_total = 0
    fruits = fruits_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in fruits:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        fruits_total = fruits_total+1

    apple_cascade = cv2.CascadeClassifier('apple.xml')
    apple = apple_cascade.detectMultiScale(gray, 1.3, 5)
    apple_total = 0
    for (x,y,w,h) in apple:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        apple_total = apple_total+1

    a = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(a)
    photo = ImageTk.PhotoImage(image=im) 
    label = Label(master=fr_Count, image=photo)
    label.image = photo # keep a reference!
    label.place(relx=0.5, rely=0.5, anchor=CENTER)
    label2 = Label(master=frame2, text="Fruits = " + str(fruits_total) + ", Apple = " + str(apple_total))
    label2.place(height=30, width=200, x=200, y=605)

def proceed_image():
    MsgBox = messagebox.askquestion ('Confirmation','Proceed?',icon = 'warning')
    if MsgBox == 'yes':
        for Widget in frame2.winfo_children():
            Widget.destroy()
        haar_cascade()
    else:
        pass

btCount = Button(root, text="COUNT", command=proceed_image)
btCount.place(height=40, width=82, x=640, y=250)

root.mainloop()