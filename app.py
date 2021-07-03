
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time 
from notifypy import Notify



HOSTPATH = "c:\Windows\System32\drivers\etc\hosts" #".\hosts" #use this path >> "c:\Windows\System32\drivers\etc\hosts"
REDIRECT = "127.0.0.1"

WEBPAGES = []
TODOLISTITEMS = []

BASICWEBPAGES = (   'www.facebook.com', 
                    'www.wikipedia.com', 
                    'www.gmail.com', 
                    'www.whatsapp.com', 
                    'www.instagram.com',
                    'www.reddit.com')

STARTLIST = []


MAINBG = "#ededed"
CLOCKBG = "#ffffff"
MAINFONT = "Helvetica"
BUTTONBG = "#ffffff"
BUTTONFRAME = "#656565"


class MyFunction():
    def saveData(lista, nameOfLista):
        file = open(f"{nameOfLista}-data.txt", "w")
        for item in lista:
            file.write(item + "\n")
        file.close()

    def readData(lista, nameOfLista):
        file = open(f"{nameOfLista}-data.txt", "r")
        contents = file.readlines()
        for line in contents:
            currentPlace = line[:-1]
            lista.append(currentPlace)

    def notifyMe(title, message):
        notification = Notify()
        notification.title = title
        notification.message = message
        notification.icon = ".\selfcontrol.ico"
        notification.send()


    def fillTheList(items, listbox):
        """
        items = list of items
        listbox = listbox element
        """
        color = "#edf3fe"
        listbox.delete(0, END) # clear listbox
        # fill the listbox with list's items
        i = 1
        for item in items:
            listbox.insert(END, item)
            if i % 2 == 0:
                listbox.itemconfigure(END, background = color)
            i += 1

    def blockWebpages(items):
        """
        items = list of webpages 
        """
        file = open(HOSTPATH , "r+")
        content = file.read()
        i = 0
        while i < len(items):
            if items[i] in content:
                pass
            else:
                file.write(REDIRECT + " " + items[i] + "\n")
            i += 1
        file.close()

    def allowWebpages(items):
        """
        items = list of webpages 
        """
        file = open(HOSTPATH , "r+")
        content = file.readlines()
        file.seek(0)
    
        i = 0
        while i < len(content):
        
            if not any(item in content[i] for item in items):
                file.write(content[i])
            i += 1
    
        file.truncate()
        
    def addToList(lista, listbox, entry):
        if entry.get() in lista:
            FailMessage.closeWin(" This item is already \n included in this list ")
        elif entry.get() == "":
            pass
        else:
            lista.append(entry.get())

        MyFunction.fillTheList(lista, listbox)
        
        entry.delete(0, 'end')
        
    def removeFromList(lista, listbox):
        if len(lista) == 0:
            FailMessage.closeWin(" The list is empty ")
        else:
            index = lista.index(listbox.get(ACTIVE))
            lista.remove(listbox.get(ACTIVE))
            
            MyFunction.fillTheList(lista, listbox) 
            listbox.selection_set(index)
            listbox.activate(index)

    def clearList(lista, listbox):
        if len(lista) == 0:
            FailMessage.closeWin(" The list is empty ")
        else:
            lista.clear()
            MyFunction.fillTheList(lista, listbox)

    def pushUp(lista, listbox):
        if len(lista) == 0:
            FailMessage.closeWin(" The list is empty ")

        else:    
            index = lista.index(listbox.get(ACTIVE))
            if index == 0:
                FailMessage.closeWin(" This item is already \n in top of the list ")
            else:
                item = lista.pop (index)
                lista.insert(index - 1, item)
                MyFunction.fillTheList(lista, listbox)
            
            listbox.selection_set(index - 1)
            listbox.activate(index - 1)

    def pushDown(lista, listbox):
        if len(lista) == 0:
            FailMessage.closeWin(" The list is empty ")
        else:
            index = lista.index(listbox.get(ACTIVE))
            if index == len(lista)-1:
                FailMessage.closeWin(" This item is already \n in bottom of the list ")
            else:
                item = lista.pop (index)
                lista.insert(index + 1, item)
                MyFunction.fillTheList(lista, listbox)
                
            listbox.selection_set(index + 1)
            listbox.activate(index + 1)

    def importBasicWebsites(lista, listbox):
        basicList = list(BASICWEBPAGES)

        for item in basicList:
            if item in lista:
                pass
            else:
                lista.append(item)

        MyFunction.fillTheList(lista, listbox)
        

