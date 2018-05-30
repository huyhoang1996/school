#!/usr/bin/python
from tkinter import *
from tkinter import scrolledtext
import raw_data
import os
# Note: run with root
root = Tk()
root.title("Welcome to LikeGeeks app")
root.geometry('700x400')
def clicked():
	txt.insert(INSERT, raw_data.data_return )
def clear():
	os.system("sudo fuser -k -n tcp 9000")
	txt.delete('1.0', END)

lbl = Label(root, text="ĐỒ ÁN CƠ SỞ NGÀNH MẠNG", fg="red", font=('times', 25, 'bold'))
lbl.grid(column=1, row=0)

lbl = Label(root, text="GVHD: ThS Mai Văn Hà")
lbl.grid(column=1, row=1)

lbl = Label(root, text="SVTH: Nguyễn Hà Huy Hoàng")
lbl.grid(column=1, row=2)

btn = Button(root, text="Thực hiện", command=clicked)
btn.grid(column=0, row=3)

btn = Button(root, text="Xóa", command=clear)
btn.grid(column=1, row=3)

txt = scrolledtext.ScrolledText(root,width=85,height=15)
txt.grid(column=0,row=5, columnspan=5, rowspan=10, sticky=W+E+N+S)

root.mainloop()
