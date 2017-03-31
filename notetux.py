#!/usr/bin/env python
#-*-coding:utf-8-*-
from Tkinter import *
from tkFileDialog import *
from tkColorChooser import askcolor
from ScrolledText import *
#Funksiyalar
def selectAll(event):
        text.tag_add(SEL, "1.0", END)
        text.mark_set(INSERT, "1.0")
        text.see(INSERT)
def yeniFayl(event):
	yaddaSaxla(event)
	text.delete(0.0, END)
def yaddaSaxla(event):
	f = asksaveasfile(mode="w", defaultextension=".txt")
	t = text.get(0.0, END)
	f.write(t.rstrip())
def faylAc(event):
	f = askopenfile(mode="r")
	t = f.read()
	text.delete(0.0, END)
	text.insert(0.0, t)
def herfReng():
        color = askcolor()
        text.config(fg=color[1])
def arxaplanReng():
        color = askcolor()
        text.config(bg=color[1])
def cixish(event):
        pencere.destroy()
pencere = Tk()
pencere.title("NoteTux")

text = ScrolledText(pencere, width="200", height="200", bg="#ADA89D", fg="#fff", font=32)
text.pack()

#Fayl Menyusu
menubar = Menu(pencere)
filemenu = Menu(menubar)
filemenu.add_command(label="Yeni Səhifə   Ctrl+n", command=yeniFayl)
filemenu.add_command(label="Aç...     Ctrl+o", command=faylAc)
filemenu.add_command(label="Saxla   Ctrl+s", command=yaddaSaxla)
filemenu.add_separator()
filemenu.add_command(label="Çıxış", command=cixish)
menubar.add_cascade(label="Fayl", menu=filemenu)

#Qisayol
filemenu.bind_all('<Control-q>', cixish)
filemenu.bind_all('<Control-s>', yaddaSaxla)
filemenu.bind_all('<Control-o>', faylAc)
filemenu.bind_all('<Control-n>', yeniFayl)
pencere.bind_all('<Control-a>', selectAll)
#color
elave = Menu(menubar)
elave.add_command(label="Hərf rəngini seç", command=herfReng)
elave.add_command(label="Arxaplan rəngini seç", command=arxaplanReng)
menubar.add_cascade(label="Əlavə", menu=elave)



pencere.config(menu=menubar)
pencere.mainloop()