class CountDown(tk.Frame):
    
    def __init__(self,master=None,**kw):
        tk.Frame.__init__(self,master=master,**kw)
        self.master.configure(bg=f"{MAINBG}")

        self.hour = StringVar()
        self.minute = StringVar()
        self.second = StringVar()

        self.hour.set("00")
        self.minute.set("25")
        self.second.set("00")

        self.frameTime = tk.Frame(self.master, bg=f"{CLOCKBG}")
        self.hourEntry = tk.Entry(self.frameTime, font=f"{MAINFONT} 14 bold",bg=f"{CLOCKBG}", width=2, relief='solid', borderwidth=0, textvariable=self.hour).grid(row = 0, column= 0 , padx = 5)
        self.minuteEntry = tk.Entry(self.frameTime, font=f"{MAINFONT} 14 bold", width=2,bg=f"{CLOCKBG}",relief='solid', borderwidth=0, textvariable=self.minute).grid(row = 0, column= 1, padx = 5)
        self.secondEntry = tk.Entry(self.frameTime, font=f"{MAINFONT} 14 bold", width=2,bg=f"{CLOCKBG}",relief='solid', borderwidth=0, textvariable=self.second).grid(row = 0, column= 2, padx = 5)
        
        self.stop = 1
        self.breakTime = 0

        def calling():
            global STARTLIST
            
            STARTLIST = WEBPAGES.copy()

            if self.breakTime == 0:
                MyFunction.blockWebpages(WEBPAGES)
            else:
                MyFunction.allowWebpages(WEBPAGES)
            global stop
            self.stop = 1
            temp = int(self.hour.get()) * 60 ** 2 + int(self.minute.get()) * 60 + int(self.second.get())    
            countDown(temp)
            

        def countDown(temp):
            global stop
            global breakTime
            MyFunction.allowWebpages(STARTLIST)
            MyFunction.blockWebpages(WEBPAGES) 
            
            hours = 0
            mins = temp // 60
            if mins >= 60:
                hours = mins //60
                mins = mins % 60
            secs = temp % 60

            self.hour.set("{0:02d}".format(hours))
            self.minute.set("{0:02d}".format(mins))
            self.second.set("{0:02d}".format(secs))

            root.update()
            time.sleep(1)
            temp -= 1
            
            if temp < 0:
                if self.breakTime == 1:
                    MyFunction.notifyMe("Let's start learn and work" , "You had a relaxing break")
                    self.hour.set("00")
                    self.minute.set("25")
                    self.second.set("00")
                    self.breakTime = 0
                else:
                    MyFunction.notifyMe("Take a five-minute break" , "You worked hard")
                    self.hour.set("00")
                    self.minute.set("05")
                    self.second.set("00")
                    self.breakTime = 1

            if temp >= 0 and self.stop == 1:
                countDown(temp)

        def pauseCountDown():
            global stop
            self.stop = 0
            
        def breakCountDown():
            global stop, breakTime
            self.stop = 0
            self.breakTime = 0   
            MyFunction.allowWebpages(WEBPAGES)
            
            self.hour.set("00")
            self.minute.set("25")
            self.second.set("00")

        self.frameBtn = tk.Frame(self.master, bg=f"{MAINBG}")
        self.sbmtBtn = tk.Button(self.frameBtn, text="Start",font=f"{MAINFONT} 10 bold", width=6, relief='solid', borderwidth=.5, bg=f"{BUTTONBG}", command = calling).grid(row = 0, column= 0, padx = 15)
        self.pauseBtn = tk.Button(self.frameBtn, text="Pause",font=f"{MAINFONT} 10 bold", width=6, relief='solid', borderwidth=.5, bg=f"{BUTTONBG}", command = pauseCountDown).grid(row = 0, column= 1 , padx = 15)
        self.breakBtn = tk.Button(self.frameBtn, text="Stop",font=f"{MAINFONT} 10 bold", width=6, relief='solid', borderwidth=.5, bg=f"{BUTTONBG}", command = breakCountDown).grid(row = 0, column= 2, padx = 15)
        
        self.frameTime.grid(row = 0, pady= 6)
        self.frameBtn.grid(row = 1, pady= 6)


