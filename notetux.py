#!/usr/bin/env python
#-*-coding:utf-8-*-
from Tkinter import *
from tkFileDialog import *
import tkMessageBox
from tkColorChooser import askcolor
from ScrolledText import *
import re
#Funksiyalar
#Faylı bir dəfə oxuyur
pattern = r"'([A-Za-z0-9_\./\\-]*)'"
def fileTest():
    global t
    if location == '':
        return "notSaved"
    else:
        f=open(location,'r')
        readFile = f.read()
        #return readFile+t
        if readFile == text.get(0.0, END).replace("\n",""):
            return "Saved"
        else:
            return "notSaved"
            window.title(" Notetux - Not Saved")
def selectAll(event):
        text.tag_add(SEL, "1.0", END)
        text.mark_set(INSERT, "1.0")
        text.see(INSERT)
def newFile(event):
    save(event)
    exit(event)
    start()
def saveas(event):
    global location, t
    t = text.get(0.0, END)
    f = asksaveasfile(mode="w", defaultextension=".txt")
    try:
        f.write(t.rstrip())
        loc = re.search(pattern,str(f))
        location = (loc.group()).replace("'","")
    except AttributeError:
        pass

def save(event):
    global location
    t = text.get(0.0, END)
    if location == '':
        saveas(event)
    else:
        f = open(location,'w')
        try:
            f.write(t)
        except AttributeError:
            pass
    window.title("Notetux"+" - "+location)
def openFile(event):
    global location
    f = askopenfile(mode="r")
    t = f.read()
    loc = re.search(pattern,str(f))
    location = (loc.group()).replace("'","")
    text.delete(0.0, END)
    text.insert(0.0, t)
    window.title("Notetux"+" - "+location)
def fontColor():
    color = askcolor()
    text.config(fg=color[1])
def bgColor():
    color = askcolor()
    text.config(bg=color[1])
def exit(event):
    if fileTest() == "notSaved":
        ask=tkMessageBox.askquestion(title="Not Saved", message="Do you want to save file?")
        if ask=="yes":
            save(event)
            window.destroy()
        else:
            window.destroy()
    else:
        window.destroy()

def start():
    global location,window,text
    location = ''
    window = Tk()
    window.title("Notetux")

    text = ScrolledText(window, width="200", height="200", bg="#292929", fg="#DEDEDE",insertbackground='white', font=("Helvetica", 20))
    text.pack()

    #Fayl Menyusu
    menubar = Menu(window)
    filemenu = Menu(menubar)
    filemenu.add_command(label="New File   Ctrl+N", command=newFile)
    filemenu.add_command(label="Open File...     Ctrl+O", command=openFile)
    filemenu.add_command(label="Save   Ctrl+S", command=save)
    filemenu.add_command(label="Save As...   Ctrl+Shift+S", command=saveas)
    filemenu.add_separator()
    filemenu.add_command(label="Quit", command=exit)
    menubar.add_cascade(label="File", menu=filemenu)

    #Qisayol
    filemenu.bind_all('<Control-q>', exit)
    filemenu.bind_all('<Control-s>', save)
    filemenu.bind_all('<Control-Shift-S>',saveas)  # upper S, because when you press Shift, it will be lowecase
    filemenu.bind_all('<Control-o>', openFile)
    filemenu.bind_all('<Control-n>', newFile)
    window.bind_all('<Control-a>', selectAll)
    #color
    more = Menu(menubar)
    more.add_command(label="Set Font Color", command=fontColor)
    more.add_command(label="Set Background Color", command=bgColor)
    menubar.add_cascade(label="More", menu=more)



    window.config(menu=menubar)
    window.mainloop()
if __name__ == '__main__':
    start()
