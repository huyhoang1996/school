#!/usr/bin/python

# import Tkinter as tk
# from Tkinter import *
from tkinter import *
from tkinter import scrolledtext
import fifo
root = Tk()

root.title("Welcome to LikeGeeks app")
root.geometry('600x400')

def clicked():
	print (fifo.process(2 , [1, 3]))
	txt.insert(INSERT, fifo.process(2 , [1, 3]))

txt = scrolledtext.ScrolledText(root,width=70,height=20)
txt.grid(column=1,row=2)

lbl = Label(root, text="Hello")
lbl.grid(column=0, row=0)

btn = Button(root, text="Click Me", command=clicked)
btn.grid(column=1, row=1)

root.mainloop()