class ToDoList(tk.Frame):
    
    def __init__(self,master=None,**kw):
        tk.Frame.__init__(self,master=master,**kw)
        self.master.configure(bg=f"{MAINBG}")
        self.label2 = tk.Label(self.master, text="The To Do List", font=f"{MAINFONT} 13 bold", bg=f"{MAINBG}").grid(row = 2, pady = 4)

        #create todoList in frame
        self.listbox = tk.Listbox(
                                    self.master, 
                                    font=f"{MAINFONT} 10",
                                    width= 38,
                                    height= 6,
                                    bg = "#ffffff",
                                    bd = 0.5,
                                    fg = "#000000",
                                    highlightthickness=0,
                                    selectbackground="#f9cbda",
                                    selectforeground="#000000",
                                    activestyle="none"   
                                ) 
        
        #create scrollbar
        self.listScroll = tk.Scrollbar(self.master)
        self.listbox.config(yscrollcommand= self.listScroll.set)
        self.listScroll.config(command=self.listbox.yview)

        self.entry = tk.Entry(self.master, width = 29,font=f"{MAINFONT} 10")
        self.add = tk.Button(self.master, width= 6, relief='solid', borderwidth=.5,text="Add", font=f"{MAINFONT} 10 bold", bg=f"{BUTTONBG}", command= lambda: MyFunction.addToList(TODOLISTITEMS, self.listbox, self.entry))
        
        self.entry.bind('<Return>', lambda event, a = TODOLISTITEMS,b = self.listbox,c = self.entry :MyFunction.addToList(a, b, c))

        self.frameBtn = tk.Frame(self.master, bg=f"{MAINBG}")
        self.up = tk.Button(self.frameBtn, text="Up", font=f"{MAINFONT} 10 bold", width=6, relief='solid', borderwidth=.5, bg=f"{BUTTONBG}", command= lambda: MyFunction.pushUp(TODOLISTITEMS, self.listbox)).grid(row=0, column=0, padx=8, sticky= W)
        self.down = tk.Button(self.frameBtn, text="Down", font=f"{MAINFONT} 10 bold", width=6, relief='solid', borderwidth=.5,bg=f"{BUTTONBG}", command= lambda: MyFunction.pushDown(TODOLISTITEMS, self.listbox)).grid(row=0, column=1, padx=8, sticky= W)
        self.clear = tk.Button(self.frameBtn, text="Clear", font=f"{MAINFONT} 10 bold", width=6, relief='solid', borderwidth=.5, bg=f"{BUTTONBG}", command= lambda: MyFunction.clearList(TODOLISTITEMS, self.listbox)).grid(row=0, column=2, padx=8, sticky= E)
        self.delete = tk.Button(self.frameBtn, text="Del", font=f"{MAINFONT} 10 bold", width=6, relief='solid', borderwidth=.5,bg=f"{BUTTONBG}", command= lambda: MyFunction.removeFromList(TODOLISTITEMS, self.listbox)).grid(row=0, column=3, padx=8, sticky= E)
        
        
        self.listbox.grid(row = 3, column= 0, sticky= W, padx=6)
        self.listScroll.grid(row = 3, column= 0, sticky=N+S+E, padx = 0)

        self.entry.grid(row = 4, column= 0, sticky= W, padx=8, pady=14)
        self.add.grid(row = 4, column= 0, sticky= E, padx=8)
        self.frameBtn.grid(row = 5, column=0)
        

        MyFunction.fillTheList(TODOLISTITEMS, self.listbox)


