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
        self.textVar= StringVar(value="")
        self.textVar2 = StringVar(value="")
        self.textVar3 = StringVar(value="")

    #запуск приложения
    def run(self):
        self.root.mainloop()



    #создание виджета с логом
    def creatList(self):

        self.text = scrolledtext.ScrolledText(self.root, state='disabled')
        self.text.configure(state='normal')
        hand = win32evtlog.OpenEventLog(None, self.log_type)
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

        while True:
            events = win32evtlog.ReadEventLog(hand, flags, 0)
            if not events:
                break

            for event in events:
                if (self.textVar.get() in f"{event.EventCategory}") or (self.textVar.get() in f"{event.TimeGenerated}") or (self.textVar.get() in f"{event.SourceName}") or (self.textVar.get() in f"{event.EventID}") or (self.textVar.get() in f"{event.EventType}") or (self.textVar.get() in f"{event.StringInserts}"):
                    if  (self.dateSearch(self.textVar2.get(),1) <= self.dateSearch(event.TimeGenerated) <= self.dateSearch(self.textVar3.get(),2)):
                        self.text.insert('insert', f"{event.EventCategory}\n")
                        self.text.insert('insert', f"{event.TimeGenerated}\n")
                       # print(self.dateSearch(event.TimeGenerated))
                        self.text.insert('insert', f"{event.SourceName}\n")
                        self.text.insert('insert', f"{event.EventID}\n")
                        self.text.insert('insert', f"{event.EventType}\n")
                        self.text.insert('insert', f"{event.StringInserts}\n")
                        self.text.insert('insert', f"{'=' * 50}\n")
        # for event in self.varIvent:
        #
        #     self.text.insert('insert', f"{event.ComputerName}\n")
        #     self.text.insert('insert', f"{event.Sid}\n")
        #     self.text.insert('insert', f"{event.RecordNumber}\n")
        #     self.text.insert('insert', f"{event.TimeWritten}\n")
        #

        self.text.configure(state='disabled')
        self.text.pack(fill='both', expand=True)

    def dateSearch(self,date,flag=0):
        date = f"{date}"
        if (date != ''):
            #print(int(date.replace('-', '')[0:8]))
            return int(date.replace('-','')[0:8])
        elif (date=='' and flag == 1):
            return 0
        elif (date=='' and flag == 2):
            return 100000000



    def updateLog(self):
        # global Security, Application, System

        # varIvent = Application
        if (self.choice.get() == 0):
            self.log_type = 'System'
        elif (self.choice.get() == 1):
            self.log_type = 'Application'
        elif (self.choice.get() == 2):
            self.log_type = 'Security'
        self.creatList()

    #Создание виджетов управления
    def drowWidgets(self):
        frameSelect = Frame(self.root)
        frameSearch = Frame(self.root)
        frameSearch2 = Frame(self.root)

        frameSelect.pack()
        frameSearch.pack()
        frameSearch2.pack()
        Radiobutton(frameSelect, text="System", width=10, height=3, variable=self.choice, value=0).pack(side=LEFT)
        Radiobutton(frameSelect, text="Application", width=10, height=3, variable=self.choice, value=1).pack(side=LEFT)
        Radiobutton(frameSelect, text="Security", width=10, height=3, variable=self.choice, value=2).pack(side=LEFT)
        self.button = Button(frameSelect, text=f"submit", command=self.update_text).pack(side=LEFT)

        self.entry = Entry(frameSearch,textvariable=self.textVar).pack(side=LEFT)
        self.button = Button(frameSearch, text="search", command=self.update_text).pack(side=LEFT)

        self.entry2 = Entry(frameSearch2, textvariable=self.textVar2).pack(side=LEFT)
        self.entry3 = Entry(frameSearch2, textvariable=self.textVar3).pack(side=LEFT)
        self.button = Button(frameSearch2, text="search", command=self.update_text).pack(side=LEFT)

    #обновление списка логов
    def update_text(self):
        self.text.pack_forget()
        self.updateLog()

    def test(self):
        print(self.textVar.get())




#чтение логов




#запуск приложения
window = Window(500, 500)
window.drowWidgets()
window.updateLog()

window.run()