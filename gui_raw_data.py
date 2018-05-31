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
	if not data.get():
		return txt.insert(INSERT, 'Bạn chưa nhập dữ liệu' )
	if status == 'Bật':
		return txt.insert(INSERT, 'Bạn chưa bật server' )
	os.system("python client.py "+ data.get())
	raw_data.process();
	txt.insert(INSERT, raw_data.result )
def clear():
	txt.delete('1.0', END)

status = 'Bật'
def setServer():
	global status
	if status == 'Bật':
		status = 'Tắt'
		btn_server['text'] = 'Tắt'
		os.system("python server.py &")
	else:
		status = 'Bật'
		btn_server['text'] = 'Bật'
		os.system("sudo fuser -k -n tcp 9000")
		
	txt.delete('1.0', END)


lbl = Label(root, text="ĐỒ ÁN CƠ SỞ NGÀNH MẠNG", fg="red", font=('times', 25, 'bold'))
lbl.grid(column=1, row=0)

lbl = Label(root, text="GVHD: ThS Mai Văn Hà")
lbl.grid(column=1, row=1)

lbl = Label(root, text="SVTH: Nguyễn Hà Huy Hoàng")
lbl.grid(column=1, row=2)

data = StringVar()
Label(root, text="Nhập dữ liệu").grid(column=0,row=3, sticky=W)
total = Entry(root, textvariable=data)
total.grid(column=1,row=3, sticky=W)

Label(root, text="Server").grid(column=0,row=4, sticky=W)
btn_server = Button(root, text=status, command=setServer)
btn_server.grid(column=1, row=4)

btn = Button(root, text="Thực hiện", command=clicked)
btn.grid(column=0, row=5)

btn = Button(root, text="Xóa", command=clear)
btn.grid(column=1, row=5)

txt = scrolledtext.ScrolledText(root,width=85,height=15)
txt.grid(column=0,row=6, columnspan=5, rowspan=10, sticky=W+E+N+S)

root.mainloop()
