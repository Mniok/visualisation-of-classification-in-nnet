import tkinter as tk
# from tkinter import *
from tkinter import ttk
from leftColumn import createLeftColumn
from rightColumn import createRightColumn
from fitAndPredict import fitAndPredict
from DataStore import dataStore
from plotComponent import plotComponent

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

programMenuCascade = tk.Menu(menu)
programMenuCascade.add_command(label="Rozwiąż", command=fitAndPredict)
programMenuCascade.add_command(label="Zamknij", command=rootWindow.destroy)
programMenuCascade.add_command(label="Wyczyść dane", command=plotComponent.clearPlot)
menu.add_cascade(label="Program", menu=programMenuCascade)

rootWindow.config(menu=menu)


# positioning in window
#rootWindow.columnconfigure(0, weight=1) # thin column, left
#rootWindow.columnconfigure(1, weight=4) # thick column

# left column (classes container)
leftColumn = createLeftColumn(rootWindow)
leftColumn.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y, expand=True)

# right column temp
rightColumn = createRightColumn(rootWindow)
rightColumn.pack(side=tk.RIGHT, anchor=tk.E, fill=tk.Y, expand=True)

# execute Tkinter
rootWindow.mainloop()
