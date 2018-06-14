#!/usr/bin/python

# import Tkinter as tk
# from Tkinter import *
from tkinter import *
from tkinter import scrolledtext
import fifo
import sjf
import srt
root = Tk()

root.title("Welcome to LikeGeeks app")
root.geometry('700x400')

def clicked():
	selection = var.get()
	list_time = [int(x) for x in list_burst.get().split(',')]
	if list_arrive.get():
		list_arrive_convert = [int(x) for x in list_arrive.get().split(',')]
	total_pro = int(total.get())
	print (total_pro)
	if selection == 1:
		txt.insert(INSERT, fifo.process(total_pro , list_time))
	if selection == 2:
		txt.insert(INSERT, sjf.process(total_pro , list_time))
	if selection == 3:
		txt.insert(INSERT, srt.process( list_arrive_convert, list_time))


lbl = Label(root, text="ĐỒ ÁN CƠ SỞ NGÀNH MẠNG", fg="red", font=('times', 25, 'bold'), anchor="center")
lbl.grid(column=0, row=0, columnspan=7)

lbl = Label(root, text="GVHD: ThS Mai Văn Hà")
lbl.grid(column=0, row=1, columnspan=7)

lbl = Label(root, text="SVTH: Nguyễn Hà Huy Hoàng")
lbl.grid(column=0, row=2, columnspan=7)

total = IntVar()
list_burst = StringVar()
list_arrive = StringVar()
Label(root, text="Enter the number of process").grid(column=0,row=3, sticky=W)
total = Entry(root, textvariable=total)
total.grid(column=0,row=4, sticky=W)

Label(root, text="Enter the burst time of the processes:    ").grid(column=0,row=5, sticky=W)
list_burst = Entry(root, textvariable=list_burst)
list_burst.grid(column=0,row=6, sticky=W)

Label(root, text="Enter the arrive time of the processes:    ").grid(column=0,row=7, sticky=W)
list_arrive = Entry(root, textvariable=list_arrive)
list_arrive.grid(column=0,row=8, sticky=W)

var = IntVar()
R1 = Radiobutton(root, text="FIFO", variable=var, value=1)
R1.grid(column=1, row=3)

R2 = Radiobutton(root, text="SJF", variable=var, value=2)
R2.grid(column=2, row=3)

R3 = Radiobutton(root, text="SRT", variable=var, value=3)
R3.grid(column=3, row=3)

# R4 = Radiobutton(root, text="Option 4", variable=var, value=4)
# R4.grid(column=4, row=1)

btn = Button(root, text="Thực hiện", command=clicked)
btn.grid(column=1, row=4)

txt = scrolledtext.ScrolledText(root,width=60,height=15)
txt.grid(column=1,row=5, columnspan=5, rowspan=10, sticky=W+E+N+S)

root.mainloop()
