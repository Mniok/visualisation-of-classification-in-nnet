import tkinter as tk

from fileInteractions import readFromFile, saveToFile

from fitAndPredict import fitAndPredict
from DataStore import dataStore
from plotComponent import plotComponent

def createMenuBar(container):
    menu = tk.Menu(container)
    fileMenuCascade = tk.Menu(menu)
    fileMenuCascade.add_command(label="Wczytaj", command=readFromFile)
    fileMenuCascade.add_command(label="Zapisz", command=lambda: saveToFile(dataStore.plotData))
    menu.add_cascade(label="Plik", menu=fileMenuCascade)

    programMenuCascade = tk.Menu(menu)
    programMenuCascade.add_command(label="Rozwiąż", command=fitAndPredict)
    programMenuCascade.add_command(label="Zamknij", command=container.destroy)
    programMenuCascade.add_command(label="Wyczyść dane", command=plotComponent.clearPlot)
    menu.add_cascade(label="Program", menu=programMenuCascade)

    return menu
