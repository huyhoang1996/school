#!/usr/bin/python
from tkinter import *
from tkinter import scrolledtext
import os
import raw_data

root = Tk()
root.title("Welcome to LikeGeeks app")
root.geometry('700x400')
def clicked():
	# print (raw_data.show_data())
	txt.insert(INSERT, raw_data.data_is_exist )


lbl = Label(root, text="Đồ Án Cơ sở Ngành Mạng")
lbl.grid(column=0, row=0, columnspan=2)

btn = Button(root, text="Thực hiện", command=clicked)
btn.grid(column=1, row=3)

txt = scrolledtext.ScrolledText(root,width=80,height=15)
txt.grid(column=1,row=5, columnspan=5, rowspan=10, sticky=W+E+N+S)

root.mainloop()
