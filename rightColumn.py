import tkinter as tk
from tkinter import ttk
from createInputs import createTopBar, createBottomBar
from fitAndPredict import fitAndPredict
from plotComponent import createPlot

def createControlsBar(container):
    controlsBarFrame = tk.Frame(container)

    fitAndPredictButton = ttk.Button(controlsBarFrame, text="Klasyfikuj", command=fitAndPredict)
    fitAndPredictButton.pack(anchor=tk.E)

    return controlsBarFrame

def createRightColumn(container):
    rightColumn = tk.Frame(container)

    topInputsBar = createTopBar(rightColumn)
    topInputsBar.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=False)
    mainPlot = createPlot(rightColumn)
    mainPlot.pack(anchor=tk.CENTER, expand=True)
    bottomInputsBar = createBottomBar(rightColumn)
    bottomInputsBar.pack(side=tk.TOP, anchor=tk.S, fill=tk.X, expand=False)

    controlsBar = createControlsBar(rightColumn)
    controlsBar.pack(side=tk.BOTTOM, anchor=tk.S, fill=tk.X)

    return rightColumn
