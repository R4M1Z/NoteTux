#!/usr/bin/env python
#-*-coding:utf-8-*-
from Tkinter import *
from tkFileDialog import *
import tkMessageBox
from tkColorChooser import askcolor
from ScrolledText import *
import re
#Functions
pattern = r"'([A-Za-z0-9_\./\\-]*)'"        # pattern to get file's name from path
def fileTest():                             # function to check if file is already saved
    global location
    if location == '':                                          # Program is opened for first time;
        if text.get(0.0, END).replace("\n","")!='':             # and user didn't write anything yet.
            return "notSaved"
    else:
        f=open(location,'r')
        readFile = f.read()
        if readFile.replace("\n","") == text.get(0.0, END).replace("\n",""):      # Check if current content is the same as file's content
            return "Saved"                                                        # used replace's coz it automatically add new line, and i should delete them for comparison
        else:
            return "notSaved"


def selectAll(event):
        text.tag_add(SEL, "1.0", END)
        text.mark_set(INSERT, END)
        text.see(INSERT)


def newFile(event):
    global ask      # variable from notSavedWarn func.
    if fileTest() == "notSaved":
        if ask == True:     # if user wants to save file
            save(event)
        elif ask==None:      # if user clicks to cancel button
            return 0         # don't do anything and close newFile func.
    exit(event)
    start()


def saveas(event):
    global location,t
    try:
        f = asksaveasfile(mode="w", defaultextension=".txt")
        f.write(t.rstrip())                         # Without rstrip, whitespaces will be deleted automatically
        loc = re.search(pattern,str(f))
        location = (loc.group()).replace("'","")
    except AttributeError:
        pass

def save(event):
    global location,t
    t = text.get(0.0, END)
    if location == '':                          # when users open window for first time, there is not location to save file, so we need save as.. window
        saveas(event)
    else:                                       # if file already has a location
        f = open(location,'w')
        try:
            f.write(t)
        except AttributeError:
            pass
    window.title("Notetux"+" - "+location)

def openFile(event):                                # Open a file
    global location,ask
    if fileTest() == "notSaved":
        notSavedWarn(event)                         # Ask question
        if ask == True:               # if user wants to open new file before save current file
            save(event)
        elif ask == None:
            return 0
    try:
        f = askopenfile(mode="r")
    except:
        pass
    t = f.read()
    loc = re.search(pattern,str(f))                 # Get file's name
    location = (loc.group()).replace("'","")
    text.delete(0.0, END)
    text.insert(0.0, t)
    window.title("Notetux"+" - "+location)          # Add current location to window's title


def fontColor():                                    # Change fonr color
    color = askcolor()
    text.config(fg=color[1])


def bgColor():                                       # Change background color
    color = askcolor()
    text.config(bg=color[1])


def notSavedWarn(event):                            # Warning message if the file is not saved
    global ask
    ask=tkMessageBox.askyesnocancel(title="Not Saved", message="Do you want to save file?")

    # NOTE:  I didn't return a value because every time when i call notSavedWarn, it will show a message
    # Instead, i used global var - ask, so it'll call notSavedWarn just one time

def exit(event):        # I think you already understand how this func. works
    global ask
    if fileTest() == "notSaved":
        notSavedWarn(event)
        if ask==True:
            save(event)
            window.destroy()
        elif ask==None:
            return 0
        else:
            window.destroy()
    else:
        window.destroy()

def start():
    global location,window,text
    location = ''
    window = Tk()
    window.title("Notetux")

    text = ScrolledText(window, width="200", height="200", bg="#292929", fg="#DEDEDE",insertbackground='white', font=("Helvetica", 20),undo=True)
    text.pack()

    #Menu
    menubar = Menu(window)
    filemenu = Menu(menubar)
    filemenu.add_command(label="New File   Ctrl+N", command=newFile)
    filemenu.add_command(label="Open File...     Ctrl+Shift+O", command=openFile)
    filemenu.add_command(label="Save   Ctrl+S", command=save)
    filemenu.add_command(label="Save As...   Ctrl+Shift+S", command=saveas)
    filemenu.add_separator()
    filemenu.add_command(label="Quit", command=exit)
    menubar.add_cascade(label="File", menu=filemenu)

    #Shortcut
    filemenu.bind_all('<Control-q>', exit)
    filemenu.bind_all('<Control-s>', save)
    filemenu.bind_all('<Control-Shift-S>',saveas)  # upper S, because when you press Shift, it will be lowecase

    #-------------------------------------------------------------------------------------------------
    filemenu.bind_all('<Control-Shift-O>', openFile) # upper O, because when you press Shift, it will be lowecase
    # NOTE:  I know it must be Ctrl+O
    # But when user press Ctrl+O, it creates new line (I couldn't describe this try and see :D )

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
