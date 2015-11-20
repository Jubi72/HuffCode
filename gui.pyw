# -*- coding: utf-8 -*-
from Tkinter import *
from huffcode import *

class Gui:

    def __init__ (self):
        self.root = Tk()
        self.root.title ("HuffCode")
        self.root.config (bg = "yellow")
        
        Label(self.root, text="Text", bg="yellow").grid(row=0, column=0)
        Label(self.root, text="Dateiname", bg="yellow").grid(row=1, column=0)

        self.tentry = Entry(self.root)
        self.nentry = Entry(self.root)

        self.tentry.grid(row=0, column=1)
        self.nentry.grid(row=1, column=1)

        self.__menu()
        
        self.root.mainloop()

    def __menu (self):
        self.menu = Menu (self.root)
        self.root.config (menu=self.menu)
        self.menu.add_command(label="Schreiben", command=self.__write)
        self.menu.add_command(label="Lesen", command=self.__read)
        self.menu.add_separator()
        self.menu.add_command(label="Schließen", command=self.root.destroy)

    def __write (self):
        text = self.tentry.get()
        name = self.nentry.get()
        if name == '': name = 'code.hfc'
        huff = HuffCode()
        huff.write(text, name)
        a = Tk()
        Message(a, text="Wurde nach " + name + " geschrieben.").pack()
        a.mainloop()

    def __read (self):
        name = self.nentry.get()
        if name == '': name = 'code.hfc'
        self.tentry.delete(0,END)
        self.tentry.insert(0, "lese ...")
        huff = HuffCode()
        text = huff.read(name)
        self.tentry.delete(0, END)
        self.tentry.insert(0, text)
        a = Tk()
        Message(a, text="Wurde von " + name + " gelesen.\nErgebnis: " + text).pack()
        a.mainloop()

gui = Gui()
