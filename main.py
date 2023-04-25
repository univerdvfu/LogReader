from tkinter import *
from tkinter import scrolledtext

import win32evtlog


class Window:
    #функция создания главного кона с размерами и переменными
    def __init__(self, width, height, title="MyWindow", resizable=(True, True)):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        self.choice = IntVar(value=0)
        self.textVar= StringVar(value=" ")
    #запуск приложения
    def run(self):
        self.root.mainloop()



    #создание виджета с логом
    def creatList(self):

        self.text = scrolledtext.ScrolledText(self.root, state='disabled')
        self.text.configure(state='normal')
        for event in self.varIvent:
            self.text.insert('insert', f"{event.EventCategory}\n")
            self.text.insert('insert', f"{event.TimeGenerated}\n")
            self.text.insert('insert', f"{event.SourceName}\n")
            self.text.insert('insert', f"{event.EventID}\n")
            self.text.insert('insert', f"{event.EventType}\n")
            self.text.insert('insert', f"{event.StringInserts}\n")
            self.text.insert('insert', f"{event.ComputerName}\n")
            self.text.insert('insert', f"{event.Sid}\n")
            self.text.insert('insert', f"{event.RecordNumber}\n")
            self.text.insert('insert', f"{event.TimeWritten}\n")
            self.text.insert('insert', f"{'=' * 50}\n")

        self.text.configure(state='disabled')
        self.text.pack(fill='both', expand=True)



    def updateLog(self):
        global Security, Application, System

        # varIvent = Application
        if (self.choice.get() == 0):
            self.varIvent = System
        elif (self.choice.get() == 1):
            self.varIvent = Application
        elif (self.choice.get() == 2):
            self.varIvent = Security
        self.creatList()

    #Создание виджетов управления
    def drowWidgets(self):
        frameSelect = Frame(self.root)
        frameSearch = Frame(self.root)
        frameSelect.pack()
        frameSearch.pack()
        Radiobutton(frameSelect, text="System", width=10, height=3, variable=self.choice, value=0).pack(side=LEFT)
        Radiobutton(frameSelect, text="Application", width=10, height=3, variable=self.choice, value=1).pack(side=LEFT)
        Radiobutton(frameSelect, text="Security", width=10, height=3, variable=self.choice, value=2).pack(side=LEFT)
        self.button = Button(frameSelect, text=f"submit", command=self.update_text).pack(side=LEFT)

        self.entry = Entry(frameSearch,textvariable=self.textVar).pack(side=LEFT)
        self.button = Button(frameSearch, text="search", command=self.update_text).pack(side=LEFT)


    #обновление списка логов
    def update_text(self):
        self.text.pack_forget()
        self.updateLog()

    def searhText(self):
        if self.textVar.get() in ()


#чтение логов


hand1 = win32evtlog.OpenEventLog(None, "Security")
hand2 = win32evtlog.OpenEventLog(None, "Application")
hand3 = win32evtlog.OpenEventLog(None, "System")
flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
Security = win32evtlog.ReadEventLog(hand1, flags, 0)
Application = win32evtlog.ReadEventLog(hand2, flags, 0)
System = win32evtlog.ReadEventLog(hand3, flags, 0)

#запуск приложения
window = Window(500, 500)
window.drowWidgets()
window.updateLog()

window.run()