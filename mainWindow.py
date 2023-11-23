import tkinter as tk
from leftColumn import createLeftColumn
from rightColumn import createRightColumn

from menuBar import createMenuBar

# create root window
rootWindow = tk.Tk()
rootWindow.title("Projekt Inżynierski - wizualizacja procesu klasyfikacji w sieci neuronowej typu MLP")
rootWindow.geometry('1200x640')
#rootWindow.configure(bg='#FFEEEE') # debug color


# top menu bar
menu = createMenuBar(rootWindow)
rootWindow.config(menu=menu)


# positioning in window
#rootWindow.columnconfigure(0, weight=1) # thin column, left
#rootWindow.columnconfigure(1, weight=4) # thick column

# left column (classes container)
leftColumn = createLeftColumn(rootWindow)
leftColumn.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y, expand=True)

# right column (parameter inputs and plot)
rightColumn = createRightColumn(rootWindow)
rightColumn.pack(side=tk.RIGHT, anchor=tk.E, fill=tk.Y, expand=True)

# execute Tkinter
rootWindow.mainloop()
