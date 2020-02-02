from tkinter import *
from Pillow import ImageTk, Image
import os

import tkinter as tk
import tkinter.messagebox as myMs


file_open = tk.Tk()
file_open.title('My First Window')
img = ImageTk.PhotoImage(Image.open("E:\\Passport.jpg"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")



def myMessage():
    myMs.showinfo('hello', 'kina click gareko')


my_btn = tk.Button(file_open, text='click button', command=myMessage)
my_btn.pack()

my_can = tk.Canvas(width=500, height=600, bg='white')
my_can.pack()

file_open.mainloop()


