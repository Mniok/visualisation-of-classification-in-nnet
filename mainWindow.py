import tkinter as tk
# from tkinter import *
from tkinter import ttk
from leftColumn import createLeftColumn

# create root window
rootWindow = tk.Tk()
rootWindow.title("Projekt Inżynierski - wizualizacja procesu klasyfikacji w sieci neuronowej typu MLP")
rootWindow.geometry('1200x640')
rootWindow.configure(bg='#FFEEEE') # debug color


# top menu bar
menu = tk.Menu(rootWindow)
fileMenuCascade = tk.Menu(menu)
fileMenuCascade.add_command(label="Otwórz")
fileMenuCascade.add_command(label="Zapisz")
fileMenuCascade.add_command(label="Eksportuj")
menu.add_cascade(label="Plik", menu=fileMenuCascade)
rootWindow.config(menu=menu)


# positioning in window
#rootWindow.columnconfigure(0, weight=1) # thin column, left
#rootWindow.columnconfigure(1, weight=4) # thick column

# left column (classes container)
leftColumn = createLeftColumn(rootWindow)

# right column temp
#ttk.Label(rootWindow, text='right column temp').grid(column=1, row=0)

# execute Tkinter
rootWindow.mainloop()