class BlackList():
    
    def goToBlacklist():
        win = tk.Toplevel()
        win.geometry("360x250")
        win.resizable(False, False)

        selfcontrolFrame = Frame(win)
        selfcontrolFrame.pack()

        #create todoList in frame
        selfcontrolList = Listbox (selfcontrolFrame, 
            font="Arial 10",
            width= 45,
            height= 8,
            bg = "#ffffff",
            bd = 0.5,
            fg = "#000000",
            highlightthickness=0,
            selectbackground="#f9cbda",
            selectforeground="#000000",
            activestyle="none"   
        )

        selfcontrolList.pack(side=LEFT, fill=BOTH, pady = 6)

        #create scrollbar
        selfcontrolScroll = Scrollbar(selfcontrolFrame)
        selfcontrolScroll.pack(side=RIGHT, fill=BOTH)
        selfcontrolList.config(yscrollcommand=selfcontrolScroll.set)
        selfcontrolScroll.config(command=selfcontrolList.yview)

        #place to add more item
        selfcontrolNewItem = Entry(win,width= 48, font="Arial 10")
        selfcontrolNewItem.pack(pady = 10)
        selfcontrolNewItem.bind('<Return>', lambda event, a = WEBPAGES,b = selfcontrolList,c = selfcontrolNewItem : MyFunction.addToList(a, b, c))


        selfcontrolBtnFrame = Frame(win)
        selfcontrolBtnFrame.pack(pady = 10)

        plusBtnFrame = Frame(selfcontrolBtnFrame, width = 100)
        plusBtnFrame.pack(side=RIGHT, padx = 10)
        Button(plusBtnFrame, text="+", font=f"{MAINFONT} 10 bold",bg=f"{BUTTONBG}", relief='solid', borderwidth=.5, width = 3, height= 1, command= lambda: MyFunction.addToList(WEBPAGES, selfcontrolList, selfcontrolNewItem)).pack(side=RIGHT, fill = X)
        Button(plusBtnFrame, text="-", font=f"{MAINFONT} 10 bold",bg=f"{BUTTONBG}", relief='solid', borderwidth=.5, width = 3, height= 1, command= lambda: MyFunction.removeFromList(WEBPAGES, selfcontrolList)).pack(side=LEFT, fill = X, padx = 15)


        Button(selfcontrolBtnFrame, text="Import", font=f"{MAINFONT} 10 bold",bg=f"{BUTTONBG}", relief='solid', borderwidth=.5, width = 12, height= 1, command= lambda: MyFunction.importBasicWebsites(WEBPAGES, selfcontrolList)).pack(side=LEFT, anchor=E, padx = 50)

        MyFunction.fillTheList(WEBPAGES, selfcontrolList)


class FailMessage():
    def closeWin(message):
        
        win = tk.Toplevel()
        win.geometry("200x140")
        win.resizable(False, False)
        win.configure(bg='#ededed')

        tk.Label(win, text = message, font="Arial 10 bold", bg='#ededed').pack(pady= 16)

        def closeWin():
            win.destroy()

        tk.Button(win, text = "OK",width=6, height=1, font="Arial 12 bold", activebackground='#345',activeforeground='white', command = closeWin).pack(pady= 10)


class MainApp(tk.Frame):
    def __init__(self,master=None,**kw):
        
        tk.Frame.__init__(self,master=master,**kw)
        
        self.master.iconbitmap('.\selfcontrol.ico')
        self.master.geometry("288x400")
        self.master.title('SelfControl')
        self.master.resizable(False, False)
        self.master.configure(bg=f"{MAINBG}")

        self.label1 = tk.Label(self.master, text="SELF CONTROL", font=f"{MAINFONT} 11 bold", bg=f"{MAINBG}").grid(row=0, column = 0, pady= 10)

        self.button1 = tk.Button(self.master, text="Edit blacklist", font=f"{MAINFONT} 10 bold", relief='solid', borderwidth=.5, width = 12, height= 1, bg=f"{BUTTONBG}",  command=BlackList.goToBlacklist).grid(row=1, column = 0, pady= 6)

        self.countDown = CountDown(master=self)
        self.countDown.grid()


        self.toDo = ToDoList(master=self)
        self.toDo.grid(pady=10)
    
        
def onClosing():

    if tk.messagebox.askokcancel("Quit", "Before you quit,\nplease stop the countdown\nwith the \"stop\" button"):
        MyFunction.allowWebpages(STARTLIST)
        MyFunction.allowWebpages(WEBPAGES)
        MyFunction.saveData(WEBPAGES, "web")
        MyFunction.saveData(TODOLISTITEMS, "todo")
        root.destroy()
    

MyFunction.readData(WEBPAGES, "web")
MyFunction.readData(TODOLISTITEMS, "todo")

#if __name__ == '__main__':

def run():
    global root

    root = tk.Tk()
    app = MainApp(master=root)
    app.grid()
    root.protocol("WM_DELETE_WINDOW", onClosing)
    root.mainloop()