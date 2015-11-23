# -*- coding: utf-8 -*-
import sys
if int(sys.version[0]) < 3: import Tkinter as tk # Python2: Tkinter
else: import tkinter as tk                       # neuer:   tkinter
from huffcode import *

class Gui:

    def __init__ (self):
        self.root = tk.Tk()
        self.root.title ("HuffCode")
        self.root.config (bg = "yellow")
        self.root.geometry ("200x50")
        
        tk.Label(self.root, text="Text", bg="yellow").grid(row=0, column=0)
        tk.Label(self.root, text="Dateiname", bg="yellow").grid(row=1, column=0)

        self.tentry = tk.Entry(self.root)
        self.nentry = tk.Entry(self.root)

        self.tentry.grid(row=0, column=1)
        self.nentry.grid(row=1, column=1)

        self.__menu()
        
        self.root.mainloop()

    def __menu (self):
        self.menu = tk.Menu (self.root)
        self.root.config (menu=self.menu)
        self.menu.add_command(label="Schreiben", command=self.__write)
        self.menu.add_command(label="Lesen", command=self.__read)
        self.menu.add_separator()
        self.menu.add_command(label="Schließen", command=self.root.destroy)

    def __write (self):
        text = self.tentry.get()
        name = self.nentry.get()
        if name == '': name = 'code.hfc'
        print(text, name)
        huff = HuffCode()
        huff.write(text, name)
        a = tk.Tk()
        tk.Message(a, text="Wurde nach " + name + " geschrieben.").pack()
        a.mainloop()

    def __read (self):
        name = self.nentry.get()
        if name == '': name = 'code.hfc'
        if int(sys.version[0]) < 3: self.tentry.delete (0, END)
        else: self.tentry.delete(0, len(self.tentry.get())-1)
        self.tentry.insert(0, "lese ...")
        huff = HuffCode()
        text = huff.read(name)
        if int(sys.version[0]) < 3: self.tentry.delete(0, END)
        else: self.tentry.delete(0, len(self.tentry.get())-1)
        self.tentry.insert(0, text)
        a = tk.Tk()
        tk.Message(a, text="Wurde von " + name + " gelesen.\nErgebnis: " + text).pack()
        a.mainloop()

gui = Gui()
