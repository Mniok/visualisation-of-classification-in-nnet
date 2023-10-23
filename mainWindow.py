from tkinter import *

# create root window
rootWindow = Tk()
rootWindow.title("Projekt Inżynierski - wizualizacja procesu klasyfikacji w sieci neuronowej typu MLP")
rootWindow.geometry('1200x800')


# top menu bar
menu = Menu(rootWindow)
fileMenuCascade = Menu(menu)
fileMenuCascade.add_command(label="Otwórz")
fileMenuCascade.add_command(label="Zapisz")
fileMenuCascade.add_command(label="Eksportuj")
menu.add_cascade(label="Plik", menu=fileMenuCascade)
rootWindow.config(menu=menu)

# execute Tkinter
rootWindow.mainloop()
                 
