"""
GUI
ToDo app
Notification
CountDown
Website blocker

"""

#Import Tkinter module - built up the app
from tkinter import *
from tkinter import ttk


#import time module
import time


#config the main root section
root = Tk()
root.title('SelfControl')
# root.iconbitmap() - icon source 
root.geometry("350x420")
root.resizable(False, False)


Label(root, text="Self Control application", font="Arial 14 bold").grid(row=1, column=0)


#Create frame - to Selfcontrol
selfcontrolframe = Frame(root)
selfcontrolframe.grid(row=2, column=0, padx=6)

#Button start countdown
Button(selfcontrolframe, text="Start",font="Arial 12 bold", width=5).grid(row=0, column=0, columnspan=4, pady=15) 
#CountDown

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("25")
second.set("00")

hourEntry = Entry(selfcontrolframe, font="Arial 12 bold", width=4, textvariable=hour).grid(row=1, column=1, padx=5)
minuteEntry = Entry(selfcontrolframe, font="Arial 12 bold", width=4, textvariable=minute).grid(row=1, column=2, padx=5)
secondEntry = Entry(selfcontrolframe, font="Arial 12 bold", width=4, textvariable=second).grid(row=1, column=3, padx=5)


#TopLevel windows
def newWindow():
    
    win = Toplevel()
    win.geometry("300x250")
    win.resizable(False, False)

    selfcontrolFrame = Frame(win)
    selfcontrolFrame.pack()
    #create todoList in frame
    selfcontrolList = Listbox (selfcontrolFrame, 
        font="Arial 12",
        width= 30,
        height= 8,
        bg = "SystemButtonFace",#"SystemButtonFace",
        bd = 0.5,
        fg = "#000000",
        highlightthickness=0,
        selectbackground="#a6a6a6",
        activestyle="none"   
    )
    selfcontrolList.pack(side=LEFT, fill=BOTH)

    #create scrollbar
    selfcontrolScroll = Scrollbar(selfcontrolFrame)
    selfcontrolScroll.pack(side=RIGHT, fill=BOTH)
    selfcontrolList.config(yscrollcommand=selfcontrolScroll.set)
    selfcontrolScroll.config(command=selfcontrolList.yview)

    

    #place to add more item
    selfcontrolNewItem = Entry(win,width= 30, font="Arial 12")
    selfcontrolNewItem.pack(pady = 10)
    
    selfcontrolBtnFrame = Frame(win)
    selfcontrolBtnFrame.pack(pady = 10, padx=50)

    plusBtnFrame = Frame(selfcontrolBtnFrame)
    plusBtnFrame.pack(side=LEFT)
    Button(plusBtnFrame, text="+", font="Arial 12 bold", width=3).pack(side=RIGHT, anchor=W)
    Button(plusBtnFrame, text="-", font="Arial 12 bold", width=3).pack(side=LEFT, anchor=W)

    Button(selfcontrolBtnFrame, text="Import", font="Arial 12 bold", width=5).pack(side=RIGHT, padx=10, anchor=E)
 

    update_listbox(selfcontrolList)
    return selfcontrolList

# function, that is fill up the toplevel list
def update_listbox(selfcontrolList):
    for item in webpages:
        selfcontrolList.insert(END, item)

#Button Edit Blacklist
Button(selfcontrolframe, text="Edit Blacklist", command= newWindow, font="Arial 12 bold", width=10).grid(row=2, column=0, columnspan=4, pady=15) 

#Create frame - to DoItList
Label(root, text="You have to do:", font="Arial 14 bold").grid(row=3, column=0)

todoframe = Frame(root)
todoframe.grid(row=4, column=0, padx=6)

#create todoList in frame
todoList = Listbox (todoframe, 
    font="Arial 12",
    width= 35,
    height= 6,
    bg = "SystemButtonFace",#"SystemButtonFace",
    bd = 0.5,
    fg = "#000000",
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none"   
)
todoList.grid(row=1, column=0)

#create scrollbar
todoListScrollbar = Scrollbar(todoframe)
todoListScrollbar.grid(row=1, column=1, rowspan=1, sticky=N+S+W)
todoList.config(yscrollcommand=todoListScrollbar.set)
todoListScrollbar.config(command=todoList.yview)

#place to add more item
todolistNewItem = Entry(todoframe,width= 35, font="Arial 12")
todolistNewItem.grid(row=2, column=0, pady=10)


#Button add new item
todoBtnFrame = Frame(todoframe)
todoBtnFrame.grid(row=3, column=0)
Button(todoBtnFrame, text="Up", font="Arial 12 bold", width=5).grid(row=0, column=0, padx=2)
Button(todoBtnFrame, text="Down", font="Arial 12 bold", width=5).grid(row=0, column=1, padx=2)
Button(todoBtnFrame, text="Clear", font="Arial 12 bold", width=5).grid(row=0, column=2, padx=2)
Button(todoBtnFrame, text="Del", font="Arial 12 bold", width=5).grid(row=0, column=3, padx=2)
Button(todoBtnFrame, text="Add", font="Arial 12 bold", width=5).grid(row=0, column=4, padx=2)


#Button move a list item up
#Button move a list item down
#Button clear list
#Button remove a item

lista = ['call mom', 'cook dinner', 'Do work Task', 'Do work Task', 'Do work Task', 'Do work Task', 'call mom']

#thi
for item in lista:
    todoList.insert(END, item) 


webpages = ['www.faceboock.com', 'www.wikipedia.com', 'www.gmail.com', 'www.whatsapp.com', 'www.instagram.com']



###########################################################

def writeToData(content):
    file = open("data.txt", "w")
    for element in content:
        file.write(element + "\n")
    file.close()

def readToData(content):
    file = open("data.txt", "r")
    lineContents = file.readlines()
    for line in lineContents:
        currentPlace = line[:-1]
        content.append(currentPlace)

def addToList(list, desc):
    list.append(desc)

def removeFromList(list, position):
    list.pop(position)

def clearList(list):
    list.clear()

def pushUp(list, position):
    if len(list)-1 < position or position <= 0:
        print("ERROR, wrong position data")
    else:
        item = list.pop(position)
        list.insert(position - 1 , item)

def pushDown(list, position):
    if len(list)-1 <= position or position < 0:
        print("ERROR, wrong position data")
    else:
        item = list.pop(position)
        list.insert(position + 1 , item)


root.mainloop()