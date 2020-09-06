#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author: Dominik Nuszkiewicz
Code of Gens v1.2
"""

import sys
from tkinter import *
from math import *
import tkinter as tk

################ windows ############
root = Tk() 
root.geometry('500x400')
root.title('Code of Gens')
window = tk.Toplevel(root)


def center(self):
        self.update()
        # szerokość / wysokość okna
        wx = self.winfo_width()
        wy = self.winfo_height()
        # szerokość wysokość ekranu
        sx = self.winfo_screenwidth()
        sy = self.winfo_screenheight()
        # środek ekranu przesunięty o 
        x = (sx - wx) // 2 # połowę szerokośi
        y = (sy - wy) // 2 # połowę wysokości

        self.geometry("{}x{}+{}+{}".format(wx, wy, x, y))

center(root)
########################## tablica aminokwasow
met = ['metionina', 'AUG']
fenylo = ['fenyloalanina','UUU','UUC',]
leu = ['leucyna','UUA', 'UUG','CUU','CUC','CUA','CUG']
izoleu = ['izoleucyna','AUU','AUC','AUA']
walina = ['walina', 'GUU', 'GUC', 'GUA', 'GUG']



amino=[fenylo, leu, met, izoleu, walina]
kodony=[]

######## pole tekstowe ##########
e = Entry(root,width=30) 

######################### widgety
l = Label(root,text = 'Podaj kod genetyczny')
l2 = Label(window, text="")


######## funkcje ################
def tworzenie_tabeli(kod):
        global kodony 
        a=0
        b=3
        for i in range(int(len(kod)/3)):
                kodony.append(kod[a:b])
                a+=3
                b+=3



def main():
        global e
        global amino
        global kodony
        code = str(e.get())
        tworzenie_tabeli(code)
        wynik=""
        
        for i in range(len(kodony)):
                for k in range(len(amino)):
                        if kodony[i] in amino[k]:
                                wynik+="-"+(amino[k][0])+"("+kodony[i]+")"+"-"+'\n'
        
        l2.config(text= wynik)
        l2.place(relx=0.5, rely=0.6, anchor=CENTER)
        kodony=[]

b2 = Button(root, text = 'Potwierdź', command=main)

######################### place widgetow

e.place(relx=0.5, rely=0.4, anchor=CENTER)
b2.place(relx=0.5, rely=0.6, anchor=CENTER)
l.place(relx=0.5, rely=0.2, anchor=CENTER)

  





root.mainloop()  
